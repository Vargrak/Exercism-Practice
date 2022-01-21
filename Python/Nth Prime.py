import itertools
def prime(number):
    if number == 0:
        raise ValueError("there is no zeroth prime")
    
    primes_list = []

    for count in itertools.count(2):
        if all( count % prime != 0 for prime in primes_list):
             primes_list.append(count)
        if len(primes_list) == number:
            return primes_list[-1]