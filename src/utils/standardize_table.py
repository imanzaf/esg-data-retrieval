import os
import re

import dotenv
import numpy as np
import pandas as pd


def save_raw_data(df, output_path):
    """
    Save the raw data to a specified file path in CSV format.
    """
    df.to_csv(output_path, index=False)
    print(f"Raw data saved at: {output_path}")


def standardize_emissions_table(raw_data):

    renamed_columns = {}
    for col in raw_data.columns:
        clean_col = re.sub(r"[^a-zA-Z0-9 ]", " ", col).strip()
        clean_col = " ".join(clean_col.split())  # Remove double spaces
        match = re.search(r"(?:FY|fy|Year)?\D*(\d{4}|\d{2})", clean_col)
        if match:
            year = match.group(1)
            if len(year) == 2:
                year = f"20{year}" if int(year) >= 10 else f"19{year}"
            renamed_columns[col] = year

    raw_data = raw_data.rename(columns=renamed_columns)
    financial_years = [
        year for year in renamed_columns.values() if re.match(r"\b20\d{2}\b", year)
    ]

    # Define regex patterns for Scope 1, Scope 2 Market, and Scope 2 Location
    scope_1_pattern = r"scope\s*1"
    scope_2_market_pattern = r"scope\s*2.*market"
    scope_2_location_pattern = r"scope\s*2.*location"
    scope_2_general_pattern = r"\bscope\s*2\b"

    # Identify the parameter column
    parameter_col_index = None
    for idx in range(len(raw_data.columns)):
        if (
            raw_data.iloc[:, idx]
            .astype(str)
            .str.contains(scope_1_pattern, case=False, regex=True)
            .any()
        ):
            parameter_col_index = idx
            break

    # Keep only relevant columns (years + parameter column)
    if parameter_col_index is not None:
        parameter_col_name = raw_data.columns[parameter_col_index]
        columns_to_keep = (
            [parameter_col_name]
            + financial_years
            + (["Units"] if "Units" in raw_data.columns else [])
        )

    else:
        columns_to_keep = financial_years

    filtered_data = raw_data[columns_to_keep]
    filtered_data = filtered_data.rename(columns={filtered_data.columns[0]: "Metric"})

    # Save a copy of the filtered table
    standardized_data = filtered_data.copy()

    # Keep rows matching Scope 1, Scope 2 Market, or Scope 2 Location
    filtered_rows = standardized_data[
        standardized_data.iloc[:, 0]
        .astype(str)
        .str.contains(
            f"({scope_1_pattern}|{scope_2_market_pattern}|{scope_2_location_pattern})",
            case=False,
            regex=True,
        )
    ]

    # If no Scope 2 Market or Location rows exist, add rows matching Scope 2 General
    if (
        not filtered_rows.iloc[:, 0]
        .astype(str)
        .str.contains(scope_2_market_pattern, case=False, regex=True)
        .any()
        and not filtered_rows.iloc[:, 0]
        .astype(str)
        .str.contains(scope_2_location_pattern, case=False, regex=True)
        .any()
    ):
        additional_rows = standardized_data[
            standardized_data.iloc[:, 0]
            .astype(str)
            .str.contains(scope_2_general_pattern, case=False, regex=True)
        ]
        filtered_rows = pd.concat([filtered_rows, additional_rows], axis=0)

    # Function to clean the 'Metric' column by removing numbers except for 1 and 2 and commas
    def clean_scope_metric(x):
        # Convert to string
        x = str(x)

        # Initialize a result list to accumulate the filtered characters
        result = []

        # Flag to indicate when to stop removing characters
        stop_removal = False

        # Start iterating from the end of the string
        for char in reversed(x):
            # If we encounter '1', '2', '(', ')', or any alphabet, stop removing
            if char in ["1", "2", "(", ")"] or char.isalpha():
                stop_removal = True

            if stop_removal:
                result.append(char)
            else:
                # Skip digits except 1 and 2, commas, and spaces
                if char.isdigit() and char not in ["1", "2"]:
                    continue
                elif char == "," or char == " ":
                    continue
                # Append allowed characters
                result.append(char)

        # Reverse the result list to get the original order and join it to form the final string
        cleaned_x = "".join(reversed(result))

        return cleaned_x

    # Apply the cleaning function to the 'Metric' column in filtered_rows
    filtered_rows["Metric"] = filtered_rows["Metric"].apply(clean_scope_metric)

    # Apply the cleaning function to the 'Metric' column in filtered_rows
    filtered_rows["Metric"] = filtered_rows["Metric"].apply(clean_scope_metric)

    filtered_rows = filtered_rows.loc[:, ~filtered_rows.T.duplicated()]
    filtered_rows.replace("", np.nan, inplace=True)

    # Drop rows where all values are NaN
    filtered_rows = filtered_rows.dropna(how="any")
    return filtered_rows


