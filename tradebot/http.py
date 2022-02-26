import os
from pathlib import Path

import requests
from dotenv import load_dotenv


def get_http_session() -> requests.Session:
    load_dotenv(Path.cwd() / Path("secrets", "api.env"))
    session = requests.Session()
    session.headers.update(
        {
            "APCA-API-KEY-ID": os.environ["API_KEY_ID"],
            "APCA-API-SECRET-KEY": os.environ["SECRET_KEY"],
        }
    )
    return session
