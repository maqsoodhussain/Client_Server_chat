from Crypto.PublicKey import RSA

key = RSA.generate(2048)
def privatekey():
    private_key = key.export_key()
    file_out = open('generateKeys/public.key','wb')
    file_out.write(private_key)
    file_out.close

def publicKey():
    public_key = key.publickey().export_key()
    file_out = open("generateKeys/private.key",'wb')
    file_out.write(public_key)
    file_out.close()
    

if __name__ == '__main__':
    privatekey()
    publicKey()
    
