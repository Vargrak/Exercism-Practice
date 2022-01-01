#Not yet marked as completed - takes too long or has an infinite loop according to exercism
#testing in vscode yields correct results, unsure how to test 'def assertFactorsEqual'
#execution time around 15.5 seconds

import itertools
import time
start = time.time()

def largest(max_factor, min_factor = 0):
    result = (None, [])
    return_product = largest_product = 0
    extra_factors = return_factors = []
    factors = initialization("large", max_factor, min_factor)
    for x in factors:
        for y in factors:
            product = x * y
            if str(product)[::-1] == str(product):
                if largest_product < product:
                    largest_product = return_product = product
                    return_factors = [x, y]
                    extra_factors = []
                elif largest_product == product:
                    already_returned = 0
                    for i in range(0, len(return_factors)-1):
                        if return_factors[i] == x and return_factors[i+1] == y or return_factors[i+1] == x and return_factors[i] == y:
                            already_returned = 1
                    if already_returned == 0:
                        extra_factors = [x, y]
    if return_product < 1:
        return result
    elif len(extra_factors) > 1:
        return (return_product, return_factors, extra_factors)
    else:
        return (return_product, return_factors)

def smallest(max_factor, min_factor = 0):
    result = (None, [])
    return_product = 0
    extra_factors = return_factors = []
    smallest_product = max_factor * max_factor
    factors = initialization("small", max_factor, min_factor)
    for x in factors:
        for y in factors:
            product = x * y
            if str(product)[::-1] == str(product):
                if smallest_product > product:
                    smallest_product = return_product = product
                    return_factors = [x, y]
                    extra_factors = []
                elif smallest_product == product:
                    already_returned = 0
                    for i in range(0, len(return_factors)-1):
                        if return_factors[i] == x and return_factors[i+1] == y or return_factors[i+1] == x and return_factors[i] == y:
                            already_returned = 1
                    if already_returned == 0:
                        extra_factors = [x, y]
    if return_product < 1:
        return result
    elif len(extra_factors) > 1:
        return (return_product, return_factors, extra_factors)
    else:
        return (return_product, return_factors)

def initialization(half, max_factor, min_factor = 0):
    factors = []
    if min_factor > max_factor:
        raise ValueError("min must be <= max")
    for factor in range (min_factor, max_factor+1):
        factors.append(factor)
    if len(factors) > 1000:
        if half == "small":
            return factors[:len(factors)//2]
        if half == "large":
            return factors[len(factors)//2:]
    else:
        return factors

print(smallest(min_factor=1, max_factor=9))
print(largest(min_factor=1, max_factor=9))
print(smallest(min_factor=10, max_factor=99))
print(largest(min_factor=10, max_factor=99))
print(smallest(min_factor=100, max_factor=999))
print(largest(min_factor=100, max_factor=999))
print(smallest(min_factor=1000, max_factor=9999))
print(largest(min_factor=1000, max_factor=9999))
print(smallest(min_factor=1002, max_factor=1003))
print(largest(min_factor=15, max_factor=15))

#error handling tests
#print(smallest(min_factor=10000, max_factor=1))
#print(largest(min_factor=2, max_factor=1))

execution_time = (time.time() - start)
print("Execution time " + str(execution_time))