# import secrets to create tokens
import secrets



# module constants

# When generating a random number with secrets
# we need to set a limit.
# The limit is 16 bytes or 64 bits or a 247 int.
LIMIT = 247



"""
generate_token()

This function generates tokens based on LIMIT variable.
"""
def generate_token():
    return secrets.randbelow(LIMIT)