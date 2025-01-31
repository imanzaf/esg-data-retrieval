import os
import re
import sys
from argparse import PARSER
from loguru import logger

import pandas as pd
from dotenv import load_dotenv

load_dotenv()
sys.path.append(os.getenv("ROOT_DIR"))

from src.find.company_profile import ROOT_OUTPUT_PATH
from src.utils.data_models import TableParsers
from src.utils.get_units import infer_units_for_rows, get_units_raw_input
from src.utils.standardize_table_rework import standardize_table


def filter_tables(directory_path, parser):
    # Regex to match 'Scope 1' and 'Scope 2'
    regex_scope = r"(Scope\s1|Scope\s2)"

    # Regex to exclude rows with words like 'excluded' or 'avoided'
    regex_exclude = r"(excluded|Excluded|avoided|Avoided|aim|Aim|goal|Goal|revenue|Revenue|target|Target|forecast|Forecast|estimate|Estimate|projection|Projection|expectation|Expectation|and 3|Scope 3|\+ 3)"

    # Combine the relevant information from all files into a single DataFrame
    scope_data = []

    # Iterate over all files in the directory
    for filename in os.listdir(os.path.join(directory_path, parser.value)):
        if filename.endswith(".csv"):
            file_path = os.path.join(directory_path, parser.value, filename)
            try:
                print(f"Processing file: {file_path}")
                # Read the CSV file
                df = pd.read_csv(file_path)
                df.to_csv(os.path.join(directory_path, "sample.csv"))
                # Append inferred units
                df = get_units_raw_input(df)
                # logger.info(f"raw input cols: {df.columns}")
                # logger.info(f"raw input units value: {df['Units']}")
                print(f"File read successfully: {file_path}")
                # Filter rows where any column matches the regex for 'Scope 1' or 'Scope 2'
                filtered_df = df[
                    df.apply(
                        lambda row: row.astype(str)
                        .str.contains(regex_scope, regex=True)
                        .any(),
                        axis=1,
                    )
                ]
                # logger.info(f"Filtered df: {filtered_df}")
                # Exclude rows where any column matches the regex for 'excluded' or 'avoided'
                filtered_df = filtered_df[
                    ~filtered_df.apply(
                        lambda row: row.astype(str)
                        .str.contains(regex_exclude, regex=True)
                        .any(),
                        axis=1,
                    )
                ]
                print(f"Filtered data from file: {file_path}")

                scope_data.append(filtered_df)
            except Exception as e:
                print(f"Error processing file {file_path}: {e}")

    # Combine all filtered data
    if scope_data:
        combined_scope_data = pd.concat(scope_data, ignore_index=True).drop_duplicates()
        # logger.info(combined_scope_data.columns)
        # Regex to match columns with various date formats
        regex_date = r"(\bFY\d{2}\b|\b20\d{2}\b|\b[Ff]iscal\s[Yy]ear\b)"

        # Identify the last column containing date-like information
        date_columns = [
            col for col in combined_scope_data.columns if re.search(regex_date, col)
        ]
        # logger.info(f"date cols: {date_columns}")

        if date_columns:
            # Find the index of the last date column
            # date_columns.append("Units")
            # logger.info(f"original cols: {combined_scope_data.columns}")
            last_date_col_index = combined_scope_data.columns.get_loc(date_columns[-1])
            # Keep only columns up to and including the last date column
            # Select all columns up to the last_date_col_index + 1
            selected_columns = combined_scope_data.iloc[:, : last_date_col_index + 1]
            # logger.info(f"new cols pt 1: {selected_columns}")
            # combined_scope_data_new = selected_columns.copy()
            # Add the "Units" column as the last column
            # logger.warning(combined_scope_data.columns)
            combined_scope_data_new = pd.concat(
                [selected_columns, combined_scope_data[["Units"]]], axis=1
            )
            # combined_scope_data_new = combined_scope_data[date_columns]
            # logger.info(f"new cols: {combined_scope_data.columns}")
            # logger.info(f"new df: {combined_scope_data_new}")

        # Drop the first column
        # TODO - check if needed
        # if not combined_scope_data_new.empty and len(combined_scope_data_new.columns) > 0:
        #     combined_scope_data_new = combined_scope_data_new.iloc[:, 1:]

        # logger.info(combined_scope_data_new.columns)

        # Drop empty columns
        combined_scope_data_new = combined_scope_data_new.dropna(axis=1, how="all")

        # Drop empty rows
        combined_scope_data_new = combined_scope_data_new.dropna(how="all")

        # logger.info(f"pre inferred df: {combined_scope_data_new}")
        # Get units
        combined_scope_data_new.to_csv(os.path.join(directory_path, "test_1.csv"))
        combined_scope_standard = infer_units_for_rows(combined_scope_data_new)
        logger.info(combined_scope_standard.columns)
        # logger.info(combined_scope_data.head(2))
        combined_scope_standard.to_csv(os.path.join(directory_path, "testing.csv"))

        # Standardise Table
        combined_scope_standard = standardize_table(combined_scope_standard)
        # Save the filtered data to a new CSV file
        output_path = os.path.join(directory_path, "esg_backup_data.csv")
        combined_scope_data.to_csv(output_path, index=False)

        output_path = os.path.join(directory_path, "esg_data.csv")
        combined_scope_standard.to_csv(output_path, index=False)
        print(f"Filtered data saved to: {output_path}")
        return combined_scope_data
    else:
        print("No data to combine.")


if __name__ == "__main__":
    import dotenv

    os.getenv("ROOT_OUTPUT_PATH")
    filter_tables(
        os.path.join(ROOT_OUTPUT_PATH, "MICROSOFT_CORP"), TableParsers.DOCLING
    )
