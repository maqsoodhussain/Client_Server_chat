import sys
sys.path.append('../../')
import socket
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA1
from Crypto.PublicKey import RSA

def main():

    host = "localhost"
    port = 1255
    print("Connecting.....")
    c = socket.socket()
    c.connect((host, port))

    def sign_message(m,):
        key = RSA.import_key(open('D:/GITHUB/Chat_App/FINAL 1.0/generateKeys/public.key').read())
        hash = SHA1.new(m.encode())

        signer = pkcs1_15.new(key)
        signature = signer.sign(hash) #signature.hex()
        return signature
    def send_userPwd():
        username = input("Enter Username: ")
        c.sendall(username.encode())
        password = input("Enter Password: ")
        c.sendall(password.encode())



    def con():
        

        send_userPwd()
        
        result = c.recv(1024).decode()
        print(f"{result}")

        if(result=="ACCESS DENIED..!"):
            return
        
        name = input("\nEnter Name: ")
        sig = sign_message(name)
        c.sendall(sig)
        c.sendall(name.encode())
        

        try:
            while True:
                msg = input("You: ")
                # sig = digitalsig.sign(msg.encode())
               
                sig = sign_message(msg)
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
