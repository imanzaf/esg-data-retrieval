import os
import dotenv
import pandas as pd
import numpy as np

from src.scripts.retrieve_emissions_data import OUTPUT_DIR

OUTPUT_DIR = os.getenv("ROOT_OUTPUT_PATH")

def standardize_emissions_table(raw_data):
    """
    Standardizes a table with Scope 1, Scope 2 (market-based and location-based) GHG emissions data.

    Parameters:
        raw_data (pd.DataFrame): Raw data table with mixed formats.

    Returns:
        pd.DataFrame: Standardized table with Scope 1 emissions as rows
                      and financial years as columns.
    """
    # Clean column headers and remove empty columns
    raw_data.columns = raw_data.columns.str.strip().str.replace('Unnamed.*', '', regex=True)


    # Normalize column names to detect financial years
    raw_data.columns = raw_data.columns.str.lower().str.replace('[^a-z0-9 ]', '', regex=True)

    # Extract financial years dynamically using regex
    financial_years = [col for col in raw_data.columns if pd.Series(col).str.contains(r'\b\d{4}\b').any()]

    # Identify the column with Scope 1 data
    scope_1_column_index = None
    for idx, col in enumerate(raw_data.columns):
        if raw_data[col].astype(str).str.contains(r'scope\s*1', case=False, regex=True).any():
            scope_1_column_index = idx
            break

    if scope_1_column_index is None:
        raise ValueError("No Scope 1 data found in the table.")


    scope_1_row_index = raw_data.iloc[:, scope_1_column_index].astype(str).str.contains(r'scope\s*1', case=False,
                                                                                        regex=True).idxmax()
    scope_1_row = raw_data.iloc[scope_1_row_index]

    # Extract data for financial years from the identified row
    scope_1_data = scope_1_row[financial_years]

    # Create a standardized DataFrame
    standardized_data = pd.DataFrame([scope_1_data], columns=financial_years)
    standardized_data.insert(0, 'Parameter', 'Scope 1')

    # Replace NA values with 0 or placeholders as needed
    standardized_data = standardized_data.fillna(0)

    return standardized_data


if __name__ == '__main__':

    raw_data = pd.read_csv(os.path.join(OUTPUT_DIR, "GOLDMAN_SACHS_GROUP_INC", 'esg_data.csv'))
    standardized_table = standardize_emissions_table(raw_data)
    output_path = os.path.join(OUTPUT_DIR, "std_esg_data.csv")
    standardized_table.to_csv(output_path, index=False)