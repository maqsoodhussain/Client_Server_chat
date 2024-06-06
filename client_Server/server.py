import socket

s = socket.socket()
print("Socket Connected")

host = '0.0.0.0'
port = 1255

s.bind((host, port))

s.listen(3)
print("Waiting for connection......")



while True:
    c, addr = s.accept()
    name = c.recv(1024).decode()
    c.send(bytes(f"Welcome, {name}!", "utf-8"))
    print(f"{name} Joined..")
    
    while True:
        try:
            print("Wait...")
            msg = c.recv(1024).decode()
            if not msg:
                print(f"{name} left..?")
                c.close()
                break
            print(f"{name}: {msg}")
            se = input("You: ")
            c.send(bytes(f"server:{se}!", "utf-8"))
        except ConnectionResetError:
            print("Client forcibly closed the connection")
            c.close()
            break
       