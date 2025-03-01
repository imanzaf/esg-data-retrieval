import datetime as dt
import json
import os
import re
import sys
from typing import List

import requests
from dotenv import load_dotenv
from loguru import logger
from pydantic import BaseModel

from src.utils.data_models import SearchKeyWords

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

from src.find.company_profile import CompanyProfile  # noqa: E402


class ESGReports:

    def __init__(self, company: CompanyProfile):
        self.company = company
        self.urls = self._get_report_search_results()

        # set output path
        try:
            # set output path
            self.output_path = os.path.join(
                ROOT_OUTPUT_PATH,
                str(self.company.name).upper().replace(" ", "_").replace("/", "_"),
            )
        except Exception:
            self.output_path = os.path.join(
                ROOT_OUTPUT_PATH,
                str(self.company.name).upper().replace(" ", "_").replace("/", "_"),
            )
        os.makedirs(self.output_path, exist_ok=True)
        # dump company profile to json
        self.save_profile()

    def _get_report_search_results(self) -> dict:
        """
        Retrieve the top 3 URLs of the company's ESG reports using Google Custom Search.
        """
        # Search parameters
        current_year = str(dt.datetime.now().year)
        search_query = f"{self.company.name} {current_year} ESG report filetype:pdf"
        url = "https://www.googleapis.com/customsearch/v1"
        params = {
            "q": search_query,
            "key": API_KEY,
            "cx": SEARCH_ENGINE_ID,
        }

        # Make the search request
        response = requests.get(url, params=params)
        response.raise_for_status()
        search_results = response.json().get("items", [])[:5]  # Get top 5 results

        if not search_results:
            logger.warning(f"No ESG reports found for {self.name}")
            # TODO - return response to display in UI
            sys.exit()

        sorted_results = self._sort_search_reults(
            self.company.name, search_results
        )  # Invoke function to get proper order of keywords
        esg_urls = {
            index: value.get("link", "") for index, value in enumerate(sorted_results)
        }
        logger.debug(f"ESG report urls for {self.company.name}: {esg_urls}")
        return esg_urls

    @staticmethod
    def _sort_search_reults(company_name: str, search_results: List[dict]):

        for result in search_results:
            result_obj = SearchResult(
                company_name=company_name,
                url=result.get("link", ""),
                title=result.get("title", ""),
                description=result.get("snippet", ""),
            )
            result["score"] = result_obj.score_search()

        sorted_results = sorted(
            search_results,
            key=lambda item: item.get("score"),
            reverse=True,
        )

        return sorted_results

    def save_profile(self):
        """Dumps the company profile as a JSON file into the specified folder."""
        if not ROOT_DIR:
            raise ValueError("ROOT_DIR is not set in the .env file.")
        try:
            # get attributes as dictionary
            data = {
                "company": self.company.__dict__,
                "esg_reports": self.urls,
            }

            file_path = f"{self.output_path}/profile.json"
            with open(file_path, "w") as json_file:
                json.dump(data, json_file, indent=4)
            logger.info(f"Company profile JSON saved to {file_path}")
        except Exception as e:
            print(f"Failed to save company profile JSON: {e}")


class SearchResult(BaseModel):
    company_name: str
    url: str
    title: str
    description: str

    def score_search(self):
        stripped_name = self.company_name.split(" ")[0].lower()

        text_score = (
            self.score_text(self.title.lower())
            + self.score_text(self.description.lower())
            + (
                -5
                if (
                    stripped_name not in self.title.lower()
                    and stripped_name not in self.description.lower()
                    and stripped_name not in self.url.lower()
                )
                else 1
            )  # strongly penalize if name is not there
        )
        url_score = self.score_text(self.url) + (1 if self.company_name_lookup() else 0)
        year_score = self.score_year(
            self.title.lower() + self.description.lower() + self.url.lower()
        )
        return text_score + url_score + year_score

    @staticmethod
    def score_text(text: str):
        count = sum(keyword.value.lower() in text.lower() for keyword in SearchKeyWords)
        return count

    def company_name_lookup(self):
        # get the site name from url
        url_index = re.search(
            r"(?:https?://)?(?:www\.)?([a-zA-Z0-9]+)", self.url
        ).group()
        stripped_name = self.company_name.split(" ")[0].lower()
        # check if company name starts with site name
        if stripped_name in url_index:
            return 2
        else:
            return 0

    @staticmethod
    def score_year(text):
        current_year = dt.datetime.now().year
        year_lag = current_year - 1
        two_year_lag = current_year - 2
        three_year_lag = current_year - 3

        # Extract all years from the text
        years_in_text = [int(year) for year in re.findall(r"\b\d{4}\b", text)]

        # Check for years that are 3 years older than the current year or older
        if any(year < three_year_lag for year in years_in_text):
            return -2

        # Check if the text contains the current year, year lag, or two-year lag
        if current_year in years_in_text:
            return 2
        if any(
            year in {current_year, year_lag, two_year_lag} for year in years_in_text
        ):
            return 1

        return -1
