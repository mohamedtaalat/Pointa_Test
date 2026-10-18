import json

import pytest

from utils import logger
from pages.home_page import HomePage
from pages.login_page import LoginPage


class TestLogin:
    with open(file="test_data/login_data.json")as f:
        data = json.load(f)
    @pytest.mark.parametrize("data", data)
    @pytest.mark.ui
    @pytest.mark.login
    def test_login(self,driver,environment,data):
        driver.get(environment['base_url'])
        log = logger.get_logger()
        log.info(data["scenario"])
        hp = HomePage(driver)
        hp.click_login()
        lp = LoginPage(driver)
        lp.login(data['email'],data['password'])
        if data["expected_result"] == "success":
            assert driver.current_url != ""
        else:
            assert driver.current_url == ""