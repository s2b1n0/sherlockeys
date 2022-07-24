import re
import json
import validators

from sherlockeys.lib.http.requester import Requester
from sherlockeys.lib.logger.log import Logger


class ZapierWebhookToken(Requester):

    """
    it looks like every request to https://hooks.zapier.com/hooks/* has the same success response.
    so this is not a reliable test, every acceptable url would works
    see if there is a way to improve it in the future
    """

    def check_if_authorized(self, http_status_code: int, http_response_text: str):
        if http_status_code == 200:
            json_response = json.loads(http_response_text)
            if json_response["status"] == "success":
                self.is_authorized = True
            else:
                self.is_authorized = False
        else:
            self.is_authorized = False

    def run(self):
        self.set_module_name("Zapier Webhook Token")
        if validators.url(self.key):
            reg_exp = re.compile(r"hooks\.zapier\.com")
            if reg_exp.search(self.key):
                self.set_url(self.key)
                self.set_http_method('get')
                self.set_json({"name": "streaak"})
                self.set_header('Accept', 'application/json')
                self.make_request()
                self.check_if_authorized(self.http_status_code, self.http_response_text)
            else:
                self.is_authorized = False
                if self.verbose:
                    Logger.info(f"module {self.module_name} not running due to hostname not being for hooks.zapier.com")
        else:
            if self.verbose:
                Logger.info(f"module {self.module_name} not running due to key not being a url")
            self.is_authorized = False
        self.doc_url = 'https://github.com/streaak/keyhacks#zapier-webhook-token'
