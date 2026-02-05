# --- IMPORTS ---
from subprocess import run, CalledProcessError
from py_git.utils.logger import get_command_logger
from shutil import which

# --- git LOCATION AND LOGGER CONFIG ---
git: str = str(which("git"))
logger = get_command_logger("push")


# --- git push COMMAND ---
def git_push(from_branch=None, to_branch=None):
    """
    Push current or specified branch to remote.
    If from_branch is None — push current branch.
    """
    logger.info("Starting git push...")

    try:
        if from_branch is None:
            current_branch_result = run(
                [git, "rev-parse", "--abbrev-ref", "HEAD"],
                capture_output=True,
                text=True,
                check=True,
            )
            from_branch = current_branch_result.stdout.strip()

        if to_branch is None:
            to_branch = f"origin/{from_branch}"

        logger.debug(f"Pushing {from_branch} -> {to_branch}")

        result = run(
            [git, "push", "origin", f"{from_branch}:{to_branch}"],
            capture_output=True,
            text=True,
            check=True,
        )

        logger.info(f"Push successful: {result.stdout.strip()}")
        return True

    except CalledProcessError as e:
        logger.error(f"Git push failed: {e.cmd}")
        logger.error(f"stderr: {e.stderr.strip()}")
        logger.error(f"stdout: {e.stdout.strip()}")
        raise

    except FileNotFoundError:
        logger.error("Git not found in PATH")
        raise

    except Exception as e:
        logger.error(f"Unexpected error during push: {type(e).__name__} - {e}")
        raise
