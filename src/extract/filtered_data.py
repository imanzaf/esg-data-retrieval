import os
import re
import sys

import pandas as pd
from dotenv import load_dotenv
from loguru import logger
from pydantic import BaseModel

load_dotenv()
sys.path.append(os.getenv("ROOT_DIR"))

from src.utils.data_models import TableParsers  # noqa: E402
from src.utils.standardize_table import standardize_table  # noqa: E402
from src.utils.units import get_units_raw_input, infer_units_for_rows  # noqa: E402

if not sys.warnoptions:
    import warnings

    warnings.simplefilter("ignore")


class Filter(BaseModel):
    # Regex to match 'Scope 1', 'Scope 2', and 'Scope 3'
    regex_scope1: str = r"Scope\s1"
    regex_scope2: str = r"Scope\s2"
    regex_scope3: str = r"Scope\s3"

    # Regex to exclude rows with words like 'excluded' or 'avoided'
    regex_exclude: str = (
        r"(excluded|Excluded|avoided|Avoided|aim|Aim|goal|Goal|target|Target|forecast|Forecast|estimate|Estimate|projection|Projection|expectation|Expectation)"
    )

    # Regex to match columns with various date formats
    regex_date: str = r"(\bFY\d{2}\b|\b20\d{2}\b|\b[Ff]iscal\s[Yy]ear\b)"

    directory_path: str
    parser: TableParsers

    filtered_df: pd.DataFrame = None

    class Config:
        arbitrary_types_allowed = True

    def _load_dfs(self):
        dfs = []
        for filename in os.listdir(
            os.path.join(self.directory_path, self.parser.value)
        ):
            if filename.endswith(".csv"):
                file_path = os.path.join(
                    self.directory_path, self.parser.value, filename
                )
                df = pd.read_csv(file_path)
                dfs.append(df)
        return dfs

    def extract_filtered_df(self):
        docling_tables = self._load_dfs()
        dfs = self._append_units_column(docling_tables)
        filtered_dfs = self._filter_data_v2(dfs)
        # dfs_to_concat = [df for df in filtered_dfs if df is not None]
        # filtered_dfs = self._filter_for_scope(dfs)
        # concatenated_df = self._filter_for_figures(filtered_dfs)
        inferred_df = self._infer_units(pd.concat(filtered_dfs, ignore_index=True))
        final_df = self._standardise_df(inferred_df)

        self.filtered_df = final_df

    def _append_units_column(self, docling_tables: list[pd.DataFrame]):
        dfs = []
        for df in docling_tables:
            dfs.append(get_units_raw_input(df))
        return dfs

    def _filter_data_v2(self, dfs: list[pd.DataFrame]):
        scope_data = []
        for idx, df in enumerate(dfs):
            try:
                # Checks if scope 1 exists in table
                contains_scope1 = df.apply(
                    lambda row: row.str.contains(
                        self.regex_scope1, regex=True, na=False
                    ).any(),
                    axis=1,
                ).any()
                # Checks if scope 2 exists in table
                contains_scope2 = df.apply(
                    lambda row: row.str.contains(
                        self.regex_scope3, regex=True, na=False
                    ).any(),
                    axis=1,
                ).any()

                if not (contains_scope1 and contains_scope2):
                    print(
                        f"Skipping file {idx} - does not contain both Scope 1 and Scope 2."
                    )
                    continue

                # **Step 2: Remove rows where both 'Scope 1' and 'Scope 3' appear in the same row**
                scope1_and_scope3 = df.apply(
                    lambda row: row.str.contains(
                        self.regex_scope1, regex=True, na=False
                    ).any()
                    and row.str.contains(self.regex_scope3, regex=True, na=False).any(),
                    axis=1,
                )
                df = df[~scope1_and_scope3]  # Remove those rows

                # Checks if scope 3 exists in table
                contains_scope3 = df.apply(
                    lambda row: row.str.contains(
                        self.regex_scope3, regex=True, na=False
                    ).any(),
                    axis=1,
                ).any()

                # Check if the table has a date column in the header
                date_columns = [
                    col for col in df.columns if re.search(self.regex_date, str(col))
                ]
                if not date_columns:
                    print(
                        f"Skipping file {idx} as it has no date-related columns in the header."
                    )
                    continue

                # Remove rows that contain excluded words
                df = df[
                    ~df.astype(str).apply(
                        lambda row: row.str.contains(
                            self.regex_exclude, regex=True, na=False
                        ).any(),
                        axis=1,
                    )
                ]

                # Convert all columns to strings to avoid dtype issues
                df = df.astype(str)

                if contains_scope3:
                    # Find the index where 'Scope 3' appears and remove it and all rows below
                    scope3_index = df.apply(
                        lambda row: row.str.contains(
                            self.regex_scope3, regex=True, na=False
                        ).any(),
                        axis=1,
                    )
                    if contains_scope3 and scope3_index.any():
                        first_scope3_idx = scope3_index[scope3_index].index[
                            0
                        ]  # First occurrence
                        df = df.loc[: first_scope3_idx - 1]  # Keep only rows above it

                if contains_scope1:
                    # Find the index where 'Scope 1' appears and remove all rows above it (excluding date rows)
                    scope1_index = df.apply(
                        lambda row: row.str.contains(
                            self.regex_scope1, regex=True, na=False
                        ).any(),
                        axis=1,
                    )
                    if contains_scope1 and scope1_index.any():
                        first_scope1_idx = scope1_index[scope1_index].index[
                            0
                        ]  # First occurrence
                        df = df.loc[first_scope1_idx:]  # Keep 'Scope 1' row and below

                # Store processed data
                scope_data.append(df)

            except Exception as e:
                logger.warning(f"Error processing df {idx}: {e}")
                continue
        return scope_data

    def _filter_for_scope(self, dfs: list[pd.DataFrame]):
        filtered_dfs = []
        for df in dfs:
            # Check if the table has a date column in the header
            date_columns = [
                col for col in df.columns if re.search(self.regex_date, str(col))
            ]
            if not date_columns:
                continue  # Skip files without date columns

            filtered_df = df[
                df.apply(
                    lambda row: row.astype(str)
                    .str.contains(self.regex_scope, regex=True)
                    .any(),
                    axis=1,
                )
            ]
            filtered_df = filtered_df[
                ~filtered_df.apply(
                    lambda row: row.astype(str)
                    .str.contains(self.regex_exclude, regex=True)
                    .any(),
                    axis=1,
                )
            ]
            filtered_dfs.append(filtered_df)
        return filtered_dfs

    def _filter_for_figures(self, dfs: list[pd.DataFrame]):
        concatenated_df = pd.concat(dfs)

        # Identify the last column containing date-like information
        date_columns = [
            col
            for col in concatenated_df.columns
            if re.search(self.regex_date, str(col))
        ]

        if date_columns:
            # Find the index of the last date column
            last_date_col_index = concatenated_df.columns.get_loc(date_columns[-1])
            # Keep only columns up to and including the last date column
            combined_scope_data = concatenated_df.iloc[:, : last_date_col_index + 1]
            # add units column
            combined_scope_data["Units"] = concatenated_df["Units"]

        # Drop the first column if necessary
        if not combined_scope_data.empty and len(combined_scope_data.columns) > 0:
            if combined_scope_data.columns[0] == "Unnamed: 0":
                combined_scope_data = combined_scope_data.iloc[:, 1:]

        # Drop empty columns
        combined_scope_data = combined_scope_data.dropna(axis=1, how="all")
        # Drop empty rows
        combined_scope_data = combined_scope_data.dropna(how="all")
        return combined_scope_data

    def _infer_units(self, df: pd.DataFrame):
        inferred_df = infer_units_for_rows(df)
        return inferred_df

    def _standardise_df(self, df: pd.DataFrame):
        standard = standardize_table(df)
        return standard


if __name__ == "__main__":
    ROOT_DIR = os.getenv("ROOT_OUTPUT_PATH")
    filter_obj = Filter(
        directory_path=os.path.join(ROOT_DIR, "META_PLATFORMS_INC-CLASS_A"),
        parser=TableParsers.DOCLING,
    )
    filter_obj.extract_filtered_df()

    filter_obj.filtered_df.to_csv(os.path.join(ROOT_DIR, "testing_meta.csv"))
