import backtrader as bt
import datetime
from strategy import TestStrategy

cerebro = bt.Cerebro()
cerebro.broker.set_cash(1000)
data = bt.feeds.YahooFinanceCSVData(dataname='oracle.csv', fromdate=datetime.datetime(2020, 2, 3),
                                    todate=datetime.datetime(2020, 4, 1),
                                    )
cerebro.adddata(data)

cerebro.addstrategy(TestStrategy)
cerebro.addsizer(bt.sizers.FixedSize, stake=10)
print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue(), '$$$$')
cerebro.run()
print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue(), '$$$$')
cerebro.plot()
