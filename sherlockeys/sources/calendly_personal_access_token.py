from sherlockeys.lib.http.requester import Requester


class CalendlyPersonalAccessToken(Requester):
    """
    supports only v1 Api Key - support is being removed on September 30, 2022
    """

    def check_if_authorized(self, http_status_code: int):
        if http_status_code != 401 and http_status_code != 530 and http_status_code != 403:
            self.is_authorized = True
        else:
            self.is_authorized = False

    def run(self):
        self.set_module_name("Calendly Personal Access Token")
        self.set_url(f"https://calendly.com/api/v1/users/me")
        self.set_http_method('get')
        self.set_header("X-TOKEN", f"{self.key}")
        self.make_request()
        self.check_if_authorized(self.http_status_code)
        self.doc_url = 'https://github.com/streaak/keyhacks#Calendly-API-Key'
