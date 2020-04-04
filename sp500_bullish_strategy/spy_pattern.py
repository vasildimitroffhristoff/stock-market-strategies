import csv


def is_bullish_candlestick(candle):
    return candle['Close'] > candle['Open']


def is_bearish_candlestick(candle):
    return candle['Close'] < candle['Open']


def is_bullish_engulfing(candles, index):
    current_day = candles[index]
    previous_day = candles[index-1]

    if is_bearish_candlestick(previous_day) \
            and current_day['Close'] > previous_day['Open'] \
            and current_day['Open'] < previous_day['Close']:
        return True


def is_bearish_engulfing(candles, index):
    current_day = candles[index]
    previous_day = candles[index-1]

    if is_bullish_candlestick(previous_day) \
            and current_day['Open'] > previous_day['Close'] \
            and current_day['Close'] < previous_day['Open']:
        return True


sp500_file = open('sp500.csv')
sp500_companies = csv.reader(sp500_file)


TOTAL_WITHIN_PATTERN = []

for company in sp500_companies:
    ticker, company_name = company
    history_file = open('history/{}.csv'.format(ticker))
    reader = csv.DictReader(history_file)
    candles = list(reader)
    candles = candles[-2:]
    if len(candles) > 1:
        if is_bullish_engulfing(candles, 1):
            # print(
            #     "{} - {} is bullish engulfing".format(ticker, candles[1]['Date']))
            TOTAL_WITHIN_PATTERN.append(ticker)

print(len(TOTAL_WITHIN_PATTERN))
