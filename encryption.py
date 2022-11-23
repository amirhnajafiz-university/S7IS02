# import pyaes to create encryption and decryption methods
import pyaes
import binascii



"""
Encryption(key: is the private key for aes, iv: is the initialization vector)

This class implements methods for encryption and decryption with AES algorithm 
over CTR method.
"""
class Encryption():
    ### __init__(self, key: private key, iv: initialization vector)
    def __init__(self, key, iv):
        self.key = binascii.unhexlify(key)
        self.counter = pyaes.Counter(initial_value = iv)
    
    ### encrypt(self, plaintext: input text)
    ### returns ciphertext
    def encrypt(self, plaintext):
        aes = pyaes.AESModeOfOperationCTR(self.key)
        return aes.encrypt(plaintext)
    
    ### decrypt(self, ciphertext: encrypted text)
    ### returns plaintext
    def decrypt(self, ciphertext):
        aes = pyaes.AESModeOfOperationCTR(self.key)
        return aes.decrypt(ciphertext)