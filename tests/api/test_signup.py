import json

import pytest

from utils import logger


class TestSignup:
    with open("test_data/signup_data.json", encoding="utf-8") as f:
        data = json.load(f)

    @pytest.mark.api
    @pytest.mark.login
    @pytest.mark.parametrize("data", data)
    def test_signup_api(self,signup_api,data):
        log = logger.get_logger()

        log.info("Scenario: %s", data["scenario"])

        response = signup_api.signup_with_payload(
            (data.get("email",""), data.get("password",""),data.get("phone_number",""),data.get("full_name",""))
        )

        assert response.status_code == data["expected_status_code"], (
            f"Scenario: {data['scenario']}; "
            f"Expected: {data['expected_status_code']}; "
            f"Actual: {response.status_code}; "
            f"Response: {response.text}"
        )