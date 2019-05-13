# Bandit Level 6

```bash
Username: bandit6
Password: DXjZPULLxYr17uwoI01bNLQbtFemEgo7
Server:   bandit.labs.overthewire.org
Port:     2220
```

Lets connect to the server:
```bash
ssh bandit6@bandit.labs.overthewire.org -p2220
```

We need to find a file **somewhere on the server**, which have these properties:
* owned by user bandit7
* owned by group bandit6
* 33 bytes in size

Lets try:
```bash
bandit6@bandit:~$ find / -size 33c -user bandit7 -group bandit6 2>&1 | grep -v "find:"
/var/lib/dpkg/info/bandit7.password
bandit6@bandit:~$ cat /var/lib/dpkg/info/bandit7.password
HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs
```

We got the password for the next level: **HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs**

**A single script is:**
```python
#!/usr/bin/env python

from pwn import *


def main():
    shell = ssh(host='bandit.labs.overthewire.org',
                user='bandit6',
                password='DXjZPULLxYr17uwoI01bNLQbtFemEgo7',
                port=2220
           )

    file = [f for f in shell['find / -size 33c -user bandit7 -group bandit6 2>&1 | grep -v "find:"'].split('\n') if 'find: ' not in f][0]

    print shell['cat ' + sh_string(os.path.join(shell.cwd, file))]

if __name__ == "__main__":
    main()
```