# importing os and pbkdf2 modules to generate key with salt
import os, binascii
from backports.pbkdf2 import pbkdf2_hmac



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
    salt = os.urandom(32)

    # sha256 hash-function for calculating HMAC, e.g. SHA256
    # 50000 iterations-count, e.g. 1024 iterations
    # 32 derived-key-len is for the output, e.g. 32 bytes (256 bits)
    key = pbkdf2_hmac("sha256", key, salt, 50000, 32)

    # hexlifying the generated key
    key = binascii.hexlify(key)

    print(f'Algorithm key is:\n\tvalue: {key}\n\tsize: {len(key)*4} bits\n')

    return key