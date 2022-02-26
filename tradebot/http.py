import os
from pathlib import Path

import requests
from dotenv import load_dotenv


def get_http_session():
    env_vars = load_dotenv(Path.cwd() / Path("secrets", "api.env"))
    session = requests.Session()
    session.headers.update({"APCA-API-KEY-ID": os})
