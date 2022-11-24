# importing key module to read the private key
from key import read_key
# importing token for generating iv
from token import generate_token
# importing encryption for using encryption and decryption methods
from encryption import Encryption



if __name__ == "__main__":
    # reading key and generating iv
    key = read_key()
    iv = generate_token()

    print(f"Initialization Vector:\n\tvalue: {iv}\n")

    # creating an encryptor
    encryptor = Encryption(key, iv)

    # get the source file
    path = input("Input file > ")

    # output files
    eout = "Cipher.txt"
    dout = "Decode.txt"

    while True:
        # user data
        data = ""

        # get user operation
        op = input("Enter operation (D, E, Q) > ")

        if op == "Q":
            break
        elif op == "E":
            pass
        elif op == "D":
            pass
        else:
            print("[ERROR][OPERATION] not exists!")
            continue

        if op == "E":
            try:
                with open(path, "r") as file:
                    data = file.readline()

                    print(f"Read:\n\tfile: {path}\n\tvalue: {data}\n")

                    cipher = encryptor.encrypt(data)

                    print(f"Encode:\n\t{cipher}\n")

                    with open(eout, "wb") as out_file:
                        out_file.write(cipher)
            except EnvironmentError:
                print("[ERROR][FILE] file key not found!")

                continue
        else:
            try:
                with open(eout, "rb") as file:
                    data = file.readline()

                    print(f"Read:\n\tfile: {path}\n\tvalue: {data}\n")

                    plaintext = encryptor.decrypt(data)

                    print(f"Decode:\n\t{plaintext}\n")

                    with open(dout, "w") as out_file:
                        out_file.write(str(plaintext))
            except EnvironmentError:
                print("[ERROR][FILE] file key not found!")

                continue
        
        print("[OK][OPERATION] operation is done.")
