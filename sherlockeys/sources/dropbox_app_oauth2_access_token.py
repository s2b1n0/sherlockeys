from sherlockeys.lib.http.requester import Requester


class DropboxAppOauth2AccessToken(Requester):

    def check_if_authorized(self, http_status_code: int):
        if http_status_code != 401 and http_status_code != 530 and http_status_code != 403 and http_status_code != 404 and http_status_code != 400:
            self.is_authorized = True
        else:
            self.is_authorized = False

    def run(self):
        self.set_module_name("Dropbox App oAuth2 Access Token")
        self.set_url("https://api.dropboxapi.com/2/users/get_current_account")
        self.set_http_method('post')
        self.set_header("Authorization", f"Bearer {self.key}")
        self.make_request()
        self.check_if_authorized(self.http_status_code)
        self.doc_url = 'https://github.com/streaak/keyhacks#Dropbox-API'
