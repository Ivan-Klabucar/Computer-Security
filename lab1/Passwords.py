from KeyGen import generate_keys
from Crypto.Cipher import AES
from Cryptors import Encryptor, Decryptor

class Passwords:
    def __init__(self, master_password):
        self.master_password = master_password
 
    def decrypt_to_plaintext(self):
        decryptor = Decryptor(self.master_password)
        plaintext_passwords = decryptor.decrypt().decode("utf-8").strip()
        return plaintext_passwords.split('\n')
    
    def get_password_for(self, address):
        plaintext_passwords = self.decrypt_to_plaintext()
        for entry in plaintext_passwords:
            if not entry == '':
                curr_addr, curr_pass = entry.split(chr(12)) # chr(12) delimiter adrese i sifre
                if curr_addr == address:
                    return curr_pass
        return None
    
    def put_password_for(self, address, password):
        pass_list = self.decrypt_to_plaintext()
        new_entry = address + chr(12) + password
        found = False
        for i in range(len(pass_list)):
            if pass_list[i] == '': break # End of file
            curr_addr, curr_pass = pass_list[i].split(chr(12)) # chr(12) delimiter adrese i sifre
            if curr_addr == address:
                pass_list[i] = new_entry
                found = True
        if not found:
            tmp = pass_list.pop()
            pass_list.append(new_entry)
            pass_list.append(tmp)
        
        new_pass_file_content = '\n'.join(pass_list).encode()
        encryptor = Encryptor(self.master_password)
        with open('./files/passwords', 'wb') as password_file:
            encryptor.encrypt_file_AES_CBC(new_pass_file_content, dest=password_file)
            


    
