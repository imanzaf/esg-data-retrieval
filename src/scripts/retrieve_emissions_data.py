import os
import sys
import time
from datetime import datetime, timedelta

import pandas as pd
from dotenv import load_dotenv
from loguru import logger

# Load environment variables from .env file
load_dotenv()
# Get ROOT_DIR from the environment variables
ROOT_DIR = os.getenv("ROOT_DIR")
OUTPUT_DIR = os.getenv("ROOT_OUTPUT_PATH")
# append path
sys.path.append(f"{os.getenv('ROOT_DIR')}")

from src.extract.tables import TableExtractor  # noqa: E402
from src.find.company_profile import CompanyProfile  # noqa: E402
from src.find.esg_reports import ESGReports  # noqa: E402
from src.utils import table_data_filtering  # noqa: E402
from src.utils.data import download_pdf_from_urls  # noqa: E402
from src.utils.data_models import TableParsers  # noqa: E402

def get_emissions_data(identifier, idType, parser):
    company = CompanyProfile(identifier, idType)

    # check cache for data
    try:
        import os
        import pandas as pd
        import logging

        logger = logging.getLogger(__name__)

        cache_dir = os.path.join(OUTPUT_DIR)
        if not os.path.exists(cache_dir):
            logger.error(f"Cache directory does not exist: {cache_dir}")
            return None

        esg_file_path = None

        def is_recent_file(file_path, days=30):
            """Checks if a file was modified within the last `days` days."""
            if os.path.exists(file_path):
                file_mtime = datetime.fromtimestamp(os.path.getmtime(file_path))
                return file_mtime >= (datetime.now() - timedelta(days=days))
            return False

        if idType == "name":
            # Get all folder names in the cache directory
            folder_names = [folder for folder in os.listdir(cache_dir) if
                            os.path.isdir(os.path.join(cache_dir, folder))]

            # Find matching folder
            matching_folder = next(
                (folder for folder in folder_names if
                 company.name.upper().replace(" ", "_") in folder.upper() or folder.upper() in company.name.upper()),
                None
            )

            if matching_folder:
                folder_path = os.path.join(cache_dir, matching_folder)
                esg_file_path = os.path.join(folder_path, "esg_data.csv")

        else:
            # For other idTypes, check the standard company output path
            esg_file_path = os.path.join(company.output_path, "esg_data.csv")

        # If the ESG file exists and is recent, load it
        if esg_file_path and os.path.exists(esg_file_path):
            if is_recent_file(esg_file_path):
                try:
                    data = pd.read_csv(esg_file_path)
                    logger.info(f"Loaded ESG data from {esg_file_path} for company {company.name}")
                    return data
                except Exception as e:
                    logger.error(f"Error reading ESG data from {esg_file_path}: {e}")
            else:
                logger.warning(f"ESG data file {esg_file_path} is older than one month, ignoring cache.")

        logger.info(f"No recent cached data found for {company.name}")

        # Load fresh data
        esg_file_path = os.path.join(company.output_path, "esg_data.csv")
        if is_recent_file(esg_file_path):
            if os.path.exists(esg_file_path):
                try:
                    data = pd.read_csv(esg_file_path)
                    logger.info(f"Loaded ESG data for {company.name}")
                    return data
                except Exception as e:
                    logger.error(f" {esg_file_path}: {e}")

    except Exception:
        logger.warning(
            "Unable to retrieve recent cached data. Retrieving emissions data from web..."
        )

    esg_reports = ESGReports(company)
    # Loop over urls until emissions data retrieved
    for url in esg_reports.urls.values():
        logger.info(f"Trying extraction with {url}")
        try:
            # Download pdf file
            path = download_pdf_from_urls([url], esg_reports.output_path)
            # get emissions data
            output = TableExtractor(
                company, path, parser, esg_reports.output_path
            ).extract()
            if output not in [None, [], False]:
                break
        except Exception as e:
            logger.debug(f"Unable to parse data from {url}: {e}")
            continue

    # TODO - pass tables as objects
    data = table_data_filtering.filter_tables(esg_reports.output_path, parser)
    return data


if __name__ == "__main__":
    start = time.time()

    identifier = "US5949181045"
    idType = "isin"
    parser = TableParsers.DOCLING
    data = get_emissions_data(identifier, idType, parser)

    end = time.time()
    total = end - start

    logger.info(f"time taken: {total}")
