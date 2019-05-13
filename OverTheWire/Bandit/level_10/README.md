# Bandit Level 10

```bash
Username: bandit10
Password: truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk
Server:   bandit.labs.overthewire.org
Port:     2220
```

Lets connect to the server:
```bash
ssh bandit10@bandit.labs.overthewire.org -p2220
```

We can use ```base64``` to solve this, Lets try:
```bash
bandit10@bandit:~$ cat data.txt 
VGhlIHBhc3N3b3JkIGlzIElGdWt3S0dzRlc4TU9xM0lSRnFyeEUxaHhUTkViVVBSCg==
bandit10@bandit:~$ cat data.txt | base64 -d
The password is IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR
```

We got the password for the next level: **IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR**

**A single script is:**
```python
#!/usr/bin/env python

from pwn import *


def main():
    shell = ssh(host='bandit.labs.overthewire.org',
                user='bandit10',
                password='truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk',
                port=2220
           )

    lines = shell['cat data.txt']
    d = b64d(lines)

    print d

if __name__ == "__main__":
    main()
```