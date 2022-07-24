from sherlockeys.lib.http.requester import Requester


class GitlabPersonalToken(Requester):

    def check_if_authorized(self, http_status_code: int):
        if http_status_code == 200:
            self.is_authorized = True
        else:
            self.is_authorized = False

    def run(self):
        self.set_module_name("Gitlab Personal Access Token")
        self.set_url(f"https://gitlab.com/api/v4/projects?private_token={self.key}")
        self.set_http_method('get')
        self.make_request()
        self.check_if_authorized(self.http_status_code)
        self.doc_url = 'https://github.com/streaak/keyhacks#Gitlab-personal-access-token'
