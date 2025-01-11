"""
Methods for extracting tables from PDFs.
"""

import os

# %%
import camelot.io as camelot
import pymupdf
import tabula
from dotenv import load_dotenv

load_dotenv()


def filter_table(df):
    """Check if the table contains Scope 1 or Scope 2 and add it to the results."""
    table_text = df.to_string(
        index=False, header=False
    )  # Convert table to string for searching keywords
    if any(
        [x in table_text.lower() for x in ["ghg emissions"]]
    ):  # Check if the table contains relevant data  # "Scope 1", "Scope 2"
        return df
    return None


def extract_tables_using_camelot(path: str):
    tables = []
    try:
        camelot_tables = camelot.read_pdf(
            path, pages="all", flavor="stream"
        )  # Extract tables using Camelot
        for table in camelot_tables:  # Loop through each extracted table
            df = filter_table(table.df)  # Convert Camelot table to a DataFrame
            if df is not None:
                tables.append(df)
        return tables
    except Exception as e:
        print(
            f"Error using Camelot: {e}"
        )  # Handle any errors during Camelot extraction


def extract_tables_using_tabula(path: str):
    tables = []
    try:
        tabula_tables = tabula.read_pdf(
            path, pages="all", stream=True
        )  # Extract tables using Camelot
        for table in tabula_tables:  # Loop through each extracted table
            df = filter_table(table.df)  # Convert Camelot table to a DataFrame
            if df is not None:
                tables.append(df)
        return tables
    except Exception as e:
        print(f"Error using Tabula: {e}")


def extract_tables_using_pymupdf(path: str):
    tables = []
    with pymupdf.open(path) as doc:
        for page in doc:
            pg_tables = page.find_tables().tables
            pd_tables = [filter_table(table.to_pandas()) for table in pg_tables]
            tables += [table for table in pd_tables if table is not None]
    return tables


# %%
path = f"{os.getenv('ROOT_DIR')}/data/HSBC/240221-esg-review-2023.pdf"
tables = extract_tables_using_camelot(path)
for idx, table in enumerate(tables):
    table.to_csv(f"{os.getenv('ROOT_DIR')}/data/HSBC/camelot/table_{idx}.csv")

# %%
path = f"{os.getenv('ROOT_DIR')}/data/HSBC/240221-esg-review-2023.pdf"
tables = extract_tables_using_tabula(path)
for idx, table in enumerate(tables):
    table.to_csv(f"{os.getenv('ROOT_DIR')}/data/HSBC/tabula/table_{idx}.csv")

# %%
hsbc_path = f"{os.getenv('ROOT_DIR')}/data/HSBC/240221-esg-review-2023.pdf"
apple_path = (
    f"{os.getenv('ROOT_DIR')}/data/AAPL/Apple_Environmental_Progress_Report_2024.pdf"
)
msft_path = f"{os.getenv('ROOT_DIR')}/data/MICROSOFT/RW1lmju.pdf"
tables = extract_tables_using_pymupdf(msft_path)
for idx, table in enumerate(tables):
    print(table)
    table.to_csv(f"{os.getenv('ROOT_DIR')}/data/MICROSOFT/pymupdf/table_{idx}.csv")

# %%
if __name__ == "__main__":
    print("hi!")


# maybe:
#  extract text, find scope 1 / scope 2 / ghg emissions followed by numbers using regex
#  save as table? or find tables in that page
