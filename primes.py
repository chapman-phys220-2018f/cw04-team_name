#!/usr/bin/env python3

import math

def gen_eratosthenes():
    index = 0
    count = 0
    list_primes = [2]
    next_prime = 3
    yield list_primes[index]
    while (True):
        for i in range(2, next_prime):
            if (next_prime % i != 0):
                count += 1
            else:
                break
            if (count == next_prime - 2):
                index += 1
                list_primes.append(next_prime)
                yield list_primes[index]
        count = 0
        next_prime += 1

def eratosthenes(n):
    p = gen_eratosthenes()
    primes = []
    for _ in range(n):
        primes.append(next(p))
    return primes