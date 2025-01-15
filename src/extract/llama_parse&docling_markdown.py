"""
Sustainability Report Parser (LlamaParse or Docling)
----------------------------------------------------

NOTE ON M3 PRO MAC COMPATIBILITY:
The docling parser has dependencies that initially conflict with M3 Pro Macs.
To resolve this:
1. First install PyTorch nightly build for ARM:
   pip install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cpu
2. Then install docling:
   pip install "docling==2.15.1"

This script automates extracting emissions-related data (Scope 1, Scope 2, etc.)
from company sustainability PDFs. It works in five major steps:

1) **Download the PDF** from a given URL.
   - Uses `requests` with retry logic to fetch the PDF into a BytesIO object.

2) **Identify Relevant Pages** that mention Scope 1 or Scope 2, contain a range
   of possible years, and reference emissions units (e.g., tCO2e, mtCO2e).
   - Employs regular expressions on each page's text to find matches.

3) **Parse Only Those Pages** using either:
   - **LlamaParse** (if `--parser llama`): Automatically extracts tables with
     their units and contextual information.
   - **Docling** (if `--parser docling`): Extracts table structure but may miss
     units since it doesn't capture surrounding text context. Future improvement
     needed to extract text around tables for unit information.

4) **Save the Extracted Tables** to a Markdown file:
   `data/emissions_tables/{company}_raw_parsed.md`.

5) **[Optional] Send the Raw Markdown to DeepSeek** for final table structuring.
   This step requires a valid DeepSeek API key (must start with "sk-"). If not
   provided or invalid, the script will finish after step 4. If provided, two
   options are available:
   - **DeepSeek V3 Open Source**: Free to download and run locally if you have
     sufficient compute resources (recommended: 32GB+ RAM, modern GPU)
   - **DeepSeek API**: If local compute is insufficient, use the API which costs
     ~99% less than OpenAI's API. Set `DEEPSEEK_API_KEY` to use.

   The DeepSeek prompt instructs it to create a "Key Table" (Scope 1 & Scope 2)
   plus breakdown tables for Scope 1, Scope 2 market-based, Scope 2 location-based,
   and Scope 3 (with total). The resulting final tables are then saved to:
   `data/emissions_tables/{company}_final_tables.md`.

Environment variables:
  Required:
  - LLAMA_API_KEY: Required for parsing PDFs with LlamaParse

  Optional:
  - DEEPSEEK_API_KEY: Must start with "sk-" if provided. If missing or invalid,
    script will only generate raw parsed tables
  - DEEPSEEK_BASE_URL: Defaults to https://api.deepseek.com

Usage examples:
  # NVIDIA
  python "src/extract/llama_parse&docling_markdown.py" "NVIDIA CORP" \
    "https://images.nvidia.com/aem-dam/Solutions/documents/FY2024-NVIDIA-Corporate-Sustainability-Report.pdf" \
    --parser llama

  python "src/extract/llama_parse&docling_markdown.py" "NVIDIA CORP" \
    "https://images.nvidia.com/aem-dam/Solutions/documents/FY2024-NVIDIA-Corporate-Sustainability-Report.pdf" \
    --parser docling

  # Microsoft
  python "src/extract/llama_parse&docling_markdown.py" "MICROSOFT CORP" \
    "https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RW1lmju" \
    --parser llama

  python "src/extract/llama_parse&docling_markdown.py" "MICROSOFT CORP" \
    "https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RW1lmju" \
    --parser docling

  # Amazon
  python "src/extract/llama_parse&docling_markdown.py" "AMAZON COM INC" \
    "https://sustainability.aboutamazon.com/2023-amazon-sustainability-report.pdf" \
    --parser llama

  python "src/extract/llama_parse&docling_markdown.py" "AMAZON COM INC" \
    "https://sustainability.aboutamazon.com/2023-amazon-sustainability-report.pdf" \
    --parser docling

  # Meta
  python "src/extract/llama_parse&docling_markdown.py" "META PLATFORMS INC CLASS A" \
    "https://sustainability.atmeta.com/wp-content/uploads/2024/08/Meta-2024-Sustainability-Report.pdf" \
    --parser llama

  python "src/extract/llama_parse&docling_markdown.py" "META PLATFORMS INC CLASS A" \
    "https://sustainability.atmeta.com/wp-content/uploads/2024/08/Meta-2024-Sustainability-Report.pdf" \
    --parser docling

  # Alphabet
  python "src/extract/llama_parse&docling_markdown.py" "ALPHABET INC CLASS A" \
    "https://www.smartenergydecisions.com/upload/research_+_reports/google-2024-environmental-report.pdf" \
    --parser llama

  python "src/extract/llama_parse&docling_markdown.py" "ALPHABET INC CLASS A" \
    "https://www.smartenergydecisions.com/upload/research_+_reports/google-2024-environmental-report.pdf" \
    --parser docling

  # Apple
  python "src/extract/llama_parse&docling_markdown.py" "APPLE INC" \
    "https://www.apple.com/environment/pdf/Apple_Environmental_Progress_Report_2024.pdf" \
    --parser llama

  python "src/extract/llama_parse&docling_markdown.py" "APPLE INC" \
    "https://www.apple.com/environment/pdf/Apple_Environmental_Progress_Report_2024.pdf" \
    --parser docling

  # Unilever
  python "src/extract/llama_parse&docling_markdown.py" "UNILEVER PLC" \
    "https://www.unilever.com/files/66bc4aea-608f-46ee-8da3-cde0ec8ebe90/unilever-annual-report-and-accounts-2023.pdf" \
    --parser llama

  python "src/extract/llama_parse&docling_markdown.py" "UNILEVER PLC" \
    "https://www.unilever.com/files/66bc4aea-608f-46ee-8da3-cde0ec8ebe90/unilever-annual-report-and-accounts-2023.pdf" \
    --parser docling
"""

