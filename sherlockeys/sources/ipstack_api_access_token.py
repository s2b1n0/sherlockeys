import json

from sherlockeys.lib.http.requester import Requester


class IpstackApiAccessToken(Requester):

    def check_if_authorized(self, http_status_code: int, http_response_text: str) -> None:
        if http_status_code == 200:
            json_response = json.loads(http_response_text)
            try:
                if json_response["ip"] == "127.0.0.1":
                    self.is_authorized = True
            except:
                self.is_authorized = False
        else:
            self.is_authorized = False

    def run(self):
        self.set_module_name("Ipstack Api Access Token")
        self.set_url(f"http://api.ipstack.com/127.0.0.1?access_key={self.key}")
        self.set_http_method('get')
        self.make_request()
        self.check_if_authorized(self.http_status_code, self.http_response_text)
        self.doc_url = 'https://github.com/streaak/keyhacks#Ipstack-API-Key'
