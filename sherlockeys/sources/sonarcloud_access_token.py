import json

from sherlockeys.lib.http.requester import Requester


class SonarcloudAccessToken(Requester):

    def check_if_authorized(self, http_status_code: int, http_response_text: str) -> None:
        if http_status_code == 200:
            json_response = json.loads(http_response_text)
            if json_response['valid']:
                self.is_authorized = True
            else:
                self.is_authorized = False
        else:
            self.is_authorized = False

    def run(self):
        self.set_module_name("Sonarcloud Access Token")
        self.set_url(f"https://sonarcloud.io/api/authentication/validate")
        self.set_http_method('get')
        self.set_basic_auth(self.key, "")
        self.make_request()
        self.check_if_authorized(self.http_status_code, self.http_response_text)
        self.doc_url = 'https://github.com/streaak/keyhacks#Sonarcloud-Token'
