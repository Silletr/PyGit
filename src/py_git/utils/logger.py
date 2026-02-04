from loguru import logger
from pathlib import Path

LOG_DIR = Path(__file__).resolve().parents[2] / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

logger.add(
    sink=LOG_DIR / "pygit.log",
    level="INFO",
    rotation="500 MB",
    retention="10 days",
    compression="zip",
    format="{time:DD/MM/YYYY HH:mm:ss} | {level: <8} | {name}:{line} | {message}",
    encoding="utf-8",
)

logger.add(
    sink=LOG_DIR / "errors.log",
    level="ERROR",
    rotation="100 MB",
    retention="30 days",
    compression="zip",
    filter=lambda record: record["level"].name in ("ERROR", "CRITICAL"),
)


def get_command_logger(command_name: str):
    command_logger = logger.bind(command=command_name)
    command_logger.add(
        sink=LOG_DIR / f"{command_name}.log",
        level="DEBUG",
        rotation="100 MB",
        retention="7 days",
        compression="zip",
        format="{time:DD/MM/YYYY HH:mm:ss} | {level: <8} | {name}:{line} | {message}",
        encoding="utf-8",
        filter=lambda record: record["extra"].get("command") == command_name,
    )
    return command_logger


__all__ = ["logger", "get_command_logger"]
