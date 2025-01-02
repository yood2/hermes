import yfinance as yf

def is_valid_ticker(ticker: str) -> bool:
    """
    - Verify if a given ticker represents a valid stock.
    - Args:
        ticker (str): The stock ticker symbol to verify        
    - Returns:
        bool: True if the ticker is valid, False otherwise
    """
    try:
        if not isinstance(ticker, str) or not ticker:
            return False
        stock = yf.Ticker(ticker)
        info = stock.info
        return 'symbol' in info and info['symbol'] == ticker
        
    except Exception:
        return False

def get_stock_info(ticker: str) -> dict:
    """
    - Get the stock info from yfinance
    - Args:
        ticker (str): The stock ticker symbol to get info for
    - Returns:
        dict: The stock info
    """
    stock = yf.Ticker(ticker)
    return stock.info