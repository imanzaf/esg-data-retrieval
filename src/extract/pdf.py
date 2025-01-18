"""
Methods for parsing full pdf documents

NOTE: NOT TESTED YET!
DOCUMENTATION: https://docs.cloud.llamaindex.ai/llamaparse/getting_started/python
"""

import os
import sys

from dotenv import load_dotenv
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_parse import LlamaParse
from loguru import logger

load_dotenv()

sys.path.append(f"{os.getenv('ROOT_DIR')}")

from src.utils.data_models import PDFParsers  # noqa: E402


class PDFAgent:

    def __init__(self, file_path: str, parser: PDFParsers = PDFParsers.LLAMA_PARSE):
        self.file_path = file_path
        self.parser = parser.value
        self.llama_api_key = os.getenv("LLAMA_API_KEY")  # get from .env
        self.parsed_pdf = None

    def parse(self):
        if self.parser == PDFParsers.LLAMA_PARSE.value:
            parsed_pdf = self._parse_with_llama()
            self.parsed_pdf = parsed_pdf
            return parsed_pdf
        else:
            logger.warning(f"Invalid parser specified: {self.parser}. Returning None.")
            return None

    def query(self, query: str):
        if self.parser == PDFParsers.LLAMA_PARSE.value:
            response = self._query_with_llama(query)
            return response
        else:
            logger.warning(f"Invalid parser specified: {self.parser}. Returning None.")
            return None

    def _parse_with_llama(self) -> str | None:
        try:
            # set up parser
            parser = LlamaParse(
                api_key=self.api_key,
                language="en",
                result_type="markdown",
            )

            # use SimpleDirectoryReader to parse file
            file_extractor = {".pdf": parser}
            documents = SimpleDirectoryReader(
                input_files=[self.file_path], file_extractor=file_extractor
            ).load_data()

            parsed_content = "\n\n---\n\n".join(
                [doc.get_content() for doc in documents]
            )
            return parsed_content

        except Exception as exc:
            logger.error(
                f"Unable to parse document with Llama - {self.file_path}: {exc}"
            )
            return None

    def _query_with_llama(self, query: str):
        parsed_pdf = self.parsed_pdf if self.parsed_pdf is not None else self.parse()
        if parsed_pdf is not None:
            index = VectorStoreIndex.from_documents(parsed_pdf)
            query_engine = index.as_query_engine()
            response = query_engine.query(query)
            return response
        else:
            return f"Unable to parse file {self.file_path}. Try again later!"
