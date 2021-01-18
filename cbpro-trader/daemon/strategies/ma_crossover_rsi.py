import Decimal


def update_indicators():
    pass


def strategy(engine, period_list, indicators):
    # new_buy_flag = True
    # new_sell_flag = False
    new_buy_flag = False
    new_sell_flag = True
    for cur_period in period_list:
        product_id = cur_period['product']
        new_buy_flag = Decimal(
            indicators[cur_period.name]['rsi']) < Decimal(
                '40') and Decimal(
                    indicators[cur_period.name]['sma14']) > Decimal(
                        indicators[cur_period.name]['ema4'])
        new_sell_flag = Decimal(
            indicators[cur_period.name]['rsi']) > Decimal(
                '70') and Decimal(
                    indicators[cur_period.name]['sma14']) < Decimal(
                        indicators[cur_period.name]['ema4'])
        # Stop loss
        last_buy_price = engine.last_buy_price[product_id]
        if indicators[
            cur_period.name][
                'close'] < last_buy_price * 0.995:
            new_sell_flag = True
        # Run away limit
        last_sell_price = engine.last_sell_price[product_id]
        if indicators[
            cur_period.name][
                'close'] > last_sell_price * 1.05:
            new_buy_flag = True
    return(new_buy_flag, new_sell_flag)
