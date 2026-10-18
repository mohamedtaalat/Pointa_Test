
import json

import pytest

from utils import logger
from pages.home_page import HomePage
from pages.signup_page import SignupPage


class TestSignup:
    with open("test_data/signup_data.json", encoding="utf-8") as f:
        data = json.load(f)

    @pytest.mark.parametrize(
        "data",
        data,
        ids=[item["scenario"] for item in data]
    )
    @pytest.mark.ui
    @pytest.mark.signup
    def test_signup(self, driver, environment, data):
        log = logger.get_logger()
        scenario = data["scenario"]

        log.info("Starting signup test: %s", scenario)

        hp = HomePage(driver)
        hp.click_signup()

        sp = SignupPage(driver)

        sp.signup(
            data.get("email", ""),
            data.get("password", ""),
            data.get("full_name", ""),
            data.get("phone_number", "")
        )
        if data["expected_result"] == "success":
            assert driver.current_url != ""
        else:
            assert driver.current_url == ""