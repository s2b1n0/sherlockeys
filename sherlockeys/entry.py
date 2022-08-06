import argparse
import sys

from sherlockeys.engine import Sherlockeys
import sherlockeys.lib.utils.const as CONST


def main():
    try:
        parser = argparse.ArgumentParser(description=f'{CONST.__header__}',
                                         formatter_class=argparse.RawDescriptionHelpFormatter,
                                         epilog='You can find check what platforms are currently supported on: https://github.com/s2b1n0/sherlockeys',
                                         add_help=False)
        parser.add_argument('key', help='key to be tested')
        parser.add_argument('-c', '--client', metavar='<id>', help='additional key to act as a client/app identifier')
        parser.add_argument('-d', '--debug', action='store_true', help='enable debug mode')
        parser.add_argument('-v', '--version', action='version', version=f'sherlockeys {CONST.__version__}')
        parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                            help='Show this help message and exit.')

        args = parser.parse_args()

        if args.debug:
            print(args)

        sherlockeys = Sherlockeys(args)
        sherlockeys.run()

    except KeyboardInterrupt:
        print()
        sys.exit(0)


if __name__ == "__main__":
    main()
