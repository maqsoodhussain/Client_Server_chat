import socket


host = "localhost"
port = 1255

s = socket.socket()
s.bind((host,port))


s.listen(1)
print("Waiting for incomming connection....")

client , address = s.accept()
print("Connected to Peer 2: ", address)

try:
    while True:
        data = client.recv(1024)
        if not data:
            break
        print("Peer 2: ", data.decode())


        msg = input("You: ")
        client.sendall(msg.encode())

except ConnectionRefusedError:
    print("Connection lost..!")
finally:
    client.close()
    s.close()