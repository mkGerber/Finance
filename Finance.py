import pandas as pd
import yfinance as yf
import datetime
import time

# Set display options for Pandas
pd.options.display.max_rows = 10

# Define start and end dates using datetime
start = datetime.datetime(2024, 1, 1, 9, 30)  # January 1, 2024, 09:30 AM
end = datetime.datetime(2024, 2, 19, 10, 30)  # February 19, 2024, 10:30 AM

# Get the first 10 allowed tickers (example: S&P 500 top 10)
tickers = ["AAPL", "GOOGL", "AMZN", "TSLA", "META", "NVDA", "BRK-B", "JPM", "V"]

# Dictionary to store downloaded data
all_data = {}

# Loop through tickers and download data
for ticker in tickers:
    print(f"Downloading {ticker} data...")

    try:
        data = yf.download(ticker, interval="1d", start=start, end=end, progress=False)

        if not data.empty:
            all_data[ticker] = data
            data.to_csv(f"{ticker}_5min.csv")  # Save each ticker's data to CSV

        # To avoid hitting the rate limit, pause for a short duration
        time.sleep(2)

    except Exception as e:
        print(f"Error downloading {ticker}: {e}")

print("Download complete!")
