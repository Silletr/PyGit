# --- IMPORTS ---
from loguru import logger
from shutil import which

# --- GIT PATH ---
git = which("git")

# --- LOGGER CONFIG ---
logger.add(
    sink="../logs/pygit_commit.log",
    level="INFO",
    colorize=True,
    format="{time:DD/MM/YYYY} | {message}",
)


# --- COMMIT FUNCTION ---
def git_commit(
    commit_message: str = "",
    changed_files: str = "",
):
    logger.info(f"Commit message: {commit_message} | Changed files: {changed_files}")


changed_file = input("Changed files: ")
commit_message = input("Message for commit: ")
git_commit(changed_files=changed_file, commit_message=commit_message)
