from sherlockeys.lib.http.requester import Requester


class GithubPersonalToken(Requester):

    def check_if_authorized(self, http_status_code: int):
        if http_status_code == 200:
            self.is_authorized = True
        else:
            self.is_authorized = False

    def run(self):
        self.set_module_name("Github Personal Access Token")
        self.set_url(f"https://api.github.com/user")
        self.set_http_method('get')
        self.set_basic_auth("user", self.key)
        self.make_request()
        self.check_if_authorized(self.http_status_code)
        self.doc_url = 'https://github.com/streaak/keyhacks#Github-Token'
