import os 
from invoke import task
from subprocess import call
from sys import platform

root_dir = "'"+os.path.dirname(os.path.abspath(__file__))+"'"


@task
def foo(ctx):
    print("bar")

@task
def start(ctx):
    ctx.run(f"python3 {root_dir}/src/index.py", pty=True)

@task
def test(ctx):
    ctx.run(f"pytest {root_dir}/src", pty=True)


@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest", pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)
    if platform != "win32":
        call(("xdg-open", "htmlcov/index.html"))
