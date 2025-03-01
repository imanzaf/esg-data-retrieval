import os
import sys

from dotenv import load_dotenv
from loguru import logger

load_dotenv()
sys.path.append(os.getenv("ROOT_DIR"))

from src.find.company_profile import CompanyProfile  # noqa: E402

# temporarily hardcoding variables here
# TODO - switch to retrieve from inputs to flask app
ROOT_DATA_DIR = os.getenv("ROOT_DIR")
COMPANY_IDENTIFIER = (
    "GB00BNC5T391"  # note: src/extract/tables.py requires ISIN currently
)

if __name__ == "__main__":
    # get the ticker symbol and company name from ISIN
    company = CompanyProfile(COMPANY_IDENTIFIER, "ISIN")
    logger.info(f"Retrieved details for {company.name}")
