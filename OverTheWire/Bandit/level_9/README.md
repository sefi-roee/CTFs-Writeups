# Bandit Level 9

```bash
Username: bandit9
Password: UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR
Server:   bandit.labs.overthewire.org
Port:     2220
```

Lets connect to the server:
```bash
ssh bandit9@bandit.labs.overthewire.org -p2220
```

We can use ```strings``` and ```grep``` to solve this, Lets try:
```bash
bandit9@bandit:~$ strings data.txt | grep =
2========== the
========== password
>t= yP
rV~dHm=
========== isa
=FQ?P\U
=   F[
pb=x
J;m=
=)$=
========== truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk
iv8!=
```

We got the password for the next level: **truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk**

**A single script is:**
```python
#!/usr/bin/env python

from pwn import *
import re


def main():
    shell = ssh(host='bandit.labs.overthewire.org',
                user='bandit9',
                password='UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR',
                port=2220
           )

    lines = shell['cat data.txt'].split('\n')
    lines = [l for l in lines if '===' in l]
    lines = [re.split('=+', l) for l in lines]
    print lines[3][1].strip()

if __name__ == "__main__":
    main()
```