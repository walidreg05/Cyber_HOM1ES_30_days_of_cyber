import socket

HOST = "192.168.1.13" #the client shd specift the host of the srver
host = socket.gethostbyname(socket.gethostname())  #the client shd specift the host of the srver

PORT = 9090

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #specifying
c.connect((host,PORT))

c.send("hello HOM13S".encode("utf-8"))
print(c.recv(1024))
# 'c' is the client endpoint




