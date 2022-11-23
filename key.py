# importing os module to generate salt
import os
import base64



# key module constant variables.

# file path of private key.
PRIVATE = "private.key"

# taking maximum advantage of the full strength of AES encryption requires
# a password of approximately 32 characters for 128-bit encryption and 
# 64 characters for 256-bit encryption.
KEY_LIMIT = 64



"""
read_key()

Reads private key from private.key file and adds a salt to it.
"""
def read_key():
    try:
        with open(PRIVATE, "r") as file:
            private_key = file.readline()

            return __add_salt(private_key)
    except EnvironmentError:
        print("[ERROR][PRIVATE KEY] private key not found")
        exit()
 

"""
__add_salt(key: any key to add salt to it)

Adds a random string into the end of our key.
"""
def __add_salt(key):
    size = KEY_LIMIT - len(key)
    
    if size <= 0:
        return key

    salt = base64.b64encode(os.urandom(size)).decode("utf-8")[:size]

    print(f'salt:\n\tvalue:{salt}\n\tsize:{len(salt)}\n')

    return key + salt