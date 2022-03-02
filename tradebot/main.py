from tradebot.market import is_market_open
from tradebot.account import get_equity

if __name__ == "__main__":
    print("Market is open:", is_market_open())
    print("Current equity:", get_equity())
