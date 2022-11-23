# import pyaes to create encryption and decryption methods
import pyaes



"""
Encryption(key: is the private key for aes, iv: is the initialization vector)

This class implements methods for encryption and decryption with AES algorithm 
over CTR method.
"""
class Encryption():
    ### __init__(self, key: private key, iv: initialization vector)
    def __init__(self, key, iv):
        counter = pyaes.Counter(initial_value = iv)
        self._aes = pyaes.AESModeOfOperationCTR(key, counter = counter)
    
    ### encrypt(self, plaintext: input text)
    ### returns ciphertext
    def encrypt(self, plaintext):
        return self._aes.encrypt(plaintext)
    
    ### decrypt(self, ciphertext: encrypted text)
    ### returns plaintext
    def decrypt(self, ciphertext):
        return self._aes.decrypt(ciphertext)