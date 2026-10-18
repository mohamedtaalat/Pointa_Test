
import os

import pytest

from api.base_client import BaseClient
from utils.config_reader import get_base_urls
from utils.driver_factory import create_driver
# from api.users_api import UsersAPI


@pytest.fixture(scope="session")
def environment():
    return get_base_urls()


@pytest.fixture
def driver():
    browser = create_driver()

    yield browser

    browser.quit()


@pytest.fixture
def api_client(environment):
    token = os.getenv("API_TOKEN")

    client = BaseClient(
        base_url=environment["api_url"],
        token=token,
    )

    yield client

    client.close()

import re
from datetime import datetime

import allure
import pytest

from utils.logger import get_logger

logger = get_logger(__name__)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when != "call" or not report.failed:
        return

    logger.error("Test failed: %s", item.nodeid)

    driver = item.funcargs.get("driver")

    if driver is not None:
        try:
            screenshot = driver.get_screenshot_as_png()

            allure.attach(
                screenshot,
                name="failure-screenshot",
                attachment_type=allure.attachment_type.PNG,
            )

            safe_name = re.sub(
                r"[^a-zA-Z0-9_-]", "_", item.name
            )
            filename = (
                f"screenshots/{safe_name}_"
                f"{datetime.now():%Y%m%d_%H%M%S}.png"
            )

            from pathlib import Path
            path = Path(filename)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(screenshot)

        except Exception:
            logger.exception("Failed to capture screenshot")

    allure.attach(
        f"Test: {item.nodeid}\n"
        f"Phase: {report.when}\n"
        f"Outcome: {report.outcome}\n"
        f"Details: {report.longrepr}",
        name="failure-details",
        attachment_type=allure.attachment_type.TEXT,
    )
