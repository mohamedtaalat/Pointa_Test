
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from utils.config_reader import get_setting
from utils.logger import get_logger

logger = get_logger(__name__)


def create_driver():
    browser = os.getenv(
        "BROWSER", get_setting("browser", "chrome")
    ).lower()

    headless = os.getenv(
        "HEADLESS", str(get_setting("headless", False))
    ).lower() == "true"

    if browser == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)

    elif browser == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("-headless")
        driver = webdriver.Firefox(options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.implicitly_wait(0)
    driver.set_page_load_timeout(
        int(get_setting("page_load_timeout", 30))
    )

    logger.info("Browser started: %s", browser)
    return driver
