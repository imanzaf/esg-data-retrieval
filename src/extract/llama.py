"""
Scope 1 and 2 (location and market based) Emissions Extractor (llama)
"""

import json
import os
import re
import sys
from datetime import datetime

import pandas as pd
from dotenv import load_dotenv
from llama_parse import LlamaParse
from loguru import logger
from pydantic import BaseModel

# Load environment variables from .env file
load_dotenv()
sys.path.append(f"{os.getenv('ROOT_DIR')}")
LLAMA_API_KEY = os.getenv("LLAMA_API_KEY")


class LlamaExtractor(BaseModel):
    api_key: str = LLAMA_API_KEY

    company_name: str
    filtered_pdf_path: str
    output_path: str

    def process_company(self):
        # Main entry point: downloads PDF, identifies relevant pages, parses them, saves raw output, updates CSV.
        logger.info(f"Processing company: {self.company_name}")

        emissions_data = self.extract_emissions_data(
            self.filtered_pdf_path, self.company_name
        )
        if not emissions_data:
            logger.warning(f"Parsing returned no data for {self.company_name}")
            return

        output_path = f"{self.output_path}/esg_data.csv"
        logger.info("Writing to CSV...")
        # 5) Update CSV with extracted data
        self.update_csv(self.company_name, emissions_data, output_path)

    # Actually runs the LlamaParse logic on the relevant pages,
    # and merges JSON blocks to find the best data
    def extract_emissions_data(
        self, pdf_file: str, company_name: str
    ):  # -> tuple[dict | None, list]:

        try:
            parser = LlamaParse(
                api_key=self.api_key,
                result_type="markdown",
                verbose=False,
                language="en",
                num_workers=4,
                table_extraction_mode="full",
                # target_pages=page_indices_str,
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
                is_formatting_instruction=True,
            )

            documents = parser.load_data(
                pdf_file,
                extra_info={
                    "file_name": f"{company_name}.pdf",
                    "processed_date": datetime.now().isoformat(),
                },
            )

            final_data = self._combine_document_data(documents)
            return final_data

        except Exception as exc:
            logger.error(f"extract_emissions_data error for {company_name}: {exc}")
            return None, []

    # Walks through each LlamaParse "document" output,
    # looking for JSON code blocks and scoring them
    def _combine_document_data(self, documents: list) -> dict:
        best_data = None
        max_points = 0
        code_fence_pattern = re.compile(
            r"```json\s*(.*?)```", re.DOTALL | re.IGNORECASE
        )
        year_pattern = re.compile(
            r"^(?:FY)?\d{2,4}$"
        )  # Matches FY20, 20, 2020, 1980, etc.

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

                # Skip if any keys contain non-year data
                is_year_based = True
                for scope_key in ["scope1", "scope2_market", "scope2_location"]:
                    scope_dict = data.get(scope_key, {})
                    if isinstance(scope_dict, dict):
                        for year in scope_dict.keys():
                            if not year_pattern.match(str(year)):
                                is_year_based = False
                                break
                    if not is_year_based:
                        break

                if not is_year_based:
                    continue

                # Score the data by counting entries with valid numeric value + unit pairs
                current_points = 0
                for scope_key in ["scope1", "scope2_market", "scope2_location"]:
                    scope_dict = data.get(scope_key, {})
                    if isinstance(scope_dict, dict):
                        for year_data in scope_dict.values():
                            if (
                                isinstance(year_data, list)
                                and len(year_data) == 2
                                and year_data[0] is not None
                                and year_data[1] is not None
                            ):
                                current_points += 1

                if current_points > max_points:
                    best_data = data
                    max_points = current_points
                    logger.debug(f"New best data found with {current_points} points")

        if not best_data:
            return {"scope1": {}, "scope2_market": {}, "scope2_location": {}}
        return best_data

    # Appends emissions data (company, year, scope1_value, scope1_unit, scope2_location_value, scope2_location_unit, scope2_market_value, scope2_market_unit) to CSV
    def update_csv(self, company_name: str, emissions_data: dict, csv_path: str):

        s1_dict = emissions_data.get("scope1", {})
        s2m_dict = emissions_data.get("scope2_market", {})
        s2l_dict = emissions_data.get("scope2_location", {}) or {}

        standard_df = pd.DataFrame()
        standard_df["Metric"] = [
            "Scope 1",
            "Scope 2 (market-based)",
            "Scope 2 (location-based)",
        ]
        # Gather all years
        all_years = set(s1_dict.keys()) | set(s2m_dict.keys()) | set(s2l_dict.keys())
        logger.info(all_years)
        # Crete empty dataframe with columns metric, all years units
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

            standard_df[year] = [s1[0], s2m[0], s2l[0]]

        try:
            standard_df["Units"] = [
                (s1_dict.get(max(all_years)))[1],
                s2m_dict.get(max(all_years))[1],
                s2l_dict.get(max(all_years))[1],
            ]
        except Exception:
            if s1_dict.get(max(all_years))[1] is not None:
                standard_df["Units"] = s1_dict.get(max(all_years))[1]
            else:
                standard_df["Units"] = None
        standard_df.to_csv(csv_path, index=False)

        logger.info(f"Appended new results to {csv_path}")


# Main script entry point
if __name__ == "__main__":
    if not LLAMA_API_KEY:
        raise ValueError("Missing LLAMA_API_KEY in environment variables.")

    company_arg = "META"
    pdf_url_arg = "https://sustainability.fb.com/wp-content/uploads/2023/07/Meta-2023-Sustainability-Report-1.pdf"

    extractor = LlamaExtractor(LLAMA_API_KEY)
    extractor.process_company(company_arg, pdf_url_arg)
