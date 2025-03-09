from socket import *
from fib import fib


def fib_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)
    while True:
        client, addr = sock.accept()
        print("Connection", addr)
        fib_handler(client)


def fib_handler(client):
    while True:
        req = client.recv(100)
        if not req:
            break
        result = fib(int(req))
        resp = str(result).encode("ascii") + b"\n"
        client.send(resp)


fib_server(("", 25000))
