#!/usr/bin/python3

import socket
import datetime
import os

BUFSIZE = 1024
def server (port) :
    sock = socket.socket (type= socket.SOCK_DGRAM)
    sock.bind(("0.0.0.0",port))
    while True:
        data , addr = sock.recvfrom (BUFSIZE)
        print(addr,data.decode())
        if data.decode() == "date":
            data = datetime.datetime.now()
        else :
            data = os.environ["USER"] + "Huguette de olivette"
        data = "%s\n" % data
        sock.sendto(data.encode(), addr)

server(5556)