
from api.base_client import BaseClient


class LoginService(BaseClient):

    def login(self, email, password):
        payload = {
            "email": email,
            "password": password,
        }

        return self.post("auth/login", json=payload)

    def login_with_payload(self, payload):
        return self.post("auth/login", json=payload)
