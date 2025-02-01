import os
import sys
import time


import pandas as pd
from dotenv import load_dotenv
from loguru import logger


# Load environment variables
load_dotenv()
# Get ROOT_DIR from environment variables
ROOT_DIR = os.getenv("ROOT_DIR")
OUTPUT_DIR = os.getenv("ROOT_OUTPUT_PATH")


# Ensure project root is on sys.path
sys.path.append(f"{os.getenv('ROOT_DIR')}")


from src.extract.tables import TableExtractor  # noqa: E402
from src.find.company_profile import CompanyProfile  # noqa: E402
from src.find.esg_reports import ESGReports  # noqa: E402
from src.utils.data import download_pdf_from_urls  # noqa: E402
from src.utils.data_models import TableParsers  # noqa: E402


# Use the LLM-based table filtering
from src.utils import llm_table_data_filtering  # noqa: E402


def get_emissions_data_pro(identifier, idType, parser):
   """
   Retrieve ESG emissions data using an LLM-based table filter.
   Returns both the LLM output and path to the relevant PDF.
   """
   company = CompanyProfile(identifier, idType)
   esg_reports = ESGReports(company)


   # Check for cached LLM data
   llm_output_file = os.path.join(esg_reports.output_path, "esg_data_llm.md")
   if os.path.isfile(llm_output_file):
       logger.info(f"Found cached LLM data for {company.name} at {llm_output_file}")
       with open(llm_output_file, "r", encoding="utf-8") as f:
           llm_markdown = f.read()
       # Look for PDFs but exclude ones with 'filtered' in the name
       pdf_files = [f for f in os.listdir(esg_reports.output_path)
                   if f.endswith('.pdf') and 'filtered' not in f.lower()]
       pdf_path = None
       if pdf_files:
           pdf_path = os.path.join(esg_reports.output_path, pdf_files[0])
       else:
           logger.warning(f"No PDF found in {esg_reports.output_path} for cached data.")
       return pd.DataFrame({"LLM_Output": [llm_markdown]}), pdf_path


   logger.warning("No cached LLM data found. Retrieving emissions data from web...")


   # Attempt to download & parse ESG PDFs
   successful_pdf_path = None
   for url in esg_reports.urls.values():
       logger.info(f"Trying extraction with {url}")
       try:
           local_pdf_path = download_pdf_from_urls([url], esg_reports.output_path)
           output = TableExtractor(company, local_pdf_path, parser, esg_reports.output_path).extract()
           if output not in [None, [], False]:
               successful_pdf_path = local_pdf_path
               break
       except Exception as e:
           logger.debug(f"Unable to parse data from {url}: {e}")
           continue


   # Use the LLM-based filter
   data = llm_table_data_filtering.filter_tables(esg_reports.output_path, parser)


   # Cache the LLM output as Markdown
   if not data.empty and "LLM_Output" in data.columns:
       llm_markdown = data["LLM_Output"].iloc[0]
       with open(llm_output_file, "w", encoding="utf-8") as f:
           f.write(llm_markdown)
       logger.info(f"Cached LLM data to {llm_output_file}")


   return data, successful_pdf_path
