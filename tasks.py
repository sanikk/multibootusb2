from invoke import task


@task
def start(c):
    c.run("python multibootusb2/start.py", pty=True)


@task
def dev(c):
    c.run("python -i multibootusb2/start.py", pty=True)


@task
def tui(c):
    c.run("python multibootusb2/start_tui.py", pty=True)
