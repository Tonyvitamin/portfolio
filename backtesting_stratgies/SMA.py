from backtesting import Backtest, Strategy 

from backtesting.lib import crossover
from backtesting.test import SMA 


class SmaCross(Strategy): 
    n1 = 5 
    n2 = 20 

    def init(self):
        self.sma1 = self.I(SMA, self.data.Close, self.n1) 
        self.sma2 = self.I(SMA, self.data.Close, self.n2)

    def next(self):
        if crossover(self.sma1, self.sma2): 
            self.buy()
        elif crossover(self.sma2, self.sma1): 
            self.sell()
