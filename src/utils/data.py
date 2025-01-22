import datetime as dt
import os
import sys
import time
import urllib
from io import BytesIO
from typing import List

import pandas as pd
import requests
from dotenv import load_dotenv
from loguru import logger

load_dotenv()

sys.path.append(os.getenv("ROOT_DIR"))

# URL to the CSV file (ACWI ETF holdings)
MSCI_FUND_URL = os.getenv("MSCI_FUND_URL")
# OPENFIGI variables
OPENFIGI_API_KEY = os.getenv("OPENFIGI_API_KEY")
OPENFIGI_URL = os.getenv("OPENFIGI_URL")


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


def count_keywords(url: dict):
    """
    Count the number of predefined keywords in the given URL, with double weight
    for the current year and the previous year keywords.
    """
    text = url.get("text")
    current_year = str(dt.datetime.now().year)
    previous_year = str(dt.datetime.now().year - 1)

    # Keywords with regular weight
    keywords = [
        "esg",
        "csr",
        "sustainability",
        "emission",
        "environment",
        "scope 1",
        "scope 2",
        "scope",
        "report",
        "statement",
        "policy",
        "progress" "fact" "sheet",
    ]
    # Double weight for current year and previous year
    count = 2 * (current_year in text) + 2 * (previous_year in text)
    # Add counts for the other keywords
    count += sum(keyword.lower() in text for keyword in keywords)

    return count


def update_esg_urls_order(search_results: List[dict]):
    # get current and previous year
    current_year = str(dt.datetime.now().year)
    previous_year = str(dt.datetime.now().year - 1)

    sorted_urls = search_results
    # Check if the any title contains the current or previous year
    if any([current_year in url.get("title") for url in search_results]) or any(
        [previous_year in url.get("title") for url in search_results]
    ):
        sorted_urls = sorted(
            [
                {"text": result.get("title"), "link": result.get("link")}
                for result in search_results
            ],
            key=count_keywords,
            reverse=True,
        )
    # Check if any description contains the current or previous year
    elif any([current_year in url.get("snippet") for url in search_results]) or any(
        [previous_year in url.get("snippet") for url in search_results]
    ):
        sorted_urls = sorted(
            [
                {"text": result.get("snippet"), "link": result.get("link")}
                for result in search_results
            ],
            key=count_keywords,
            reverse=True,
        )

    elif any([current_year in url.get("link") for url in search_results]) or any(
        [previous_year in url.get("link") for url in search_results]
    ):
        sorted_urls = sorted(
            [
                {"text": result.get("snippet"), "link": result.get("link")}
                for result in search_results
            ],
            key=count_keywords,
            reverse=True,
        )
    # Create a new dictionary where the values are just the URL attribute, and are re-indexed according to their new order
    updated_urls = {index: value.get("link") for index, value in enumerate(sorted_urls)}
    return updated_urls


def openfigi_post_request(data):
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
            logger.warning("Rate limit reached for OPENFIGI, retrying in 3 seconds...")
            time.sleep(3)
            response = requests.post(OPENFIGI_URL, json=data, headers=headers)

        # Return the JSON response
        return response.json()
    except Exception as e:
        logger.error(f"Error sending POST request to OpenFIGI API: {e}")
        return None


def download_pdf_from_urls(urls: List[str], root_path: str):
    """
    Function to download a PDF file from a URL. Breaks on the first successful download.

    Args:
        urls (List[str]): List of URLs to try to download in pdf format.
    """
    for url in urls:
        try:
            # isolate PDF filename from URL
            pdf_file_name = (
                os.path.basename(url) + ".pdf"
                if not url.endswith(".pdf")
                else os.path.basename(url)
            )
            urllib.request.urlretrieve(url, os.path.join(root_path, pdf_file_name))
            return os.path.join(root_path, pdf_file_name)
        except Exception as e:
            logger.error(f"Uh oh! Could not download {url}: {e}")
            continue
