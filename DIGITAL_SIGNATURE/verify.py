from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA1
from Crypto.PublicKey import RSA 
import sign


def main():

    def verify():
            key = RSA.import_key(open('D:/GITHUB/Chat_App/Connection_P2P_Digital_signature/RSA_GENERATE_PRIVATE_PUBLIC_KEY/public.key').read())

            # file_in = open("message.txt",'rb')
            # message = file_in.read()   #message = b"i am txexting you"
            # file_in.close()
            


            # file_in=open("signature.pem","rb")
            # signature = file_in.read()
            # file_in.close()
            signature = sign.main()
            # signature = b'\x97,!\xcd\xa8\xb4\x86bp\xef#\xb1\x9d\x19\xce\x13\xd8\r\xd1\xea\x0c\xa0]vA\xf9\xf4e\xdd\x84MTo\x95{OZ/#\x08,\xf2\xcb\xe19\xb7\xf6\xff\xde*\xf4\xe80d\x8a\x1eu\x0e\x92R\xe8\xbaZ8\x03\xa6B\x11\xe9\xbf?\x0c\xb9\x9b\x8b\x89\x16\xc9\xb1\x7fJ\x1c\x9d\x87\xac\x13m0\x7fi^F\x87M\xac\x0c\xf7\xc4]\x19"\x9ed\xe9I\x89\x9a\x93\xbd\x11\xc6\'@\xd8\r\x17\x07U\x02)2AN\xb9\\\xd9_\xa7\x03\xd6\xf2\\\x19\x95\x14\x99\x95|\xf1\x88\xa5\x8a2\xa1\xee\xd1\x98^\xa3\x1d\xcf\xe4\x8e\xdf"\xc1\xb3\x95?\x89J@\xe4\xf5\xf5j\xbb%\xf2>\xcc,6H;\x06\xd0?\x92[GK,\xfd\xa8\xbd\xe9B1(\x8b\xbf\x8e?b5\x14\x92\xbd\xf1Z\xd9hS*3\xe5\xc1\xdd\xfa\xc4wXep:\xd4\xc1\x14!1b\xdb\xfb\x9f\xe9.\x94\xb8D\x0f\xfb\xba\xbf\xcco\x9bBt\x9a\x01\xba6K\xfa\x10\xf7_\x02:\x80\xa4Dy\xe0N'

            
            message = b"i am texting you"
            hash2 = SHA1.new(message)


            try:
                pkcs1_15.new(key).verify(hash2,signature)
                print("The sigature is valid")
            except (ValueError,TypeError):
                print("Not recive original message")

    verify()


if __name__ == '__main__':
     main()