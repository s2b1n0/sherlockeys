from sherlockeys.lib.http.requester import Requester


class VisualStudioAppCenterApiKey(Requester):

    def check_if_authorized(self, http_status_code: int):
        if http_status_code == 401:
            self.is_authorized = False
        else:
            self.is_authorized = True

    def run(self):
        self.set_module_name("Visual Studio App Center Api Key")
        self.set_url(f"https://api.appcenter.ms/v0.1/apps")
        self.set_http_method('get')
        self.set_header("Content-Type", "application/json")
        self.set_header("X-Api-Token", self.key)
        self.make_request()
        self.check_if_authorized(self.http_status_code)
        self.doc_url = 'https://github.com/streaak/keyhacks#Visual-Studio-App-Center-API-Token'
