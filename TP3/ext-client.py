#!/usr/bin/python3

import socket
import sys

BUFSIZE = 1024
def client (host , port):
    sock = socket.socket(type=socket.SOCK_DGRAM)
    addr = (host , port)
    sock.sendto(b"user",addr)
    data = sock.recv( BUFSIZE )
    print (data.decode (), end="")

client(sys.argv[1],5555)