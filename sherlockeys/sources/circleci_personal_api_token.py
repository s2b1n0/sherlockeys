from sherlockeys.lib.http.requester import Requester


class CircleciPersonalApiToken(Requester):

    def check_if_authorized(self, http_status_code: int):
        if http_status_code != 401 and http_status_code != 530 and http_status_code != 403:
            self.is_authorized = True
        else:
            self.is_authorized = False

    def run(self):
        self.set_module_name("CircleCI Personal Api Token")
        self.set_url(f"https://circleci.com/api/v1.1/me?circle-token={self.key}")
        self.set_http_method('get')
        self.make_request()
        self.check_if_authorized(self.http_status_code)
        self.doc_url = "https://github.com/streaak/keyhacks#circleci-access-token"