import argparse
import os
import re
import tempfile
from io import BytesIO

import PyPDF2
import requests
from docling.backend.pypdfium2_backend import PyPdfiumDocumentBackend
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.document_converter import DocumentConverter, PdfFormatOption
from dotenv import load_dotenv
from llama_parse import LlamaParse
from loguru import logger
from openai import OpenAI

load_dotenv()
LLAMA_API_KEY = os.getenv("LLAMA_API_KEY")
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL")

# Default output directory
PARSED_OUTPUTS_DIR = "data/emissions_tables"


class EmissionsDataExtractor:
    def __init__(self, llama_api_key: str, deepseek_api_key: str, parser_choice: str):
        """
        parser_choice: 'llama' or 'docling'.
        """
        if not llama_api_key:
            raise ValueError("LLAMA_API_KEY is missing or invalid.")

        self.api_key = llama_api_key
        # Simple check: is it a valid DeepSeek key?
        self.deepseek_api_key = (
            deepseek_api_key
            if deepseek_api_key and deepseek_api_key.startswith("sk-")
            else None
        )
        self.deepseek_base_url = "https://api.deepseek.com"
        self.parser_choice = parser_choice

        # Regex patterns to identify relevant pages
        self.pattern_scope1 = re.compile(
            r"\b(scope\s*1|scope\s*i|scope\s*one)\b", re.IGNORECASE
        )
        self.pattern_scope2 = re.compile(
            r"\b(scope\s*2|scope\s*ii|scope\s*two)\b", re.IGNORECASE
        )
        self.patterns_year = re.compile(
            r"\b(?:FY|FISCAL\s*YEAR)?\s*(\d{2}|20\d{2})" r"(?:[-–]\d{2}|\s)?\b",
            re.IGNORECASE,
        )
        self.units_pattern = re.compile(
            r"(?:\b(?:\d+(?:,\d{3})*(?:\.\d+)?|million|billion|thousand)?"
            r"\s*(?:tco2e|tco2-e|co2e|co₂e|co2-eq|co₂-eq"
            r"|mtco2e|mtco₂e|ktco2e|ktco₂e"
            r"|mt|kt"
            r"|tons?|tonnes?|metric\s*tons?))",
            re.IGNORECASE,
        )

    def process_company(self, company_name: str, sustainability_url: str):
        """
        Main entry point: downloads PDF, identifies relevant pages, parses them,
        and sends to LLM for markdown table generation.
        """
        logger.info(
            f"Processing company: {company_name} via parser={self.parser_choice}"
        )

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

        # 3) Parse relevant pages with the chosen parser (LlamaParse or Docling)
        page_indices_str = ",".join(map(str, relevant_pages))
        pdf_file.seek(0)
        emissions_data = self.extract_emissions_data(
            pdf_file, page_indices_str, company_name, relevant_pages
        )
        if not emissions_data:
            logger.warning(f"Parsing returned no data for {company_name}")
            return

        # 4) Write raw parse output
        os.makedirs(PARSED_OUTPUTS_DIR, exist_ok=True)
        raw_output_file = os.path.join(
            PARSED_OUTPUTS_DIR, f"{company_name.replace(' ', '_')}_raw_parsed.md"
        )
        with open(raw_output_file, "w", encoding="utf-8") as f:
            f.write(
                f"# {company_name} - Raw {self.parser_choice.capitalize()} Output\n\n"
            )
            f.write(f"Pages processed: {page_indices_str}\n\n")
            f.write("---\n\n")
            f.write(emissions_data)
        logger.info(f"Raw parse saved: {raw_output_file}")

        # 5) Only proceed with DeepSeek if API key is provided and not empty
        if self.deepseek_api_key:
            logger.info(
                "DeepSeek API key found, proceeding with final table generation"
            )
            final_tables = self.send_to_deepseek(emissions_data)
            if final_tables:
                tables_file = os.path.join(
                    PARSED_OUTPUTS_DIR,
                    f"{company_name.replace(' ', '_')}_final_tables.md",
                )
                with open(tables_file, "w", encoding="utf-8") as f:
                    f.write(final_tables)
                logger.info(f"Final tables saved: {tables_file}")
        else:
            logger.info("No DeepSeek API key provided, skipping final table generation")

    def download_pdf(self, url: str, company_name: str) -> BytesIO | None:
        """
        Download PDF with retries. Returns BytesIO on success, or None on failure.
        """
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
            response = session.get(
                url, timeout=30, headers=headers, allow_redirects=True
            )
            response.raise_for_status()

            return BytesIO(response.content)

        except Exception as exc:
            logger.error(f"Download error for {company_name}: {exc}")
            return None

    def find_relevant_pages(self, pdf_file: BytesIO):
        """
        Locate pages that mention Scope 1, Scope 2, years, and units.
        """
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

    def extract_emissions_data(
        self,
        pdf_file: BytesIO,
        page_indices_str: str,
        company_name: str,
        relevant_pages: list[int],
    ) -> str | None:
        """
        Depending on parser_choice, either LlamaParse or Docling is used,
        but both only parse the relevant pages. If docling, we create a
        subset PDF with only those pages, then feed that subset to docling.
        """
        if self.parser_choice == "llama":
            return self.extract_with_llama(pdf_file, page_indices_str, company_name)
        else:
            return self.extract_with_docling(pdf_file, company_name, relevant_pages)

    def extract_with_llama(
        self, pdf_file: BytesIO, page_indices_str: str, company_name: str
    ) -> str | None:
        """
        LlamaParse approach: pass page_indices_str directly to the parser.
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
                parsing_instruction=(
                    "These pages are from company sustainability reports.\n"
                    "Return tables containing GHG emissions and environmental "
                    "data (e.g., Scope 1, Scope 2 (location-based or "
                    "market-based), Scope 3, and further breakdowns). "
                    "Ensure that the tables contain relevant units "
                    "(e.g., tCO2e, tonnes CO2e). Exclude any non-tabular text, "
                    "captions, and footnotes. If no table data is found, "
                    "return 'null'."
                ),
                is_formatting_instruction=False,
            )

            documents = parser.load_data(
                temp_path, extra_info={"file_name": f"{company_name}.pdf"}
            )
            os.unlink(temp_path)

            parsed_content = "\n\n---\n\n".join(
                doc.get_content() for doc in documents if doc.get_content()
            )
            return parsed_content if parsed_content.strip() else None

        except Exception as exc:
            logger.error(f"extract_with_llama error for {company_name}: {exc}")
            return None

    def extract_with_docling(
        self, pdf_file: BytesIO, company_name: str, relevant_pages: list[int]
    ) -> str | None:
        """
        Docling approach: create a new subset PDF with only the relevant pages,
        then parse with docling, then return Markdown for the found tables.
        """
        try:
            # 1) Create a subset PDF with only relevant_pages
            with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as temp_in:
                temp_in.write(pdf_file.getvalue())
                orig_pdf_path = temp_in.name

            subset_pdf_path = self.make_subset_pdf(
                orig_pdf_path, relevant_pages, company_name
            )

            # 2) Use Docling to parse that subset PDF - matching your working code
            pipeline_options = PdfPipelineOptions()
            pipeline_options.do_ocr = False
            pipeline_options.do_table_structure = True
            pipeline_options.table_structure_options.do_cell_matching = True

            doc_converter = DocumentConverter(
                format_options={
                    InputFormat.PDF: PdfFormatOption(
                        pipeline_options=pipeline_options,
                        backend=PyPdfiumDocumentBackend,
                    )
                }
            )

            logger.debug(f"Converting document: {subset_pdf_path}")
            conv_result = doc_converter.convert(subset_pdf_path)

            # 3) Export tables - matching your working code's approach
            markdown_chunks = []
            table_count = 0

            if hasattr(conv_result.document, "tables"):
                for table in conv_result.document.tables:
                    table_count += 1
                    markdown_chunks.append(table.export_to_markdown())
                    logger.debug(f"Found table {table_count}")

            # Clean up temp files
            os.unlink(orig_pdf_path)
            os.unlink(subset_pdf_path)

            if table_count == 0:
                logger.warning(f"No tables found in document for {company_name}")
                return None

            return "\n\n---\n\n".join(markdown_chunks)

        except Exception as exc:
            logger.error(f"extract_with_docling error for {company_name}: {exc}")
            logger.exception("Full traceback:")
            return None

    def make_subset_pdf(
        self, original_pdf_path: str, relevant_pages: list[int], company_name: str
    ) -> str:
        """
        Create a new PDF that contains only the pages in relevant_pages (0-based).
        Return the path to the new PDF.
        """
        try:
            reader = PyPDF2.PdfReader(original_pdf_path, strict=False)
            writer = PyPDF2.PdfWriter()

            for page_idx in relevant_pages:
                writer.add_page(reader.pages[page_idx])

            with tempfile.NamedTemporaryFile(
                suffix="_subset.pdf", delete=False
            ) as temp_out:
                writer.write(temp_out)
                subset_path = temp_out.name

            logger.debug(
                f"Subset PDF created for {company_name} with pages: {relevant_pages}"
            )
            return subset_path

        except Exception as exc:
            logger.error(f"Error creating subset PDF for docling: {exc}")
            return original_pdf_path  # fallback: original PDF if something fails

    def send_to_deepseek(self, raw_markdown: str) -> str | None:
        """
        Sends the parsed markdown to DeepSeek to produce structured markdown tables.
        """
        if not self.deepseek_api_key:
            logger.error("Missing DEEPSEEK_API_KEY. Cannot proceed with LLM.")
            return None

        client = OpenAI(api_key=self.deepseek_api_key, base_url=self.deepseek_base_url)

        prompt_instructions = f"""
