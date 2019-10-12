# Bandit Level 20

```bash
Username: bandit20
Password: GbKksEFF4yrVs6il55v6gwY5aVje5f0j
Server:   bandit.labs.overthewire.org
Port:     2220
```

First we need to connect:
```bash
ssh bandit20@bandit.labs.overthewire.org -p2220
```

We just need to create network server which upon connection sends the contents of /etc/bandit_pass/bandit20.

Then we will used the setuid file with our server and get the password.
```bash
bandit20@bandit:~$ cat /etc/bandit_pass/bandit20 | nc -l -p 32123 & ./suconnect 32123
[6] 10407
Read: GbKksEFF4yrVs6il55v6gwY5aVje5f0j
Password matches, sending next password
gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr
[5]-  Done                    cat /etc/bandit_pass/bandit20 | nc -l -p 32123
```

We got the password for the next level: **gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr**

**A single script is:**
```python
#!/usr/bin/env python

from pwn import *


def main():
  shell = ssh(host='bandit.labs.overthewire.org',
            user='bandit20',
            password='GbKksEFF4yrVs6il55v6gwY5aVje5f0j',
            port=2220
       )

  s = shell.process('nc -l -p 32123 < /etc/bandit_pass/bandit20', shell=True)
  l = shell.process('./suconnect 32123', shell=True)

  print s.recv()

  shell.close()

if __name__ == "__main__":
  main()
```