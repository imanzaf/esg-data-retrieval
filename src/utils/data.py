import datetime as dt
import os
import sys
import time
import urllib
from io import BytesIO
from typing import List
import re

from src.utils.data_models import SearchKeyWords
from pydantic import BaseModel
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


class SearchResult(BaseModel):
    company_name: str
    url: str
    title: str
    description: str
    
    def score_search(self):
        text_score = self.score_text(self.title) + self.score_text(self.description)
        url_score = self.score_text(self.url) + (1 if self.company_name_lookup() else 0)
        return text_score + url_score

    @staticmethod
    def score_text(text: str):
        count = sum(keyword.value.lower() in text.lower() for keyword in SearchKeyWords)
        return count

    def company_name_lookup(self):
        # get the site name from url
        url_index = re.search(r"(?:https?://)?(?:www\.)?([a-zA-Z0-9]+)", self.url).group()
        # check if company name starts with site name
        if self.company_name.startswith(url_index):
            return True
        else:
            return False


def sort_search_reults(company_name: str, search_results: List[dict]):

    for result in search_results:
        result_obj = SearchResult(company_name=company_name, url=result.get("link", ""), title=result.get("title", ""), description=result.get("snippet", ""))
        result["score"] = result_obj.score_search()
    
    sorted_results = sorted(
        search_results,
        key=lambda item: item.get("score"),
        reverse=True,
    )

    return sorted_results


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
