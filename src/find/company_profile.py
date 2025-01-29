# TODO - if name provided instead of ISIN, use yahoo finance to get ticker symbol to use as label for saving data

import os
import sys
import time

import requests
from dotenv import load_dotenv
from loguru import logger

load_dotenv()
sys.path.append(os.getenv("ROOT_DIR"))

ROOT_DIR = os.getenv("ROOT_DIR")
ROOT_OUTPUT_PATH = os.getenv("ROOT_OUTPUT_PATH")
# OPENFIGI variables
OPENFIGI_API_KEY = os.getenv("OPENFIGI_API_KEY")
OPENFIGI_URL = os.getenv("OPENFIGI_URL")


class CompanyProfile:

    def __init__(
        self,
        identifier,
        idType,
    ):  # idType is TICKER, NAME or ISIN
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
        self.output_path = (os.path.join(ROOT_OUTPUT_PATH, self.name.replace(" ", "_").upper()))
        logger.debug(f"Company Identifier: {self.identifier}")

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

    def get_profile_from_identifier(self, identifier, idType):
        """
        Function to fetch the ticker symbol from OpenFIGI API using the ISIN code.
        """
        # Send a POST request to the OpenFIGI API
        openfigi_response = None

        if idType == "isin":
            openfigi_response = self._openfigi_post_request(
                [{"idType": "ID_ISIN", "idValue": identifier}]
            )
        elif idType == "ticker":
            openfigi_response = self._openfigi_post_request(
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

    @staticmethod
    def _openfigi_post_request(data):
        """
        Function to send a POST request to the OpenFIGI API with the given data.

        Args:
            data (list): List of dictionaries containing the data to send in the request

        Returns:
            dict: Dictionary containing the response from the OpenFIGI API
        """
        headers = {
            "Content-Type": "application/json",
            "X-OPENFIGI-APIKEY": OPENFIGI_API_KEY,
        }
        try:
            # Make the POST request to OpenFIGI API
            response = requests.post(OPENFIGI_URL, json=data, headers=headers)

            # Handle rate-limiting with retries
            while response.status_code == 429:
                logger.warning(
                    "Rate limit reached for OPENFIGI, retrying in 3 seconds..."
                )
                time.sleep(3)
                response = requests.post(OPENFIGI_URL, json=data, headers=headers)

            # Return the JSON response
            return response.json()
        except Exception as e:
            logger.error(f"Error sending POST request to OpenFIGI API: {e}")
            return None


# Main script to fetch company information
if __name__ == "__main__":
    # Ask the user for input
    id_type = input("Enter idType (TICKER, NAME, ISIN): ").strip()
    identifier = input("Enter ISIN, Ticker, or Company Name: ").strip()
    company = CompanyProfile(identifier, id_type)
    logger.info(f"Company Name: {company.name}, Ticker: {company.ticker}")
