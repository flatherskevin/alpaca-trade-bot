from sys import api_version
from tradebot.alpaca import alpaca_client

async def print_stream(v):
    print(v)

def stream_btc():
    alpaca_client.stream.subscribe_crypto_quotes(print_stream, "BTCUSD")
    alpaca_client.stream.run()
