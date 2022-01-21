import string
def is_pangram(sentence):
    return all(sentence.lower().find(char) > -1 for char in string.ascii_lowercase)