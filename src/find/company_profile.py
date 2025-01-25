# TODO - if name provided instead of ISIN, use yahoo finance to get ticker symbol to use as label for saving data

import datetime as dt
import json
import os
import sys

import requests
from dotenv import load_dotenv
from loguru import logger

load_dotenv()
sys.path.append(os.getenv("ROOT_DIR"))

ROOT_DIR = os.getenv("ROOT_DIR")
ROOT_OUTPUT_PATH = os.getenv("ROOT_OUTPUT_PATH")
API_KEY = os.getenv("GOOGLE_API_KEY")
SEARCH_ENGINE_ID = os.getenv("GOOGLE_SEARCH_ENGINE_ID")

if not any([API_KEY, SEARCH_ENGINE_ID]):
    raise ValueError(
        "Environment variables GOOGLE_API_KEY or GOOGLE_SEARCH_ENGINE_ID are not set."
    )

from src.utils.data import openfigi_post_request  # noqa: E402
from src.utils.data import update_esg_urls_order  # noqa: E402


class CompanyProfile:

    def __init__(self, identifier, idType):  # idType is TICKER, NAME or ISIN
        # initialise default attributes
        self.identifier = identifier
        self.idType = idType.lower()
        self.isin = (
            identifier
            if self.idType.lower() == "isin" and self.is_valid_isin(identifier)
            else None
        )
        self.name = identifier if self.idType.lower() == "name" else None
        self.ticker = identifier if self.idType.lower() == "ticker" else None
        self.description = None

        # invoke company details function to retrieve missing attributes
        self._complete_company_profile()
        # set output path
        self.output_path = os.path.join(
            ROOT_OUTPUT_PATH, str(self.name).upper().replace(" ", "_").replace("/", "_")
        )
        os.makedirs(self.output_path, exist_ok=True)
        # invoke function to retrieve esg report url
        self.esg_report_urls = {}
        self._get_esg_report_urls()
        # dump company profile to json
        self.dump_as_json()

    def dump_as_json(self):
        """Dumps the company profile as a JSON file into the specified folder."""
        if not ROOT_DIR:
            raise ValueError("ROOT_DIR is not set in the .env file.")
        try:
            file_path = f"{self.output_path}/profile.json"
            with open(file_path, "w") as json_file:
                json.dump(self.__dict__, json_file, indent=4)
            logger.info(f"Company profile JSON saved to {file_path}")
        except Exception as e:
            print(f"Failed to save company profile JSON: {e}")

    @staticmethod
    def is_valid_isin(ISIN):
        """
        Function to check if the input is a valid ISIN.
            2 letters followed by any combination of letters or digits
            for the next 10 characters (12 characters in total)

        Params:
            ISIN (str): The input string to validate

        Returns:
            bool: True if the ISIN is valid, False otherwise
        """
        if (
            len(ISIN) == 12
            and ISIN[:2].isalpha()
            and all(c.isalnum() for c in ISIN[2:])
        ):
            return True
        return False

    @staticmethod
    def get_profile_from_identifier(identifier, idType):
        """
        Function to fetch the ticker symbol from OpenFIGI API using the ISIN code.
        """
        # Send a POST request to the OpenFIGI API
        openfigi_response = None

        if idType == "isin":
            openfigi_response = openfigi_post_request(
                [{"idType": "ID_ISIN", "idValue": identifier}]
            )
        elif idType == "ticker":
            openfigi_response = openfigi_post_request(
                [{"idType": "TICKER", "idValue": identifier}]
            )

        if openfigi_response is not None:
            try:
                comp_dict = dict(openfigi_response[0]["data"][0])
                return comp_dict
            except Exception as e:
                logger.error(
                    f"Error fetching details for identifier{identifier}: {e}. Returning None."
                )
                return None

    def _complete_company_profile(self) -> None:
        """
        Function to get corresponding details if ISIN provided.
        """
        if self.name is not None:  # for names keep user input
            return
            # Check if identifier is an ISIN
        if self.identifier is not None:

            profile = self.get_profile_from_identifier(self.identifier, self.idType)
            if profile is not None:
                self.name = profile.get("name")
                self.ticker = profile.get("ticker")
                self.description = profile.get("securityDescription")
            else:
                logger.warning(
                    f"ISIN {self.isin} not found. Unable to fetch the corresponding details."
                )
                sys.exit()

    def _get_esg_report_urls(self) -> None:
        """
        Retrieve the top 3 URLs of the company's ESG reports using Google Custom Search.
        """
        # Search parameters
        current_year = str(dt.datetime.now().year)
        search_query = f"{self.name} {current_year} ESG report filetype:pdf"
        url = "https://www.googleapis.com/customsearch/v1"
        params = {
            "q": search_query,
            "key": API_KEY,
            "cx": SEARCH_ENGINE_ID,
        }

        # Make the search request
        response = requests.get(url, params=params)
        response.raise_for_status()
        search_results = response.json().get("items", [])[:4]  # Get top 3 results

        if not search_results:
            logger.warning(f"No ESG reports found for {self.identifier}.")
            return
        # Filter results based on year
        primary_results = {}
        secondary_results = {}

        for index, res in enumerate(search_results):
            logger.info(f"Result {index + 1}: {res.get('title')} - {res.get('link')}")
            try:
                # Append result to respective dictionary if it is from the current year
                if str(current_year) in res.get("title"):
                    primary_results[index] = res
                else:
                    secondary_results[index] = res
            except Exception as e:
                logger.warning(f"Unable to process result: {e}")
                continue

        # Get all results from the current year
        if primary_results:
            self.esg_report_urls.update(primary_results)

        # If no results from the current year, append all results from previous years
        if not primary_results:
            self.esg_report_urls.update(secondary_results)

        if not self.esg_report_urls:
            logger.warning(f"No ESG report found for {self.name}")
            # TODO - return response to display in UI
            sys.exit()

        self.esg_report_urls = update_esg_urls_order(
            list(self.esg_report_urls.values())
        )  # Invoke function to get proper order of keywords
        logger.debug(f"ESG report urls for {self.name}: {self.esg_report_urls}")


# Main script to fetch company information
if __name__ == "__main__":
    # Ask the user for input
    id_type = input("Enter idType (TICKER, NAME, ISIN): ").strip()
    identifier = input("Enter ISIN, Ticker, or Company Name: ").strip()
    company = CompanyProfile(identifier, id_type)
    logger.info(f"Company Name: {company.name}, Ticker: {company.ticker}")
    print(company.esg_report_urls[0])
