import sys
from Initializer import *
from Passwords import *

def init(master_password):
    initializer = Initializer(master_password)
    initializer.initialize_tajnik()

def which_action(argv, master_password):
    action = argv[1]
    if action == 'init':
        init(master_password)
        print("Password manager (tajnik) initialized.")
    elif action == 'get':
        address = argv[3]
        passwords = Passwords(master_password)
        requested_pass = passwords.get_password_for(address)
        if requested_pass:
            print(f"Password for {argv[3]}: {requested_pass}")
        else:
            print("No password for that address")
    elif action == 'put':
        address = argv[3]
        password = argv[4]
        passwords = Passwords(master_password)
        passwords.put_password_for(address, password)
        print(f"Stored password for {address}")



if len(sys.argv) < 2:
    print("Use a keyword such as init, put, or get")
else:
    which_action(sys.argv, master_password=sys.argv[2])