# TODO - if name provided instead of ISIN, use yahoo finance to get ticker symbol to use as label for saving data

import datetime as dt
import os
import sys

import googlesearch as gs
from dotenv import load_dotenv
from loguru import logger

load_dotenv()

sys.path.append(os.getenv("ROOT_DIR"))

from src.utils.data import openfigi_post_request  # noqa: E402


class CompanyProfile:

    def __init__(self, identifier):
        # initialise default attributes
        self.isin = identifier if self.is_valid_isin(identifier) else None
        self.name = identifier if self.isin is None else None
        self.ticker = None
        self.description = None

        # invoke company details function to retrieve missing attributes
        self._complete_company_profile()
        # invoke function to retrieve esg report url
        self.esg_report_urls = {}
        self._get_esg_report_urls()

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
    def get_profile_from_isin(ISIN):
        """
        Function to fetch the ticker symbol from OpenFIGI API using the ISIN code.
        """
        # Send a POST request to the OpenFIGI API
        openfigi_response = openfigi_post_request(
            [{"idType": "ID_ISIN", "idValue": ISIN}]
        )

        if openfigi_response is not None:
            try:
                comp_dict = dict(openfigi_response[0]["data"][0])
                return comp_dict
            except Exception as e:
                logger.error(
                    f"Error fetching details for ISIN {ISIN}: {e}. Returning None."
                )
                return None

    def _complete_company_profile(self) -> None:
        """
        Function to get corresponding details if ISIN provided.
        """
        # Check if identifier is an ISIN
        if self.isin is not None:
            profile = self.get_profile_from_isin(self.isin)
            if profile is not None:
                self.name = profile.get("name")
                self.ticker = profile.get("ticker")
                self.description = profile.get("securityDescription")
            else:
                logger.warning(
                    f"ISIN {self.isin} not found. Unable to fetch the corresponding details."
                )

    def _get_esg_report_urls(self) -> None:
        """
        Find a link to the best result from google for the company's latest ESG report.
        """
        # get current year as string
        current_year = str(dt.datetime.now().year)
        # use company name to search for the latest ESG report
        query = f"{self.name} {current_year} ESG report filetype:pdf"
        search_results = gs.search(query, num_results=3, advanced=True)

        # filter results based on year
        # TODO - check if search results include year of publication for cleaner filtering
        primary_results = {}
        secondary_results = {}
        for idx, result in enumerate(search_results):
            logger.debug(f"Result {idx}: {result.title} - {result.url}")

            # append result to respective dictionary if it is from current year
            if current_year in result.title:
                primary_results[idx] = result.url
            else:
                secondary_results[idx] = result.url

        # get all results from current year
        if primary_results:
            self.esg_report_urls.update(primary_results)

        # if no results from current year, append all results from previous years
        if not primary_results:
            self.esg_report_urls.update(secondary_results)

        if not self.esg_report_urls:
            logger.warning(f"No ESG report found for {self.name}")

        logger.debug(f"ESG report urls for {self.name}: {self.esg_report_urls}")


# Main script to fetch company information
if __name__ == "__main__":
    # Ask the user for input
    user_input = input("Enter ISIN, Ticker, or Company Name: ").strip()
    company = CompanyProfile(user_input)
    logger.info(f"Company Name: {company.name}, Ticker: {company.ticker}")
