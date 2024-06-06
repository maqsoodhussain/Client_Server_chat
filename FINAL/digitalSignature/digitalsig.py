import sys
sys.path.append('../')
from generateKeys import genkey
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA1
from Crypto.PublicKey import RSA

def verify(signature,message):
        key = RSA.import_key(open('D:/GITHUB/Chat_App/FINAL/public.key').read())
        #message = b'hello '
        

        hash2 = SHA1.new(message)


        try:
            pkcs1_15.new(key).verify(hash2,signature)
            return "VERIFIED"
        except (ValueError,TypeError):
            return "NOT VERIFIED"
        
def sign(message,):
        #message = b'hello'
        key = RSA.import_key(open('D:/GITHUB/Chat_App/FINAL/private.key').read())


        hash = SHA1.new(message)

        signer = pkcs1_15.new(key)
        signature = signer.sign(hash) #signature.hex()

        return signature
        


if __name__ =='__main__':
     message = b'hello'
     sig = sign(message)
     verify(sig,message)