def add_prefix_un(word):
    return "un" + word

def make_word_groups(vocab_words):
    for single_word in vocab_words:
        if vocab_words=[0] != single_word:
            vocab_words[0].join(single_word)

def remove_suffix_ness(word):
    new_str = word[:-4]
    if "i" in new_str[-1]:
        new_str=new_str[:-1] + "y"
    return new_str

def noun_to_verb(sentence, index):
    a