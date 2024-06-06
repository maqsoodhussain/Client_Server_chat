import socket

def main():
    
    def con():
        host = "192.168.43.239"
        port = 1255



        print("connecting.....")


        c = socket.socket()
        c.connect((host, port))

        name = input ("Enter Name :")
        c.sendall(name.encode())

        print(f"connected to sender")

        try:
            while True:
            
                msg = input("You: ")
                c.sendall(msg.encode())
                print("wait...")
                data = c.recv(1024)
                if not data:
                    break
                print("Sender: ", data.decode())
        except ConnectionResetError:
            print("Connected lost")
        finally:
            c.close()

    con()


if __name__ == '__main__':
    main()