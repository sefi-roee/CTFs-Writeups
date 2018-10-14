# Problem
This one is a little bit harder. Can you find the flag in /problems/grep-2_3_826f886f547acb8a9c3fccb030e8168d/files on the shell server? Remember, grep is your friend.

## Hints:
grep [tutorial](https://ryanstutorials.net/linuxtutorial/grep.php)

## Solution:

Now, we dont know where to find the flag, We can use ```find```
```python
#!/usr/bin/env python

from pwn import *


user = 'roeesefi'
pw = '123123'

s = ssh(host = '2018shell1.picoctf.com', user=user, password=pw)
bash = s.process('bash')

bash.sendline('find /problems/grep-2_3_826f886f547acb8a9c3fccb030e8168d/files -type f -exec cat {} \; | grep picoCTF')

print bash.recvline()
```

Flag: picoCTF{grep_r_and_you_will_find_556620f7}
