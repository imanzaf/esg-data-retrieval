import os
import sys
import time

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
        data = pd.read_csv(os.path.join(company.output_path, "esg_data.csv"))
        logger.info(f"Found cached data for {company.name}")
        return data
    except Exception:
        logger.warning(
            "Unable to retrieve cached data. Retrieving emissions data from web..."
        )

    esg_reports = ESGReports(company)
    # Loop over urls until emissions data retrieved
    for url in esg_reports.urls.values():
        try:
            # Download pdf file
            path = download_pdf_from_urls([url], company.output_path)
            # get emissions data
            output = TableExtractor(company, path, parser).extract()
            if output not in [None, [], False]:
                break
        except Exception as e:
            logger.debug(f"Unable to parse data from {url}: {e}")
            continue

    # TODO - pass tables as objects
    data = table_data_filtering.filter_tables(company.output_path, parser)
    return data


# Example Usage
if __name__ == "__main__":
    start = time.time()

    identifier = "US67066G1040"
    idType = "isin"
    parser = TableParsers.DOCLING
    data = get_emissions_data(identifier, idType, parser)

    end = time.time()
    total = end - start

    logger.info(f"time taken: {total}")
