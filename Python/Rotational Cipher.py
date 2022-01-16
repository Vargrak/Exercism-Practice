import string
def rotate(text, key):
    alphabet = str(string.ascii_lowercase)
    cipherbet = alphabet[key:] + alphabet[:key]
    cipher_table = str.maketrans(alphabet+alphabet.upper(), cipherbet+cipherbet.upper())
    return text.translate(cipher_table)