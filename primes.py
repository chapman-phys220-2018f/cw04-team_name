#!/usr/bin/env python3

import math

def gen_eratosthenes():
    """generates a list of prime numbers"""
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
    """returns list of prime numbers less than n"""
    primes = list(range(2, n))
    for i in range(2, int(math.sqrt(n)) + 1):
        for j in primes:
            if (i != j) and (j % i == 0):
                   primes.remove(j)
    return primes

def eratosthenes_with_gen(n):
    """uses generator to return list of prime numbers less than n"""
    p = gen_eratosthenes()
    primes = []
    p_iteration = 0
    for _ in range(n):
        p_iteration = next(p)
        if (p_iteration < n):
            primes.append(p_iteration)
    return primes