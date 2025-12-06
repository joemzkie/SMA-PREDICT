import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

class Trade:
    def __init__(self, ticker=None, start=None, end=None):
        self.ticker = ticker
        self.start = start
        self.end = end
        self.df = None

    def retrieve(self):
        self.df = yf.download(self.ticker, start=self.start, end=self.end)
        self.df = self.df[["Close"]]

        self.df["SMA20"] = self.df["Close"].rolling(window=20).mean()
        self.df["SMA50"] = self.df["Close"].rolling(window=50).mean()
        self.df["SMA200"] = self.df["Close"].rolling(window=200).mean()

        return self.df

    def plot(self):
        if self.df is None:
            print(" No data. Run retrieve() first.")
            return

        plt.figure(figsize=(14,7))
        plt.plot(self.df.index, self.df["Close"], label="Close Price", alpha=0.6)
        plt.plot(self.df.index, self.df["SMA20"], label="SMA 20", linestyle="--")
        plt.plot(self.df.index, self.df["SMA50"], label="SMA 50", linestyle="--")
        plt.plot(self.df.index, self.df["SMA200"], label="SMA 200", linestyle="--")

        plt.title(f"{self.ticker} Stock with SMA(20), SMA(50), SMA(200)")
        plt.xlabel("Date")
        plt.ylabel("Price ($)")
        plt.legend()
        plt.show()


def main():
    print("Pick stocks: AAPL, MSFT, AMZN, TSLA, GOOGL")
    stock = str(input("Enter Stock: "))
    end_date = datetime.today().strftime("%Y-%m-%d")
    start_date = (datetime.today() - timedelta(days=365)).strftime("%Y-%m-%d")

    t = Trade(stock, start_date, end_date)
    t.retrieve()
    t.plot()

if __name__ == "__main__":
    main()
