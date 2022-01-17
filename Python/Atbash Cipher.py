import string
def encode(plain_text):
    count = 0
    ignore = ",.!?-_ "
    pre_space = plain_text.translate(str.maketrans(string.ascii_lowercase+string.ascii_uppercase, string.ascii_lowercase[::-1]+string.ascii_lowercase[::-1]))
    post_space = [char for char in pre_space if char not in ignore]
    for index, char in enumerate(post_space):
        if char.isalnum():
            count+=1
        if char.isspace():
            continue
        if count % 5 == 0:
            post_space.insert(index+1, " ")
    encoded = ''.join(post_space)
    return encoded.strip(" ")

def decode(ciphered_text):
    pre_space = ciphered_text.translate(str.maketrans(string.ascii_lowercase[::-1]+string.ascii_uppercase[::-1], string.ascii_lowercase+string.ascii_lowercase))
    return pre_space.replace(" ", "")