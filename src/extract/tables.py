"""
Methods for extracting emissions tables from ESG report using PyPDF and Docling
"""
from typing import List
from loguru import logger
import dateutil.relativedelta
from PyPDF2 import PdfReader, PdfWriter
from PyPDF2._page import PageObject
from docling.document_converter import DocumentConverter
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv
from datetime import datetime
import os
import sys
import tabula
import re

load_dotenv()
logger.info(os.getenv('ROOT_DIR'))
sys.path.append(f"{os.getenv('ROOT_DIR')}")
from src.utils.data_models import RegexPatterns, Company, TableParsers




class TableExtractor:
    def __init__(self, company: Company, file_path: str, parser: TableParsers):
        self.company = company
        self.file_path = file_path
        self.file_name = file_path.split("/")[-1].replace(".pdf", "")
        self.output_dir = f"{os.getenv('ROOT_DIR')}/data/cache/{self.company.isin}"
        self.parser = parser.value

        # create output dir
        os.makedirs(self.output_dir, exist_ok=True)
    
    def extract(self):
        # check for cached data
        cached_tables = self._get_tables_from_cache()
        if cached_tables is not None:
            return cached_tables

        tables = self._extract()
        if tables is None:
            logger.error(f"Unable to extract tables for {self.company.isin}")
            return None
        self._save_tables(tables)
        return tables

    def _extract(self):
        """
        Extract emissions tables
        """
        # Identify relevant pages
        pdf = self._read_pdf()
        pages, indeces = self._filter_pdf_pages(pdf)
        if not pages:
            logger.error(f"No relevant pages found for {self.company.name}. Returning None.")
            return None
        # parse document
        if self.parser == TableParsers.DOCLING.value:
            # write filtered pdf to cache
            filtered_file_path = f"{self.output_dir}/{self.file_name}-filtered.pdf"
            self._write_pages_to_pdf(pages, filtered_file_path)
            # extract from filtered pdf
            emissions_tables = self._extract_with_docling(filtered_file_path)
            return emissions_tables
        elif self.parser == TableParsers.TABULA.value:
            emissions_tables = self._extract_with_tabula(indeces)
            return emissions_tables
        else:
            logger.error(f"Valid parser not specified. Returning None.")
            return None

    def _extract_with_docling(self, file_path):
        """
        Extract tables using docling
        """
        # parse document using docling
        doc_converter = DocumentConverter()
        conv_res = doc_converter.convert(file_path)
        tables = [table.export_to_dataframe() for table in conv_res.document.tables]
        return tables
    
    def _extract_with_tabula(self, page_indeces):
        tables = tabula.read_pdf(self.file_path, pages=page_indeces, multiple_tables=True)
        return tables

    def _read_pdf(self):
        reader = PdfReader(self.file_path, strict=False)
        return reader.pages
    
    def _write_pages_to_pdf(self, pages, path):
        writer = PdfWriter()
        for page in pages:
            writer.add_page(page)
        with open(path, "wb") as file:
            writer.write(file)

    def _save_tables(self, tables: List[pd.DataFrame]):
        # create output dir (if it doesn't exist)
        output_dir = Path(f"{self.output_dir}/{self.parser}")
        output_dir.mkdir(parents=True, exist_ok=True)
        
        for idx, table in enumerate(tables):
            # Save the table as csv
            element_csv_filepath = (
                output_dir / f"{self.file_name}-table-{idx+1}.csv"
            )
            table.to_csv(element_csv_filepath)

    def _get_tables_from_cache(self):
        parser_dir = f"{self.output_dir}/{self.parser}"
        if os.path.isdir(parser_dir):
            last_modified_times = [{f"{parser_dir}/{file}": datetime.fromtimestamp(os.path.getmtime(f"{parser_dir}/{file}"))} for file in os.listdir(parser_dir)]
            # filter for files modified within past month
            current_date = datetime.today()
            cutoff_date = current_date - dateutil.relativedelta.relativedelta(months=1)
            valid_files = []
            for item in last_modified_times:
                if item.values()[0] >= cutoff_date:
                    valid_files.append(item.keys()[0])
            # load tables if any present
            if valid_files:
                tables = [pd.read_csv(file) for file in valid_files]
                return tables
            else:
                logger.warning("No cached data found.")
                return None

    def _filter_pdf_pages(self, pdf_pages):
        """
        Locate pages that mention Scope 1, Scope 2, years, and units.
        """
        pages = []
        indeces = []
        for idx, page in enumerate(pdf_pages):
            try:
                page_text = page.extract_text().lower()
                if (
                    re.search(RegexPatterns.SCOPE1.value, page_text, re.IGNORECASE)
                    and re.search(RegexPatterns.SCOPE2.value, page_text, re.IGNORECASE)
                    and any([re.search(RegexPatterns.YEAR_1.value, page_text, re.IGNORECASE), re.search(RegexPatterns.YEAR_2.value, page_text, re.IGNORECASE)])  # TODO - make this optional??
                    and any([re.search(RegexPatterns.UNITS_1.value, page_text, re.IGNORECASE), re.search(RegexPatterns.UNITS_2.value, page_text, re.IGNORECASE)])
                ):
                    pages.append(page)
                    indeces.append(idx)
                    logger.debug(f"Page {idx} is relevant.")
            except Exception as e:
                logger.warning(f"Unable to process page {idx}: {e}")
        return pages, indeces

if __name__ == "__main__":
    company = Company(isin="US0378331005", name="APPLE")
    file_path = "data/archive/AAPL/Apple_Environmental_Progress_Report_2024.pdf"

    extractor = TableExtractor(company, file_path, TableParsers.DOCLING)
    tables = extractor.extract()
    logger.info(f"Emissions tables for {company.name}:")
    logger.info(tables)
