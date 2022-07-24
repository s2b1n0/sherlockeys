from sherlockeys.lib.http.requester import Requester


class ButterCMSApiKey(Requester):

    def check_if_authorized(self, http_status_code: int):
        if http_status_code == 200:
            self.is_authorized = True
        else:
            self.is_authorized = False

    def run(self):
        self.set_module_name("ButterCMS Api Key")
        self.set_url(f"https://api.buttercms.com/v2/posts/?auth_token={self.key}")
        self.set_http_method('get')
        self.make_request()
        self.check_if_authorized(self.http_status_code)
        self.doc_url = 'https://github.com/streaak/keyhacks/#buttercms-api-key'
