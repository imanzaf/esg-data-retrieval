"""
Methods for parsing full pdf documents

# https://docs.cloud.llamaindex.ai/llamaparse/getting_started/python
"""
from llama_parse import LlamaParse
from llama_index.core import SimpleDirectoryReader
from loguru import logger
from src.utils.data_models import PDFParsers


class PDFAgent:

    def __init__(self):
        self.llama_api_key = ""  # get from env
        self.file_path = ""

    def parse(self):
        pass

    def query(self):
        pass

    def _parse_with_llama(
        self
    ) -> str | None:
        """
        # TODO
        """
        try:
            # set up parser
            parser = LlamaParse(
                api_key=self.api_key,
                language="en",
                result_type="markdown",
            )

            # use SimpleDirectoryReader to parse file
            file_extractor = {".pdf": parser}
            documents = SimpleDirectoryReader(input_files=[self.file_path], file_extractor=file_extractor).load_data()

            parsed_content = "\n\n---\n\n".join(
                [doc.get_content() for doc in documents]
            )
            return parsed_content

        except Exception as exc:
            logger.error(f"Unable to parse document with Llama - {self.file_path}: {exc}")
            return None
    
    def _query_with_llama(self):
        pass
