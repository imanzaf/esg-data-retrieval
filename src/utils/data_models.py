from typing import Union

from pydantic import BaseModel, Field


class Company(BaseModel):
    ticker: str = Field(..., title="Ticker Symbol")
    name: str = Field(..., title="Company Name")
    isin: str = Field(None, title="Company ISIN")
    esg_report_url: Union[str, None] = Field(None, title="Link to ESG Report")
