from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

class SaltedHTTPRequestHandler(SimpleHTTPRequestHandler):

    def __init__(self, *args, salt=None, directory=None, **kwargs):
        if not salt:
            raise ValueError
        self.salt = salt
        self.salted = len(salt) - 1
        super().__init__(*args, **kwargs)
    
    def do_GET(self):
        if not self.path.startswith(self.salt):
            return
        self.path = self.path[self.salted:]
        super().do_GET()

if __name__ == '__main__':

    import argparse
    from os import getcwd
    parser = argparse.ArgumentParser()
    parser.add_argument('--directory', '-d', default=getcwd(),
                        help='Specify alternative directory '
                        '[default:current directory]')
    parser.add_argument('port', action='store',
                        default=8000, type=int,
                        nargs='?',
                        help='Specify alternate port [default: 8000]')
    args = parser.parse_args()

    from hashlib import md5 as hash
    from random import random as rnd
    args.salt = '/' + hash(str(rnd()).encode()).hexdigest() + '/'

    from socket import gethostname, gethostbyname
    args.bind = gethostbyname(gethostname())

    handler = partial(SaltedHTTPRequestHandler,
                      salt=args.salt,
                      directory=args.directory)

    with ThreadingHTTPServer(('', args.port), handler) as httpd:
        message = 'Serving HTTP on http://{}:{}{} ...'
        print(message.format(args.bind, args.port, args.salt))
        httpd.serve_forever()
