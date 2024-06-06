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

        print("Connecting.....")

        c = socket.socket()
        c.connect((host, port))

        username = input("Enter Username: ")
        c.sendall(username.encode())
        password = input("Enter Password: ")
        c.sendall(password.encode())

        result = c.recv(1024).decode()
        print(f"{result}")

        if(result=="ACCESS DENIED..!"):
            return
        
        name = input("\nEnter Name: ")

        sig = digitalsig.sign(name.encode())
        c.sendall(sig)
        c.sendall(name.encode())

        try:
            while True:
                msg = input("You: ")
                
                sig = digitalsig.sign(msg.encode())
                c.sendall(sig)
                c.sendall(msg.encode())
                print("wait...")
                data = c.recv(1024)
                if not data:
                    break
                print("Server: ", data.decode())
        except ConnectionResetError:
            print("Connection lost")
        finally:
            c.close()

    con()

if __name__ == '__main__':
    main()
