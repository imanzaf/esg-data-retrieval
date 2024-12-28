import datetime as dt
import os
import sys

import googlesearch as gs
from dotenv import load_dotenv
from loguru import logger

load_dotenv()

sys.path.append(os.getenv("ROOT_DIR"))

from src.utils.data import get_msci_index_df, openfigi_post_request  # noqa: E402


class CompanyProfile:

    def __init__(self, identifier):
        # initialise default attributes
        self.isin = identifier if self.is_valid_isin(identifier) else None
        self.ticker = None
        self.name = None

        # if identifier is not an ISIN, check if identifier is a valid ticker
        # TODO - if ISIN found not to be valid at a later stage, treat it as a name and look for esg report again
        if self.isin is None:
            self.ticker = (
                identifier.upper() if self.is_valid_ticker(identifier) else None
            )
            # if identifier is not a ticker, treat it as a name
            if self.ticker is None:
                # TODO - allow partial matches for name when searching for corresponding ticker
                self.name = identifier

        # invoke company details function to retrieve missing attributes
        self._complete_company_profile()
        # invoke function to retrieve esg report url
        self.esg_report_url = None
        self._get_esg_report_url()

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
    def is_valid_ticker(ticker):
        """
        Function to check if the input is a valid ticker of 3-5 letters.

        Params:
            ticker (str): The input string to validate

        Returns:
            bool: True if the ticker is valid, False otherwise
        """
        if len(ticker) <= 11 and ticker.isalnum():
            return True
        return False

    @staticmethod
    def get_ticker_from_isin(ISIN):
        """
        Function to fetch the ticker symbol from OpenFIGI API using the ISIN code.
        """
        # Send a POST request to the OpenFIGI API
        openfigi_response = openfigi_post_request(
            [{"idType": "ID_ISIN", "idValue": ISIN}]
        )

        if openfigi_response is not None:
            try:
                # Extract the ticker symbol from the response
                ticker = openfigi_response[0]["data"][0]["ticker"]
                return ticker
            except Exception as e:
                logger.error(
                    f"Error fetching ticker for ISIN {ISIN}: {e}. Returning None."
                )
                return None

    def _complete_company_profile(self) -> None:
        """
        Function to process available company attributes and find any missing attributes (company name and ticker).

        # TODO - use yahoo finance to get company name from ticker and vice versa if available?
        """
        # get filtered MSCI df
        df_filtered = get_msci_index_df()

        # Check if identifier is an ISIN
        if self.isin is not None:
            ticker = self.get_ticker_from_isin(self.isin)
            self.ticker = ticker
            if ticker is not None:
                logger.info(f"ISIN {self.isin} corresponds to Ticker: {ticker}")
                # Find the row for the ticker in the filtered data
                if ticker in df_filtered["Ticker"].values:
                    # TODO - BALAZS - test this works
                    name = df_filtered[df_filtered["Ticker"] == ticker]["Name"].values[
                        0
                    ]
                    self.name = name
                else:
                    logger.warning(
                        f"Ticker {ticker} not found. Unable to fetch the corresponding details."
                    )
            else:
                logger.warning(
                    f"ISIN {self.isin} not found. Unable to fetch the corresponding details."
                )

        # If the identifier is a Ticker
        # TODO - BALAZS - get company name from ticker using yahoo finance?
        elif self.ticker is not None:
            name = df_filtered[df_filtered["Ticker"] == self.ticker]["Name"].values[0]
            self.name = name

        # If the identifier is a Company Name
        # TODO - BALAZS - get ticker from company name using yahoo finance?
        elif self.name is not None:
            ticker = df_filtered[df_filtered["Name"] == self.name]["Ticker"].values[0]
            self.ticker = ticker

        else:
            logger.warning(
                "Company identifier not found in the filtered data. Unable to fetch the corresponding details."
            )

    def _get_esg_report_url(self) -> None:
        """
        Find a link to the best result from google for the company's latest ESG report.
        """
        # use company name to search for the latest ESG report
        query = f"{self.name} latest ESG report filetype:pdf"
        search_results = gs.search(query, num_results=3, advanced=True)

        # get current year as string
        current_year = str(dt.datetime.now().year)
        previous_year = str(dt.datetime.now().year - 1)

        # filter out results that are not from the current or previous year and are not pdf files
        # TODO - check if search results include year of publication for cleaner filtering
        current_year_results = {}
        previous_year_results = {}
        for idx, result in enumerate(search_results):
            # check next result if file is not a pdf
            if not result.url.endswith(".pdf"):
                continue

            # append result to respective dictionary if it is from current or previous year
            if current_year in result.title:
                current_year_results[idx] = result.url
            elif previous_year in result.title:
                previous_year_results[idx] = result.url
            else:
                continue

        # get the first result from the current or previous year
        if current_year_results:
            first_result_idx = min(current_year_results, key=current_year_results.get)
            self.esg_report_url = current_year_results[first_result_idx]
        elif previous_year_results:
            first_result_idx = min(previous_year_results, key=previous_year_results.get)
            self.esg_report_url = previous_year_results[first_result_idx]
        else:
            # if no result is from current or previous year, return None for url
            logger.warning(
                f"Direct link to recent ESG report not found for {self.name}."
            )

        logger.debug(f"ESG report url for {self.name}: {self.esg_report_url}")


# Main script to fetch company information
if __name__ == "__main__":
    # Ask the user for input
    user_input = input("Enter ISIN, Ticker, or Company Name: ").strip()
    company = CompanyProfile(user_input)
    logger.info(f"Company Name: {company.name}, Ticker: {company.ticker}")
