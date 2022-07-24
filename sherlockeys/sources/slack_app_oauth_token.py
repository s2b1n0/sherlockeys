import json

from sherlockeys.lib.http.requester import Requester


class SlackAppOauthToken(Requester):

    def check_if_authorized(self, http_status_code: int, http_response_text: str) -> None:
        if len(http_response_text) > 0:
            http_response_json = json.loads(http_response_text)
            if http_response_json['error'] == "invalid_auth" or http_response_json['error'] == "not_authed":
                self.is_authorized = False
            elif http_response_json['ok']:
                self.is_authorized = True
            else:
                self.is_authorized = True

        else:
            self.is_authorized = False

    def run(self):
        self.set_module_name("Slack App xoxp/xoxb")
        self.set_url(f"https://slack.com/api/auth.test")
        self.set_http_method('post')
        self.set_header("Authorization", f"token {self.key}")
        self.make_request()
        self.check_if_authorized(self.http_status_code, self.http_response_text)
        self.doc_url = 'https://github.com/streaak/keyhacks#Slack-API-token'
