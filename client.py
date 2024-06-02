import socket

s = socket.socket()
host = '192.168.239.145'
port = 1255
s.connect((host, port))

name = input("Enter Name: ")
s.send(bytes(name, 'utf-8'))
print(s.recv(1024).decode())

while True:
    message = input("You: ")
    s.send(bytes(message, 'utf-8'))
    print(s.recv(1024).decode())
    print("Wait...")
