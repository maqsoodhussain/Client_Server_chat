import sys
sys.path.append('D:/GITHUB/Chat_App/FINAL 1.0/')
import socket
from generateKeys import genkey # type: ignore
import connect # type: ignore
from digitalSignature import digitalsig 
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA1
from Crypto.PublicKey import RSA




def main():


    host = "localhost"
    port = 1255

    s = socket.socket()
    s.bind((host, port))

    s.listen(1)
    print("Waiting for connection....")

    client, address = s.accept()
    print("Connected to", address)




    def verify_user():
        username = client.recv(1024).decode()
        password = client.recv(1024).decode()
        print(f" USERNAME: {username}, PASSWORD: {password}")

        result = connect.verify_credentials(username,password)
        return result

    def verify():
        pass

  

    def con():
        
        res = verify_user()
        if res is True:
            client.sendall("ACCESS GRANTED..".encode())
            print("VALID USER ACCESSED")
        else:
            client.sendall("ACCESS DENIED..!".encode())
            print("UNAUTHORIZED USER TRY TO ACCESS")
            client.close()
            return 


        sig = client.recv(1024)
        name = client.recv(1024)
        vr = digitalsig.verify(sig, name)
        
        print(f"Connected to {name.decode()}    --{vr}--", end='\n')
        try:
            while True:
                print("wait...")
                sig = client.recv(1024)
                data = client.recv(1024)
                vr = digitalsig.verify(sig, data)
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
