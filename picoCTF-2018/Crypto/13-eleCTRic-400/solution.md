# Problem
You came across a custom server that Dr Xernon's company eleCTRic Ltd uses. It seems to be storing some encrypted files. Can you get us the flag? Connect with ```nc 2018shell1.picoctf.com 15037```. [Source](https://2018shell1.picoctf.com/static/61d78e61c2bd099775499bba7edc1d62/eleCTRic.py).

## Hints:
I have repeated myself many many many times- do not repeat yourself.

Do I need to say it in different words? You mustn't repeat thyself.

## Solution:
First, we download:
```bash
wget https://2018shell1.picoctf.com/static/61d78e61c2bd099775499bba7edc1d62/eleCTRic.py
```

Lets look at the code:
```python
#!/usr/bin/python

from Crypto import Random
from Crypto.Cipher import AES
import sys
import time
import binascii


class AESCipher(object):
    def __init__(self):
        self.bs = 32
        random = Random.new()
        self.key = random.read(AES.block_size)
        self.ctr = random.read(AES.block_size)

    def encrypt(self, raw):
        cipher = AES.new(self.key, AES.MODE_CTR, counter=lambda: self.ctr)
        return cipher.encrypt(raw).encode('base64').replace('\n', '')

    def decrypt(self, enc):
        try:
            enc = enc.decode('base64')
        except binascii.Error:
            return None
        cipher = AES.new(self.key, AES.MODE_CTR, counter=lambda: self.ctr)
        return cipher.decrypt(enc)

class Unbuffered(object):
    def __init__(self, stream):
        self.stream = stream
    def write(self, data):
        self.stream.write(data)
        self.stream.flush()
    def writelines(self, datas):
        self.stream.writelines(datas)
        self.stream.flush()
    def __getattr__(self, attr):
        return getattr(self.stream, attr)
    
sys.stdout = Unbuffered(sys.stdout)
    
def get_flag():
    try:
        with open("flag.txt") as f:
            return f.read().strip()
    except IOError:
        return "picoCTF{xxxFAKEFLAGxxx} Something went wrong. Contact organizers."
    
def welcome():
    print "Welcome to eleCTRic Ltd's Safe Crypto Storage"
    print "---------------------------------------------"


def menu():
    print ""
    print "Choices:"
    print "  E[n]crypt and store file"
    print "  D[e]crypt file"
    print "  L[i]st files"
    print "  E[x]it"
    while True:
        choice = raw_input("Please choose: ")
        if choice in list('neix'):
            print ""
            return choice


def do_encrypt(aes, files):
    filename = raw_input("Name of file? ")
    if any(x in filename for x in '._/\\ '):
        print "Disallowed characters"
        return
    filename += '.txt'
    if filename in files:
        if raw_input("Clobber previously existing file? [yN] ") != 'y':
            return
    data = raw_input("Data? ")
    files[filename] = aes.encrypt(data)
    print "Share code:"
    print aes.encrypt(filename)


def do_decrypt(aes, files):
    enc = raw_input("Share code? ")
    filename = aes.decrypt(enc)
    if filename is None:
        print "Invalid share code"
        return
    if filename in files:
        print "Data: "
        print aes.decrypt(files[filename])
    else:
        print "Could not find file"
        return


def do_list_files(files):
    print "Files:"
    for f in files:
        print "  " + f


def main():
    print "Initializing Problem..."
    aes = AESCipher()
    flag = get_flag()
    flag_file_name = "flag_%s" % Random.new().read(10).encode('hex')

    files = {flag_file_name + ".txt": aes.encrypt(flag)}

    welcome()
    while True:
        choice = menu()
        if choice == 'n':       # Encrypt
            do_encrypt(aes, files)
        elif choice == 'e':     # Decrypt
            do_decrypt(aes, files)
        elif choice == 'i':     # List files
            do_list_files(files)
        elif choice == 'x':     # Exit
            break
        else:
            print "Impossible! Contact contest admins."
            sys.exit(1)


main()
```

What's going on here?

First we can see that all encryptions/decryptions using the same [counter](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Counter_(CTR))

Strategy:
* The flag filename is being encrypted and added to the ```files``` list.
* We can list files and get the encrypted flag file name.
* We can encrypt our own file name and calculate the padding.
* We then decrypt the flag file name (we already know the pad), and we ask to decrypt the file.
* We can the flag

We can use this code:
```python
#!/usr/bin/env python

from pwn import *
import base64


def xor_strings(s1, s2):
	s = ''

	for a, b in zip(s1, s2):
		s += chr(ord(a) ^ ord(b))

	return s

r = remote('2018shell1.picoctf.com', 15037)

print r.recvuntil('Please choose:')

log.info('Get flag file')
r.sendline('i')

lines = r.recvuntil('Please choose:').split('\n')
print '\n'.join(lines)

flag_fn = lines[2].strip()
log.info('Flag file: {}'.format(flag_fn))

fn = 'aaaaaaaaaaaaaaaaaaaaaaaaa'
log.info('Encrypting: {}'.format(fn))
r.sendline('n')
r.sendline(fn)
r.sendline('a')

lines = r.recvuntil('Please choose:').split('\n')
print '\n'.join(lines)

share_code = lines[2]

crafted_share_code = base64.b64encode(xor_strings(xor_strings(base64.b64decode(share_code), '{}.txt'.format(fn)), '{}'.format(flag_fn)))

log.info('Sendling: {}'.format(crafted_share_code))
r.sendline('e')
r.sendline(crafted_share_code)
r.sendline('x')

print r.recvall()
```

Flag: picoCTF{alw4ys_4lways_Always_check_int3grity_9d5e42a2}
