import json
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
COMPANY_IDENTIFIER = "US0378331005"

if __name__ == "__main__":

    # get the ticker symbol and company name from ISIN
    company = CompanyProfile(COMPANY_IDENTIFIER)
    logger.info(f"Retrieved details for {company.name}")

    # save to df
    # TODO - update implementation for scalability once database is decided on
    logger.info("Saving to database...")
    with open(f"{ROOT_DATA_DIR}/data/{company.ticker}.json", "w") as f:
        json.dump(company.__dict__, f, indent=4)

    logger.info("Done!")
