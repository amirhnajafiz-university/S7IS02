<h1 align="center">
  AES Encryption
</h1>

Implementing **AES** _encryption_ and _decryption_ with Python. Data security second project. In this project I used the important data security modules in python.

- Secrets
- Pyaes
- OS
- Binascii

More information about encryption can be found in ```encription``` module:

```python
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
```

## Run

Add your key in ```private.key``` file. Run the program:

```shell
python main.py
```

Results will be stored in ```gen``` directory (Please do not remove any files from ```gen``` directory).
