from HelperFunctions import *
from Users import *
import getpass

class LoginManager:
    def login(self, user):
        hpass = salt = forcechng = None
        try:
            hpass, salt, forcechng = get_pass_and_salt(user)
        except Exception as e:
            print(e)
            return
        passwd = getpass.getpass()
        if not get_hash(passwd, salt) == hpass:
            print('Username or password incorrect.')
            return
        if forcechng:
            passwd = get_double_pass(first_txt='New password:', second_text='Retype new password:')
            if not passwd: print('Passwords do not match!')
            Users().new_password(user, passwd)
        print('Login successful.')