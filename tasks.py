from invoke import task


@task
def start(c):
    c.run("python start.py", pty=True)


@task
def dev(c):
    c.run("python -i start.py", pty=True)
