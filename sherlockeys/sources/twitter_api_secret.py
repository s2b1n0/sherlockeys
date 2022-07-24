from sherlockeys.lib.http.requester import Requester


class TwitterApiSecret(Requester):

    def check_if_authorized(self, http_status_code: int):
        if http_status_code == 401:
            self.is_authorized = False
        else:
            self.is_authorized = True

    def run(self):
        self.set_module_name("Twitter Api Secret")
        self.set_url(f"https://www.googleapis.com/youtube/v3/activities?part=contentDetails&maxResults=25&channelId=UC-lHJZR3Gqxm24_Vd_AJ5Yw&key={self.key}")
        self.set_http_method('get')
        self.make_request()
        self.check_if_authorized(self.http_status_code)
        self.doc_url = 'https://github.com/streaak/keyhacks#Twitter-API-Secret'