You are given sustainability report tables as markdown below:
{raw_markdown}

Please perform the following steps:

1. Identify the table(s) with the most complete year-by-year data for
   Scope 1, Scope 2 (market-based), and Scope 2 (location-based)
   from the provided markdown.
   - Use judgment to select tables with the most complete and likely
     accurate data across all years.
   - Prioritize completeness and consistency.
   - For Scope 2, include both market-based and location-based data if
     available, and explicitly note which is which.
   - Convert all values to tCO2e and keep units consistent across years.
   - Use null for years where data is missing or unavailable.

2. Create a **"Key Table"** in Markdown with columns for:
   | Category | Year | Emissions (tCO2e) | Notes |
   The rows should be:
     - Scope 1
     - Scope 2 (Market-based)
     - Scope 2 (Location-based)
   Include data for as many years as can be found (e.g., 2020, 2021, 2022, 2023).
   Convert all values to tCO2e. Use null for years where data is missing.

3. Create up to four additional Markdown tables (breakdown tables) if
   information is available; otherwise, return them with "No Data" or "N/A":
   - **Scope 1 Breakdown**:
     | Scope 1 Source / Subcategory | Year | Emissions (tCO2e) | Notes |
   - **Scope 2 Market-based Breakdown**:
     | Region or Business Unit | Year | Emissions (tCO2e) | Notes |
   - **Scope 2 Location-based Breakdown**:
     | Region or Business Unit | Year | Emissions (tCO2e) | Notes |
   - **Scope 3 Breakdown**:
     | Scope 3 Category | Year | Emissions (tCO2e) | Notes |
     Always include a "Total Scope 3" row.

