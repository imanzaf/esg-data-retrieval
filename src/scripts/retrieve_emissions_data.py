import os
import sys
from src.utils import table_data_filtering
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


def get_emissions_data(identifier, idType, parser):
    company = CompanyProfile(identifier, idType)
    # Loop over urls until emissions data retrieved
    for url in company.esg_report_urls.values():
        # Download pdf file
        path = data.download_pdf_from_urls([url], company.output_path)
        # get emissions data
        output = TableExtractor(
            company, path, parser
        ).extract()
        if output is not None:
            break

    path = os.path.join(company.output_path, parser.value)
    table_data_filtering.filter_tables(path)


# Example Usage
if __name__ == "__main__":
    identifier = "Apple"
    idType = "Name"
    parser = TableParsers.DOCLING
    get_emissions_data(identifier, idType, parser)
