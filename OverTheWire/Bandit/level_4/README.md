# Bandit Level 4

```bash
Username: bandit4
Password: pIwrPrtPN36QITSp3EQaw936yaFoFgAB
Server:   bandit.labs.overthewire.org
Port:     2220
```

Lets connect to the server:
```bash
ssh bandit4@bandit.labs.overthewire.org -p2220
```

We need to find the only human-readble file inside ```inhere```.

Lets try:
```bash
bandit4@bandit:~$ file inhere/*
inhere/-file00: data
inhere/-file01: data
inhere/-file02: data
inhere/-file03: data
inhere/-file04: data
inhere/-file05: data
inhere/-file06: data
inhere/-file07: ASCII text
inhere/-file08: data
inhere/-file09: data
```

We need ```-file07```:
```bash
bandit4@bandit:~$ cat inhere/-file07 
koReBOKuIDDepwhWk7jZC0RTdopnAYKh
```

We got the password for the next level: **koReBOKuIDDepwhWk7jZC0RTdopnAYKh**

**A single script is:**
```python
#!/usr/bin/env python

from pwn import *


def main():
    shell = ssh(host='bandit.labs.overthewire.org',
                user='bandit4',
                password='pIwrPrtPN36QITSp3EQaw936yaFoFgAB',
                port=2220
           )

    files = shell['ls inhere'].replace('\n', ' ').split()
    files = [os.path.join(shell.cwd, 'inhere', f) for f in files]

    types = [shell['file ' + f] for f in files]

    index = [i for i, s in enumerate(types) if 'ASCII' in s]

    print shell['cat ' + sh_string(os.path.join(shell.cwd, files[index[0]]))]

if __name__ == "__main__":
    main()
```