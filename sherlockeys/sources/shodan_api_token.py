from sherlockeys.lib.http.requester import Requester


class ShodanApiToken(Requester):

    def check_if_authorized(self, http_status_code: int):
        if http_status_code != 401 and http_status_code != 530 and http_status_code != 403 and http_status_code != 500:
            self.is_authorized = True
        else:
            self.is_authorized = False

    def run(self):
        self.set_module_name("Shodan Api Token")
        self.set_url(f"https://api.shodan.io/shodan/host/8.8.8.8?key={self.key}")
        self.set_http_method('get')
        self.make_request()
        self.check_if_authorized(self.http_status_code)
        self.doc_url = 'https://developer.shodan.io/api/requirements'
