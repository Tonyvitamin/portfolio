import datetime
import pandas as pd  
from bt_strategies.SMA import SmaCross

import backtrader as bt

cerebro = bt.Cerebro()
stock = "2330.TW"
df = pd.read_csv(f"./data/{stock}.csv", index_col=0)
df = df.interpolate()
df.index = pd.to_datetime(df.index)


data = bt.feeds.PandasData(dataname=df)
cerebro.adddata(data)

cerebro.addstrategy(SmaCross)
cerebro.run()
cerebro.plot()
