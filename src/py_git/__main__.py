import typer

from py_git.commands.commit.git_commit import git_commit
from py_git.commands.pull.git_pull import git_pull
from py_git.commands.auth.gh_status import ssh_connection as status_main
from py_git.commands.clone.gh_clone import clone_repo as clone_main

app = typer.Typer(help="PyGit - Python wrapper for GitHub CLI")


@app.command()
def pull():
    """Perform git pull"""
    git_pull()


@app.command()
def commit(message: str = typer.Argument(..., help="Commit message")):
    """Commit changes with message"""
    git_commit()


@app.command()
def status():
    status_main()


@app.command()
def clone(repo_url: str):
    clone_main(repo_url)


if __name__ == "__main__":
    app()
