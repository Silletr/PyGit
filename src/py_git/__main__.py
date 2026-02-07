import typer
from typing import Optional

from py_git import (
    git_commit,
    git_pull,
    gh_status as status_main,
    clone_repo as clone_main,
    create_repo,
    git_push,
)

app = typer.Typer(help="PyGit - Python wrapper for GitHub CLI")


@app.command()
def pull():
    """Perform git pull"""
    git_pull()


@app.command()
def commit(message: str = typer.Argument(..., help="Commit message")):
    """Commit changes with message"""
    git_commit(message)


@app.command()
def status():
    """Check gh auth status. Run before: pygit pull, clone"""
    status_main()


@app.command()
def clone(repo_url: str):
    """Clone repo by URL"""
    clone_main(repo_url)


@app.command()
def create_repository(
    repository_name: str,
    remote: Optional[bool] = None,  # Fixed: Optional[bool], not bool=None
    mode: str = "public",
    source: str = ".",
):
    create_repo(
        repository_name=repository_name,
        remote=remote,
        mode=mode,
        source=source,
    )


@app.command()
def push(to_branch: str = "master"):
    """Push to branch (default: master - specify to override)"""
    git_push(to_branch=to_branch)


if __name__ == "__main__":
    app()
