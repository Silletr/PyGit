# --- IMPORTS ---
from py_git.utils.logger import get_command_logger
from ..auth.gh_status import ssh_connection
from subprocess import run, CalledProcessError
from shutil import which


# --- GIT PATH ---
git = str(which("git"))

# --- LOGGER CONFIG ---
logger = get_command_logger("pull")


# --- GIT PULL COMMAND ---
def git_pull():
    ssh_connection()

    try:
        result = run([git, "pull"], capture_output=True, text=True, check=True)
        logger.info(f"Git pull executed successfully:\n{result.stdout}")
    except CalledProcessError as e:
        logger.error(f"Git pull failed:\n{e.stderr}")


if __name__ == "__main__":
    git_pull()
