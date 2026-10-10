
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

LOG_DIR = Path(__file__).resolve().parent.parent / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)


def get_logger(name="automation"):
    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | "
        "%(filename)s:%(lineno)d | %(message)s"
    )

    general = RotatingFileHandler(
        LOG_DIR / "automation.log",
        maxBytes=5_000_000,
        backupCount=3,
        encoding="utf-8",
    )
    general.setLevel(logging.INFO)
    general.setFormatter(formatter)

    errors = RotatingFileHandler(
        LOG_DIR / "errors.log",
        maxBytes=2_000_000,
        backupCount=3,
        encoding="utf-8",
    )
    errors.setLevel(logging.ERROR)
    errors.setFormatter(formatter)

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(formatter)

    logger.addHandler(general)
    logger.addHandler(errors)
    logger.addHandler(console)
    logger.propagate = False

    return logger
