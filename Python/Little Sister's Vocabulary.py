def add_prefix_un(word):
    return "un" + word

def make_word_groups(vocab_words):
    prefix = ' :: ' + vocab_words[0]
    return prefix.join(vocab_words)

def remove_suffix_ness(word):
    if "i" in word[-5]:
        return word[:-5] + "y"
    else:
        return word[:-4]

def noun_to_verb(sentence, index):
    verb = sentence.split()[index]
    if "." in verb:
        verb = verb[:-1]
    return verb + "en"