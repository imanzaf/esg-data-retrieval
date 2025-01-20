
from jsonref import requests
from sympy.physics.units import length

from src.extract import tables
from src.find import company_profile
from src.utils import data

import os
import json
import requests
import shutil
from dotenv import load_dotenv

from src.utils.data_models import TableParsers

# Load environment variables from .env file
load_dotenv()

# Get ROOT_DIR from the environment variables
ROOT_DIR = os.getenv("ROOT_DIR")


def download_reports():
    """
    Downloads ESG reports from the URLs specified in the 'company_profile.json'
    and saves them in the same folder as the JSON file.
    """
    # Define the path to the JSON file
    json_path = os.path.join(ROOT_DIR, "data", "current_data", "company_profile.json")

    # Define the folder to save the downloaded reports (same folder as the JSON file)
    download_folder = os.path.join(ROOT_DIR, "data", "current_data")

    # Ensure the folder exists
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    # Read the JSON file
    try:
        with open(json_path, 'r') as file:
            company_profile = json.load(file)
    except Exception as e:
        print(f"Failed to read JSON file: {e}")
        return

    # Extract ESG report URLs
    esg_report_urls = company_profile.get("esg_report_urls", {})
    if not esg_report_urls:
        print("No ESG report URLs found in the JSON file.")
        return

    # Download reports
    for index, url in esg_report_urls.items():
        file_name = f"{int(index) + 1}.pdf"  # Naming files as 1.pdf, 2.pdf, etc.
        file_path = os.path.join(download_folder, file_name)

        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()

            with open(file_path, 'wb') as file:
                shutil.copyfileobj(response.raw, file)

            print(f"Downloaded {file_name} from {url}")
        except requests.exceptions.RequestException as e:
            print(f"Failed to download {url}: {e}")


def end_to_end_query(identifier, idType, parser):
    # Call the function without any arguments
    load_dotenv()
    ROOT_DIR = os.getenv("ROOT_DIR")

    company = company_profile.CompanyProfile(identifier, idType)
    download_reports()
    #Get pdf links from current data folder
    pdfs = []
    for index in range(len(company.esg_report_urls.keys())):
        # Generate the file path for each index (1.pdf, 2.pdf, 3.pdf)
        file_path = os.path.join(ROOT_DIR, "data", "current_data", f"{index + 1}.pdf")
        pdfs.append(file_path)
        print(file_path)

    for pdf in pdfs:
        output = tables.TableExtractor(company, pdf, parser).extract()
        if output is not None:
            break

# Example Usage
if __name__ == "__main__":
    identifier = "GB00B10RZP78"
    idType = "ISIN"
    parser = TableParsers.DOCLING
    end_to_end_query(identifier, idType, parser)


