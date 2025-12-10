import socket

def client(host, port):
    sock = socket.socket()
    sock.connect((host, port))
    f = sock.makefile(mode="rw")
    while True:
        v = input("rentrez une valeur")
        f.write(v)
        f.flush()
        print(f.readline(), end="")
        if v=="quit":
            break
        else : 
            print(f.readline(), end="")
    f.close()
    sock.shutdown(socket.SHUT_RDWR )
    sock.close()

client("localhost", 5560)
