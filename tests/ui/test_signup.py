import json

import pytest
from utils import logger
from pages.home_page import HomePage
from pages.signup_page import SignupPage


class TestSignup:
    with open(file="test_data/signup_data.json") as f:
        data = json.load(f)
    @pytest.mark.parametrize("data",data)
    @pytest.mark.ui
    @pytest.mark.signup
    def test_signup(self,driver,environment,data):
        log = logger.get_logger()
        log.info(data["scenario"])
        hp = HomePage(driver)
        hp.click_signup()
        sp = SignupPage(driver)
        sp.signup(data['email'],data['password'],data["full_name"],data["phone_number"])
        if data["expected_result"] == "success":
            assert driver.current_url != ""
        else:
            assert driver.current_url == ""