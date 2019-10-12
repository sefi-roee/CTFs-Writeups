# Bandit Level 19

```bash
Username: bandit19
Password: IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x
Server:   bandit.labs.overthewire.org
Port:     2220
```

First we need to connect:
```bash
ssh bandit19@bandit.labs.overthewire.org -p2220
bandit19@bandit:~$ ls -l
total 8
-rwsr-x--- 1 bandit20 bandit19 7296 Oct 16  2018 bandit20-do
bandit19@bandit:~$ file bandit20-do 
bandit20-do: setuid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=8e941f24b8c5cd0af67b22b724c57e1ab92a92a1, not stripped
```

We have a setuid executable with bandit20 as its owner.

Lets try to play with it:
```bash
bandit19@bandit:~$ ./bandit20-do 
Run a command as another user.
  Example: ./bandit20-do id
bandit19@bandit:~$ ./bandit20-do id
uid=11019(bandit19) gid=11019(bandit19) euid=11020(bandit20) groups=11019(bandit19)
bandit19@bandit:~$ ./bandit20-do cat /etc/bandit_pass/bandit20 
GbKksEFF4yrVs6il55v6gwY5aVje5f0j
```

We got the password for the next level: **GbKksEFF4yrVs6il55v6gwY5aVje5f0j**

**A single script is:**
```python
in/env python

from pwn import *


def main():
  shell = ssh(host='bandit.labs.overthewire.org',
            user='bandit19',
            password='IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x',
            port=2220
       )

  p = shell['./bandit20-do cat /etc/bandit_pass/bandit20']
  
  print p

  shell.close()

if __name__ == "__main__":
  main()
```