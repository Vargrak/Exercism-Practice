import itertools
from functools import cache

@cache
def triplets_with_sum(number):
    for m in range(2, number):
        for n in range(1, m):
            a = (m**2) - (n**2)
            b = 2*m*n
            c = (m**2) + (n**2)
        print(a, b, c)
        if a + b + c == number:
            print(number)








    return []

print(triplets_with_sum(1000))