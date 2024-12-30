import json
import os
import sys

from dotenv import load_dotenv
from loguru import logger

load_dotenv()

sys.path.append(os.getenv("ROOT_DIR"))

from src.find.company_profile import CompanyProfile  # noqa: E402
from src.utils.data import download_pdf_from_url  # noqa: E402

# temporarily hardcoding variables here
# TODO - switch to retrieve from inputs to flask app

ROOT_DATA_DIR = os.getenv("ROOT_DIR")
COMPANY_IDENTIFIER = "US0378331005"  # NVDA

if __name__ == "__main__":

    # get the ticker symbol and company name from ISIN
    company = CompanyProfile(COMPANY_IDENTIFIER)
    logger.info(f"Retrieved details for {company.name}")

    # save to df
    # TODO - update implementation for scalability once database is decided on
    logger.info("Saving to database...")
    root_save_dir = f"{ROOT_DATA_DIR}/data/{company.ticker}"
    # create directory if it doesn't exist
    os.makedirs(root_save_dir, exist_ok=True)
    # save company details to json
    with open(f"{root_save_dir}/{company.ticker}.json", "w") as f:
        json.dump(company.__dict__, f, indent=4)
    # download esg report
    download_pdf_from_url(company.esg_report_url, root_save_dir)

    logger.info("Done!")
