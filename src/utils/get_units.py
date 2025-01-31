import os

import dotenv
import pandas as pd
import numpy as np
import pandas as pd
import re
from src.utils.data_models import TableParsers


#to do:iterate through all the files in the directory

def get_units_raw_input(df):
    # Function to extract units of measurement
    def extract_units(value):
        match = re.search(r'\b(t\s*o\s*n\s*s\s*o\s*f\s*C\s*O\s*2\s*e|C\s*O\s*2\s*e|t\s*C\s*O\s*2\s*e|M\s*T\s*C\s*O\s*2\s*e|k\s*g\s*C\s*O\s*2\s*e|k\s*t\s*C\s*O\s*2\s*e|g\s*C\s*O\s*2\s*e|h\s*u\s*n\s*d\s*r\s*e\s*d\s*s\s*o\s*f\s*t\s*o\s*n\s*n\s*e\s*s\s*C\s*O\s*2\s*e|t\s*h\s*o\s*u\s*s\s*a\s*n\s*d\s*s\s*o\s*f\s*t\s*o\s*n\s*n\s*e\s*s\s*C\s*O\s*2\s*e|m\s*i\s*l\s*l\s*i\s*o\s*n\s*s\s*o\s*f\s*t\s*o\s*n\s*n\s*e\s*s\s*C\s*O\s*2\s*e|b\s*i\s*l\s*l\s*i\s*o\s*n\s*s\s*o\s*f\s*t\s*o\s*n\s*n\s*e\s*s\s*C\s*O\s*2\s*e|m\s*e\s*t\s*r\s*i\s*c\s*t\s*o\s*n\s*n\s*e\s*s\s*C\s*O\s*2\s*e|m\s*e\s*t\s*r\s*i\s*c\s*t\s*o\s*n\s*s\s*C\s*O\s*2\s*e|t\s*o\s*n\s*s\s*C\s*O\s*2\s*e|t\s*o\s*n\s*n\s*e\s*s\s*C\s*O\s*2\s*e)\b', str(value), re.IGNORECASE)

        return match.group(0) if match else None

        # Apply unit extraction function to each row

    df['Units'] = df.apply(lambda row: extract_units(row.to_string()) if pd.notna(row).all() else None, axis=1)
    # Find the first valid unit (ignoring None and NaN)
    first_unit = df['Units'].dropna().replace("None", pd.NA).dropna().iloc[0] if not df['Units'].dropna().replace("None", pd.NA).empty else None

    # Replace missing values (None, NaN, "None") with the first valid unit
    df['Units'] = df['Units'].apply(lambda x: first_unit if pd.isna(x) or x == "None" else x)

    # Print the DataFrame with the new column
    print(df)
    return df





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



def infer_units_for_rows(filtered_rows):
    """
    Infer emissions unit for each row based on numerical values.
    """
    if "Units" not in filtered_rows.columns:
        filtered_rows["Units"] = None  # Add "Units" column if missing

    unit_inferences = []

    for idx, row in filtered_rows.iterrows():
        # If the row already has a valid unit, keep it
        if pd.notna(row.get("Units")) and row["Units"] not in ["", None, "Unknown"]:
            unit_inferences.append(row["Units"])
            continue

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

def clean_numeric_values(row):
    # Now apply the cleaning to all columns, including the first one (Metric)
    numeric_values = pd.to_numeric(
        row.astype(str).str.replace(r'(?<=\d),(?=\d{3}\b)', '', regex=True),  # Remove commas only for thousands
        errors='coerce'  # Ignore non-numeric values, treat them as NaN
    ).dropna()
    return numeric_values


if __name__ == '__main__':
    dotenv.load_dotenv()
    OUTPUT_DIR = os.getenv("ROOT_OUTPUT_PATH")
    df = pd.read_csv(os.path.join(OUTPUT_DIR, "NVIDA", TableParsers.DOCLING.value, "FY2024-NVIDIA-Corporate-Sustainability-Report-table-2.csv" ))
    get_units_raw_input(df)