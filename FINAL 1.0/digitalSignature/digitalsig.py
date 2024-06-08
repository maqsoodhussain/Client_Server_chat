import sys
sys.path.append('../')
from generateKeys import genkey
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA1
from Crypto.PublicKey import RSA

# verify using private key and sign using public key
def verify(signature,message):
        key = RSA.import_key(open('D:/GITHUB/Chat_App/FINAL 1.0/generateKeys/private.key').read())
        #message = b'hello '
        

        hash2 = SHA1.new(message)


        try:
            pkcs1_15.new(key).verify(hash2,signature)
            return "VERIFIED"
        except (ValueError,TypeError):
            return "NOT VERIFIED"
        
def sign(msg,):
        #message = b'hello'
        key = RSA.import_key(open('D:/GITHUB/Chat_App/FINAL 1.0/generateKeys/public.key').read())
        hash = SHA1.new(msg)

        signer = pkcs1_15.new(key)
        signature = signer.sign(hash) #signature.hex()

        return signature
        


if __name__ =='__main__':
     message = b'hello'
     sig = sign(message)
     verify(sig,message)