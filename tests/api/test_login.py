
import json
import pytest
from utils import logger


class TestLogin:

    with open("test_data/login_data.json", encoding="utf-8") as f:
        data = json.load(f)

    @pytest.mark.api
    @pytest.mark.login
    @pytest.mark.parametrize("data", data)
    def test_login(self, login_api, data):
        log = logger.get_logger()

        log.info("Scenario: %s", data["scenario"])

        response = login_api.login_with_payload((data.get("email",""), data.get("password","")))

        assert response.status_code == data["expected_status_code"], (
            f"Scenario: {data['scenario']}; "
            f"Expected: {data['expected_status_code']}; "
            f"Actual: {response.status_code}; "
            f"Response: {response.text}"
        )

