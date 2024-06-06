from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA1
from Crypto.PublicKey import RSA

def main():
    
    def sign():
        message = b"i am texting you"
        key = RSA.import_key(open('D:/GITHUB/Chat_App/Connection_P2P_Digital_signature/RSA_GENERATE_PRIVATE_PUBLIC_KEY/private.key').read())

        hash = SHA1.new(message)

        signer = pkcs1_15.new(key)
        signature = signer.sign(hash) #signature.hex()

        print(signature)
        return signature
        # file_out = open("signature.pem","wb")
        # file_out.write(signature)
        # file_out.close()


        # file_out = open("message.txt","wb")
        # file_out.write(message)
        # file_out.close()

    sign()


if __name__ == '__main__':
    main()