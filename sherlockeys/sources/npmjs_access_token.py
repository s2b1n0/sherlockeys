from sherlockeys.lib.http.requester import Requester


class NpmJsAccessToken(Requester):

    def check_if_authorized(self, http_status_code: int):
        if http_status_code != 401 and http_status_code != 530:
            self.is_authorized = True
        else:
            self.is_authorized = False

    def run(self):
        self.set_module_name("NPM JS Access Token")
        self.set_url(f"https://registry.npmjs.org/-/whoami")
        self.set_http_method('get')
        self.set_header("Authorization", f"Bearer {self.key}")
        self.make_request()
        self.check_if_authorized(self.http_status_code)
        self.doc_url = 'https://github.com/streaak/keyhacks#NPM-token'
