
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
