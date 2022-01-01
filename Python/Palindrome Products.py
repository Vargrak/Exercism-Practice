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
        return (return_product, [return_factors, extra_factors])
    else:
        return (return_product, [return_factors])

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
        return (return_product, [return_factors, extra_factors])
    else:
        return (return_product, [return_factors])

def initialization(half, max_factor, min_factor = 0):
    factors = []
    if min_factor > max_factor:
        raise ValueError("min must be <= max")
    for factor in range (min_factor, max_factor+1):
        factors.append(factor)
    if len(factors) > 1000:
        if half == "small":
            factors = factors[:len(factors)//2]
            return factors[:len(factors)//2]
        if half == "large":
            factors = factors[len(factors)//2:]
            return factors[len(factors)//2:]
    else:
        return factors

print(largest(min_factor=1000, max_factor=9999))