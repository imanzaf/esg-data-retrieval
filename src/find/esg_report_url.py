import datetime as dt
import os
import sys

import googlesearch as gs
from dotenv import load_dotenv
from loguru import logger

load_dotenv()

sys.path.append(os.getenv("ROOT_DIR"))

from src.find.company_details import CompanyInfo  # noqa: E402


def get_esg_report_url(company_identifier: str):
    """
    Find a link to the best result from google for the company's latest ESG report.

    Parameters:
        company_indentifier (str): The ISIN, ticker, or name of a company.

    Returns:
        company_details (Company): Company object for respective ISIN with esg_report_link attribute.
    """
    # get the ticker symbol and company name from ISIN
    company = CompanyInfo(company_identifier)
    company_details = company.get_company_details()
    # use company name to search for the latest ESG report
    query = f"{company_details.name} latest ESG report filetype:pdf"
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
        company_details.esg_report_url = current_year_results[first_result_idx]
    elif previous_year_results:
        first_result_idx = min(previous_year_results, key=previous_year_results.get)
        company_details.esg_report_url = previous_year_results[first_result_idx]
    else:
        # if no result is from current or previous year, return None for url
        logger.warning(
            f"Direct link to recent ESG report not found for {company_details.name}."
        )
        company_details.esg_report_url = None

    logger.debug(
        f"ESG report url for {company_details.name}: {company_details.esg_report_url}"
    )

    return company_details


if __name__ == "__main__":
    # ISIN = "US0378331005"
    ticker = "AAPL"
    company_details = get_esg_report_url(ticker)
    logger.info(company_details.esg_report_url)
