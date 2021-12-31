import itertools

def equilateral(sides):
    return test_triangle(sides) == 3

def isosceles(sides):
    return test_triangle(sides) >= 1

def scalene(sides):
    return test_triangle(sides) is 0

def test_triangle(sides):
    for a, b, c in itertools.permutations(sides, 3):
        if a <= 0 or a >= b+c:
            return False
    total = 0
    for a, b in itertools.combinations(sides, 2):
        if a == b:
            total += 1
    return total