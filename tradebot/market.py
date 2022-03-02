from tradebot.alpaca import AlpacaClient

def is_market_open():
    return AlpacaClient.get_clock().is_open
