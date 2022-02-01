import string
import secrets
class Cipher:
    def __init__(self, key=None):
        if key != None:
            self.key = key
        else:
            self.key = ""
            while len(self.key) != 100:
                self.key = f"{self.key}{secrets.choice(string.ascii_lowercase.lower())}"

    def encode(self, text):
        key_len = len(self.key)
        encoded = ""
        for i in range(0, len(text)):
            key = string.ascii_lowercase.index(self.key[i % key_len])
            letter = text[i].lower()
            alphabet = str(string.ascii_lowercase)
            cipherbet = alphabet[key:] + alphabet[:key]
            cipher_table = str.maketrans(alphabet, cipherbet)
            encoded = f"{encoded}{letter.translate(cipher_table)}"
        return encoded

    def decode(self, text):
        key_len = len(self.key)
        decoded = ""
        for i in range(0, len(text)):
            key = string.ascii_lowercase.index(self.key[i % key_len])
            letter = text[i].lower()
            alphabet = str(string.ascii_lowercase)
            cipherbet = alphabet[key:] + alphabet[:key]
            cipher_table = str.maketrans(cipherbet, alphabet)
            decoded = f"{decoded}{letter.translate(cipher_table)}"    
        return decoded