"""
Methods for extracting emissions tables from ESG report using PyPDF and Docling
"""

import os
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import List, Union

import dateutil.relativedelta
import pandas as pd
import tabula
from docling.document_converter import DocumentConverter
from dotenv import load_dotenv
from loguru import logger
from PyPDF2 import PdfReader, PdfWriter

from src.find.company_profile import CompanyProfile

load_dotenv()

sys.path.append(f"{os.getenv('ROOT_DIR')}")

from src.utils.data_models import Company, RegexPatterns, TableParsers  # noqa: E402


class TableExtractor:
    """
    Methods for extracting tables from PDF using docling or tabula
    """

    def __init__(
        self,
        company: CompanyProfile,
        file_path: str,
        parser: Union[TableParsers, List[TableParsers]],
    ):
        self.company = company
        self.file_path = file_path
        self.file_name = os.path.basename(file_path).replace(".pdf", "")
        self.output_dir = company.output_path
        self.parser = parser.value

        # create output dir
        os.makedirs(self.output_dir, exist_ok=True)

    def extract(self):
        """
        1. Returns list of extracted tables as pandas dataframes
        2. Saves tables to cache
        """
        # check for cached data
        cached_tables = self._get_tables_from_cache()
        if cached_tables is not None:
            return cached_tables

        if isinstance(self.parser, List):
            all_tables = []
            for parser in self.parser:
                logger.info(f"Extracting data for {parser.value}")
                logger.info(datetime.now())
                # create output dir (if it doesn't exist)
                output_dir_parser = Path(f"{self.output_dir}/{parser}")
                output_dir_parser.mkdir(parents=True, exist_ok=True)
                # extract and save tables
                tables = self._extract(parser)
                self._save_tables(tables, output_dir_parser)
                all_tables.append(tables)
        else:
            # extract tables
            all_tables = self._extract(self.parser)
            output_dir_parser = Path(f"{self.output_dir}/{self.parser}")
            output_dir_parser.mkdir(parents=True, exist_ok=True)
            # save tables
            self._save_tables(all_tables, output_dir_parser)

        return all_tables

    def _extract(self, parser):
        """
        Method for extracting tables for specified parser.

        Returns
            emissions_tables (list[pd.DataFrame]): list of extracted tables
        """
        # Identify relevant pages
        pdf = self._read_pdf()
        pages, indeces = self._filter_pdf_pages(pdf)
        if not pages:
            logger.error(
                f"No relevant pages found for {self.company.name}. Returning None."
            )
            return None

        # parse document
        if parser == TableParsers.DOCLING.value:
            # write filtered pdf to cache
            filtered_file_path = f"{self.output_dir}/{self.file_name}-filtered.pdf"
            self._write_pages_to_pdf(pages, filtered_file_path)
            # extract from filtered pdf
            emissions_tables = self._extract_with_docling(filtered_file_path)
            return emissions_tables
        elif parser == TableParsers.TABULA.value:
            emissions_tables = self._extract_with_tabula(indeces)
            return emissions_tables
        else:
            logger.error(f"Invalid parsesr {self.parser} specified.")
            return None

    def _extract_with_docling(self, file_path):
        """
        Extract tables using docling.
        """
        # parse document using docling
        doc_converter = DocumentConverter()
        conv_res = doc_converter.convert(file_path)
        tables = [table.export_to_dataframe() for table in conv_res.document.tables]
        return tables

    def _extract_with_tabula(self, page_indeces):
        """
        Extract tables using tabula.
        """
        tables = tabula.read_pdf(
            self.file_path, pages=page_indeces, multiple_tables=True
        )
        return tables

    def _read_pdf(self):
        """
        Read PDF using PyPDF2.

        Returns
            pages (list[PageObject]): list of page objects returned by PyPDF2
        """
        reader = PdfReader(self.file_path, strict=False)
        return reader.pages

    def _write_pages_to_pdf(self, pages, path):
        """
        Write pages to pdf file.

        Args
            pages (list[PageObject]): list of page objects to write to file
            path (str): output file path to write pages to
        """
        writer = PdfWriter()
        for page in pages:
            writer.add_page(page)
        with open(path, "wb") as file:
            writer.write(file)

    def _save_tables(self, tables: Union[List[pd.DataFrame], None], output_dir):
        """
        Save tables to output dir

        Args
            tables (list[pd.DataFrame]): list of tables to write to folder
        """
        if tables is None:
            logger.error(f"No tables found for {self.company.isin}")
            return None

        for idx, table in enumerate(tables):
            # Save the table as csv
            element_csv_filepath = os.path.join(
                output_dir, f"{self.file_name}-table-{idx+1}.csv"
            )
            table.to_csv(element_csv_filepath)

    def _get_tables_from_cache(self):
        """
        Load tables from cache if recently saved
        """
        # Define the root output path and process the company name
        ROOT_OUTPUT_PATH = os.getenv("ROOT_OUTPUT_PATH")
        company_name = (
            str(self.company.name).upper().replace(" ", "_").replace("/", "_")
        )
        parser_dir = None
        # Check if the company name exists in the folder name
        for folder in os.listdir(ROOT_OUTPUT_PATH):
            if (company_name in folder) or (folder in company_name):
                folder_path = os.path.join(ROOT_OUTPUT_PATH, folder)
                # Check if the folder_path contains a subfolder named self.parser
                if os.path.isdir(folder_path):
                    for subfolder in os.listdir(folder_path):
                        if subfolder == self.parser and os.path.isdir(
                            os.path.join(folder_path, subfolder)
                        ):
                            parser_dir = os.path.join(folder_path, subfolder)
                            break

                if parser_dir:  # If the parser directory is found, break the outer loop
                    break

        if parser_dir is None:
            logger.debug("No cached data found.")
            return None
        # check if cache path exists

        if os.path.isdir(parser_dir):
            last_modified_times = [
                {
                    f"{parser_dir}/{file}": datetime.fromtimestamp(
                        os.path.getmtime(f"{parser_dir}/{file}")
                    )
                }
                for file in os.listdir(parser_dir)
            ]
            # filter for files modified within past month
            current_date = datetime.today()
            cutoff_date = current_date - dateutil.relativedelta.relativedelta(months=1)
            valid_files = []
            for item in last_modified_times:
                # Iterate over key-value pairs in the dictionary
                for file_path, modified_time in item.items():
                    if modified_time >= cutoff_date:
                        valid_files.append(file_path)

                # Load tables if any valid files are found
            if valid_files:
                tables = [
                    pd.read_csv(file)
                    for file in valid_files
                    if str(file).endswith(".csv")
                ]
                return tables
            else:
                logger.debug("No recent cached data found.")
                return None
        else:
            logger.debug("No cached data found.")
            return None

    def _filter_pdf_pages(self, pdf_pages):
        """
        Locate pages that include relevant information.

        Args
            pdf_pages (List[PageObject]): list of pages to filter

        Return
            pages (List[PageObject]): list of pages that could include relevant information
            indexed (List[int]): index of each page returned in pages list
        """
        pages = []
        indeces = []
        for idx, page in enumerate(pdf_pages):
            try:
                page_text = page.extract_text().lower()
                if (
                    re.search(RegexPatterns.SCOPE1.value, page_text, re.IGNORECASE)
                    and re.search(RegexPatterns.SCOPE2.value, page_text, re.IGNORECASE)
                    and any(
                        [
                            re.search(
                                RegexPatterns.YEAR_1.value, page_text, re.IGNORECASE
                            ),
                            re.search(
                                RegexPatterns.YEAR_2.value, page_text, re.IGNORECASE
                            ),
                        ]
                    )
                    and all(
                        [
                            re.search(
                                RegexPatterns.UNITS_1.value, page_text, re.IGNORECASE
                            ),
                            re.search(
                                RegexPatterns.UNITS_2.value, page_text, re.IGNORECASE
                            ),
                        ]
                    )
                ):
                    pages.append(page)
                    indeces.append(idx)
                    logger.debug(f"Page {idx} is relevant.")
            except Exception as e:
                logger.warning(f"Unable to process page {idx}: {e}")
        return pages, indeces


if __name__ == "__main__":
    company = Company(isin="US5949181045")
    file_path = "data/cache/US5949181045/RW1lmju.pdf"

    extractor = TableExtractor(company, file_path, TableParsers.TABULA)
    tables = extractor.extract()
    logger.info(f"Emissions tables for {company.identifier} extracted!")
