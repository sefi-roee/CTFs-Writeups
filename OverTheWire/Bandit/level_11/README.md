# Bandit Level 11

```bash
Username: bandit11
Password: IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR
Server:   bandit.labs.overthewire.org
Port:     2220
```

Lets connect to the server:
```bash
ssh bandit11@bandit.labs.overthewire.org -p2220
```

This is Rot13.

We can use ```tr``` to decrypt the text, Lets try:
```bash
bandit11@bandit:~$ cat data.txt 
Gur cnffjbeq vf 5Gr8L4qetPEsPk8htqjhRK8XSP6x2RHh
bandit11@bandit:~$ cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
The password is 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu
```

We got the password for the next level: **5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu**

**A single script is:**
```python
#!/usr/bin/env python

from pwn import *


def rot13(c):
    assert len(c) == 1

    if 'a' <= c <= 'z':
        return chr(((ord(c) - ord('a') + 13) % 26) + ord('a'))
    elif 'A' <= c <= 'Z':
        return chr(((ord(c) - ord('A') + 13) % 26) + ord('A'))
    else:
        return c

def main():
    shell = ssh(host='bandit.labs.overthewire.org',
                user='bandit11',
                password='IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR',
                port=2220
           )

    text = shell['cat data.txt']
    text = ''.join([rot13(c) for c in text])

    print text

if __name__ == "__main__":
    main()
```