def sum_of_multiples(limit, multiples):
    return sum([i for i in range(0, limit) if 0 in [i % factor for factor in multiples if factor != 0]])