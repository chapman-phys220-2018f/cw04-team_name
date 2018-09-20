#!/usr/bin/env python3

import math

def gen_eratosthenes():
    count = 0
    list_primes = [2]
    next_prime = 3
    while (True):
        yield list_primes[count]
        for i in list_primes:
            if (next_prime % i == 0):
                break
            elif (next_prime % i != 0) and not(next_prime in list_primes):
                count += 1
                list_primes.append(next_prime)
        next_prime += 1
            
def eratosthenes(n):
    p = gen_eratosthenes()
    primes = []
    for _ in range(n):
        primes.append(next(p))
    return primes

print(eratosthenes(5))

