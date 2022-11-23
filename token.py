# import secrets to create tokens
import secrets



# module constants

# Return a random byte string containing nbytes number of bytes. 
# If nbytes is None or not supplied, a reasonable default is used.
SIZE = 16



"""
generate_token()

This function generates bytes tokens based on SIZE variable.
"""
def generate_token():
    return secrets.token_bytes(SIZE)