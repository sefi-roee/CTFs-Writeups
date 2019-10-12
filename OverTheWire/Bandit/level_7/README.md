# Bandit Level 7

```bash
Username: bandit7
Password: HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs
Server:   bandit.labs.overthewire.org
Port:     2220
```

Lets connect to the server:
```bash
ssh bandit7@bandit.labs.overthewire.org -p2220
```

This one is easy, Lets try:
```bash
bandit7@bandit:~$ cat data.txt | grep millionth
millionth   cvX2JJa4CFALtqS87jk27qwqGhBM9plV
```

We got the password for the next level: **cvX2JJa4CFALtqS87jk27qwqGhBM9plV**

**A single script is:**
```python
#!/usr/bin/env python

from pwn import *


def main():
    shell = ssh(host='bandit.labs.overthewire.org',
                user='bandit7',
                password='HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs',
                port=2220
           )

    line = shell['cat data.txt | grep millionth']

    print line.split()[1]

if __name__ == "__main__":
    main()
```