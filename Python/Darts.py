from math import sqrt
def score(x, y):
    location = sqrt(((x-0)**2)+((y-0)**2))
    if location > 10:
        return 0
    elif location <= 10 and location > 5:
        return 1
    elif location <= 5 and location > 1:
        return 5
    elif location <= 1:
        return 10