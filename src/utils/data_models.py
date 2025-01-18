# NOTE - data model not being used currently, leaving in codebase for future reference if needed
"""
Stores constants / data models
"""

from typing import Union
import re

from enum import Enum
from pydantic import BaseModel, Field


class RegexPatterns(Enum):
    SCOPE1 = r"\b(scope\s*1|scope\s*i|scope\s*one)\b"
    SCOPE2 = r"\b(scope\s*2|scope\s*ii|scope\s*two)\b"
    YEAR_1 = r"\b(?:FY|FISCAL\s*YEAR)?\s*(\d{2}|20\d{2})"
    YEAR_2 = r"(?:[-–]\d{2}|\s)?\b"
    UNITS_1 = r"(?:\b(?:\d+(?:,\d{3})*(?:\.\d+)?|million|billion|thousand)?)"
    UNITS_2 = r"\s*(?:tco2e|tco2-e|co2e|co₂e|co2-eq|co₂-eq|mtco2e|mtco₂e|ktco2e|ktco₂e|mt|kt|tons?|tonnes?|metric\s*tons?)"


class TableParsers(Enum):
    DOCLING = "docling"
    TABULA = "tabula"


class PDFParsers(Enum):
    LLAMA_PARSE = "llama"


class Company(BaseModel):
    ticker: str = Field(None, title="Ticker Symbol")
    name: str = Field(None, title="Company Name")
    isin: str = Field(None, title="Company ISIN")
    esg_report_url: Union[str, None] = Field(None, title="Link to ESG Report")
