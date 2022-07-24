from sherlockeys.lib.http.requester import Requester


class HubspotPrivateAppKey(Requester):

    def check_if_authorized(self, http_status_code: int):
        if http_status_code != 401 and http_status_code != 530:
            self.is_authorized = True
        else:
            self.is_authorized = False

    def run(self):
        self.set_module_name("Hubspot Private App Key")
        self.set_url(f"https://api.hubapi.com/crm/v3/objects/contacts")
        self.set_http_method('get')
        self.set_header("Authorization", f"Bearer {self.key}")
        self.set_content_type("application/json")
        self.make_request()
        self.check_if_authorized(self.http_status_code)
        self.doc_url = 'https://github.com/streaak/keyhacks#Hubspot-API-key'
