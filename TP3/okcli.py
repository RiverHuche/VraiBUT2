#!/usr/bin/python3

import socket
import sys

BUFSIZE = 1024
def client (port):
    sock = socket.socket(type=socket.SOCK_DGRAM)
    addr = ("255.255.255.255", port)
    sock.bind(addr)
    while True:
        data, saddr = sock.recvfrom(128)
        print(saddr, data.decode())

client(6666)