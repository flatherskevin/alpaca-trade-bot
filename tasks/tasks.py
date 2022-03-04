from invoke import task
from pathlib import Path

@task
def run(c):
    c.run("python -m tradebot.main")