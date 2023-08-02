# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 17:40:57 2023

@author: Amar Doshi


WARNING

The implementation of the public key cipher in this projct is based on the
RSA cipher. However, this implementation is unsuitable for real-world use.


DISCLAIMER

This code is on an “As Is” basis, without warranty. The author shall not have any
liability to any person or entity with respect to any loss or damage caused or
alleged to be caused directly or indirectly by the information contained in it.
"""


KEY_FILE_NAME = 'Key1024'

PLAIN_TEXT_FILE_NAME = 'Turing.txt'
ENCRYPTED_FILE_NAME = 'Turing.csv'
DECRYPTED_FILE_NAME = 'Turing.txt'


#------------------------------------------------------------------------------


import csv, json, pickle
from Convert import toNumbers, toText
from EncryptDecrypt import encrypt, decrypt


PUBLIC_KEY_FILE = './PublicKey/' + KEY_FILE_NAME + '.json'
PRIVATE_KEY_FILE = './PrivateKey/' + KEY_FILE_NAME + '.pkl'

PLAIN_TEXT_FILE = './PlainText/' + PLAIN_TEXT_FILE_NAME
ENCRYPTED_FILE = './Encrypted/' + ENCRYPTED_FILE_NAME
DECRYPTED_FILE = './Decrypted/' + DECRYPTED_FILE_NAME


def encryptMessage() -> None:
    with open(PUBLIC_KEY_FILE, mode='rt') as f:
        key = json.load(f)

    with open(PLAIN_TEXT_FILE, mode='rt', encoding='UTF-8',
              errors='replace') as f:
        plainText = f.read().replace('\n', ' ')

    numbers = toNumbers(plainText, key['KeySize'])

    code = encrypt(numbers, key['e'], key['n'])

    with open(ENCRYPTED_FILE, mode='wt', newline='') as f:
        w = csv.writer(f, delimiter=',')
        w.writerow(code)


def decryptMessage() -> None:
    with open(PRIVATE_KEY_FILE, mode='rb') as f:
        key = pickle.load(f)

    with open(ENCRYPTED_FILE, mode='rt') as f:
        code = [int(i) for i in list(csv.reader(f, delimiter=','))[0]]

    numbers = decrypt(code, key['d'], key['n'])
    plainText = toText(numbers, key['KeySize'])

    with open(DECRYPTED_FILE, mode='wt', encoding='UTF-8') as f:
        f.write(plainText)


if __name__ == '__main__':

    encryptMessage()
    decryptMessage()
