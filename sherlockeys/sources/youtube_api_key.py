import json

from sherlockeys.lib.http.requester import Requester
from sherlockeys.lib.logger.log import Logger


class YoutubeApiKey(Requester):

    def check_if_authorized(self, http_status_code: int):
        if http_status_code == 400:
            http_response_json = json.loads(self.http_response_text)
            if http_response_json['error']['message'] == 'API key not valid. Please pass a valid API key.':
                self.is_authorized = False
            else:
                self.is_authorized = False
                if self.verbose:
                    Logger.warning(f"credential to {self.url} may be valid, check it manually")
        else:
            self.is_authorized = True

    def run(self):
        self.set_module_name("Youtube API Key")
        self.set_url(f"https://www.googleapis.com/youtube/v3/activities?part=contentDetails&maxResults=25&channelId=UC-lHJZR3Gqxm24_Vd_AJ5Yw&key={self.key}")
        self.set_http_method('get')
        self.make_request()
        self.check_if_authorized(self.http_status_code)
        self.doc_url = 'https://github.com/streaak/keyhacks#youtube-api-key'
