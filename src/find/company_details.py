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


def is_valid_isin(ISIN):
    """
    Function to check if the input is a valid ISIN.
        2 letters followed by any combination of letters or digits
        for the next 10 characters (12 characters in total)

    Returns:
        bool: True if the ISIN is valid, False otherwise
    """
    if len(ISIN) == 12 and ISIN[:2].isalpha() and all(c.isalnum() for c in ISIN[2:]):
        return True
    return False


def get_msci_index_df(write=False):
    """
    Function to fetch the MSCI ACWI ETF holdings data and return a filtered DataFrame.

    Args:
        write (bool): Whether to write the CSV file to disk (default: False)

    Returns:
        pd.DataFrame: DataFrame containing the MSCI ACWI ETF holdings data
    """
    response = requests.get(MSCI_FUND_URL)
    if response.status_code == 200:
        if write:
            # Save the CSV file to disk (optional)
            with open(f'{os.getenv("ROOT_DIR")}/data/ACWI_holdings.csv', "wb") as f:
                f.write(response.content)

        # Load the content into a Pandas DataFrame (headers are on row 10 (0-indexed: row 9))
        file_content = BytesIO(response.content)
        df = pd.read_csv(file_content, header=9)
        # Filter the rows where the 'Asset Class' column is equal to 'Equity'
        df_filtered = df[df["Asset Class"] == "Equity"]
        # Select the first two columns (Ticker and Name)
        # TODO - filter using column names instead
        df_filtered = df_filtered.iloc[
            :, [0, 1]
        ]  # Assuming first column is ticker, second is name
        return df_filtered


def get_ticker_from_isin(ISIN):
    """
    Function to fetch the ticker symbol from OpenFIGI API using the ISIN code.
    """
    headers = {
        "Content-Type": "application/json",
        "X-OPENFIGI-APIKEY": OPENFIGI_API_KEY,
    }
    data = [{"idType": "ID_ISIN", "idValue": ISIN}]

    try:
        # Make the POST request to OpenFIGI API
        response = requests.post(OPENFIGI_URL, json=data, headers=headers)

        # Handle rate-limiting with retries
        while response.status_code == 429:
            logger.warning("Rate limit reached for OPENFIGI, retrying in 3 seconds...")
            time.sleep(3)
            response = requests.post(OPENFIGI_URL, json=data, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            results = response.json()
            try:
                # Search for ticker in the response
                return results[0]["data"][0].get("ticker")
            except (IndexError, KeyError):
                logger.warning(f"Ticker not found for ISIN {ISIN}. Returning None.")
                return None
        else:
            # Handle failed requests (non-200 status codes)
            logger.warning(
                f"Error fetching data for ISIN {ISIN}, status code: {response.status_code}. Returning None."
            )
            return None
    except Exception as e:
        logger.error(f"Error fetching ticker for ISIN {ISIN}: {e}. Returning None.")
        return None


def get_company_details(query):
    """
    Function to process user input and return the corresponding company name and ticker.
    """
    # get filtered MSCI df
    df_filtered = get_msci_index_df()
    # Check if the query is a valid ISIN
    if is_valid_isin(query):
        ticker = get_ticker_from_isin(query)
        if ticker is not None:
            logger.info(f"ISIN {query} corresponds to Ticker: {ticker}")
            # Find the row for the ticker in the filtered data
            if ticker in df_filtered["Ticker"].values:
                row = df_filtered[df_filtered["Ticker"] == ticker].index[0]
                company_data = Company(
                    isin=query, ticker=ticker, name=df_filtered.loc[row, "Name"]
                )
                return company_data
            else:
                logger.warning(
                    f"Ticker {ticker} not found in the filtered data. Returning None."
                )
                return None
        else:
            logger.warning(
                f"ISIN {query} not found. Unable to fetch the corresponding Ticker. Returning None."
            )
            return None

    # If the query is a Ticker
    # TODO - check if ticker using regex and get company name using yahoo finance
    elif query in df_filtered["Ticker"].values:
        row = df_filtered[df_filtered["Ticker"] == query].index[0]
        company_data = Company(ticker=query, name=df_filtered.loc[row, "Name"])
        return company_data

    # If the query is a Company Name
    # TODO - check if company name using regex and get ticker using yahoo finance
    elif query in df_filtered["Name"].values:
        row = df_filtered[df_filtered["Name"] == query].index[0]
        ticker = df_filtered.loc[row, "Ticker"]
        company_data = Company(ticker=ticker, name=query)
        return company_data

    else:
        logger.warning("Query not found in the filtered data. Returning None.")
        return None


# Main script to fetch company information
if __name__ == "__main__":
    # Ask the user for input
    user_input = input("Enter ISIN, Ticker, or Company Name: ").strip()
    company_data = get_company_details(user_input)
    if company_data is not None:
        logger.info(
            f"Company Name: {company_data.name}, Ticker: {company_data.ticker}, ISIN: {company_data.isin}"
        )
    else:
        logger.error("Company data not found for the given input.")
