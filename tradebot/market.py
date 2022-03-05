from tradebot.alpaca import alpaca_client


def is_market_open():
    return alpaca_client.rest.get_clock().is_open
