# Problem
James Brahm, James Bond's less-franchised cousin, has left his secure communication with HQ running, but we couldn't find a way to steal his agent identification code. Can you? Conect with ```nc 2018shell1.picoctf.com 30399```. [Source](https://2018shell1.picoctf.com/static/0cf0cf189f87fd142d6ddfc70af5ed3a/spy_terminal_no_flag.py).

## Hints:
What mode is being used?

## Solution:

Lets take a look at the source:
```python
#!/usr/bin/python2 -u
from Crypto.Cipher import AES

agent_code = """flag"""

def pad(message):
    if len(message) % 16 != 0:
        message = message + '0'*(16 - len(message)%16 )
    return message

def encrypt(key, plain):
    cipher = AES.new( key.decode('hex'), AES.MODE_ECB )
    return cipher.encrypt(plain).encode('hex')

welcome = "Welcome, Agent 006!"
print welcome

sitrep = raw_input("Please enter your situation report: ")
message = """Agent,
Greetings. My situation report is as follows:
{0}
My agent identifying code is: {1}.
Down with the Soviets,
006
""".format( sitrep, agent_code )

message = pad(message)
print encrypt( """key""", message )
```

We see that the mode of operation is [ECB](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Electronic_Codebook_(ECB)).

Same plain blocks being encrypted to the same cipher blocks.

First, lets calculate the length of the flag (the idea is to search for a flag length which produces cipher with the same padding length as in the remote server):
```python
#!/usr/bin/env python

from Crypto.Cipher import AES
from pwn import *
import sys


context.log_level = 'error'

def pad(message):
    if len(message) % 16 != 0:
        message = message + '0'*(16 - len(message)%16 )
    return message

def encrypt(key, plain):
    cipher = AES.new( key.decode('hex'), AES.MODE_ECB )
    
    return cipher.encrypt(plain).encode('hex')

def decrypt(key, cipher):
    cipher = AES.new( key.decode('hex'), AES.MODE_ECB )

    return cipher.decrypt(cipher).encode('hex')

message = """Agent,
Greetings. My situation report is as follows:
{0}
My agent identifying code is: {1}.
Down with the Soviets,
006
"""

flag_length = 1
while True:
	log.info('Try flag length: {}'.format(flag_length))

	for l in range(1, 16 + 1):
		log.info('Check for name length: {}'.format(l))
		name = 'A' * l

		r = remote('2018shell1.picoctf.com', 30399)

		r.recvuntil('Please enter your situation report:')

		r.sendline('{}'.format(name))

		ciphertext = r.recvall()[:-1].strip()

		expected_length = len(encrypt('AA' * 16, pad(message.format(name, 'X' * flag_length))))

		if expected_length != len(ciphertext):
			flag_length += 1

			break

	else:
		print 'Flag length: {}'.format(flag_length)

		break
```

We got ```38```.

Since we can control the length of the "situation", we can control the alignment of the flag in the message, and we can iterate bytes one after one.

This is the pattern of messages:
> Flag length is: 38 (try encrypting messages, python script get_flag_length.py)

> Message is:
> "Agent,\nGreetings" + ". My situation r" + "eport is as foll" + ("ows:\n" + <11 from name>) + (<16 - rest of name> + ) + "\nMy agent identi" + "fying code is: {1}.\nDown with the Soviets,\n006\n"

> Block 5 (6th) and block 7 (8th) must be equal, when we guess first byte of flag, we check "p".

Using this script:
```python
#!/usr/bin/env python

from Crypto.Cipher import AES
from pwn import *
import string


def xor_strings(a, b):
	s = ''

	for aa, bb in zip(a, b):
		s += chr(ord(aa) ^ ord(bb))

	return s.encode('hex')

flag = ''

ll = 480

while True:
	for c in string.ascii_lowercase + string.digits + string.punctuation + string.ascii_uppercase:
		r = remote('2018shell1.picoctf.com', 30399, level='error')

		r.recvuntil('Please enter your situation report:')
		name = 'A' * 11 + "fying code is: {}{}".format(flag, c)[-16:] + 'B' * (48 - len(flag))
		r.sendline('{}'.format(name)) # 9 to complete block, 16 full block

		ciphertext = r.recvall()[:-1].strip()

		try:
			assert len(ciphertext) == ll
		except AssertionError:
			ll -= 32

		ciphertext = ciphertext
		blocks = [ciphertext[i:i + 32] for i in range(0, len(ciphertext), 32)]
		n_blocks = len(blocks)

		if blocks[4] == blocks[9]:
			flag += c

			log.info('Partial flag: {}'.format(flag))

			r.close()

			break

		r.close()

	else:
		log.info('Exiting, final flag: {}'.format(flag))

		break
```

We get:
```
[*] Partial flag: p
[*] Partial flag: pi
[*] Partial flag: pic
[*] Partial flag: pico
[*] Partial flag: picoC
[*] Partial flag: picoCT
[*] Partial flag: picoCTF
[*] Partial flag: picoCTF{
[*] Partial flag: picoCTF{@
[*] Partial flag: picoCTF{@g
[*] Partial flag: picoCTF{@g3
[*] Partial flag: picoCTF{@g3n
[*] Partial flag: picoCTF{@g3nt
[*] Partial flag: picoCTF{@g3nt6
[*] Partial flag: picoCTF{@g3nt6_
[*] Partial flag: picoCTF{@g3nt6_1
[*] Partial flag: picoCTF{@g3nt6_1$
[*] Partial flag: picoCTF{@g3nt6_1$_
[*] Partial flag: picoCTF{@g3nt6_1$_t
[*] Partial flag: picoCTF{@g3nt6_1$_th
[*] Partial flag: picoCTF{@g3nt6_1$_th3
[*] Partial flag: picoCTF{@g3nt6_1$_th3_
[*] Partial flag: picoCTF{@g3nt6_1$_th3_c
[*] Partial flag: picoCTF{@g3nt6_1$_th3_c0
[*] Partial flag: picoCTF{@g3nt6_1$_th3_c00
[*] Partial flag: picoCTF{@g3nt6_1$_th3_c00l
[*] Partial flag: picoCTF{@g3nt6_1$_th3_c00l3
[*] Partial flag: picoCTF{@g3nt6_1$_th3_c00l3$
[*] Partial flag: picoCTF{@g3nt6_1$_th3_c00l3$t
[*] Partial flag: picoCTF{@g3nt6_1$_th3_c00l3$t_
[*] Partial flag: picoCTF{@g3nt6_1$_th3_c00l3$t_8
[*] Partial flag: picoCTF{@g3nt6_1$_th3_c00l3$t_81
[*] Partial flag: picoCTF{@g3nt6_1$_th3_c00l3$t_810
[*] Partial flag: picoCTF{@g3nt6_1$_th3_c00l3$t_8107
[*] Partial flag: picoCTF{@g3nt6_1$_th3_c00l3$t_81077
[*] Partial flag: picoCTF{@g3nt6_1$_th3_c00l3$t_810774
[*] Partial flag: picoCTF{@g3nt6_1$_th3_c00l3$t_8107740
[*] Partial flag: picoCTF{@g3nt6_1$_th3_c00l3$t_8107740}
[*] Partial flag: picoCTF{@g3nt6_1$_th3_c00l3$t_8107740}.
[*] Exiting, final flag: picoCTF{@g3nt6_1$_th3_c00l3$t_8107740}.
```

Flag: picoCTF{@g3nt6_1$_th3_c00l3$t_8107740}
