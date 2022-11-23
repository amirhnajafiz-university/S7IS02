# importing key module to read the private key
from key import read_key
from token import generate_token
from encryption import Encryption



if __name__ == "__main__":
    private = read_key()
    iv = generate_token()

    print(f"Initialization Vector:\n\tvalue: {iv}\n")

    enc = Encryption(private, iv)

    print(enc.encrypt("Hello world"))