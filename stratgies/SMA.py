import backtrader as bt

class SmaCross(bt.Strategy):
    def log(self, txt, dt=None):
        dt = dt or self.datas[0].datatime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))
        
    params = dict(ma_period_short=10, ma_period_long=30)
    
    def __init__(self):
        sma1 = bt.ind.SMA(period=self.p.ma_period_short) 
        sma2 = bt.ind.SMA(period=self.p.ma_period_long)
        
        self.crossover = bt.ind.CrossOver(sma1, sma2)
        
    def next(self):
        if not self.position:
            if self.crossover > 0:
                self.buy()
        elif self.crossover < 0:
            self.close()