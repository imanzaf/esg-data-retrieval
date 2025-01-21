import os
import sys

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
# Get ROOT_DIR from the environment variables
ROOT_DIR = os.getenv("ROOT_DIR")
OUTPUT_DIR = os.getenv("ROOT_OUTPUT_PATH")
# append path
sys.path.append(f"{os.getenv('ROOT_DIR')}")

from src.extract.tables import TableExtractor  # noqa: E402
from src.find.company_profile import CompanyProfile  # noqa: E402
from src.utils import data  # noqa: E402
from src.utils.data_models import TableParsers  # noqa: E402


def get_emissions_data(identifier, idType):
    company = CompanyProfile(identifier, idType)
    # Loop over urls until emissions data retrieved
    for url in company.esg_report_urls.values():
        # Download pdf file
        path = data.download_pdf_from_urls([url], os.path.join(OUTPUT_DIR))
        # get emissions data
        output = TableExtractor(
            company, path, [TableParsers.DOCLING, TableParsers.TABULA]
        ).extract()
        if output is not None:
            break


# Example Usage
if __name__ == "__main__":
    identifier = "US2546871060"
    idType = "ISIN"
    get_emissions_data(identifier, idType)
