import ccxt
import numpy as np


# boll 布林 线


def handle(context, Symbol, start, end):

    # 获取历史数据
    hist = context.data.get_price(context.security, count=context.user_data.period_window +
                                  context.user_data.bbands_opt_width_m + 1, frequency="1d")
    if len(hist.index) < (context.user_data.period_window + context.user_data.bbands_opt_width_m + 1):
        context.log.warn("bar的数量不足, 等待下一根bar...")
        return
    # 获取收盘价
    prices = np.array(hist["close"])
    # 初始化做多/做空信号
    long_signal_triggered = False
    short_signal_triggered = False

    # 使用talib计算布林线的上中下三条线
    upper, middle, lower = talib.BBANDS(prices, timeperiod=context.user_data.period_window, nbdevup=context.user_data.standard_deviation_range,
                                        nbdevdn=context.user_data.standard_deviation_range, matype=talib.MA_Type.SMA)

    # 获取最新价格
    current_price = context.data.get_current_price(context.security)

    # 生成交易信号
    if current_price > upper[-1]:  # 穿越上轨，买入信号
        long_signal_triggered = True

    if current_price < lower[-1]:  # 穿越下轨，卖出信号
        short_signal_triggered = True
    context.log.info("当前 价格为：%s, 上轨为：%s, 下轨为: %s" %
                     (current_price, upper[-1], lower[-1]))

    # 根据信号买入/卖出
    if short_signal_triggered:
        context.log.info("价格穿越下轨，产生卖出信号")
        if context.account.huobi_cny_btc >= HUOBI_CNY_BTC_MIN_ORDER_QUANTITY:
            # 卖出信号，且不是空仓，则市价单全仓清空
            context.log.info("正在卖出 %s" % context.security)
            context.log.info("卖出数量为 %s" % context.account.huobi_cny_btc)
            context.order.sell(context.security, quantity=str(
                context.account.huobi_cny_btc))
        else:
            context.log.info("仓位不足，无法卖出")
    elif long_signal_triggered:
        context.log.info("价格穿越上轨，产生买入信号")
        if context.account.huobi_cny_cash >= HUOBI_CNY_BTC_MIN_ORDER_CASH_AMOUNT:
            # 买入信号，且持有现金，则市价单全仓买入
            context.log.info("正在买入 %s" % context.security)
            context.log.info("下单金额为 %s 元" % context.account.huobi_cny_cash)
            context.order.buy(context.security, cash_amount=str(
                context.account.huobi_cny_cash))
        else:
            context.log.info("现金不足，无法下单")
    else:
        context.log.info("无交易信号，进入下一根bar")
