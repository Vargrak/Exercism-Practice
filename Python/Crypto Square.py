def cipher_text(plain_text):
    if len(plain_text) < 2:
        return plain_text.lower()

    ignored = "!@$%^&*,.'`_ "
    only_text = ''.join([char for char in plain_text if char not in ignored])

    i=0
    while True:
        i += 1
        if i >= len(only_text)/i:
            break

    segmented = [only_text[x:x+i] for x in range(0, len(plain_text)-i, i) if only_text[x:x+i] != '']
    if len(segmented[-1]) != i:
       segmented[-1] = segmented[-1].ljust(i)

    return_ = []
    for x in range(0, i):
        return_.append(''.join([segment[x] for segment in segmented]))
    return ' '.join(return_).lower()