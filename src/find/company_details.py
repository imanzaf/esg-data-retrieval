import os
import sys
import time
from io import BytesIO

import pandas as pd
import requests
from dotenv import load_dotenv
from loguru import logger

load_dotenv()

sys.path.append(os.getenv("ROOT_DIR"))

from src.utils.data_models import Company  # noqa: E402

# OPENFIGI variables
OPENFIGI_API_KEY = os.getenv("OPENFIGI_API_KEY")
OPENFIGI_URL = os.getenv("OPENFIGI_URL")
# URL to the CSV file (ACWI ETF holdings)
MSCI_FUND_URL = os.getenv("MSCI_FUND_URL")


def get_msci_index_df(write=False):
    """
    # TODO - add functionality for data refresh every 2 months
    Function to fetch the MSCI ACWI ETF holdings data and return a filtered DataFrame.

    Args:
        write (bool): Whether to write the CSV file to disk (default: False)

    Returns:
        pd.DataFrame: DataFrame containing the MSCI ACWI ETF holdings data
    """
    # if file already downloaded read directly from disk
    if os.path.exists(f'{os.getenv("ROOT_DIR")}/data/ACWI_holdings.csv'):
        # Load the CSV file from disk
        df = pd.read_csv(f'{os.getenv("ROOT_DIR")}/data/ACWI_holdings.csv', header=9)
    else:
        response = requests.get(MSCI_FUND_URL)
        # Save the CSV file to disk (optional)
        if write:
            with open(f'{os.getenv("ROOT_DIR")}/data/ACWI_holdings.csv', "wb") as f:
                f.write(response.content)
        # Load the content into a Pandas DataFrame (headers are on row 10 (0-indexed: row 9))
        file_content = BytesIO(response.content)
        df = pd.read_csv(file_content, header=9)
    # Filter the rows where the 'Asset Class' column is equal to 'Equity'
    df_filtered = df[df["Asset Class"] == "Equity"]
    # Select the first two columns (Ticker and Name)
    df_filtered = df_filtered[["Ticker", "Name"]]
    return df_filtered


class CompanyInfo:

    def __init__(self, identifier):
        self.isin = identifier if self.is_valid_isin(identifier) else None
        self.ticker = identifier.upper() if self.is_valid_ticker(identifier) else None
        # TODO - allow partial matches for name
        self.name = (
            identifier if all([x is None for x in [self.isin, self.ticker]]) else None
        )

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

    def get_ticker_from_isin(self):
        """
        Function to fetch the ticker symbol from OpenFIGI API using the ISIN code.
        """
        headers = {
            "Content-Type": "application/json",
            "X-OPENFIGI-APIKEY": OPENFIGI_API_KEY,
        }
        data = [{"idType": "ID_ISIN", "idValue": self.isin}]

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

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                results = response.json()
                # Search for ticker in the response
                return results[0]["data"][0].get("ticker")
        except Exception as e:
            logger.error(
                f"Error fetching ticker for ISIN {self.isin}: {e}. Returning None."
            )
            return None

    def get_company_details(self):
        """
        Function to process user input and return the corresponding company name and ticker.

        # TODO - use yahoo finance to get company name from ticker and vice versa if available?
        """
        # get filtered MSCI df
        df_filtered = get_msci_index_df()

        # Check if identifier is an ISIN
        if self.isin is not None:
            ticker = self.get_ticker_from_isin()
            if ticker is not None:
                logger.info(f"ISIN {self.isin} corresponds to Ticker: {ticker}")
                # Find the row for the ticker in the filtered data
                if ticker in df_filtered["Ticker"].values:
                    name = df_filtered[df_filtered["Ticker"] == ticker]["Name"].values[
                        0
                    ]
                    company_data = Company(isin=self.isin, ticker=ticker, name=name)
                    return company_data
                else:
                    logger.warning(
                        f"Ticker {ticker} not found in the filtered data. Returning None."
                    )
                    return None
            else:
                logger.warning(
                    f"ISIN {self.isin} not found. Unable to fetch the corresponding Ticker. Returning None."
                )
                return None

        # If the identifier is a Ticker
        # TODO - get company name from ticker using yahoo finance?
        elif self.ticker is not None:
            name = df_filtered[df_filtered["Ticker"] == self.ticker]["Name"].values[0]
            company_data = Company(ticker=self.ticker, name=name)
            return company_data

        # If the identifier is a Company Name
        # TODO - get ticker from company name using yahoo finance?
        elif self.name is not None:
            ticker = df_filtered[df_filtered["Name"] == self.name]["Ticker"].values[0]
            company_data = Company(ticker=ticker, name=self.name)
            return company_data

        else:
            logger.warning(
                "Company identifier not found in the filtered data. Returning None."
            )
            return None


# Main script to fetch company information
if __name__ == "__main__":
    # Ask the user for input
    user_input = input("Enter ISIN, Ticker, or Company Name: ").strip()
    company = CompanyInfo(user_input)
    company_data = company.get_company_details()
    if company_data is not None:
        logger.info(
            f"Company Name: {company_data.name}, Ticker: {company_data.ticker}, ISIN: {company_data.isin}"
        )
    else:
        logger.error("Company data not found for the given input.")
