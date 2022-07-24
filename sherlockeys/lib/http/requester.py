import sys
import requests
import argparse

from sherlockeys.lib.logger.log import Logger
from sherlockeys.lib.utils.helper import Helper


class Requester:

    def __init__(self, args: argparse):
        self.key = args.key
        self.url = ""
        self.include_json = False
        self.json = {}
        self.content_type = ""
        self.http_method = ""
        self.module_name = ""
        self.headers = {}
        self.verbose = args.debug
        self.doc_url = ""
        self.http_status_code = 0
        self.http_response_text = ""

        self.is_authorized = bool

    def set_http_method(self, http_method: str) -> None:
        self.http_method = http_method
        if self.verbose:
            Logger.info(f"http method for {self.module_name} set to {self.http_method}")

    def set_url(self, url: str) -> None:
        self.url = url
        if self.verbose:
            Logger.info(f"url for module {self.module_name} set to {self.url}")

    def set_content_type(self, content_type: str) -> None:
        self.headers['Content-Type'] = content_type
        if self.verbose:
            Logger.info(f"content type for {self.module_name} set to {self.content_type}")

    def set_module_name(self, module_name: str):
        self.module_name = module_name
        if self.verbose:
            Logger.info(f"module name set {self.module_name}")

    def set_basic_auth(self, user: str, password: str) -> None:
        user_and_pass_in_b64 = Helper.generate_basic_authentication_b64(user, password)
        self.headers['Authorization'] = f"Basic {user_and_pass_in_b64}"
        if self.verbose:
            Logger.info(f"header added to {self.module_name} = {self.headers}")

    def set_header(self, header_name: str, header_value: str) -> None:
        self.headers[header_name] = header_value
        if self.verbose:
            Logger.info(f"header added to {self.module_name} = {self.headers}")

    def set_json(self, json: object) -> None:
        self.json = json
        self.include_json = True

    def make_request(self):

        try:
            if self.http_method == "get":
                if self.include_json:
                    request = requests.get(url=self.url, headers=self.headers, json=self.json)
                else:
                    request = requests.get(url=self.url, headers=self.headers)

            elif self.http_method == "post":
                if self.include_json:
                    request = requests.post(url=self.url, headers=self.headers, json=self.json)
                else:
                    request = requests.post(url=self.url, headers=self.headers)

            else:
                Logger.error(f"http method doesn't supported for {self.module_name}")
                sys.exit(0)

            self.http_status_code = request.status_code
            self.http_response_text = request.text

            if self.verbose:
                Logger.info(f"Request to {self.url} returns {self.http_status_code} \ {self.http_response_text}")
        except Exception as error:
            Logger.error(f"Error: {error}")
