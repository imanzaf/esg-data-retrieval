import os
import re

import dotenv
import pandas as pd

from src.utils.data_models import TableParsers


def extract_units(value):
    match = re.search(
        r"\b(t\s*o\s*n\s*s\s*o\s*f\s*C\s*O\s*2\s*e|m\s*e\s*t\s*r\s*i\s*c\s*t\s*o\s*n\s*s\s*o\s*f\s*C\s*O\s*2\s*e|C\s*O\s*2\s*e|t\s*C\s*O\s*2\s*e|M\s*T\s*C\s*O\s*2\s*e|k\s*g\s*C\s*O\s*2\s*e|k\s*t\s*C\s*O\s*2\s*e|g\s*C\s*O\s*2\s*e|h\s*u\s*n\s*d\s*r\s*e\s*d\s*s\s*o\s*f\s*t\s*o\s*n\s*n\s*e\s*s\s*C\s*O\s*2\s*e|t\s*h\s*o\s*u\s*s\s*a\s*n\s*d\s*s\s*o\s*f\s*t\s*o\s*n\s*n\s*e\s*s\s*C\s*O\s*2\s*e|m\s*i\s*l\s*l\s*i\s*o\s*n\s*s\s*o\s*f\s*t\s*o\s*n\s*n\s*e\s*s\s*C\s*O\s*2\s*e|b\s*i\s*l\s*l\s*i\s*o\s*n\s*s\s*o\s*f\s*t\s*o\s*n\s*n\s*e\s*s\s*C\s*O\s*2\s*e|m\s*e\s*t\s*r\s*i\s*c\s*t\s*o\s*n\s*n\s*e\s*s\s*C\s*O\s*2\s*e|m\s*e\s*t\s*r\s*i\s*c\s*t\s*o\s*n\s*s\s*C\s*O\s*2\s*e|t\s*o\s*n\s*s\s*C\s*O\s*2\s*e|t\s*o\s*n\s*n\s*e\s*s\s*C\s*O\s*2\s*e)\b",
        str(value),
        re.IGNORECASE,
    )

    return match.group(0) if match else None


def get_units_raw_input(df: pd.DataFrame):
    updated_df = df.copy()

    updated_df["Units"] = None
    first_unit = None
    for idx, row in df.iterrows():
        extracted_units = extract_units(pd.DataFrame(row).to_string())
        updated_df.iloc[idx]["Units"] = extracted_units

        if first_unit is None and extract_units is not None:
            first_unit = extracted_units

    updated_df["Units"] = updated_df["Units"].apply(
        lambda x: first_unit if x is None else x
    )

    return updated_df


def infer_emissions_unit(max, min):
    """
    Infer the unit of measurement based on the numerical value.
    """
    if max < 7:
        return "Inferred: CO₂e per FTE"  # Emissions per Full-Time Employee
    elif min > 2 and max < 100:
        return "Inferred: MMT CO₂e"  # Million Metric Tons
    elif min > 10 and max < 500:
        return "Inferred: thousand MT CO₂e"  # Thousand Metric Tons
    return "Inferred: MT CO₂e"  # Metric Tons


def clean_numeric_values(row):
    # Now apply the cleaning to all columns, including the first one (Metric)
    numeric_values = pd.to_numeric(
        row.astype(str).str.replace(
            r"(?<=\d),(?=\d{3}\b)", "", regex=True
        ),  # Remove commas only for thousands
        errors="coerce",  # Ignore non-numeric values, treat them as NaN
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
        except Exception:
            unit_inferences.append(None)

        # Extract numerical values from the row (excluding the first column 'Metric')
        numeric_values = clean_numeric_values(row)

        if numeric_values.empty:
            unit_inferences.append(None)  # No valid numerical data
        else:
            # Infer unit based on the maximum value in the row
            inferred_unit = infer_emissions_unit(
                numeric_values.max(), numeric_values.min()
            )
            unit_inferences.append(inferred_unit)

    # Add the inferred units as a new column
    filtered_rows["Units"] = unit_inferences
    return filtered_rows


if __name__ == "__main__":
    dotenv.load_dotenv()
    OUTPUT_DIR = os.getenv("ROOT_OUTPUT_PATH")
    df = pd.read_csv(
        os.path.join(
            OUTPUT_DIR,
            "NVIDA",
            TableParsers.DOCLING.value,
            "FY2024-NVIDIA-Corporate-Sustainability-Report-table-2.csv",
        )
    )
    get_units_raw_input(df)
