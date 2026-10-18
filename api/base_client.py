
import requests

from utils.logger import get_logger

logger = get_logger(__name__)


class BaseClient:
    def __init__(self, base_url, token=None, timeout=15):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()

        self.session.headers.update({
            "Accept": "application/json",
            "Content-Type": "application/json",
        })

        if token:
            self.session.headers["Authorization"] = (
                f"Bearer {token}"
            )

    def request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        kwargs.setdefault("timeout", self.timeout)

        logger.info("API request: %s %s", method.upper(), url)

        try:
            response = self.session.request(method, url, **kwargs)

            logger.info(
                "API response: status=%s, elapsed=%.3fs",
                response.status_code,
                response.elapsed.total_seconds(),
            )

            return response

        except requests.RequestException:
            logger.exception("API request failed: %s %s", method.upper(), url)
            raise

    def get(self, endpoint, **kwargs):
        return self.request("GET", endpoint, **kwargs)

    def post(self, endpoint, **kwargs):
        return self.request("POST", endpoint, **kwargs)

    def put(self, endpoint, **kwargs):
        return self.request("PUT", endpoint, **kwargs)

    def patch(self, endpoint, **kwargs):
        return self.request("PATCH", endpoint, **kwargs)

    def delete(self, endpoint, **kwargs):
        return self.request("DELETE", endpoint, **kwargs)

    def close(self):
        self.session.close()
