# Bandit Level 3

```bash
Username: bandit3
Password: UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK
Server:   bandit.labs.overthewire.org
Port:     2220
```

Lets connect to the server:
```bash
ssh bandit3@bandit.labs.overthewire.org -p2220
```

Using:
```bash
ls -l
```

We get:
```bash
bandit3@bandit:~$ ls -l
total 4
drwxr-xr-x 2 root root 4096 Oct 16  2018 inhere
```

Lets take a look inside:
```bash
bandit3@bandit:~$ ls -l inhere/
total 0
bandit3@bandit:~$ ls -la inhere/
total 12
drwxr-xr-x 2 root    root    4096 Oct 16  2018 .
drwxr-xr-x 3 root    root    4096 Oct 16  2018 ..
-rw-r----- 1 bandit4 bandit3   33 Oct 16  2018 .hidden
```
And the password is:
```bash
bandit3@bandit:~$ cat inhere/.hidden 
pIwrPrtPN36QITSp3EQaw936yaFoFgAB
```

We got the password for the next level: **pIwrPrtPN36QITSp3EQaw936yaFoFgAB**

**A single script is:**
```python
#!/usr/bin/env python

from pwn import *


def main():
    shell = ssh(host='bandit.labs.overthewire.org',
                user='bandit3',
                password='UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK',
                port=2220
           )

    hidden_file = shell['ls -a inhere'].split()[-1]

    print shell['cat ' + sh_string(os.path.join(shell.cwd, 'inhere', hidden_file))]

if __name__ == "__main__":
    main()
```