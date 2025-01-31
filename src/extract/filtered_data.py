import os
import re
import sys
from argparse import PARSER
from loguru import logger
from pydantic import BaseModel

import pandas as pd
from dotenv import load_dotenv
load_dotenv()
sys.path.append(os.getenv("ROOT_DIR"))

from src.find.company_profile import ROOT_OUTPUT_PATH
from src.utils.data_models import TableParsers
from src.utils.get_units import infer_units_for_rows
from src.utils.standardize_table_rework import standardize_table


class Filter(BaseModel):
    regex_scope: str = r"(Scope\s1|Scope\s2)"
    regex_exclude: str = r"(excluded|Excluded|avoided|Avoided|aim|Aim|goal|Goal|revenue|Revenue|target|Target|forecast|Forecast|estimate|Estimate|projection|Projection|expectation|Expectation|and 3|Scope 3|\+ 3)"
    regex_date: str = r"(\bFY\d{2}\b|\b20\d{2}\b|\b[Ff]iscal\s[Yy]ear\b)"

    scope_data: list = []

    directory_path: str
    parser: TableParsers

    docling_tables: list = []
    tables_with_units: list = []
    concantenated_df: pd.DataFrame = None
    filtered_df: pd.DataFrame = None
    inferred_df: pd.DataFrame = None

    final_df: pd.DataFrame = None

    class Config:
        arbitrary_types_allowed = True

    def load_dfs(self):
        dfs = []
        for filename in os.listdir(os.path.join(self.directory_path, self.parser.value)):
            if filename.endswith(".csv"):
                file_path = os.path.join(self.directory_path, self.parser.value, filename)
                df = pd.read_csv(file_path)
                dfs.append(df)
        self.docling_tables = dfs
        return dfs
    
    def append_units_column(self):
        dfs = []
        for df in self.docling_tables:
            dfs.append(get_units_raw_input(df))
        self.tables_with_units = dfs
        return dfs
    
    def filter_for_scope(self):
        filtered_dfs = []
        for df in self.tables_with_units:
            filtered_df = df[df.apply(
                            lambda row: row.astype(str)
                            .str.contains(self.regex_scope, regex=True)
                            .any(),
                            axis=1,
                        )]
            filtered_df = filtered_df[
                    ~filtered_df.apply(
                        lambda row: row.astype(str)
                        .str.contains(self.regex_exclude, regex=True)
                        .any(),
                        axis=1,
                    )
                ]
            filtered_dfs.append(filtered_df)
            self.concantenated_df = pd.concat(filtered_dfs)
        return filtered_dfs
    
    def filter_for_figures(self):
        date_columns = [
            col for col in self.concantenated_df.columns if re.search(self.regex_date, col)
        ]

        last_date_col_index = self.concantenated_df.columns.get_loc(date_columns[-1])
        filtered_df = self.concantenated_df.iloc[:, :last_date_col_index + 1]
        
        if not filtered_df.empty and len(filtered_df.columns) > 0:
            filtered_df = filtered_df.iloc[:, 1:]
        filtered_df = filtered_df.dropna(axis=1, how="all")
        filtered_df = filtered_df.dropna(how="all")
        self.filtered_df = filtered_df
        return filtered_df
    
    def infer_units(self):
        inferred_df = infer_units_for_rows(self.filtered_df)
        self.inferred_df = inferred_df
        return inferred_df
    
    def standardise_df(self):
        standard = standardize_table(self.inferred_df)
        self.final_df = standard
        return standard



