import os
from pathlib import Path

from alpaca_trade_api import REST, Stream
from dotenv import load_dotenv

class AlpacaClient:
    def __init__(self) -> None:
        load_dotenv(Path.cwd() / Path("secrets", "api.env"))
        self.base_url = "https://paper-api.alpaca.markets"
        self.key_id = os.environ["ALPACA_API_KEY_ID"]
        self.secret_key = os.environ["ALPACA_API_SECRET_KEY"]
        self.rest: REST = self._get_rest_client()
        self.stream: Stream = self.get_stream_client()

    def _get_rest_client(self) -> REST:
        return REST(
            key_id=self.key_id,
            secret_key=self.secret_key,
            base_url=self.base_url,
            api_version="v2",
        )

    def get_stream_client(self):
        return Stream(key_id=self.key_id, secret_key=self.secret_key, base_url=self.base_url)


alpaca_client = AlpacaClient()
