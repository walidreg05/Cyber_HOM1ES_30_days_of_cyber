import socket

HOST = "192.168.1.13"
host = socket.gethostbyname(socket.gethostname())

PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #specifying
server.bind((host,PORT))


server.listen(5) 

while True: 
    communication_socket , addres = server.accept()
    #communication_socket is the server's endpoint 
    print(f"connected to {addres}")
    message = communication_socket.recv(1024).decode('utf-8') #specifying the size and decode the message because the message received by the client is encoded
    print(f"message from the client is {message}")
    communication_socket.send(f"GOT ur message , thanks".encode("utf-8"))
    communication_socket.close()
    print("safi rah salaw ")



