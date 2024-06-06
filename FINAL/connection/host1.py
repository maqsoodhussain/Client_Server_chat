import sys
sys.path.append('../')
import socket
from generateKeys import genkey
from digitalSignature import digitalsig
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA1

def main():
    def con():
        host = "localhost"
        port = 1255

        s = socket.socket()
        s.bind((host, port))

        s.listen(1)
        print("Waiting for connection....")

        client, address = s.accept()
        print("Connected to", address)

        sig = client.recv(1024)
        name = client.recv(1024)
        vr = digitalsig.verify(sig, name)
        print(f"Connected to {name.decode()}    --{vr}--", end='\n')
        try:
            while True:
                print("wait...")
                sig = client.recv(1024)
                data = client.recv(1024)
                vr = digitalsig.verify(sig, name)
                if not data:
                    break
                print(f"{name.decode()}:  {data.decode()} --{vr}-- ")

                msg = input("You: ")
                client.sendall(msg.encode())

        except ConnectionRefusedError:
            print("Connection lost..!")
        finally:
            client.close()
            s.close()

    con()

if __name__ == '__main__':
    main()
