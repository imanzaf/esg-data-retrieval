import os

import pandas as pd
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
ROOT_DIR = os.getenv("ROOT_DIR")


def get_data():
    # Load the CSV file
    csv_file_path = os.path.join(
        ROOT_DIR, "data/XWD_holdings.csv"
    )  # Path to your input CSV file
    df = pd.read_csv(
        csv_file_path, header=0
    )  # Assuming header is already in the first row (change as needed)

    # Filter the DataFrame for rows where 'Asset Class' is 'Equity'
    df_filtered = df[df["Asset Class"] == "Equity"]

    # Select the required columns
    columns_to_keep = ["Ticker", "Name", "Sector", "Location", "Currency", "Exchange"]
    return df_filtered[columns_to_keep]


# Function to get unique locations
def get_unique_locations():
    df = get_data()
    """
    Get a list of unique locations from the DataFrame.
    """
    return df["Location"].unique().tolist()


# Function to get unique sectors
def get_unique_sectors():
    df = get_data()
    """
    Get a list of unique sectors from the DataFrame.
    """
    return df["Sector"].unique().tolist()


# Function to filter by country and/or sector
def filter_dataframe(df_filtered, country=None, sector=None):
    if country is None and sector is None:
        df_filtered = df
    else:
        # Filter by country if provided
        if country is not None:
            df_filtered = df[df["Location"] == country]
        else:
            df_filtered = df

        # Filter by sector if provided
        if sector is not None:
            df_filtered = df_filtered[df_filtered["Sector"] == sector]

        # Save the filtered DataFrame
    file_name = "current_query.csv"
    output_path = os.path.join(ROOT_DIR, "data", file_name)
    df_filtered.to_csv(output_path, index=False)
    print(f"Filtered data saved to: {output_path}")

    return df_filtered


if __name__ == "__main__":
    # Example usage:
    # Let's say the user inputs a country and/or sector from the enums:
    df = get_data()
    print(get_unique_sectors())
    print(get_unique_locations())

    country_input = None  # Example: country input from LocationEnum, None if not filtering by country
    sector_input = "Information Technology"  # Example: sector input from SectorEnum, None if not filtering by sector

    # Get filtered dataframe
    filtered_df = filter_dataframe(
        get_data(), country=country_input, sector=sector_input
    )

    # You can now use filtered_df for further processing or save it to a new CSV
    print(filtered_df)
