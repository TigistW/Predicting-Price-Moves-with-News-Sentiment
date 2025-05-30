import pandas as pd

def load_headlines(path="data/headlines.csv"):
    return pd.read_csv(path, parse_dates=["date"])

def load_stock_data(ticker="AAPL", start="2023-01-01", end="2024-01-01"):
    import yfinance as yf
    return yf.download(ticker, start=start, end=end)
