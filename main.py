# importing key module to read the private key
from key import read_key
# importing token for generating iv
from token import generate_token
# importing encryption for using encryption and decryption methods
from encryption import Encryption
# importing utils
import utils
import binascii



if __name__ == "__main__":
    # set project requirements
    utils.start()

    # reading key and generating iv
    key = read_key()
    iv = generate_token()

    print(f"Initialization Vector:\n\tvalue: {iv}\n")

    # creating an encryptor
    encryptor = Encryption(key, iv)

    # output files
    keyout = utils.MAIN + "/key.txt"
    eout = utils.MAIN + "/Cipher.txt"
    binout = utils.MAIN + "/Cipher.bin"
    dout = utils.MAIN + "/Decode.txt"

    # save key into file
    with open(keyout, "w") as file:
        file.write(str(key))
    
    # get the source file
    path = input("Input file > ")

    # main loop
    while True:
        # user data
        data = ""

        # get user operation
        op = input("\nEnter operation (D [Dec] , E [Enc], Q [Quit], C[Change file]) > ")

        if op == "Q":
            break
        elif op == "E":
            pass
        elif op == "D":
            pass
        elif op == "C":
            path = input("Input file > ")
            continue
        else:
            print("[ERROR][OPERATION] not exists!")
            continue

        if op == "E":
            try:
                with open(path, "r") as file:
                    data = file.readline()

                print(f"Read:\n\tfile: {path}\n\tvalue: {data}\n")

                cipher = encryptor.encrypt(data)

                with open(binout, "wb") as out_file:
                    out_file.write(cipher)
                with open(eout, "w") as out_file:
                    out_file.write(str(binascii.hexlify(cipher)))
            except EnvironmentError:
                print("[ERROR][FILE] file key not found!")

                continue
        else:
            try:
                with open(binout, "rb") as file:
                    data = file.readline()

                print(f"Read:\n\tfile: {path}\n\tvalue: {data}\n")

                plaintext = encryptor.decrypt(data)

                with open(dout, "w") as out_file:
                    out_file.write(plaintext.decode('utf-8'))
            except EnvironmentError:
                print("[ERROR][FILE] file key not found!")

                continue
        
        print("\n[OK][OPERATION] operation is done.")
