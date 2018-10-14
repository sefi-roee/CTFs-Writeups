# Problem
Sometimes you have to configure environment variables before executing a program. Can you find the flag we've hidden in an environment variable on the shell server?

## Hints:
unix [env](https://www.tutorialspoint.com/unix/unix-environment.htm)

## Solution:

We just need to login to the remote shell, and look for relevant environment variables.

There is one named SECRET_FLAG

Using a simple script:
```python
#!/usr/bin/env python

from pwn import *


user = 'roeesefi'
pw = '123123'

s = ssh(host = '2018shell1.picoctf.com', user=user, password=pw)
r = s.shell()

r.sendline('env')

r.recvuntil('SECRET_FLAG=')
print r.recvline()
```

Flag: picoCTF{eNv1r0nM3nT_v4r14Bl3_fL4g_3758492}