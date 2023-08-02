# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 15:46:10 2023

@author: Amar Doshi
"""

import json, pickle
from random import randrange
from PrimeNumber import generateLargePrime


def saveKeysToFile(filename: str, data: tuple[int]) -> None:
    public = {'KeySize': data['KeySize'], 'e': data['e'], 'n': data['n']}
    private = {'KeySize': data['KeySize'], 'd': data['d'], 'n': data['n']}

    try:
        with open('./PublicKey/' + filename + '.json' , 'xt') as f:
            json.dump(public, f)

        with open('./PrivateKey/' + filename + '.pkl', 'xb') as f:
            pickle.dump(private, f)

    except FileExistsError:
        print('File Already Exists!')


def generateKeys(keySize):
    p = q = 0

    # Step 1: Create two prime numbers, p and q. Calculate n = p * q:
    while p == q:
        p = generateLargePrime(keySize)
        q = generateLargePrime(keySize)

    n = p * q

    pq1 = (p - 1) * (q - 1)

    ks1 = 2**(keySize - 1)
    ks2 = ks1 * 2               # equivalent to 2**keySize

    e = 0

    # Step 2: Create a number e that is relatively prime to (p-1)*(q-1):
    while gcd(e, pq1) != 1:
        e = randrange(ks1, ks2)

    # Step 3: Calculate d, the mod inverse of e:
    d = findModInverse(e, pq1)

    return {'KeySize': keySize, 'e': e, 'd': d, 'n': n}


def gcd(n1: int, n2: int) -> int:
    while n2 > 0:
        n1, n2 = n2, n1 % n2

    return n1


def findModInverse(a, m):
    if gcd(a, m) != 1:
        return None     # No mod inverse if a & m aren't relatively prime.

    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m

    while v3 != 0:
        q = u3 // v3    # Note that // is the integer division operator.

        v1, v2, v3, u1, u2, u3 = \
            (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3

    return u1 % m


if __name__ == '__main__':

    KeySize = 1024
    Key_File_Name = 'Key1024'

    data = generateKeys(KeySize)
    saveKeysToFile(Key_File_Name, data)
  