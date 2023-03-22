import ccxt


def handle():

    ok = ccxt.okex()
    markets = ok.load_markets()
    print(markets)


handle()
