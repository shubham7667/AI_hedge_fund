import os
import time
import yfinance as yf
def load_weekly_data():
    day = time.localtime().tm_mday

    data = yf.download(
        "AMZN",
        start="2016-11-10",
        end="2026-07-10",
        interval='1wk'
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

def load_daily_data():
    day = time.localtime().tm_mday
    data = yf.download(
        "AMZN",
        start="2016-11-10",
        end="2026-07-10",
        interval='1d'
    )
    
    data_folder = os.path.dirname(__file__)
    file_name = os.path.join(
        data_folder,
        f"stock_daily_data_on_data{day}.csv"
    )
    data.to_csv(file_name,index=False)
    return data