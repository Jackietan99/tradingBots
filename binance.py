
import ccxt


api_key = input("Please input your binance api_key: ")
api_secret = input("Please input your binance api_secret: ")

binance = ccxt.binance({
    'apiKey': api_key,
    'secret': api_secret,
    'enableRateLimit': True,
    'options': {
        'defaultType': 'future',
    }
})

# # set stop loss


# def set_stop_loss(symbol, side, amount, price):
#     try:
#         order = binance.create_order(symbol, side, 'limit', amount, price)
#         print(order)
#         return order
#     except Exception as e:
#         print(e)
#         return None

# # set take profit


# def set_take_profit(symbol, side, amount, price):
#     try:
#         order = binance.create_order(symbol, side, 'limit', amount, price)
#         print(order)
#         return order
#     except Exception as e:
#         print(e)
#         return None

# # load defined trade pair


# def load_trade_pair():
#     biance = ccxt.binance()

#     result = biance.fetch_ticker('ETH/USDT')
#     print(result)


def load_history_data():

    from_timestamp = binance.parse8601(f'2023-03-21 00:00:00')
    end_timestamp = binance.parse8601(f'2023-03-22 14:00:00')
    print(from_timestamp)
    result = binance.fetch_closed_orders('ETH/USDT', from_timestamp)
    print(result)


load_history_data()
