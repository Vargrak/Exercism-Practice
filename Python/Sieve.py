def primes(number):
    primes_list = []
    for i in range (2, number+1):
        if all( i % prime != 0 for prime in primes_list):
            primes_list.append(i)
    return primes_list