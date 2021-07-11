import datetime
import pandas as pd  
from backtesting_stratgies.SMA import SmaCross

from backtesting import Backtest


stock = "2330.TW"
df = pd.read_csv(f"./data/{stock}.csv", index_col=0)
df = df.interpolate()


df.index = pd.to_datetime(df.index) 


test = Backtest(df, SmaCross, cash=10000, commission=.002)

result = test.run()

opt_result = test.optimize(n1=range(5, 50, 5),  
                    n2=range(10, 120, 5),
                    maximize='SQN',  
                    constraint=lambda p: p.n1 < p.n2)  
      
print("Original strategy")
print(result) 
print() 
print("Optimize strategy")
print(opt_result)  

#test.plot(filename=f"./backtest_result/{stock}.html") 