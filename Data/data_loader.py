import os
import time
import yfinance as yf
def load_data():
    day = time.localtime().tm_mday

    data = yf.download(
        "AMZN",
        start="2016-11-10",
        end="2026-07-10"
    )

    # Get the Data folder path
    data_folder = os.path.dirname(__file__)

    # Create the full path
    filename = os.path.join(
        data_folder,
        f"stock_data_on_date_{day}.csv"
    )

    data.to_csv(filename, index=False)

    return data