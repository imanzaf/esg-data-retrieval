"""
Simple Emissions Data Extraction
-------------------------------------
1) Download the PDF from the URL.
2) Parse only relevant pages using LlamaParse.
3) Write raw parse text to `data/parsed_outputs/{company}_raw_parsed.md`.
4) Choose the best JSON block and update the CSV (`company_emissions.csv`).

Requires environment variable:
  - LLAMA_API_KEY
Usage:
  python src/scripts/retrieve_emissions_llama_parse.py <company_name> <sustainability_report_url>

  Example:
  python src/scripts/retrieve_emissions_llama_parse.py "NVIDIA CORP" "https://images.nvidia.com/aem-dam/Solutions/documents/FY2024-NVIDIA-Corporate-Sustainability-Report.pdf"
  python src/scripts/retrieve_emissions_llama_parse.py "MICROSOFT CORP" "https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RW1lmju"
  python src/scripts/retrieve_emissions_llama_parse.py "AMAZON COM INC" "https://sustainability.aboutamazon.com/2023-amazon-sustainability-report.pdf"
  python src/scripts/retrieve_emissions_llama_parse.py "META PLATFORMS INC CLASS A" "https://sustainability.atmeta.com/wp-content/uploads/2024/08/Meta-2024-Sustainability-Report.pdf"
  python src/scripts/retrieve_emissions_llama_parse.py "ALPHABET INC CLASS A" "https://www.smartenergydecisions.com/upload/research_+_reports/google-2024-environmental-report.pdf"
  python src/scripts/retrieve_emissions_llama_parse.py "APPLE INC" "https://www.apple.com/environment/pdf/Apple_Environmental_Progress_Report_2024.pdf"
"""



import sys
import os
import re
import json
import tempfile
from datetime import datetime
from io import BytesIO

import requests
import PyPDF2
import pandas as pd
from dotenv import load_dotenv
from loguru import logger
from llama_parse import LlamaParse

# Load environment variables
load_dotenv()
LLAMA_API_KEY = os.getenv("LLAMA_API_KEY")

# Default output paths
OUTPUT_CSV = "data/company_emissions.csv"
PARSED_OUTPUTS_DIR = "data/parsed_outputs"


