"""
Sustainability report llama parse to markdown
---------------------------------------------

Steps:
1) Download the PDF from the given URL.
2) Parse the relevant pages using LlamaParse, determined by mentions of Scope 1, Scope 2, years/FY, and units.
3) Output tables to markdown in: data/parsed_outputs/{company}_raw_parsed.md
4) Send the raw parsed tables to LLM to pick results

Environment variables required:
  - LLAMA_API_KEY
  - OPENAI_API_KEY

Usage examples:
  python src/extract/llama_parse_markdown.py "NVIDIA CORP" "https://images.nvidia.com/aem-dam/Solutions/documents/FY2024-NVIDIA-Corporate-Sustainability-Report.pdf"
  python src/extract/llama_parse_markdown.py "MICROSOFT CORP" "https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RW1lmju"
  python src/extract/llama_parse_markdown.py "AMAZON COM INC" "https://sustainability.aboutamazon.com/2023-amazon-sustainability-report.pdf"
  python src/extract/llama_parse_markdown.py "META PLATFORMS INC CLASS A" "https://sustainability.atmeta.com/wp-content/uploads/2024/08/Meta-2024-Sustainability-Report.pdf"
  python src/extract/llama_parse_markdown.py "ALPHABET INC CLASS A" "https://www.smartenergydecisions.com/upload/research_+_reports/google-2024-environmental-report.pdf"
  python src/extract/llama_parse_markdown.py "APPLE INC" "https://www.apple.com/environment/pdf/Apple_Environmental_Progress_Report_2024.pdf"
"""

import os
import re
import sys
import tempfile
from io import BytesIO
import json

import PyPDF2
import requests
from dotenv import load_dotenv
from llama_parse import LlamaParse
from loguru import logger
import openai
from openai import OpenAI

