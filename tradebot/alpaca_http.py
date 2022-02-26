import os
from pathlib import Path
from typing import Callable

import requests
from dotenv import load_dotenv

ALPACA_BASE_URL = "https://www.paper-api.alpaca.markets/v2"


class AlpacaHttpClient:
    def __init__(self) -> None:
        self.client: requests.Session = self.get_http_session()

    def get_http_client(self) -> requests.Session:
        load_dotenv(Path.cwd() / Path("secrets", "api.env"))
        client = requests.Session()
        client.headers.update(
            {
                "APCA-API-KEY-ID": os.environ["API_KEY_ID"],
                "APCA-API-SECRET-KEY": os.environ["SECRET_KEY"],
            }
        )
        return client

    def call(self, url_path: str, fn: Callable, **kwargs):
        kwargs["headers"] = dict(**self.client.headers, **kwargs.get("headers", {}))
        separator = "" if url_path[0] == "/" else "/"
        fn(url=f"{ALPACA_BASE_URL}{separator}{url_path}", **kwargs)

    def get(self, url_path: str, **kwargs):
        self.call(url_path, self.client.get, **kwargs)
