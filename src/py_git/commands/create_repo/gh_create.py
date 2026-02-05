# --- IMPORTS ---
from py_git.utils.logger import get_command_logger
from subprocess import run, CalledProcessError
from shutil import which

# --- LOGGER ---
logger = get_command_logger("repo_create")

# --- gh LOCATION ---
gh = str(which("gh"))


# --- gh repo create {repository_name} [If provided: --source=.] --remote=upstream
def create_repo(
    repository_name: str = "",
    source: str | None = ".",
    remote: str = "upstream",
    mode: str = "public",
):  # "public" not "--public"
    try:
        logger.info("Executing: gh repo create")
        cmd = [gh, "repo", "create", repository_name, "--source=" + (source or ".")]

        # Add visibility flag
        if mode in ("public", "private", "internal"):
            cmd.append(f"--{mode}")

        # Add remote flag conditionally
        if remote:
            cmd.extend(["--remote=" + remote])

        result = run(cmd, check=True, capture_output=True, text=True)
        logger.info(f"Repo created: \n{result.stdout}")

    except CalledProcessError as e:
        logger.error(f"Failed: {e.returncode}")
        logger.error(f"stdout: {e.stdout}")
        logger.error(f"stderr: {e.stderr}")


if __name__ == "__main__":
    repository_name = input("Please input your repo name: ")

    source_dir = input("Are your source will be current dir? Y/N?\n")
    if source_dir.lower() == "y":
        source = "."
    else:
        source = input("Enter your repo directory in UNIX format:\n")

    remote_yn = input("Are remote branch need? Y/N\n")
    remote = "upstream" if remote_yn.lower() == "y" else ""

    mode = input(
        "What's mode of repo: public, private, internal? [Default: Public]\n"
    ).strip()
    mode = mode or "public"

    # Call the function
    create_repo(
        repository_name=repository_name.strip(),
        source=source.strip(),
        remote=remote,
        mode=mode,
    )
