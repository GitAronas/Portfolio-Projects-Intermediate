# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 17:10:54 2023

@author: Amar Doshi
"""

'''
                    C = (M ** e) mod n

                    M = (C ** d) mod n
'''


def encrypt(numbers: list[int], e: int, n: int) -> list[int]:
    c = []

    for num in numbers:
        c.append(pow(num, e, n))

    return c


def decrypt(code: list[int], d: int, n: int) -> list[int]:
    m = []

    for num in code:
        m.append(pow(num, d, n))

    return m
