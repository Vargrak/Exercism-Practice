def add_prefix_un(word):
    return "un" + word

def make_word_groups(vocab_words):
    return vocab_words[0].join(vocab_words[1:])

def remove_suffix_ness(word):
    new_str = word[:-4]
    if "i" in new_str[-1]:
        new_str=new_str[:-1] + "y"
    return new_str

def noun_to_verb(sentence, index):
    a