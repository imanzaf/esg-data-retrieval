"""
Stores enums and data models
"""

from enum import Enum

from pydantic import BaseModel, Field


class SearchKeyWords(Enum):
    ESG = "esg"
    CSR = "csr"
    SUSTAINABILITY = "sustainability"
    EMISSION = "emission"
    ENVIRONMENT = "environment"
    SCOPE_1 = "scope 1"
    SCOPE_2 = "scope 2"
    SCOPE = "scope"
    SUSTAINABLE = "sustainable"
    IMPACT = "impact"
    REPORT = "report"
    FACT_SHEET = "fact sheet"


class RegexPatterns(Enum):
    SCOPE1 = r"\b(scope\s*1|scope\s*i|scope\s*one)\b"
    SCOPE2 = r"\b(scope\s*2|scope\s*ii|scope\s*two)\b"
    YEAR_1 = r"\b(?:FY|FISCAL\s*YEAR)?\s*(\d{2}|20\d{2}|[-–]\d{2})"
    YEAR_2 = r"\b(\d{2}|20\d{2}|[-–]\d{2})"
    UNITS_1 = r"\b(?:\d+(?:,\d{3})*(?:\.\d+)?|million|billion|thousand)"
    UNITS_2 = r"\s*(?:tco2e|tco2-e|co2e|co₂e|co2-eq|co₂-eq|mtco2e|mtco₂e|ktco2e|ktco₂e|mt|kt|tons?|tonnes?|metric\s*tons?)"


class TableParsers(Enum):
    DOCLING = "docling"
    TABULA = "tabula"


class PDFParsers(Enum):
    LLAMA_PARSE = "llama"


class Company(BaseModel):
    ticker: str = Field(..., title="Ticker Symbol")
    name: str = Field(..., title="Company Name")
    isin: str = Field(..., title="Company ISIN")
