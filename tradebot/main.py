from pathlib import Path

from dotenv import load_dotenv

from tradebot.market import get_clock

if __name__ == "__main__":
    load_dotenv(Path.cwd() / Path("secrets", "api.env"))
    print(get_clock())