def clean_header(headers):
    """
    Clean the header by removing any columns that match 'untitled' or 'Unnamed' (case-insensitive)
    after the first valid one.
    """
    # Define the regex pattern to match 'untitled' or 'Unnamed' (case-insensitive)
    invalid_pattern = re.compile(r"untitled|Unnamed", re.IGNORECASE)

    # Find the first valid header (non-"untitled" or "Unnamed" columns)
    first_valid_header_index = next(
        (i for i, header in enumerate(headers) if not invalid_pattern.search(header)),
        None,
    )

    if first_valid_header_index is not None:
        # Remove all "untitled" or "Unnamed" columns after the first valid header
        new_headers = headers[: first_valid_header_index + 1] + [
            header
            for header in headers[first_valid_header_index + 1 :]  # noqa: E203
            if not invalid_pattern.search(header)
        ]
    else:
        # If no valid header found, keep only the first and remove others
        new_headers = headers[:1] + [
            header for header in headers[1:] if not invalid_pattern.search(header)
        ]

    return new_headers


def clean_rows(df):
    """
    Clean rows by removing NaN values and shifting the data to the left.
    """
    cleaned_rows = []
    for _, row in df.iterrows():
        # Remove NaN values and shift the data to the left
        cleaned_row = row.dropna().values.tolist()
        cleaned_rows.append(cleaned_row)
    return cleaned_rows


def merge_rows_with_headers(cleaned_rows, headers):
    """
    Merge cleaned rows back into a DataFrame, filling with NA where necessary.
    """
    max_len = max(len(row) for row in cleaned_rows)
    # Adjust each row to match the length of the header, filling missing values with NaN
    adjusted_rows = [row + [np.nan] * (max_len - len(row)) for row in cleaned_rows]

    # Ensure all rows are aligned to the headers length
    return pd.DataFrame(adjusted_rows, columns=headers)


def process_dataframe(df):
    """
    Process the raw CSV file and clean up the data based on specified requirements.
    """

    # Clean the header by removing "Untitled" columns after the first valid one
    cleaned_headers = clean_header(df.columns.tolist())

    # Clean the rows by removing NaN values and shifting to the left
    cleaned_rows = clean_rows(df)

    # Merge cleaned rows back into a DataFrame, aligning with the cleaned header
    cleaned_df = merge_rows_with_headers(cleaned_rows, cleaned_headers)

    return cleaned_df


def standardize_table(data):
    try:
        cleaned_data = process_dataframe(data)
        print(cleaned_data.head())
    except Exception as e:
        print(f"Table clearing failed: {e}")
        return data

    try:
        standardized_table = standardize_emissions_table(
            cleaned_data
        )  # Pass the cleaned data
        return standardized_table

    except Exception as e:
        print(f"Standardization failed: {e}")
        return cleaned_data


if __name__ == "__main__":
    dotenv.load_dotenv()
    OUTPUT_DIR = os.getenv("ROOT_OUTPUT_PATH")
    file_path = os.path.join(OUTPUT_DIR, "BANK_OF_AMERICA_CORP", "esg_data.csv")
    df = pd.read_csv(file_path)
    try:
        df = standardize_table(df)
        print(df.head())
        output_path = os.path.join(OUTPUT_DIR, "std_esg_data.csv")
        save_raw_data(df, output_path)
    except Exception as e:
        print(f"Table clearing failed: {e}")
