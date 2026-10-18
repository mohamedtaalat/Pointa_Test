from api.base_client import BaseClient


class SignupService(BaseClient):
    def signup_with_payload(self, payload):
        return self.post("auth/signup", json=payload)