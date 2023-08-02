# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 18:58:59 2023

@author: Amar Doshi
"""

'''
    2 ** (key_size) > symbol_set_size ** (block_size)

    block_size < key_size / log2(symbol_set_size)
'''


from math import log2


SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

ERROR_SYMBOL_INDEX = SYMBOLS.index(SYMBOLS[-2])

FILLER_SYMBOL = SYMBOLS[-4]

SYMBOL_SET_SIZE = len(SYMBOLS)



def toNumbers(text: str, KeySize: int) -> list[int]:
    BLOCK_SIZE = int(KeySize // log2(SYMBOL_SET_SIZE))

    r = len(text) % BLOCK_SIZE

    if r != 0:
        text += FILLER_SYMBOL * (BLOCK_SIZE - r)

    blocks = []

    for i in range(0, len(text), BLOCK_SIZE):
        m = 1

        if text[i] in SYMBOLS:
            t = SYMBOLS.index(text[i])
        else:
            t = ERROR_SYMBOL_INDEX

        for c in text[i + 1: i + BLOCK_SIZE]:
            m *= SYMBOL_SET_SIZE

            if c in SYMBOLS:
                t += (SYMBOLS.index(c) * m)
            else:
                t += (ERROR_SYMBOL_INDEX * m)

        blocks.append(t)

    return blocks


def toText(numbers: list[int], KeySize: int) -> str:
    text = []
    chars = []

    BLOCK_SIZE = int(KeySize // log2(SYMBOL_SET_SIZE))

    p = pow(SYMBOL_SET_SIZE, BLOCK_SIZE - 1)

    for num in numbers:
        m = p

        for _ in range(BLOCK_SIZE - 1):
            i = num // m

            chars.append(SYMBOLS[i])

            num -= i * m
            m //= SYMBOL_SET_SIZE

        chars.append(SYMBOLS[num])
        text.append(''.join(chars[::-1]))
        chars.clear()

    return ''.join(text).rstrip()
