import socket

s = socket.socket()
host = 'localhost'
port = 1255
s.connect((host, port))

name = input("Enter Name: ")
s.send(bytes(name, 'utf-8'))
print(s.recv(1024).decode())

while True:
    print("Wait...")
    message = input("You: ")
    if message =='0':
        print("Disconnected..!")
        break
    s.send(bytes(message, 'utf-8'))
    print(s.recv(1024).decode())
    
