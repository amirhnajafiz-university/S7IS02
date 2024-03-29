# importing os and pbkdf2 modules to generate key with salt
import os, binascii
from pbkdf2 import PBKDF2



# key module constant variables.

# file path of private key.
PRIVATE = "private.key"

# taking maximum advantage of the full strength of AES encryption requires
# a password of approximately 32 characters for 128-bit encryption and 
# 64 characters for 256-bit encryption.
KEY_LIMIT = 32



"""
read_key()

Reads private key from private.key file and adds a salt to it.
"""
def read_key():
    try:
        with open(PRIVATE, "r") as file:
            private_key = file.readline()

            print(f"Read private key:\n\tfile: {PRIVATE}\n\tvalue: {private_key}\n")

            return __add_salt(private_key)
    except EnvironmentError:
        print("[ERROR][PRIVATE KEY] private key not found")
        exit()
 

"""
__add_salt(key: any key to add salt to it)

Adds a random string into the end of our key.
"""
def __add_salt(key):
    key = key.encode("utf8")

    # salt – securely-generated random bytes, 
    # e.g. "df1f2d3f4d77ac66e9c5a6c3d8f921b6" (minimum 64 bits, 128 bits is recommended)
    # generating 256 bit salt
    salt = os.urandom(KEY_LIMIT)

    # generating a 256 bit key with salt
    key = PBKDF2(key, salt).read(KEY_LIMIT) # 256-bit key

    # hexlifying the generated key
    key = binascii.hexlify(key)

    print(f'Algorithm key is:\n\tvalue: {key}\n\tsize: {len(key)*4} bits\n')

    return key