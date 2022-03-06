from threading import local
from tradebot.crypto import stream_btc
from tradebot.market import is_market_open
from tradebot.account import get_equity
from tradebot.cache import local_cache

if __name__ == "__main__":
    print("Market is open:", is_market_open())
    print("Current equity:", get_equity())
    # stream_btc()