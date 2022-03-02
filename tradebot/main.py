from pathlib import Path

from dotenv import load_dotenv

from tradebot.market import is_market_open

if __name__ == "__main__":
    print("Market is open:", is_market_open())
