from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.config_reader import get_setting
from utils.logger import get_logger

logger = get_logger(__name__)


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(
            driver, int(get_setting("explicit_wait", 10))
        )

    def open(self, url):
        logger.info("Opening page: %s", url)
        self.driver.get(url)

    def click(self, locator):
        element = self.wait.until(
            EC.element_to_be_clickable(
                locator
            )
        )
        element.click()
        logger.info("Clicked element: %s", locator)

    def enter_text(self, locator, text):
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)
        logger.info("Entered text into: %s", locator)

    def get_text(self, locator):
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        return element.text

    def is_visible(self, locator):
        try:
            self.wait.until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except Exception:
            return False
