import os
import re

import pandas as pd


def filter_tables(directory_path, parser):
    # Regex to match 'Scope 1' and 'Scope 2'
    regex_scope = r"(Scope\s1|Scope\s2)"

    # Regex to exclude rows with words like 'excluded' or 'avoided'
    regex_exclude = r"(excluded|Excluded|avoided|Avoided|aim|Aim|goal|Goal|revenue|Revenue|target|Target|forecast|Forecast|estimate|Estimate|projection|Projection|expectation|Expectation)"

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

        # Regex to match columns with various date formats
        regex_date = r"(\bFY\d{2}\b|\b20\d{2}\b|\b[Ff]iscal\s[Yy]ear\b)"

        # Identify the last column containing date-like information
        date_columns = [
            col for col in combined_scope_data.columns if re.search(regex_date, col)
        ]

        if date_columns:
            # Find the index of the last date column
            last_date_col_index = combined_scope_data.columns.get_loc(date_columns[-1])
            # Keep only columns up to and including the last date column
            combined_scope_data = combined_scope_data.iloc[:, : last_date_col_index + 1]

        # Drop the first column
        if not combined_scope_data.empty and len(combined_scope_data.columns) > 0:
            combined_scope_data = combined_scope_data.iloc[:, 1:]

        # Drop empty columns
        combined_scope_data = combined_scope_data.dropna(axis=1, how="all")

        # Drop empty rows
        combined_scope_data = combined_scope_data.dropna(how="all")

        # Save the filtered data to a new CSV file
        output_path = os.path.join(directory_path,  "esg_data.csv")
        combined_scope_data.to_csv(output_path, index=False)
        print(f"Filtered data saved to: {output_path}")
        return combined_scope_data
    else:
        print("No data to combine.")
