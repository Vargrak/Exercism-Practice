from collections import Counter
import string
def count_words(sentence):
    ignored = ".,?!$%@&^:'\"\n\t  "
    sentence = sentence.translate({ord(ch):" " for ch in ".,?!$%@&^:\"\n\t_  "})
    word_list = [sentence.strip(ignored).lower() for sentence in sentence.split(" ") if sentence not in ignored]
    return Counter(word_list)