import re

def abbreviate(words):
    acronym = ""
    words = re.sub('[\_\-]', ' ', words)
    words_list = words.split()
    for word in words_list:
        acronym += word[0]
    return acronym.upper()