from base64 import b64encode

from sherlockeys.lib.logger.log import Logger


class Helper:

    @staticmethod
    def start_script_message():
        Logger.cli_green(f"Starting Sherlockeys\n")

    @staticmethod
    def generate_basic_authentication_b64(user: str, password: str) -> str:
        user_and_pass = f"{user}:{password}".encode("utf-8")
        to_b64 = b64encode(user_and_pass).decode("ascii")
        return to_b64
