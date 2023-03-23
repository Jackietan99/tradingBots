
import ccxt
import datetime
import numpy as np
import talib
import pandas as pd


# api_key = input("Please input your binance api_key: ")
# api_secret = input("Please input your binance api_secret: ")

binance = ccxt.binance({
    'enableRateLimit': False,
})

# set stop loss


def set_stop_loss(symbol, side, amount, price):
    try:
        order = binance.create_order(symbol, side, 'limit', amount, price)
        print(order)
        return order
    except Exception as e:
        print(e)
        return None

# set take profit


def set_take_profit(symbol, side, amount, price):
    try:
        order = binance.create_order(symbol, side, 'limit', amount, price)
        print(order)
        return order
    except Exception as e:
        print(e)
        return None


# def k_line_hours():

#     start_time = int(datetime.datetime(2023, 2, 1).timestamp() * 1000)
#     while True:
#         klines = binance.fetch_ohlcv(
#             'BTC/USDT', '1h', since=start_time, limit=None)
#         print(klines)
#         for kline in klines:
#             # 将时间戳转换为日期时间格式
#             ts = kline[0] / 1000  # 将毫秒转换为秒
#             dt_object = datetime.datetime.fromtimestamp(ts)
#             start_time = kline[0] + 3600000
#             print(dt_object, kline[1])
#             np.append(prices, kline[1])

#         # current_ts = int(datetime.datetime.now().timestamp())
#         current_ts = int(datetime.datetime.now().timestamp() * 1000)
#         time_diff = current_ts - start_time
#         # 判断时间差是否小于一小时
#         if time_diff > 3600000:
#             continue
#         else:
#             print('prices ', prices)
#             return prices


# prices = k_line_hours()


start_time = int(datetime.datetime(2023, 3, 20).timestamp() * 1000)
klines = binance.fetch_ohlcv('BTC/USDT', '1h', since=start_time, limit=2000)

for kline in klines:
    # 将时间戳转换为日期时间格式
    ts = kline[0] / 1000  # 将毫秒转换为秒
    dt_object = datetime.datetime.fromtimestamp(ts)
    print(dt_object, kline[1:])

df = pd.DataFrame(klines, columns=['timestamp',
                  'open', 'high', 'low', 'close', 'volume'])

prices = np.array(df["close"])
# 布林线的长度（回看时间窗口为20个bar）
period_window = 14
# 布林线的宽度（2倍标准差）
standard_deviation_range = 2
bbands_opt_width_m = 60
# 使用talib计算布林线的上中下三条线
print(prices)
upper, middle, lower = talib.BBANDS(prices, timeperiod=period_window, nbdevup=standard_deviation_range,
                                    nbdevdn=standard_deviation_range, matype=talib.MA_Type.SMA)
print(upper, middle, lower)
