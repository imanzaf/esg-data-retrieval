"""
Methods for extracting tables from PDFs.
"""

# import os

from pathlib import Path

import pandas as pd
from docling.document_converter import DocumentConverter

# %%
from dotenv import load_dotenv

# from transformers import pipeline
# import transformers
# import torch
# from huggingface_hub import InferenceClient

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


# %%
# class Emissions:
#     def __init__(self, csv_path):
#         self.df_path = csv_path
#         self.markdown = self.df_to_markdown()

#     def df_to_markdown(self):
#         df = pd.read_csv(self.df_path)
#         df_md = df.to_markdown()
#         return df_md

#     def extract(self):
#         client = InferenceClient(api_key="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")
#         # model_id = "meta-llama/Llama-3.3-70B-Instruct"
#         # pipeline = transformers.pipeline(
#         #     "text-generation",
#         #     model=model_id,
#         #     model_kwargs={"torch_dtype": torch.bfloat16},
#         #     device_map="auto",
#         # )

#         messages = [
#             {"role": "system", "content": "You are an expert at reviewing tables and extracting Scope 1 and Scope 2 emissions data from them. You always return the data in json format."},
#             {"role": "user", "content": self.markdown},
#         ]

#         completion = client.chat.completions.create(
#                         model="meta-llama/Llama-3.3-70B-Instruct",
# 	                    messages=messages,
# 	                    max_tokens=500
#                     )
#         # outputs = pipeline(
#         #     messages,
#         #     max_new_tokens=256,
#         # )
#         # return outputs[0]["generated_text"][-1]
#         return completion.choices[0].message


# %%
# hsbc_path = f"{os.getenv('ROOT_DIR')}/data/HSBC/240221-esg-review-2023.pdf"
# apple_path = (
#     f"{os.getenv('ROOT_DIR')}/data/AAPL/Apple_Environmental_Progress_Report_2024.pdf"
# )
# msft_path = f"{os.getenv('ROOT_DIR')}/data/MICROSOFT/RW1lmju.pdf"

# #%%
# output_dir = f"{os.getenv('ROOT_DIR')}/data/AAPL/docling"
# extractor = TableExtractor(apple_path, output_dir)
# tables = extractor.docling(save=True)

# %%


# %%
# if __name__ == "__main__":
#     df_path = f"{os.getenv('ROOT_DIR')}/data/AAPL/docling/Apple_Environmental_Progress_Report_2024-table-18.csv"
#     emissions = Emissions(df_path).extract()
#     print(emissions)


# maybe:
#  extract text, find scope 1 / scope 2 / ghg emissions followed by numbers using regex
#  save as table? or find tables in that page
