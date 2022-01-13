def is_isogram(string):
    string_processed = ''.join(char.lower() for char in string if char.isalpha())
    if len(string_processed) == len(set(string_processed)):
        return True
    return False