class EmissionsDataExtractor:
    def __init__(self, llama_api_key: str):
        if not llama_api_key:
            raise ValueError("LLAMA_API_KEY is missing or invalid.")
        self.api_key = llama_api_key

        # Regex patterns for identifying relevant pages
        self.pattern_scope1 = re.compile(r"\b(scope\s*1|scope\s*i|scope\s*one)\b", re.IGNORECASE)
        self.pattern_scope2 = re.compile(r"\b(scope\s*2|scope\s*ii|scope\s*two)\b", re.IGNORECASE)
        self.patterns_year = re.compile(
            r"\b(?:FY|FISCAL\s*YEAR)?\s*(\d{2}|20\d{2})(?:[-–]\d{2}|\s)?\b",
            re.IGNORECASE
        )
        self.units_pattern = re.compile(
            r"(?:\b(?:\d+(?:,\d{3})*(?:\.\d+)?|million|billion|thousand)?\s*)?"
            r"(?:tco2e|tco2-e|co2e|co₂e|co2-eq|co₂-eq"
            r"|mtco2e|mtco₂e|ktco2e|ktco₂e"
            r"|mt|kt"
            r"|tons?|tonnes?|metric\s*tons?)",
            re.IGNORECASE
        )

    def process_company(self, company_name: str, sustainability_url: str):
        """Main entry point: downloads PDF, identifies relevant pages, parses them, saves raw output, updates CSV."""
        logger.info(f"Processing company: {company_name}")

        # 1) Download PDF
        pdf_file = self.download_pdf(sustainability_url, company_name)
        if not pdf_file:
            logger.error(f"Skipping {company_name} due to download failure.")
            return

        # 2) Identify relevant pages
        relevant_pages = self.find_relevant_pages(pdf_file)
        if not relevant_pages:
            logger.warning(f"No relevant pages found for {company_name}")
            return

        # 3) Parse the relevant pages with LlamaParse
        page_indices_str = ",".join(map(str, relevant_pages))
        pdf_file.seek(0)  # Reset pointer
        emissions_data, documents = self.extract_emissions_data(pdf_file, page_indices_str, company_name)

        if not emissions_data:
            logger.warning(f"Parsing returned no data for {company_name}")
            return

        # 4) Write raw LlamaParse output for debugging
        os.makedirs(PARSED_OUTPUTS_DIR, exist_ok=True)
        raw_output_file = os.path.join(
            PARSED_OUTPUTS_DIR, f"{company_name.replace(' ', '_')}_raw_parsed.md"
        )

        with open(raw_output_file, "w", encoding="utf-8") as f:
            f.write(f"# {company_name} - Raw LlamaParse Output\n\n")
            f.write(f"Pages processed: {page_indices_str}\n\n")
            f.write("---\n\n")
            for doc in documents:
                content = doc.get_content()
                # Write the entire text chunk
                f.write(content)
                f.write("\n\n---\n\n")

        logger.info(f"Raw parse saved: {raw_output_file}")

        # 5) Update CSV with new data
        self.update_csv(company_name, emissions_data, OUTPUT_CSV)

    def download_pdf(self, url: str, company_name: str) -> BytesIO | None:
        """Download PDF via a browser-like session (3 retries). Returns BytesIO or None on failure."""
        try:
            session = requests.Session()
            adapter = requests.adapters.HTTPAdapter(max_retries=3)
            session.mount("http://", adapter)
            session.mount("https://", adapter)

            headers = {
                "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                               " AppleWebKit/537.36 (KHTML, like Gecko) "
                               "Chrome/111.0.0.0 Safari/537.36"),
                "Accept": "application/pdf,*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-US,en;q=0.9",
            }
            response = session.get(url, timeout=30, headers=headers, allow_redirects=True)
            response.raise_for_status()

            return BytesIO(response.content)

        except Exception as exc:
            logger.error(f"Download error for {company_name}: {exc}")
            return None

    def find_relevant_pages(self, pdf_file: BytesIO) -> list[int]:
        """Return a sorted list of pages referencing Scope 1/2, year, and units."""
        relevant_pages = []
        try:
            reader = PyPDF2.PdfReader(pdf_file, strict=False)
            for page_index in range(len(reader.pages)):
                page_text = reader.pages[page_index].extract_text() or ""
                text_lower = page_text.lower()

                if (self.pattern_scope1.search(text_lower)
                    and self.pattern_scope2.search(text_lower)
                    and self.patterns_year.search(text_lower)
                    and self.units_pattern.search(text_lower)):
                    relevant_pages.append(page_index)
                    logger.debug(f"Page {page_index} relevant.")
            return sorted(set(relevant_pages))
        except Exception as exc:
            logger.error(f"Error in find_relevant_pages: {exc}")
            return []

    def extract_emissions_data(
        self, pdf_file: BytesIO, page_indices_str: str, company_name: str
    ) -> tuple[dict | None, list]:
        """
        1) Write PDF to temp file
        2) Parse relevant pages with LlamaParse
        3) Combine their JSON blocks to pick the best
        """
        try:
            with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as temp_file:
                temp_file.write(pdf_file.getvalue())
                temp_path = temp_file.name

            parser = LlamaParse(
                api_key=self.api_key,
                result_type="markdown",
                verbose=False,
                language="en",
                num_workers=4,
                table_extraction_mode="full",
                target_pages=page_indices_str,
                parsing_instruction="""
                This is a company sustainability report. Extract Scope 1 and Scope 2 emissions data for all available years with units.
                For Scope 2, note if it's "market-based" or "location-based."
                If no data is available for a category, use null.

                Return a single JSON object:
                {
                  "scope1": {"year": [value, unit]},
                  "scope2_market": {"year": [value, unit]},
                  "scope2_location": {"year": [value, unit]}
                }
                """,
                is_formatting_instruction=True
            )

            documents = parser.load_data(
                temp_path,
                extra_info={
                    "file_name": f"{company_name}.pdf",
                    "processed_date": datetime.now().isoformat()
                }
            )
            os.unlink(temp_path)  # clean up

            final_data = self._combine_document_data(documents)
            return final_data, documents

        except Exception as exc:
            logger.error(f"extract_emissions_data error for {company_name}: {exc}")
            return None, []

    def _combine_document_data(self, documents: list) -> dict:
        best_data = None
        max_points = 0
        code_fence_pattern = re.compile(r"```json\s*(.*?)```", re.DOTALL | re.IGNORECASE)

        for doc in documents:
            content = doc.get_content()
            if not content:
                continue

            blocks = code_fence_pattern.findall(content)
            for block in blocks:
                try:
                    data = json.loads(block.strip())
                except Exception as exc:
                    logger.error(f"Failed to parse JSON block: {exc}")
                    continue

                # Improved scoring system
                current_points = 0
                for scope_key in ["scope1", "scope2_market", "scope2_location"]:
                    scope_dict = data.get(scope_key, {})
                    if isinstance(scope_dict, dict):
                        for year_data in scope_dict.values():
                            # Properly check if it's a valid [value, unit] pair
                            if (isinstance(year_data, list) and 
                                len(year_data) == 2 and 
                                year_data[0] is not None and 
                                year_data[1] is not None):
                                current_points += 1

                if current_points > max_points:
                    best_data = data
                    max_points = current_points
                    logger.debug(f"New best data found with {current_points} points")

        if not best_data:
            return {
                "scope1": {},
                "scope2_market": {},
                "scope2_location": {}
            }
        return best_data

    def update_csv(self, company_name: str, emissions_data: dict, csv_path: str):
        """
        Flatten the chosen emissions_data to rows and append to CSV:
          company, year, scope1_value, scope1_unit, scope2_location_value, scope2_location_unit, scope2_market_value, scope2_market_unit
        """
        logger.info(f"Updating CSV {csv_path} with data for {company_name}")
        rows = []

        s1_dict = emissions_data.get("scope1", {})
        s2m_dict = emissions_data.get("scope2_market", {})
        s2l_dict = emissions_data.get("scope2_location", {})

        # Gather all years
        all_years = set(s1_dict.keys()) | set(s2m_dict.keys()) | set(s2l_dict.keys())

        for year in sorted(all_years):
            s1 = s1_dict.get(year, [None, None])
            s2m = s2m_dict.get(year, [None, None])
            s2l = s2l_dict.get(year, [None, None])

            # Ensure each is [val, unit]
            if not isinstance(s1, list) or len(s1) != 2:
                s1 = [None, None]
            if not isinstance(s2m, list) or len(s2m) != 2:
                s2m = [None, None]
            if not isinstance(s2l, list) or len(s2l) != 2:
                s2l = [None, None]

            rows.append({
                "company": company_name,
                "year": year,
                "scope1_value": s1[0],
                "scope1_unit": s1[1],
                "scope2_location_value": s2l[0],
                "scope2_location_unit": s2l[1],
                "scope2_market_value": s2m[0],
                "scope2_market_unit": s2m[1],
            })

        new_df = pd.DataFrame(rows)
        if os.path.exists(csv_path):
            existing_df = pd.read_csv(csv_path)
            combined = pd.concat([existing_df, new_df], ignore_index=True)
            combined.to_csv(csv_path, index=False)
        else:
            new_df.to_csv(csv_path, index=False)

        logger.info(f"Appended new results to {csv_path}")


if __name__ == "__main__":
    if not LLAMA_API_KEY:
        raise ValueError("Missing LLAMA_API_KEY in environment variables.")

    if len(sys.argv) < 3:
        print("Usage: python src/scripts/retrieve_emissions_llama_parse.py <company_name> <sustainability_report_url>")
        sys.exit(1)

    company_arg = sys.argv[1]
    pdf_url_arg = sys.argv[2]

    extractor = EmissionsDataExtractor(LLAMA_API_KEY)
    extractor.process_company(company_arg, pdf_url_arg)
