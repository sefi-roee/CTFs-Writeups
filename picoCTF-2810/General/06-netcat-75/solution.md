# Problem
Using netcat (nc) will be a necessity throughout your adventure. Can you connect to ```2018shell1.picoctf.com``` at port ```37721``` to get the flag?

## Hints:
nc [tutorial](https://linux.die.net/man/1/nc)

## Solution:

```python
#!/usr/bin/env python

from pwn import *


r = remote('2018shell1.picoctf.com', 37721)

print r.recvall()
```

Flag: picoCTF{NEtcat_iS_a_NEcESSiTy_0b4c4174}
