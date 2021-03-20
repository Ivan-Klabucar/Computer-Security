from KeyGen import generate_keys
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Crypto.Hash import HMAC, SHA256

class Encryptor:
    def __init__(self, master_password):
        self.salt = get_random_bytes(16)
        self.master_password = master_password
        with open('./files/config', 'wb') as config_file:
            config_file.write(self.salt)
        
        self.AES_key, self.HMAC_key = generate_keys(master_password, self.salt)

    def ensure_integrity(self, data):
        hmac_manager = HMAC_Manager(self.master_password)
        hmac_manager.create_hmac(data)

    def encrypt_file_AES_CBC(self, contents, dest):
        iv = get_random_bytes(16)
        aes_cbc = AES.new(key=self.AES_key, mode=AES.MODE_CBC, IV=iv)
        
        # skriveni_tekst = | <-- IV --> | <-- padded content --> |
        encrypted_data = iv + aes_cbc.encrypt(pad(contents, AES.block_size))
        dest.write(encrypted_data)
        self.ensure_integrity(encrypted_data)
        

class Decryptor:
    def __init__(self, master_password):
        self.master_password = master_password
        with open('./files/config', 'rb') as config_file:
            self.salt = config_file.read()
        
        self.AES_key, self.HMAC_key = generate_keys(master_password, self.salt)

    def check_integrity(self, content):
        hmac_manager = HMAC_Manager(self.master_password)
        return hmac_manager.check_hmac(content)
    
    def decrypt(self):
        with open('./files/passwords', 'rb') as passwords_file:
            pass_file_contents = passwords_file.read()
            if not self.check_integrity(pass_file_contents): raise Exception("Integrity compromised / wrong password.")
            iv = pass_file_contents[:16]
            encrypted_data = pass_file_contents[16:]
            aes_cbc = AES.new(key=self.AES_key, mode=AES.MODE_CBC, IV=iv)
            decrypted_data = unpad(aes_cbc.decrypt(encrypted_data), AES.block_size)
            return decrypted_data

class HMAC_Manager:
    def __init__(self, master_password):
        with open('./files/config', 'rb') as config_file:
            self.salt = config_file.read()
        
        self.AES_key, self.HMAC_key = generate_keys(master_password, self.salt)
    
    def create_hmac(self, content):
        h = HMAC.new(self.HMAC_key, msg=content, digestmod=SHA256)
        tag = h.digest()
        with open('./files/integrity', 'wb') as hmac_file:
            hmac_file.write(tag)
    
    def check_hmac(self, content):
        tag = b''
        with open('./files/integrity', 'rb') as hmac_file:
            tag = hmac_file.read()
        h = HMAC.new(self.HMAC_key, msg=content, digestmod=SHA256)
        try:
            h.verify(tag)
        except ValueError:
            return False
        return True

