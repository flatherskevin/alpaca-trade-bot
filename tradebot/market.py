from tradebot.alpaca import AlpacaClient

def get_clock():
    return AlpacaClient.get_clock()
