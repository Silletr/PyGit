# --- IMPORTS ---
from subprocess import run
from loguru import logger as log
from pathlib import Path


# --- PATH TO SSH KEY ---
pub_key = Path.home() / ".ssh" / "id_ed25519.pub"

# --- LOGGER CONFIG ---
log.add(
    sink="pygit_auth.log",
    level="INFO",
    colorize=True,
    format="{time:DD/MM/YYYY} | {message}",
)


# --- CHECK SSH CONNECTION ---
def ssh_connection(is_connected: bool = None):  # pyright: ignore
    """
    Checking is your SSH-key exists and returns True/False,
    corresponding result of search
    """
    if not pub_key.exists():
        log.critical(f"SSH-key not found: {pub_key}")
        return False

    log.info(f"SSH key found: {pub_key}")
    result = run(
        ["ssh", "-T", "git@github.com"], check=False, capture_output=True, text=True
    )

    if (
        result.returncode == 1
        and "successfully authenticated, but GitHub" in result.stdout
    ):
        log.info("SSH connected to GitHub")
        return True

    else:
        log.error(f"SSH-connection error! \n{result.stderr}")
        return False


def main():
    ssh_connection()


if __name__ == "__main__":
    main()
