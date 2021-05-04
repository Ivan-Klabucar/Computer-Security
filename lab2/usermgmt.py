import sys
import os
from os import path
from Users import Users

def init():
    if not path.exists('./files'):
        os.mkdir('./files')
    if not path.exists('./files/passwords'):
        with open('./files/passwords', 'w') as pass_file:
            pass_file.write('')

def which_action(action, user):
    init()
    users = Users()
    if action == 'add':
        users.add(user)
    elif action == 'passwd':
        users.change_password(user)
    elif action == 'forcepass':
        users.force_pass_change(user)
    elif action == 'del':
        users.remove(user)
    else:
        print('Unrecognized action.')


if len(sys.argv) < 3:
    print("Use a keyword such as add, passwd, forcepass, or del and a username")
else:
    which_action(action=sys.argv[1], user=sys.argv[2])