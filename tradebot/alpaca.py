import os
from pathlib import Path

from alpaca_trade_api import REST
from dotenv import load_dotenv


class Alpaca:
    def __init__(self) -> None:
        self.client: REST = self._get_client()

    def _get_client(self) -> REST:
        load_dotenv(Path.cwd() / Path("secrets", "api.env"))
        return REST(
            key_id=os.environ["ALPACA_API_KEY_ID"],
            secret_key=os.environ["ALPACA_API_SECRET_KEY"],
            base_url="https://paper-api.alpaca.markets",
            api_version="v2",
        )

AlpacaClient = Alpaca().client
