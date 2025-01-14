import tabula
import pandas as pd
import os
from pypdf import PdfReader


def tables_extraction(pdf_path, keywords, output_dir="output_tables"):
   """
   Extracts tables from a PDF, filters them based on the presence of specified keywords,
   and exports the filtered tables to CSV files.
   Adds NaN when two words from the same column and row are on 2 separate lines in the terminal output
   but not in CSV file so see whether that needs to be fixed


   Args:
       pdf_path (str): Path to PDF file.
       keywords (list): List of keywords to search for in the tables.
       output_dir (str): Directory where filtered tables will be saved as CSV files.


   Returns:
       None
   """
   # Use Pandas for better visualization
   pd.set_option('display.max_rows', None)
   pd.set_option('display.max_columns', None)
   pd.set_option('display.width', None)
   pd.set_option('display.max_colwidth', None)


   # Checks that the folder for CSV files exists
   os.makedirs(output_dir, exist_ok=True)


   # Read all tables from PDF
   tables = tabula.read_pdf(pdf_path, pages="all", multiple_tables=True)


   # Checks if a table contains any of the keywords
   def contains_keywords(table, keywords):
       if table is not None:
           for keyword in keywords:
               if table.apply(lambda x: x.astype(str).str.contains(keyword, case=False, na=False)).any().any():
                   return True
       return False


   # Only process and save tables containing the keywords
   for i, table in enumerate(tables):
       if contains_keywords(table, keywords):
           print(f"\nTable {i + 1} contains the specified keywords:\n")
           print(table)


           # Creates a folder in src directory containing all tables saved as CSV files
           output_file = os.path.join(output_dir, f"table_{i + 1}.csv")
           table.to_csv(output_file, index=False)
           print("\n--- Extracting Tables ---")
           print(f"Table {i + 1} exported to {output_file}")




def text_extraction(pdf_path):
   """
   Extracts and filters sentences containing specific keywords from a PDF document..
   """
   keywords = ["Scope 1", "Scope 2", "Scopes 1", "Scopes 2", "Scopes 1 & 2"]


   # Extract sentences with PyPDF
   print("\n--- Extracting Sentences ---")
   reader = PdfReader(pdf_path)


   for page_num, page in enumerate(reader.pages):
       text = page.extract_text()


       if text:
           sentences = text.split('. ')
           for sentence in sentences:
               if any(keyword.lower() in sentence.lower() for keyword in keywords):
                   print(f"Page {page_num + 1}: {sentence.strip()}.")




# Takes file from local machine, gave an example of how it would look for me
pdf_path = "/Users/estheragossa/PycharmProjects/esg-data-retrieval/data/BARCLAYS/TCFD%20BISL%20report%202024.pdf"
keywords = ["Scope 1", "Scope 2", "Scopes 1", "Scopes 2", "Scopes 1 & 2"]


tables_extraction(pdf_path, keywords)
text_extraction(pdf_path)
