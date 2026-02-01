# --- IMPORTS ---
# from subprocess import run, CalledProcessError  <- Unused, soon will be used
from loguru import logger as log

# --- LOGGER CONFIG ---
log.add(
    sink="pygit_auth.log",  # pyright: ignore
    # Uses default stderr; specify "file.log" for file output
    level="INFO",
    colorize=True,
    format="{time:DD/MM/YYYY} | {message}",
)

log.info("This logs with date | message")
