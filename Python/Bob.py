def response(hey_bob):
    hey_bob = hey_bob.strip()
    if hey_bob.endswith("?") and not hey_bob.isupper():
        return "Sure."
    elif hey_bob.endswith("?") and hey_bob.isupper():
        return "Calm down, I know what I'm doing!"
    elif hey_bob.isupper():
        return "Whoa, chill out!"
    elif hey_bob.isspace() or len(hey_bob) == 0:
        return "Fine. Be that way!"
    else:
        return "Whatever."