from sherlockeys import __version__
from sherlockeys.lib.http.requester import Requester

def test_version():
    assert __version__ == '0.1.0'

if __name__ == '__main__':
    r = Requester("")
