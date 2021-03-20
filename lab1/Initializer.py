import os
from Crypto.Protocol.KDF import scrypt
from Crypto.Random import get_random_bytes
from Cryptors import Encryptor

class Initializer:
    def __init__(self, master_password):
        self.master_password = master_password
    
    def initialize_tajnik(self):
        try:
            os.mkdir('./files')
        except Exception as e:
            answ = input('Tajnik already exists, do you want to reset it? [y/n]: ')
            answ = answ.strip().lower()
            if answ == 'y':
                print('Tajnik was reset.')
            else:
                print('Aborting...')
                return
        
        salt = get_random_bytes(16)
        with open('./files/config', 'wb') as config_file:
            config_file.write(salt)

        with open('./files/passwords', 'wb') as password_file:
            initial_contents = b'fun\x0chejhejdeckotigay\n'
            encryptor = Encryptor(self.master_password)
            encryptor.encrypt_file_AES_CBC(initial_contents, dest=password_file)
            

            
        
