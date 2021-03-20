from KeyGen import generate_keys
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad

class Cryptor:
    def __init__(self, master_password):
        with open('./files/config', 'rb') as config_file:
            self.salt = config_file.read()
        
        self.AES_key, self.HMAC_key = generate_keys(master_password, self.salt)

class Encryptor(Cryptor):
    def __init__(self, master_password):
        super().__init__(master_password)

    def encrypt_file_AES_CBC(self, contents, dest):
        iv = get_random_bytes(16)
        aes_cbc = AES.new(key=self.AES_key, mode=AES.MODE_CBC, IV=iv)
        
        # skriveni_tekst = | <-- IV --> | <-- padded content --> |
        encrypted_data = iv + aes_cbc.encrypt(pad(contents, AES.block_size))
        dest.write(encrypted_data)

class Decryptor(Cryptor):
    def __init__(self, master_password):
        super().__init__(master_password)

    def decrypt(self):
        with open('./files/passwords', 'rb') as passwords_file:
            pass_file_contents = passwords_file.read()
            iv = pass_file_contents[:16]
            encrypted_data = pass_file_contents[16:]
            aes_cbc = AES.new(key=self.AES_key, mode=AES.MODE_CBC, IV=iv)
            decrypted_data = unpad(aes_cbc.decrypt(encrypted_data), AES.block_size)
            return decrypted_data
