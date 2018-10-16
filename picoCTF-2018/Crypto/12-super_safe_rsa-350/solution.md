# Problem
Dr. Xernon made the mistake of rolling his own crypto.. Can you find the bug and decrypt the message? Connect with ```nc 2018shell1.picoctf.com 59208```.

## Hints:
Just try the first thing that comes to mind.

## Solution:

Lets connect:
```bash
nc 2018shell1.picoctf.com 59208

c: 7447716830713775626797602562755672388885977436943768936184625367606146075559926
n: 24845538108817092891792374686195248987039492885911767063175060537839533468162539
e: 65537
```

We probably need to decrypt it. n is ~80 digits long, so we can still factorize it in a decent amount of time.

Using [factordb](http://factordb.com/index.php?query=24845538108817092891792374686195248987039492885911767063175060537839533468162539), we get (after few minutes) ```p = ```, ```q = ```.


Decryption now is straight forward:
```python
#!/usr/bin/env python

from pwn import *


MMI = lambda A, n,s=1,t=0,N=0: (n < 2 and t%N or MMI(n, A%n, t, s-A//n*t, N or n),-1)[n<1]

c = 7447716830713775626797602562755672388885977436943768936184625367606146075559926
n = 24845538108817092891792374686195248987039492885911767063175060537839533468162539
e = 65537

p = 147731204717925735267651069208108064837
q = 168180704653810557486377517313556083649647

phi = (p - 1) * (q - 1)
log.info('Calculated phi: {}'.format(phi))

d = MMI(e, phi)
log.info('Calculated d: {}'.format(d))

assert((e * d) % phi == 1)

plain = pow(c, d, n)
log.info('Calculated plaintext: {}'.format(plain))
log.info('In hex: {}'.format(hex(plain)))

log.info('Unhexlified: {}'.format(unhex(hex(plain)[2:]))) # python 2
```

Flag: picoCTF{us3_l@rg3r_pr1m3$_5327}
