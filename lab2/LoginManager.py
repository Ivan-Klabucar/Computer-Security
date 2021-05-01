from HelperFunctions import *
from Users import *
import getpass

class LoginManager:
    def is_valid(self, passwd, old_pass):
        if not passwd: 
            print('Passwords do not match!')
            return False
        if passwd == old_pass:
            print('New password can\'t be old password.')
            return False
        return True
    
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
            new_passwd = get_double_pass(first_txt='New password:', second_text='Retype new password:')
            if not self.is_valid(new_passwd, passwd): return
            if not Users().new_password(user, new_passwd):
                print('Login unsuccessful.')
                return
        print('Login successful.')