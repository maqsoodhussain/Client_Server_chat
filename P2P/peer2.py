import socket


host = "localhost"
port = 1255
print("connecting.....")
c = socket.socket()
c.connect((host, port))


print("connected to peer 1")

try:
    while True:
        msg = input("You: ")
        c.sendall(msg.encode())

        data = c.recv(1024)
        if not data:
            break
        print("Sender: ", data.decode())
except ConnectionResetError:
    print("Connected lost")
finally:
    c.close()