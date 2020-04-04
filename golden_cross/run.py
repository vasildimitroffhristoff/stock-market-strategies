import os
import sys
import argparse
import pandas as pd
import backtrader as bt
from strategies.GoldenCross import GoldenCross
from strategies.BuyHold import BuyHold

strategies = {
    "golden_cross": GoldenCross,
    "buy_hold": BuyHold
}
parser = argparse.ArgumentParser()
parser.add_argument("strategy", help="which strategy to run", type=str)
args = parser.parse_args()

if not args.strategy in strategies:
    print("Invalid strategy mus be one of {}".format(strategies.keys()))
    sys.exit()

cerebro = bt.Cerebro()
cerebro.broker.setcash(1000)

spy_prices = pd.read_csv('SPY.csv', index_col="Date", parse_dates=True)

feed = bt.feeds.PandasData(dataname=spy_prices)

cerebro.adddata(feed)
# cerebro.addstrategy(GoldenCross)
cerebro.addstrategy(args.strategy)
cerebro.run()
print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue(), '$$$$')
cerebro.plot()
