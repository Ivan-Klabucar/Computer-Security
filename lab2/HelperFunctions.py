from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import scrypt
import getpass

def load_hpasswords():
    content = ''
    with open('./files/passwords', 'r') as pass_file:
        content = pass_file.read()
    content = content.split('\n')
    result = dict()
    for x in content:
        if x:
            usr, pass_hash = x.split('Partition 0')
            result[usr] = pass_hash
    return result

def store_hpasswords(hdict):
    with open('./files/passwords', 'w') as pass_file:
        pass_file.write('\n'.join([usr + 'Partition 0' + hdict[usr] for usr in hdict]))

def get_double_pass(first_txt='Password:', second_text='Retype password:'):
    pass_1 = getpass.getpass(first_txt)
    pass_2 = getpass.getpass(second_text)
    if not pass_1 == pass_2:
        return False
    return pass_1

def get_salt():
    return get_random_bytes(16)

def get_hash(passwd, salt):
    key = scrypt(passwd.encode(), salt, 16, N=2**14, r=8, p=1)
    return str(key)

def hash_pass_with_salt(passwd, salt):
    return get_hash(passwd, salt) + 'Partition 1' + str(salt)

def get_pass_and_salt(user):
    hpass_dict = load_hpasswords()
    if not user in hpass_dict: raise Exception('Login unsuccessful.')
    hpass, salt = hpass_dict[user].split('Partition 1')
    forcechng = False
    if 'forcechange' in salt:
        forcechng = True
        salt = salt.split('forcechange')[0]
    salt = eval(salt)
    return hpass, salt, forcechng