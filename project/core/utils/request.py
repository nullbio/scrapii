import logging
import time

from requests import Session


class Request(Session):
    def __init__(self, session, log: logging.Logger, sleep_seconds=5, max_retries=5):
        self.session = session
        self.log = log
        self.sleep_seconds = sleep_seconds
        self.max_retries = max_retries

    def get(self, url, params=None, headers=None):
        self.log.debug(f"Requesting {url}")
        counter = 1
        result = None
        while counter <= self.max_retries:
            try:
                result = self.session.get(url, params=params, headers=headers)
                if result.status_code != 200:
                    raise Exception(f"failed with status code {result.status_code}")

            except Exception as e:
                self.log.error(
                    "Error while requesting %s: %s, status code: %s. "
                    "Trying again in %s seconds",
                    url,
                    e,
                    result.status_code,
                    self.sleep_seconds * counter,
                )
                if counter == self.max_retries:
                    self.log.error(
                        "Error while requesting %s: %s, status code: %s."
                        "Max retries reached",
                        url,
                        e,
                        result.status_code,
                    )
                    exit(1)
                time.sleep(self.sleep_seconds * counter)
                counter += 1
                continue
            if result is None:
                exit(1)
            return result