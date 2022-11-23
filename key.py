# importing os module to generate salt
import os



# constant variables
PRIVATE = "private.key"



"""
read_key()

Reads private key from private.key file and adds a salt to it.
"""
def read_key():
    try:
        with open(PRIVATE, "r") as file:
            private_key = file.readline()

            return private_key
    except EnvironmentError:
        print("[ERROR][PRIVATE KEY] private key not found")
        exit()
    