import argparse
import multiprocessing

from sherlockeys.lib.logger.log import Logger
from sherlockeys.lib.utils.helper import Helper

import sherlockeys.lib.utils.const as CONST
from sherlockeys.sources import *


class Sherlockeys:

    def __init__(self, args: argparse) -> None:
        print(CONST.__header__)

        self.args = args

        self.client_mode = False
        if self.args.client is not None:
            self.client_mode = True

        self.SOURCES = (
            GitlabPersonalToken(self.args),
            GithubPersonalToken(self.args),
            YoutubeApiKey(self.args),
            TwitterBearerToken(self.args),
            HubspotPrivateAppKey(self.args),
            HerokuApiKey(self.args),
            NpmJsAccessToken(self.args),
            SlackAppOauthToken(self.args),
            SpotifyClientSecret(self.args),
            VisualStudioAppCenterApiKey(self.args),
            BitlyApiAccessToken(self.args),
            AsanaPersonalAccessToken(self.args),
            ZapierWebhookToken(self.args),
            CalendlyPersonalAccessToken(self.args),
            DropboxAppOauth2AccessToken(self.args),
            SonarcloudAccessToken(self.args),
            IpstackApiAccessToken(self.args),
            ShodanApiToken(self.args),
            TravisciApiTokenCom(self.args),
            TravisciApiTokenOrg(self.args),
            CircleciPersonalApiToken(self.args),
            JumpcloudPersonalApiKey(self.args),
            PivotalTrackerApiToken(self.args),
            WakatimeApiKey(self.args),
            BuildkiteAccessToken(self.args),
            DelightedApiKey(self.args),
            ButterCMSApiKey(self.args),
            LokaliseApiKey(self.args),
            FacebookAppSecret(self.args)
        )
        if self.args.debug:
            Logger.info(f"\nKey: {self.args.key}\n"
                        f"Verbose: {self.args.debug}\n")
        Helper.start_script_message()

    def scan(self, source):
        if self.client_mode is False and source.client_mode is False:
            source.run()
            print(f"{source.module_name} = ✅ ({source.http_status_code}) {source.doc_url}"
                  if source.is_authorized else f"{source.module_name} = ❌ ({source.http_status_code})")
        elif self.client_mode is True and source.client_mode is True:
            source.run()
            print(f"{source.module_name} = ✅ ({source.http_status_code}) {source.doc_url}"
                  if source.is_authorized else f"{source.module_name} = ❌ ({source.http_status_code})")
        else:
            pass

    def run(self):
        try:
            pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
            pool.map(self.scan, self.SOURCES)

            Logger.cli_green("\nExecution finished.")
        except Exception as error:
            print(error)
