import json
import os
import sys

from dotenv import load_dotenv
from loguru import logger

load_dotenv()

sys.path.append(os.getenv("ROOT_DIR"))

from src.find.company_profile import CompanyProfile  # noqa: E402
from src.utils.data import download_pdf_from_urls  # noqa: E402

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
    clean_company_label = (
        company.name.split(" ")[0].upper() if company.ticker is None else company.ticker
    )
    root_save_dir = f"{ROOT_DATA_DIR}/data/{clean_company_label}"
    # create directory if it doesn't exist
    os.makedirs(root_save_dir, exist_ok=True)
    # save company details to json
    with open(f"{root_save_dir}/{clean_company_label}.json", "w") as f:
        json.dump(company.__dict__, f, indent=4)
    # download esg report
    download_pdf_from_urls(company.esg_report_urls.values(), root_save_dir)

    logger.info("Done!")
