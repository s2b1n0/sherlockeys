from sherlockeys.lib.http.requester import Requester


class LokaliseApiKey(Requester):

    def check_if_authorized(self, http_status_code: int):
        if http_status_code == 200:
            self.is_authorized = True
        else:
            self.is_authorized = False

    def run(self):
        self.set_module_name("Lokalise Api Key")
        self.set_url(f"https://api.lokalise.com/api2/projects/")
        self.set_http_method('get')
        self.set_header("x-api-token", self.key)
        self.make_request()
        self.check_if_authorized(self.http_status_code)
        self.doc_url = 'https://github.com/streaak/keyhacks/#Lokalise-API-Key'
