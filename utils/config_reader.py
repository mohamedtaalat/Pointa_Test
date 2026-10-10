
import os
from pathlib import Path

import yaml
from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parent.parent
load_dotenv(ROOT_DIR / ".env")


def load_yaml(filename):
    path = ROOT_DIR / "config" / filename
    with path.open(encoding="utf-8") as file:
        return yaml.safe_load(file) or {}


def get_environment():
    return os.getenv("TEST_ENV", "staging")


def get_base_urls():
    environments = load_yaml("environments.yaml")
    env_name = get_environment()

    if env_name not in environments:
        raise ValueError(f"Unknown test environment: {env_name}")

    return environments[env_name]


def get_setting(key, default=None):
    settings = load_yaml("settings.yaml")
    return settings.get(key, default)
