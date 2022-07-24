from sherlockeys.lib.http.requester import Requester


class TwitterBearerToken(Requester):

    def check_if_authorized(self, http_status_code: int):
        if http_status_code != 401:
            self.is_authorized = True
        else:
            self.is_authorized = False

    def run(self):
        self.set_module_name("Twitter Bearer Token")
        self.set_url(f"https://api.twitter.com/1.1/account_activity/all/subscriptions/count.json")
        self.set_http_method('get')
        self.set_header("authorization", f"Bearer {self.key}")
        self.make_request()
        self.check_if_authorized(self.http_status_code)
        self.doc_url = 'https://github.com/streaak/keyhacks#twitter-bearer-token'
