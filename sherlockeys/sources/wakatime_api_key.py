from sherlockeys.lib.http.requester import Requester


class WakatimeApiKey(Requester):

    def check_if_authorized(self, http_status_code: int):
        if http_status_code == 200:
            self.is_authorized = True
        else:
            self.is_authorized = False

    def run(self):
        self.set_module_name("WakaTime Api Key")
        self.set_url(f"https://wakatime.com/api/v1/users/current/projects/?api_key={self.key}")
        self.set_http_method('get')
        self.make_request()
        self.check_if_authorized(self.http_status_code)
        self.doc_url = 'https://github.com/streaak/keyhacks/#wakatime-api-key'
