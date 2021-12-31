import itertools

def factors(value):
    prime_factors = []

    for count in itertools.count(start=2):
        while True:
            if value % count == 0:
                value = value / count
                prime_factors.append(count)
            else:
                break
        if value == 1:
            break
    return prime_factors