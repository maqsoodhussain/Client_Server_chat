import socket

s = socket.socket()
print("Socket Connected")

host = '192.168.239.145'
port = 1255

s.bind((host, port))

s.listen(3)
print("Waiting for connection......")

clients = []

while True:
    c, addr = s.accept()
    clients.append(c)
    name = c.recv(1024).decode()
    c.send(bytes(f"Welcome, {name}!", "utf-8"))
    print(f"{name} has joined the chat")
    
    while True:
        msg = c.recv(1024).decode()
        print(f"{name}: {msg}")
        se = input("You: ")
        c.send(bytes(f"server: , {se}!", "utf-8"))
        print("Wait...")