from sqlmodel import SQLModel, Field
from typing import Optional
from app.utils.market_utils import is_valid_ticker, get_stock_info
from datetime import datetime

class Stock(SQLModel, table=True):
    stock_id: Optional[int] = Field(default=None, primary_key=True)
    ticker: str
    fullName: str
    exchange: Optional[str]
    sector: Optional[str]
    createdAt: datetime = Field(default_factory=datetime.utcnow)

    def __init__(self, ticker: str):
        self.ticker = self.validate_ticker(ticker)
        self.createdAt = datetime.utcnow()
        info = get_stock_info(ticker)
        self.fullName = info['longName']
        self.exchange = info['exchange']
        self.sector = info['sector']

    def validate_ticker(self, ticker):
        if not ticker:
            raise ValueError("Ticker cannot be empty")
        if not is_valid_ticker(ticker):
            raise ValueError("Ticker is not valid")
        return ticker