from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA1
from Crypto.PublicKey import RSA 


key = RSA.import_key(open('D:/GITHUB/Chat_App/Connection_P2P_Digital_signature/RSA_GENERATE_PRIVATE_PUBLIC_KEY/public.key').read())

file_in = open("message.txt",'rb')
message = file_in.read()   #message = b"i am txexting you"
file_in.close()


file_in=open("signature.pem","rb")
signature = file_in.read()
file_in.close()

hash2 = SHA1.new(message)


try:
    pkcs1_15.new(key).verify(hash2,signature)
    print("The sigature is valid")
except (ValueError,TypeError):
    print("Not recive original message")