4. Return exactly **these five Markdown tables** in this order:
   A) Key Table
   B) Scope 1 Breakdown
   C) Scope 2 Market-based Breakdown
   D) Scope 2 Location-based Breakdown
   E) Scope 3 Breakdown (with Total)

5. Provide **no additional commentary**, just the five tables in Markdown format.
"""
        try:
            response = client.chat.completions.create(
                model="deepseek-chat",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are a concise assistant that returns only "
                            "the requested markdown tables with no additional text."
                        ),
                    },
                    {"role": "user", "content": prompt_instructions},
                ],
                temperature=0.2,
                max_tokens=4000,  # Increased for longer markdown tables
            )
            final_content = response.choices[0].message.content
            return final_content.strip()

        except Exception as exc:
            logger.error(f"DeepSeek API error: {exc}")
            return None


def main():
    parser = argparse.ArgumentParser(
        description="Parse a sustainability report PDF using either LlamaParse or Docling, then push to DeepSeek."
    )
    parser.add_argument("company_name", help="Company name, e.g. 'NVIDIA CORP'")
    parser.add_argument("sustainability_url", help="URL to the sustainability PDF")
    parser.add_argument(
        "--parser",
        choices=["llama", "docling"],
        default="llama",
        help="Choose 'llama' (default) or 'docling'",
    )
    args = parser.parse_args()

    # Validate LLAMA_API_KEY (required)
    if not LLAMA_API_KEY:
        raise ValueError("Missing LLAMA_API_KEY in environment variables.")

    # DEEPSEEK_API_KEY is optional
    if not DEEPSEEK_API_KEY:
        logger.warning(
            "No DEEPSEEK_API_KEY found. Will only generate raw parsed tables."
        )

    extractor = EmissionsDataExtractor(LLAMA_API_KEY, DEEPSEEK_API_KEY, args.parser)
    extractor.process_company(args.company_name, args.sustainability_url)


if __name__ == "__main__":
    main()
