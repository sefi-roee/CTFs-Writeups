# Bandit Level 21

```bash
Username: bandit21
Password: gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr
Server:   bandit.labs.overthewire.org
Port:     2220
```

First we need to connect:
```bash
ssh bandit21@bandit.labs.overthewire.org -p2220
```

Lets take a look at the cronjob:
```bash
bandit21@bandit:~$ ls -l /etc/cron.d/
total 12
-rw-r--r-- 1 root root 120 Oct 16  2018 cronjob_bandit22
-rw-r--r-- 1 root root 122 Oct 16  2018 cronjob_bandit23
-rw-r--r-- 1 root root 120 Oct 16  2018 cronjob_bandit24
bandit21@bandit:~$ cat /etc/cron.d/cronjob_bandit22 
@reboot bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
* * * * * bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
bandit21@bandit:~$ ls -l /usr/bin/cronjob_bandit2*
-rwxr-x--- 1 bandit22 bandit21 130 Oct 16  2018 /usr/bin/cronjob_bandit22.sh
-rwxr-x--- 1 bandit23 bandit22 211 Oct 16  2018 /usr/bin/cronjob_bandit23.sh
-rwxr-x--- 1 bandit24 bandit23 253 Oct 16  2018 /usr/bin/cronjob_bandit24.sh
bandit21@bandit:~$ cat /usr/bin/cronjob_bandit22.sh 
#!/bin/bash
chmod 644 /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
cat /etc/bandit_pass/bandit22 > /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
```

Every minute the password for level22 is being written to ```/tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv```.

Lets print it:
```bash
bandit21@bandit:~$ cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI
```

We got the password for the next level: **Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI**

**A single script is:**
```python
#!/usr/bin/env python

from pwn import *


def main():
  shell = ssh(host='bandit.labs.overthewire.org',
            user='bandit21',
            password='gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr',
            port=2220
       )

  
  p = shell['cat /etc/cron.d/cronjob_bandit22']

  bash_script = p.split('\n')[1].split()[-3]
  log.info('Found bash script: {}'.format(bash_script))

  p = shell['cat {}'.format(bash_script)]

  pass_file = p.split('\n')[2].split()[-1]
  log.info('Found password file: {}'.format(pass_file))

  p = shell['cat {}'.format(pass_file)]

  print p

if __name__ == "__main__":
  main()
```