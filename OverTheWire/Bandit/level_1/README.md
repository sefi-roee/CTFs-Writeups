# Bandit Level 0

```bash
Username: bandit1
Password: boJ9jbbUNNfktd78OOpsqOltutMc3MY1
Server:   bandit.labs.overthewire.org
Port:     2220
```

Lets connect to the server:
```bash
ssh bandit1@bandit.labs.overthewire.org -p2220
```

Using:
```bash
ls
```

We get:
```bash
bandit1@bandit:~$ ls
-
```

We need to print the content of the file: -.

Unfortunately the symbol - in ```cat``` means "read from standard input".

```
CAT(1)                                                                                       User Commands                                                                                      CAT(1)

NAME
       cat - concatenate files and print on the standard output

SYNOPSIS
       cat [OPTION]... [FILE]...

DESCRIPTION
       Concatenate FILE(s) to standard output.

       With no FILE, or when FILE is -, read standard input.
```

To overcome this, we can use a full path:
```bash
cat ./-

bandit1@bandit:~$ cat ./-
CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9
```

We got the password for the next level: **CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9**

**A single script is:**
```python
#!/usr/bin/env python

from pwn import *


def main():
  shell = ssh(host='bandit.labs.overthewire.org',
            user='bandit1',
            password='boJ9jbbUNNfktd78OOpsqOltutMc3MY1',
            port=2220
       )

  file_in_dir = shell['ls']

  print shell['cat ' + os.path.join(shell.cwd, file_in_dir)]

if __name__ == "__main__":
  main()
```