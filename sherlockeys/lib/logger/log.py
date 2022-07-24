from colorama import Fore, Back, Style


class Logger:

    @staticmethod
    def info(log: str) -> None:
        print(Fore.CYAN + "[INFO] " + log + Style.RESET_ALL)

    @staticmethod
    def success(log: str) -> None:
        print(Fore.GREEN + "[SUCCESS] " + log + Style.RESET_ALL)

    @staticmethod
    def warning(log: str) -> None:
        print(Fore.YELLOW + "[WARNING] " + log + Style.RESET_ALL)

    @staticmethod
    def error(log: str) -> None:
        print(Fore.RED + "[ERROR] " + log + Style.RESET_ALL)

    @staticmethod
    def cli_green(log: str) -> None:
        print(Fore.GREEN + log + Style.RESET_ALL)
