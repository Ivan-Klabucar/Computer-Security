from HelperFunctions import *

class Users:
    def is_long_pass(self, passwd):
        if not passwd: return False
        if len(passwd) < 3: return False
        return True

    def add_usr_pass(self, user):
        hpass_dict = load_hpasswords()
        passwd = get_double_pass()
        if not self.is_long_pass(passwd): return False
        hpass_dict[user] = hash_pass_with_salt(passwd, get_salt())
        store_hpasswords(hpass_dict)
        return True

    def add(self, user):
        if self.add_usr_pass(user):
            print('User add successfuly added.')
        else:
            print('User add failed. Password mismatch or too short.')
    
    def change_password(self, user):
        if self.add_usr_pass(user):
            print('Password change successful.')
        else:
            print('Password change failed. Password mismatch or too short.')
    
    def new_password(self, user, new_p):
        hpass_dict = load_hpasswords()
        if user in hpass_dict and self.is_long_pass(new_p):
            hpass_dict[user] = hash_pass_with_salt(new_p, get_salt())
            store_hpasswords(hpass_dict)
            return True
        else:
            print('No such user or password too short.')
            return False
    
    def force_pass_change(self, user):
        hpass, salt, forcechng = get_pass_and_salt(user)
        if not forcechng:   
            hpass_dict = load_hpasswords()
            hpass_dict[user] = hpass_dict[user] + 'forcechange'
            store_hpasswords(hpass_dict)
        print('User will be requested to change password on next login.')
    
    def remove(self, user):
        hpass_dict = load_hpasswords()
        if user in hpass_dict:
            del hpass_dict[user]
            print('User successfuly removed.')
            store_hpasswords(hpass_dict)
        else:
            print('No such user.')

        
        
            