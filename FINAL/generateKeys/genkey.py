from Crypto.PublicKey import RSA

key = RSA.generate(2048)
def privatekey():
    private_key = key.export_key()
    return private_key

def publicKey():
    public_key = key.publickey().export_key()
    return public_key

if __name__ == '__main__':
    privatekey()
    publicKey()
    
