"""
Methods for extracting tables from PDFs.
"""

# %%

# %%
import os
from pathlib import Path

import pandas as pd

# import torch
# import transformers
from docling.document_converter import DocumentConverter

# %%
from dotenv import load_dotenv

# from huggingface_hub import InferenceClient
from transformers import pipeline

# %%
# from docling.document_converter import DocumentConverter


load_dotenv()


class TableExtractor:

    def __init__(self, path, output_dir):
        self.input_path = path
        self.output_dir = output_dir
        self.tables = []

    @staticmethod
    def filter_table(df):
        """Check if the table contains Scope 1 or Scope 2 and add it to the results."""
        table_text = df.to_string(
            index=False, header=False
        )  # Convert table to string for searching keywords
        if any(
            [x in table_text.lower() for x in ["ghg emissions", "scope 1", "scope 2"]]
        ):  # Check if the table contains relevant data  # "Scope 1", "Scope 2"
            return df
        return None

    def docling(self, save: bool = True):
        tables = []
        # convert document using docling
        doc_converter = DocumentConverter()
        conv_res = doc_converter.convert(self.input_path)
        # create output dir
        output_dir = Path(self.output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        doc_filename = conv_res.input.file.stem

        # Export tables
        for table_ix, table in enumerate(conv_res.document.tables):
            table_df: pd.DataFrame = table.export_to_dataframe()

            # filter table for presence of relevant info
            table_filtered = self.filter_table(table_df)
            if table_filtered is not None and save:
                # Save the table as csv
                element_csv_filename = (
                    output_dir / f"{doc_filename}-table-{table_ix+1}.csv"
                )
                table_df.to_csv(element_csv_filename)
                tables.append(table_df)
        self.tables = tables

    def get_docling_groups(self):
        # convert document using docling
        doc_converter = DocumentConverter()
        conv_res = doc_converter.convert(self.input_path)

        # return groups
        return conv_res.groups


# %%
os.environ["PYTORCH_ENABLE_MPS_FALLBACK"] = "1"
import torch  # noqa: E402


class Emissions:
    def __init__(self, csv_path):
        self.df_path = csv_path
        self.markdown = self.df_to_markdown()

    def df_to_markdown(self):
        df = pd.read_csv(self.df_path)
        df_md = df.to_markdown()
        return df_md

    def extract(self):
        # need cuda & gpu to run this - mps doesnt work
        pipe = pipeline(
            "text-generation",
            model="google/gemma-2-2b-it",
            model_kwargs={"torch_dtype": torch.float16},
            device="cuda",  # replace with "mps" to run on a Mac device
        )

        messages = [
            {
                "role": "user",
                "content": f"Extract the scope 1 and scope 2 emissions from the following table: \n{self.markdown}",
            },
        ]

        outputs = pipe(messages, max_new_tokens=256)
        assistant_response = outputs[0]["generated_text"][-1]["content"].strip()
        print(assistant_response)
        return assistant_response


# %%
hsbc_path = f"{os.getenv('ROOT_DIR')}/data/HSBC/240221-esg-review-2023.pdf"
apple_path = (
    f"{os.getenv('ROOT_DIR')}/data/AAPL/Apple_Environmental_Progress_Report_2024.pdf"
)
# msft_path = f"{os.getenv('ROOT_DIR')}/data/MICROSOFT/RW1lmju.pdf"

# %%
output_dir = f"{os.getenv('ROOT_DIR')}/data/AAPL/docling"
extractor = TableExtractor(apple_path, output_dir)
tables = extractor.docling(save=True)
# groups = extractor.get_docling_groups()

# %%
df_path = f"{os.getenv('ROOT_DIR')}/data/AAPL/docling/Apple_Environmental_Progress_Report_2024-table-18.csv"
emissions = Emissions(df_path).extract()

# %%
# if __name__ == "__main__":
#     df_path = f"{os.getenv('ROOT_DIR')}/data/AAPL/docling/Apple_Environmental_Progress_Report_2024-table-18.csv"
#     emissions = Emissions(df_path).extract()
#     print(emissions)


# maybe:
#  extract text, find scope 1 / scope 2 / ghg emissions followed by numbers using regex
#  save as table? or find tables in that page
