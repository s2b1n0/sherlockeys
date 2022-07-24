from sherlockeys.lib.http.requester import Requester


class TravisciApiTokenOrg(Requester):

    def check_if_authorized(self, http_status_code: int):
        if http_status_code != 401 and http_status_code != 530 and http_status_code != 403:
            self.is_authorized = True
        else:
            self.is_authorized = False

    def run(self):
        self.set_module_name("Travis CI Api Token .org")
        self.set_url(f"https://api.travis-ci.org/repos")
        self.set_http_method('get')
        self.set_header("Travis-API-Version", "3")
        self.set_header("Authorization", f"token {self.key}")
        self.make_request()
        self.check_if_authorized(self.http_status_code)
        self.doc_url = 'https://github.com/streaak/keyhacks#Travis-CI-API-token'
