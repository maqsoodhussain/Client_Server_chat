import sys
sys.path.append('../')
import socket
from generateKeys import genkey
from digitalSignature import digitalsig
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA1

def main():

    host = "localhost"
    port = 1255
    print("Connecting.....")
    c = socket.socket()
    c.connect((host, port))


    def sign(n):
        sig = digitalsig.sign(n.encode())
        c.sendall(sig)
        c.sendall(n.encode())


    def con():
        

        username = input("Enter Username: ")
        c.sendall(username.encode())
        password = input("Enter Password: ")
        c.sendall(password.encode())

        result = c.recv(1024).decode()
        print(f"{result}")

        if(result=="ACCESS DENIED..!"):
            return
        
        name = input("\nEnter Name: ")
        sign(name)
        

        try:
            while True:
                msg = input("You: ")
                # sig = digitalsig.sign(msg.encode())
                # c.sendall(sig)
                # c.sendall(msg.encode())
                sign(msg)
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
