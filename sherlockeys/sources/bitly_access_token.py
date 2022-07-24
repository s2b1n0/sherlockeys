import json

from sherlockeys.lib.http.requester import Requester


class BitlyApiAccessToken(Requester):

    def check_if_authorized(self, http_status_code: int, http_response_text: str):
        if http_status_code == 200:
            json_response = json.loads(http_response_text)
            if json_response["status_txt"] == "INVALID_ARG_ACCESS_TOKEN":
                self.is_authorized = False
            else:
                self.is_authorized = True
        else:
            self.is_authorized = False

    def run(self):
        self.set_module_name("Bitly Api Access Token")
        self.set_url(f"https://api-ssl.bitly.com/v3/shorten?access_token={self.key}&longUrl=https://www.google.com")
        self.set_http_method('get')
        self.make_request()
        self.check_if_authorized(self.http_status_code, self.http_response_text)
        self.doc_url = 'https://github.com/streaak/keyhacks#Bitly-Access-token'
