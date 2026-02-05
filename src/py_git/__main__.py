import typer

from py_git.commands.commit.git_commit import git_commit
from py_git.commands.pull.git_pull import git_pull
from py_git.commands.auth.gh_status import ssh_connection as status_main
from py_git.commands.clone.gh_clone import clone_repo as clone_main
from py_git.commands.create_repo.gh_create import create_repo
from py_git.commands.push.git_push import git_push


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
    """Checking your gh auth status. Needs to: pygit pull, clone"""
    status_main()


@app.command()
def clone(repo_url: str):
    """Cloning the repo by link"""
    clone_main(repo_url)


@app.command()
def create_repository(
    repository_name: str,
    remote: bool = None,  # pyright: ignore
    mode: str = "public",
    source: str = ".",
):
    create_repo(
        repository_name=repository_name,
        remote=remote,  # pyright: ignore
        mode=mode,
        source=source,
    )


@app.command()
def push(to_branch: str = "master"):
    git_push(to_branch=to_branch)


if __name__ == "__main__":
    app()
