# Bandit Level 8

```bash
Username: bandit8
Password: cvX2JJa4CFALtqS87jk27qwqGhBM9plV
Server:   bandit.labs.overthewire.org
Port:     2220
```

Lets connect to the server:
```bash
ssh bandit8@bandit.labs.overthewire.org -p2220
```

We can use ```sort``` and ```uniq``` to solve this, Lets try:
```bash
bandit8@bandit:~$ cat data.txt | sort | uniq -c | grep "1 "
      1 UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR
```

We got the password for the next level: **UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR**

**A single script is:**
```python
#!/usr/bin/env python

from pwn import *
from collections import Counter


def main():
    shell = ssh(host='bandit.labs.overthewire.org',
                user='bandit8',
                password='cvX2JJa4CFALtqS87jk27qwqGhBM9plV',
                port=2220
           )

    lines = shell['cat data.txt'].split('\n')
    c = Counter(lines)

    print [i[0] for i in c.iteritems() if i[1] == 1][0]

if __name__ == "__main__":
    main()
```