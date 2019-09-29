# Problem
Using netcat (nc) is going to be pretty important. Can you connect to 2019shell1.picoctf.com at port 32225 to get the flag?

## Hints:
nc [tutorial](https://linux.die.net/man/1/nc)

## Solution:

```python
#!/usr/bin/env python

from pwn import *

r = remote('2019shell1.picoctf.com', 32225)

print r.recvall()
```

Flag: picoCTF{nEtCat_Mast3ry_b1d25ece}
