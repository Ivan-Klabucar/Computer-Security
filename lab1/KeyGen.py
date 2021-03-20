from Crypto.Protocol.KDF import scrypt

def generate_keys(master_password, salt):
    return scrypt(master_password, salt, 16, N=2**14, r=8, p=1, num_keys=2)
    