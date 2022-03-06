from pathlib import Path

from invoke import task


@task
def bootup(c):
    c.run("sudo service redis-server start")


@task(pre=[bootup])
def run(c):
    c.run("python -m tradebot.main")


@task
def shutdown(c):
    c.run("sudo service redis-server stop")
