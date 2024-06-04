import socket


host = "localhost"
port = 1255

s = socket.socket()
s.bind((host,port))


s.listen(1)
print("Waiting for incomming connection....")

client , address = s.accept()
print("Connected to .",address)

name = client.recv(1024).decode()
try:
    while True:
        print("wait...")
        data = client.recv(1024)
        if not data:
            break
        print(f"{name}: ", data.decode())


        msg = input("You: ")
        client.sendall(msg.encode())

except ConnectionRefusedError:
    print("Connection lost..!")
finally:
    client.close()
    s.close()