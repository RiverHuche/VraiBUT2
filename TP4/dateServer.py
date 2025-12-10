import socket

from pytest import Session

class Server : 

    def __init__(self):
        self.counter=0
    
    def mainServer(self,port):
        sock = socket.socket()
        sock.bind(("0.0.0.0",port))
        sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
        sock.listen(10)
        while True:
            cli,addr = sock.accept()
            sess = Session(self,cli)
            sess.mainSession()

class Session:

    def __init__(self,server,sock):
        self.server = server
        self.socket = sock
        self.file = sock.makefile(mode="rw")

    def mainSession(self):
        while True:
            line = self.file.readline().strip()
            if line == "get":
                self.file.write("huguette %d\n" % self.server.counter )
                self.file.flush()
            elif line =="incr":
                self.file.write("hugo %d\n" % self.server.counter +1)
                self.file.flush()
            elif line == "decr":
                self.file.write("hug %d\n" %self.server.counter -1)
                self.file.flush()
            elif line == "add N":
                n = line[-1]
                self.file.write("hu %d\n" %self.server.counter + n)
            elif line == "quit":
                self.file.write("quit\n")
                self.file.flush()
                break
            else:
                self.file.write("err\n")
                self.file.flush()
        
        self.file.close()
        self.socket.shutdown(socket.SHUT_RDWR)
        self.socket.close()

Server().mainServer(5558)
