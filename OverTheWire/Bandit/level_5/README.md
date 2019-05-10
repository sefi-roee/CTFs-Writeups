# Bandit Level 5

```bash
Username: bandit5
Password: koReBOKuIDDepwhWk7jZC0RTdopnAYKh
Server:   bandit.labs.overthewire.org
Port:     2220
```

Lets connect to the server:
```bash
ssh bandit5@bandit.labs.overthewire.org -p2220
```

We need to find a file inside ```inhere```, which have these properties:
* human-readable
* 1033 bytes in size
* not executable

Lets try:
```bash
bandit5@bandit:~$ find ./inhere/ -size 1033c ! -executable -exec file {} +
./inhere/maybehere07/.file2: ASCII text, with very long lines
bandit5@bandit:~$ cat ./inhere/maybehere07/.file2 
DXjZPULLxYr17uwoI01bNLQbtFemEgo7
```

We got the password for the next level: **DXjZPULLxYr17uwoI01bNLQbtFemEgo7**

**A single script is:**
```python
#!/usr/bin/env python

from pwn import *


def main():
    shell = ssh(host='bandit.labs.overthewire.org',
                user='bandit5',
                password='koReBOKuIDDepwhWk7jZC0RTdopnAYKh',
                port=2220
           )

    file = shell['find ' + os.path.join(shell.cwd, 'inhere') + ' -size 1033c ! -executable -exec file {} + | grep ASCII'].replace('\n', ' ').split()[0].replace(':', '')

    print shell['cat ' + sh_string(os.path.join(shell.cwd, file))]

if __name__ == "__main__":
    main()
```