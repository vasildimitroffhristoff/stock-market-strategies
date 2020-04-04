import math
import backtrader as bt


class GoldenCross(bt.Strategy):
    params = (('fast', 50), ('slow', 200),
              ('order_percentage', 0.95), ('ticker', 'SPY'))

    def __init__(self):
        self.fast_moving_avg = bt.indicators.SMA(
            self.data.close, period=self.params.fast, plotname="50 day moving average")

        self.slow_moving_avg = bt.indicators.SMA(
            self.data.close, period=self.params.slow, plotname="200 day moving average")

        self.crossover = bt.indicators.CrossOver(
            self.fast_moving_avg, self.slow_moving_avg)

    def next(self):
        # print('Current position size:'.format(self.position))
        if self.position.size == 0:
            if self.crossover > 0:
                amount_to_invest = (
                    self.params.order_percentage * self.broker.cash)
                self.size = math.floor(amount_to_invest / self.data.close)

                print("BUY {} shares of {} at ${}".format(
                    self.size, self.params.ticker, self.data.close[0]))
                self.buy(size=self.size)

        if self.position.size > 0:
            if self.crossover < 0:
                print("SELL {} shares of {} at ${}".format(
                    self.size, self.params.ticker, self.data.close[0]))
                self.close()
