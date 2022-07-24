from sherlockeys.lib.http.requester import Requester


class BuildkiteAccessToken(Requester):

    def check_if_authorized(self, http_status_code: int):
        if http_status_code == 200:
            self.is_authorized = True
        else:
            self.is_authorized = False

    def run(self):
        self.set_module_name("BuildKite Api Access Token")
        self.set_url(f"https://api.buildkite.com/v2/user")
        self.set_http_method('get')
        self.set_header("Authorization", f"Bearer {self.key}")
        self.make_request()
        self.check_if_authorized(self.http_status_code)
        self.doc_url = 'https://github.com/streaak/keyhacks/#buildkite-access-token'
