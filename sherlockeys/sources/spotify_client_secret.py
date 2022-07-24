from sherlockeys.lib.http.requester import Requester


class SpotifyClientSecret(Requester):

    def check_if_authorized(self, http_status_code: int) -> None:
        if http_status_code == 401:
            self.is_authorized = False
        else:
            self.is_authorized = True

    def run(self):
        self.set_module_name("Spotify Client Secret")
        self.set_url(f"https://api.spotify.com/v1/me")
        self.set_http_method('get')
        self.set_header("Authorization", f"Bearer {self.key}")
        self.make_request()
        self.check_if_authorized(self.http_status_code)
        self.doc_url = 'https://github.com/streaak/keyhacks#spotify-access-token'
