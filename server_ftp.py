import os

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


def main():
    authorizer = DummyAuthorizer()

    authorizer.add_user('client', 'open~sesame', '.', perm='elradfmwMT')

    handler = FTPHandler
    handler.authorizer = authorizer

    address = ('', 2121)
    server = FTPServer(address, handler)

    server.max_cons = 256
    server.max_cons_per_ip = 25

    server.serve_forever()

if __name__ == '__main__':
    main()
