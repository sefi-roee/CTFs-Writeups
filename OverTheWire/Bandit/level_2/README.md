# Bandit Level 2

```bash
Username: bandit2
Password: CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9
Server:   bandit.labs.overthewire.org
Port:     2220
```

Lets connect to the server:
```bash
ssh bandit2@bandit.labs.overthewire.org -p2220
```

Using:
```bash
ls
```

We get:
```bash
bandit2@bandit:~$ ls
spaces in this filename
```

In order to pring its contents, we can:
* enclose the filename in parentheses ```cat "spaces in this filename"```
* use escape symbol ```cat spaces\ in\ this\ filename```

And the password is:
```bash
bandit2@bandit:~$ cat spaces\ in\ this\ filename 
UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK
bandit2@bandit:~$ cat "spaces in this filename"
UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK
```

We got the password for the next level: **UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK**

**A single script is:**
```python
#!/usr/bin/env python

from pwn import *


def main():
  shell = ssh(host='bandit.labs.overthewire.org',
            user='bandit2',
            password='CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9',
            port=2220
       )

  file_in_dir = shell['ls']

  print shell['cat ' + sh_string(os.path.join(shell.cwd, file_in_dir))]

if __name__ == "__main__":
  main()
```