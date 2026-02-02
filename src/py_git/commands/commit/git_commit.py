# --- IMPORTS ---
from subprocess import run, CalledProcessError
from loguru import logger
from shutil import which

# --- GIT PATH ---
git = str(which("git"))

# --- LOGGER CONFIG ---
logger.add(
    sink="../logs/pygit_commit.log",
    level="INFO",
    colorize=True,
    format="{time:DD/MM/YYYY} | {message}",
)


# --- COMMIT FUNCTION ---
def git_commit(commit_message: str = "", changed_files: str = ""):
    try:
        # Stage files first (handle single file or space-separated list)
        files_list = changed_files.split() if changed_files else [""]
        if files_list[0]:  # If files provided
            run([git, "add"] + files_list, check=True, capture_output=True)
            logger.info(f"Staged files: {changed_files}")

        # Commit
        result = run(
            [git, "commit", "-m", commit_message], check=True, capture_output=True
        )
        logger.info(f"Commit successful: {commit_message} | Files: {changed_files}")
        logger.info(f"Output: {result}")
    except CalledProcessError as e:
        logger.error(f"Git error: {e.stderr.decode()}")
        raise


changed_file = input("Changed files: ")
commit_message = input("Message for commit: ")
git_commit(changed_files=changed_file, commit_message=commit_message)
