from sherlockeys.lib.http.requester import Requester


class PivotalTrackerApiToken(Requester):

    def check_if_authorized(self, http_status_code: int):
        if http_status_code != 401 and http_status_code != 530 and http_status_code != 403 and http_status_code != 500:
            self.is_authorized = True
        else:
            self.is_authorized = False

    def run(self):
        self.set_module_name("PivotalTracker Api Token")
        self.set_url(f"https://www.pivotaltracker.com/services/v5/me?fields=%3Adefault")
        self.set_http_method('get')
        self.set_header("X-TrackerToken", self.key)
        self.make_request()
        self.check_if_authorized(self.http_status_code)
        self.doc_url = 'https://github.com/streaak/keyhacks/#pivotaltracker-api-token'
