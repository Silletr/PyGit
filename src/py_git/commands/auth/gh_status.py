# --- IMPORTS ---
from subprocess import run
from py_git.utils.logger import get_command_logger
from pathlib import Path
from os import environ
from shutil import which

# --- PATH TO SSH KEY ---
pub_key = Path.home() / ".ssh" / "id_ed25519.pub"
env = environ.copy()
env["SSH_AUTH_SOCK"] = environ.get("SSH_AUTH_SOCK", "")

# --- LOGGER ---
log = get_command_logger("auth")

# --- gh, SSH LOCATING ---
gh = str(which("gh"))
ssh = str(which("ssh"))


# --- CHECK SSH CONNECTION ---
def ssh_connection():
    if not pub_key.exists():
        log.critical(f"SSH-key not found: {pub_key}")
        return False, ""

    log.info(f"SSH key found: {pub_key}")

    result = run([ssh, "-T", "git@github.com"], capture_output=True, text=True, env=env)

    full_output = (result.stdout or "") + (result.stderr or "")

    if "successfully authenticated" in full_output:
        log.info("SSH connected to GitHub")
        return True, full_output

    log.error(f"SSH-connection error!\n{full_output}")
    return False, full_output


# --- Execute 'gh auth status' ---
def gh_status():
    ok, ssh_log = ssh_connection()

    if not ok:
        log.error(f"Can't connect to SSH:\n{ssh_log}")
        return

    log.info("Executing 'gh auth status', SSH is good")

    result = run([gh, "auth", "status"], capture_output=True, text=True, env=env)

    log.debug(f"gh auth status was executed:\n{result.stdout}")


def main():
    gh_status()


if __name__ == "__main__":
    main()
