import sys
import os
from os import path
from LoginManager import *


def check_if_initialized():
    if not path.exists('./files') or not path.exists('./files/passwords'): return False
    return True

if len(sys.argv) < 2:
    print("Enter a username.")
else:
    if not check_if_initialized():
        print('Login system not initialized.\nUse usermgmt tool first to add a user.')
    else:
        LoginManager().login(sys.argv[1])
    