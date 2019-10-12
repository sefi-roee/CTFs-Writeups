# Bandit Level 14

```bash
Username: bandit14
Password: 4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e
Server:   bandit.labs.overthewire.org
Port:     2220
```

## Level Goal
The password for the next level can be retrieved by submitting the password of the current level to port 30000 on localhost.

Lets do it:
```bash
ssh bandit13@bandit.labs.overthewire.org -p2220
echo 4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e | nc localhost 30000
Correct!
BfMYroe26WYalil77FoDi9qh59eK5xNr
```

Nice!

We got the password for the next level: **BfMYroe26WYalil77FoDi9qh59eK5xNr**

**A single script is:**
```python
#!/usr/bin/env python

from pwn import *


def main():
  shell = ssh(host='bandit.labs.overthewire.org',
            user='bandit14',
            password='4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e',
            port=2220
       )

  print shell['cat /etc/bandit_pass/bandit14 | nc localhost 30000']

if __name__ == "__main__":
  main()
```