def extract_units(value):
    match = re.search(r'\b(t\s*o\s*n\s*s\s*o\s*f\s*C\s*O\s*2\s*e|m\s*e\s*t\s*r\s*i\s*c\s*t\s*o\s*n\s*s\s*o\s*f\s*C\s*O\s*2\s*e|C\s*O\s*2\s*e|t\s*C\s*O\s*2\s*e|M\s*T\s*C\s*O\s*2\s*e|k\s*g\s*C\s*O\s*2\s*e|k\s*t\s*C\s*O\s*2\s*e|g\s*C\s*O\s*2\s*e|h\s*u\s*n\s*d\s*r\s*e\s*d\s*s\s*o\s*f\s*t\s*o\s*n\s*n\s*e\s*s\s*C\s*O\s*2\s*e|t\s*h\s*o\s*u\s*s\s*a\s*n\s*d\s*s\s*o\s*f\s*t\s*o\s*n\s*n\s*e\s*s\s*C\s*O\s*2\s*e|m\s*i\s*l\s*l\s*i\s*o\s*n\s*s\s*o\s*f\s*t\s*o\s*n\s*n\s*e\s*s\s*C\s*O\s*2\s*e|b\s*i\s*l\s*l\s*i\s*o\s*n\s*s\s*o\s*f\s*t\s*o\s*n\s*n\s*e\s*s\s*C\s*O\s*2\s*e|m\s*e\s*t\s*r\s*i\s*c\s*t\s*o\s*n\s*n\s*e\s*s\s*C\s*O\s*2\s*e|m\s*e\s*t\s*r\s*i\s*c\s*t\s*o\s*n\s*s\s*C\s*O\s*2\s*e|t\s*o\s*n\s*s\s*C\s*O\s*2\s*e|t\s*o\s*n\s*n\s*e\s*s\s*C\s*O\s*2\s*e)\b', str(value), re.IGNORECASE)

    return match.group(0) if match else None

def get_units_raw_input(df: pd.DataFrame):
    updated_df = df.copy()
    
    updated_df["Units"] = None
    first_unit = None
    for idx, row in df.iterrows():
        extracted_units = extract_units(pd.DataFrame(row).to_string())
        updated_df.iloc[idx]['Units'] = extracted_units

        if first_unit is None and extract_units is not None:
            first_unit = extracted_units
    
    updated_df["Units"] = updated_df["Units"].apply(lambda x: first_unit if x is None else x)

    return updated_df

def infer_emissions_unit(max, min):
    """
    Infer the unit of measurement based on the numerical value.
    """
    if max < 7:
        return "Inferred: CO₂e per FTE"  # Emissions per Full-Time Employee
    elif min > 2 and max < 100:
        return "Inferred: MMT CO₂e"  # Million Metric Tons
    elif min >10 and max < 500 :
        return "Inferred: thousand MT CO₂e"  # Thousand Metric Tons
    return "Inferred: MT CO₂e"  # Metric Tons

def clean_numeric_values(row):
    # Now apply the cleaning to all columns, including the first one (Metric)
    numeric_values = pd.to_numeric(
        row.astype(str).str.replace(r'(?<=\d),(?=\d{3}\b)', '', regex=True),  # Remove commas only for thousands
        errors='coerce'  # Ignore non-numeric values, treat them as NaN
    ).dropna()
    return numeric_values

def infer_units_for_rows(filtered_rows):
    """
    Infer emissions unit for each row based on numerical values.
    """
    unit_inferences = []
    for idx, row in filtered_rows.iterrows():
        try:
            # If the row already has a valid unit, keep it
            if row["Units"] not in ["", None, "Unknown"]:
                unit_inferences.append(row["Units"])
                continue
        except:
            unit_inferences.append(None)

        # Extract numerical values from the row (excluding the first column 'Metric')
        numeric_values = clean_numeric_values(row)

        if numeric_values.empty:
            unit_inferences.append(None)  # No valid numerical data
        else:
            # Infer unit based on the maximum value in the row
            inferred_unit = infer_emissions_unit(numeric_values.max(), numeric_values.min())
            unit_inferences.append(inferred_unit)

    # Add the inferred units as a new column
    filtered_rows["Units"] = unit_inferences
    return filtered_rows


if __name__ == '__main__':
    ROOT_DIR = os.getenv("ROOT_OUTPUT_PATH")
    filter_obj = Filter(directory_path=os.path.join(ROOT_DIR, "MICROSOFT_CORP"), parser=TableParsers.DOCLING)
    filter_obj.load_dfs()
    filter_obj.append_units_column()
    filter_obj.filter_for_scope()
    filter_obj.filter_for_figures()
    filter_obj.infer_units()
    df = filter_obj.standardise_df()
    
    df.to_csv(os.path.join(ROOT_DIR, "testing_iz_final.csv"))
