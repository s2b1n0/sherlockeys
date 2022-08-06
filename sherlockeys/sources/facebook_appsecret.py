from sherlockeys.lib.http.requester import Requester


class FacebookAppSecret(Requester):
    def __init__(self, args):
        super().__init__(args)
        self.client_mode = True

    def check_if_authorized(self, http_status_code: int):
        if http_status_code == 400:
            self.is_authorized = False
        elif http_status_code == 200:
            self.is_authorized = True
        else:
            self.is_authorized = False

    def run(self):
        self.set_module_name("FacebookAppSecret")
        self.set_url(f"https://graph.facebook.com/oauth/access_token?client_id={self.client_key}&client_secret={self.key}&redirect_uri=&grant_type=client_credentials")
        self.set_http_method('get')
        self.make_request()
        self.check_if_authorized(self.http_status_code)
        self.doc_url = "https://github.com/streaak/keyhacks#facebook-appsecret"
