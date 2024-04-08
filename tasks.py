import os 
from invoke import task
from subprocess import call
from sys import platform

root_dir_raw = os.path.dirname(os.path.abspath(__file__))
root_dir = "'"+root_dir_raw+"'"

@task
def start(ctx):
    ctx.run(f"python3 {root_dir}/src/index.py", pty=True)
    
@task
def init(ctx):
    ctx.run(f"cd {root_dir}/ && python3 src/initialize_database.py", pty=True)

@task
def test(ctx):
    ctx.run(f"pytest {root_dir}/src", pty=True)

@task
def coverage(ctx):
    ctx.run(f"cd {root_dir} && coverage run --branch -m pytest src", pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run(f"cd {root_dir} && coverage html", pty=True)
    if platform != "win32":
        call(("xdg-open", f"{root_dir_raw}/htmlcov/index.html"))