load_dotenv()
LLAMA_API_KEY = os.getenv("LLAMA_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Default output directory
PARSED_OUTPUTS_DIR = "data/llama_markdown"


class EmissionsDataExtractor:
    def __init__(self, llama_api_key: str, openai_api_key: str):
        if not llama_api_key:
            raise ValueError("LLAMA_API_KEY is missing or invalid.")
        if not openai_api_key:
            raise ValueError("OPENAI_API_KEY is missing or invalid.")

        self.api_key = llama_api_key
        self.openai_api_key = openai_api_key

        # Regex patterns to identify relevant pages
        self.pattern_scope1 = re.compile(
            r"\b(scope\s*1|scope\s*i|scope\s*one)\b", re.IGNORECASE
        )
        self.pattern_scope2 = re.compile(
            r"\b(scope\s*2|scope\s*ii|scope\s*two)\b", re.IGNORECASE
        )
        self.patterns_year = re.compile(
            r"\b(?:FY|FISCAL\s*YEAR)?\s*(\d{2}|20\d{2})(?:[-–]\d{2}|\s)?\b", re.IGNORECASE
        )
        self.units_pattern = re.compile(
            r"(?:\b(?:\d+(?:,\d{3})*(?:\.\d+)?|million|billion|thousand)?\s*"
            r"(?:tco2e|tco2-e|co2e|co₂e|co2-eq|co₂-eq"
            r"|mtco2e|mtco₂e|ktco2e|ktco₂e"
            r"|mt|kt"
            r"|tons?|tonnes?|metric\s*tons?))",
            re.IGNORECASE
        )

    def process_company(self, company_name: str, sustainability_url: str):
        """Main entry point: downloads PDF, identifies relevant pages, parses them, and sends to LLM."""
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
        pdf_file.seek(0)  # Reset pointer to start
        emissions_data = self.extract_emissions_data(pdf_file, page_indices_str, company_name)

        if not emissions_data:
            logger.warning(f"Parsing returned no data for {company_name}")
            return

        # 4) Write raw LlamaParse output
        os.makedirs(PARSED_OUTPUTS_DIR, exist_ok=True)
        raw_output_file = os.path.join(
            PARSED_OUTPUTS_DIR, f"{company_name.replace(' ', '_')}_raw_parsed.md"
        )
        with open(raw_output_file, "w", encoding="utf-8") as f:
            f.write(f"# {company_name} - Raw LlamaParse Output\n\n")
            f.write(f"Pages processed: {page_indices_str}\n\n")
            f.write("---\n\n")
            f.write(emissions_data)

        logger.info(f"Raw parse saved: {raw_output_file}")

        # 5) Optionally send to OpenAI if API key exists
        if self.openai_api_key:
            final_json = self.send_to_openai(emissions_data)
            if final_json:
                json_output_file = os.path.join(
                    PARSED_OUTPUTS_DIR, f"{company_name.replace(' ', '_')}_final.json"
                )
                with open(json_output_file, "w", encoding="utf-8") as jf:
                    jf.write(final_json)
                logger.info(f"Final JSON saved: {json_output_file}")

    def download_pdf(self, url: str, company_name: str) -> BytesIO | None:
        """Download PDF with retries. Returns BytesIO on success, None on failure."""
        try:
            session = requests.Session()
            adapter = requests.adapters.HTTPAdapter(max_retries=3)
            session.mount("http://", adapter)
            session.mount("https://", adapter)

            headers = {
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/111.0.0.0 Safari/537.36"
                ),
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

    def find_relevant_pages(self, pdf_file: BytesIO):
        """Locate pages that mention Scope 1, Scope 2, years, and units."""
        relevant_pages = []
        try:
            reader = PyPDF2.PdfReader(pdf_file, strict=False)
            for page_index in range(len(reader.pages)):
                page_text = reader.pages[page_index].extract_text() or ""
                text_lower = page_text.lower()

                if (
                    self.pattern_scope1.search(text_lower)
                    and self.pattern_scope2.search(text_lower)
                    and self.patterns_year.search(text_lower)
                    and self.units_pattern.search(text_lower)
                ):
                    relevant_pages.append(page_index)
                    logger.debug(f"Page {page_index} is relevant.")
            return sorted(set(relevant_pages))
        except Exception as exc:
            logger.error(f"Error in find_relevant_pages: {exc}")
            return []

    def extract_emissions_data(self, pdf_file: BytesIO, page_indices_str: str, company_name: str):
        """Run LlamaParse on the relevant pages to extract tables in Markdown."""
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
                These pages are from company sustainability reports. 
                Return tables containing GHG emissions and environmental data (e.g., Scope 1, Scope 2 (location-based or market-based), Scope 3, and further breakdowns). 
                Ensure that the tables contain relevant units (e.g., tCO2e, tonnes CO2e).
                Exclude any non-tabular text, captions, and footnotes. If no table data is found, return 'null'.
                """,
                is_formatting_instruction=False
            )

            documents = parser.load_data(temp_path, extra_info={"file_name": f"{company_name}.pdf"})
            os.unlink(temp_path)

            # Combine all extracted markdown tables
            parsed_content = "\n\n---\n\n".join(
                doc.get_content() for doc in documents if doc.get_content()
            )
            return parsed_content

        except Exception as exc:
            logger.error(f"extract_emissions_data error for {company_name}: {exc}")
            return None

    def send_to_openai(self, raw_markdown: str) -> str | None:
        """
        Sends the parsed markdown to OpenAI with a prompt to produce the final JSON structure.
        """
        if not self.openai_api_key:
            logger.error("Missing OPENAI_API_KEY. Cannot proceed with LLM completion.")
            return None

        client = OpenAI(api_key=self.openai_api_key)

       
        prompt_instructions = f"""You are given sustainability report tables as markdown below.

{raw_markdown}

1. Analyze all tables and identify the one with the most complete year-by-year data for each scope (Scope 1, Scope 2 market-based, Scope 2 location-based).
2. Use the table data to populate the JSON structure below. For Scope 2, include both market-based and location-based data if available, and explicitly note which is which.
3. Convert all values to tCO2e, keeping units consistent across years.
4. Use null for years where data is missing or unavailable.
5. Return only the JSON structure below, with no explanations or additional text:

{{
  "scope1": {{"year": [value, "tCO2e"], ...}},
  "scope2_market": {{"year": [value, "tCO2e"], ...}},
  "scope2_location": {{"year": [value, "tCO2e"], ...}}
}}

Use judgment to select tables with the most complete and likely accurate data across all years. Prioritize completeness and consistency.
Analyze the following tables and return the JSON:"""

        try:
            response = client.chat.completions.create(
                model="gpt-4o",  
                messages=[
                    {
                        "role": "system",
                        "content": "You are a concise assistant that returns only the requested JSON."
                    },
                    {
                        "role": "user",
                        "content": prompt_instructions
                    }
                ],
                temperature=0.2,
                max_tokens=2000
            )

            # Extract the text content from the response
            final_content = response.choices[0].message.content
            return final_content.strip()

        except Exception as exc:
            logger.error(f"OpenAI API error: {exc}")
            return None


if __name__ == "__main__":
    if not LLAMA_API_KEY:
        raise ValueError("Missing LLAMA_API_KEY in environment variables.")
    if not OPENAI_API_KEY:
        raise ValueError("Missing OPENAI_API_KEY in environment variables.")

    if len(sys.argv) < 3:
        print(
            "Usage: python src/extract/llama_parse_markdown.py <company_name> <sustainability_report_url>"
        )
        sys.exit(1)

    company_arg = sys.argv[1]
    pdf_url_arg = sys.argv[2]

    extractor = EmissionsDataExtractor(LLAMA_API_KEY, OPENAI_API_KEY)
    extractor.process_company(company_arg, pdf_url_arg)