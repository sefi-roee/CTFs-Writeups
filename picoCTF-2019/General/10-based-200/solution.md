# Problem
To get truly 1337, you must understand different data encodings, such as hexadecimal or binary. Can you get the flag from this program to prove you are on the way to becoming 1337? Connect with nc 2019shell1.picoctf.com 44303.

## Hints:
I hear python can convert things.

It might help to have multiple windows open

## Solution:

Lets connect:
```bash
2019shell1.picoctf.com 44303

Let us see how data is stored
oven
Please give the 01101111 01110110 01100101 01101110 as a word.
...
you have 45 seconds.....

Input:
```

We need to convert data between bases etc.

After investigation I got this script:
```python
#!/usr/bin/env python

from pwn import *


r = remote('2019shell1.picoctf.com', 44303)

# Challenge 1 - binary string to ASCII
lines = r.recvuntil('Input:\n')

challenge = lines.splitlines()[2].split()
challenge = challenge[challenge.index('the')+1 : challenge.index('as')]

log.info('Got challenge: {}'.format(challenge))

ans = ''.join(map(chr,[int(c, 2) for c in challenge]))

log.info('Send solution: {}'.format(ans))

r.sendline('{}'.format(ans))

# Challenge 2 - octal to ASCII
lines = r.recvuntil('Input:\n')

challenge = lines.splitlines()[0].split()
challenge = challenge[challenge.index('the')+1 : challenge.index('as')]

log.info('Got challenge: {}'.format(challenge))

ans = ''.join(map(chr,[int(c, 8) for c in challenge]))

log.info('Send solution: {}'.format(ans))

r.sendline('{}'.format(ans))

# Challenge 3 - hex to ASCII
lines = r.recvuntil('Input:\n')

challenge = lines.splitlines()[0].split()
challenge = challenge[challenge.index('the')+1 : challenge.index('as')]

log.info('Got challenge: {}'.format(challenge))

ans = challenge[0].decode('hex')

log.info('Send solution: {}'.format(ans))

r.sendline('{}'.format(ans))

print r.recvall()
```

Flag: picoCTF{learning_about_converting_values_b515dfd2}
