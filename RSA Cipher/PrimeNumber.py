# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 15:48:44 2023

@author: Amar Doshi
"""

import random
from math import sqrt
from array import array
from itertools import repeat


def sqrRootBounds(num: int) -> tuple[int, int]:
    if num <= 1: return num, num + 1

    l = 0
    h = num

    while h - l > 1:
        m = (l + h) // 2
        m2 = m * m

        if m2 > num:
            h = m
        elif m2 == num:
            l = m
            h = l + 1
            break
        elif m2 < num:
            l = m

    return l, h


def primeSieve(sieveSize: int) -> tuple[int]:
    '''
    Returns a list of prime numbers calculated using
    the Sieve of Eratosthenes algorithm.
    '''

    sieve = array('B', repeat(True, sieveSize + 1))

    sieve[0] = sieve[1] = False

    for i in range(4, sieveSize + 1, 2):
        sieve[i] = False

    _, r = sqrRootBounds(sieveSize)

    for i in range(3, r, 2):
        if sieve[i]:
            for j in range(i, (sieveSize // i) + 1, 2):
                sieve[i * j] = False

    return tuple([i for i, v in enumerate(sieve) if v]) # Fastest way to create tuple


def rabinMiller(num):
    '''
    Finds numbers that are very likely to be prime but are not
    guaranteed to be prime.
    '''

    if  num < 2: return False

    # Rabin-Miller doesn't work on even integers.
    if num == 2: return True

    # If the number ends in an even digit
    if not (num & 1): return False

    if num == 3: return True

    t = 0
    s = num - 1

    while not (s & 1): # Checks if the number is even
        # Keep halving s until it is odd
        # (and use t to count how many times we halve s):
        s //= 2
        t += 1

    for trials in range(5): # Try to falsify num's primality 5 times.
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)

        if v != 1: # This test does not apply if v is 1.
            i = 0

            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % num

    return True


LOW_PRIMES = primeSieve(10_000)


def isPrime(num):
    if num < 2: return False

    if num == 2: return True

    # Tests if number ends in an even digit
    if not (num & 1): return False

    for prime in LOW_PRIMES:
        if num == prime: return True
        if num % prime == 0: return False

    # If all else fails, call rabinMiller() to determine if num is prime:
    return rabinMiller(num)


def generateLargePrime(keysize=1024):
    # Return a random prime number that is keysize bits in size.

    ks1 = 2**(keysize - 1)
    ks2 = ks1 * 2                # equivalent to 2**keySize

    while True:
        num = random.randrange(ks1, ks2)

        if isPrime(num): return num
