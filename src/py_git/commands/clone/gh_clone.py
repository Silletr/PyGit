# --- IMPORTS ---
from shutil import which
from loguru import logger
from subprocess import run, CalledProcessError

# --- gh PATH ---
gh_path = which("gh")
if not gh_path:
    logger.critical("GITHUB CLI (gh) NOT FOUND. Install it: sudo apt install gh")
    exit(1)
gh = str(gh_path)

# --- LOGGER CONFIG ---
logger.add(
    sink="../logs/pygit_commit.log",
    level="INFO",
    colorize=True,
    format="{time:DD/MM/YYYY} | {message}",
)


# --- CLONE FUNCTION ---
def clone_repo(repo_owner: str = "", repository_name: str = ""):
    if not repo_owner or not repository_name:
        logger.error("No owner or repository name provided")
        raise ValueError("Must provide repo_owner and repository_name!")

    repo_url = f"{repo_owner}/{repository_name}"
    logger.info(f"Executing: gh repo clone {repo_url}")

    try:
        run([gh, "repo", "clone", repo_url], capture_output=True, text=True, check=True)

        logger.success(f"Successfully cloned {repo_url} to {repository_name}/")
        return 0

    except CalledProcessError as e:
        logger.error(f"Clone failed: {e}\nSTDOUT: {e.stdout}\nSTDERR: {e.stderr}")
        return 1
    except FileNotFoundError:
        logger.error("gh command not found in PATH")
        return 1


# --- ENTRY POINT ---
if __name__ == "__main__":
    repo_name = input("Enter the repository name: ")
    repo_owner = input("Enter the repository owner name: ")
    clone_repo(repo_owner=repo_owner, repository_name=repo_name)
