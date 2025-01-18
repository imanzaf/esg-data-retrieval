"""
Methods for extracting emissions tables from ESG report using PyPDF and Docling
"""
from typing import List
from src.utils.data_models import RegexPatterns, Company, TableParsers
from loguru import logger
import dateutil.relativedelta
import PyPDF2
from PyPDF2 import PdfReader, PdfWriter
from docling.document_converter import DocumentConverter
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv
from datetime import datetime
import os
import tabula


load_dotenv()


class TableExtractor:
    def __init__(self, company: Company, file_path: str, parser: TableParsers):
        self.company = company
        self.file_path = file_path
        self.file_name = file_path.split("/")[-1].replace(".pdf", "")
        self.output_dir = f"{os.getenv('ROOT_DIR')}/data/cache/{self.company.isin}"
        self.parser = parser
    
    def extract(self):
        # check for cached data
        cached_tables = self._get_tables_from_cache()
        if cached_tables is not None:
            return cached_tables

        tables = self._extract()
        self._save_tables()
        return tables

    def _extract(self):
        """
        Extract emissions tables
        """
        # Identify relevant pages
        pdf = self._read_pdf()
        filtered_pdf = self._filter_pdf_pages(pdf)
        if not filtered_pdf:
            logger.error(f"No relevant pages found for {self.company.name}. Returning None.")
            return None
        # parse document
        if self.parser == TableParsers.DOCLING:
            # write filtered pdf to cache
            filtered_file_path = f"{self.output_dir}/{self.file_name}-filtered.pdf"
            self._write_pages_to_pdf(filtered_pdf, filtered_file_path)
            # extract from filtered pdf
            emissions_tables = self._extract_with_docling(filtered_file_path)
            return emissions_tables
        elif self.parser == TableParsers.TABULA:
            emissions_tables = self._extract_with_tabula(filtered_pdf.keys())
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
        relevant_pages = []
        for idx, page in enumerate(pdf_pages):
            try:
                page_text = page.extract_text().lower()
                if (
                    RegexPatterns.scope1.search(page_text)
                    and RegexPatterns.scope2.search(page_text)
                    and RegexPatterns.year.search(page_text)  # TODO - make this optional??
                    and RegexPatterns.units.search(page_text)
                ):
                    relevant_pages.append({idx: page})
                    logger.debug(f"Page {idx} is relevant.")
            except Exception as e:
                logger.warning(f"Unable to process page {idx}: {e}")
        return relevant_pages
