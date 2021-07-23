import yfinance as yf 
import  pandas as pd
from pandas_datareader import data
import datetime
import csv 

yf.pdr_override()

stock_list = []
with open("data/stock_id.csv") as f:
    for row in f:
        stock_list.append(row.split()[0])


target_stock = '2887.TW'

start_date = datetime.datetime(2021, 4, 1)
end_date = datetime.datetime(2021, 7, 18)
df = data.get_data_yahoo([target_stock], start_date, end_date)

filename = f'./data/{target_stock}.csv'
df.to_csv(filename)



