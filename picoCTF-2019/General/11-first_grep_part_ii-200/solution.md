# Problem
Can you find the flag in /problems/first-grep--part-ii_4_ca16fbcd16c92f0cb1e376a6c188d58f/files on the shell server? Remember to use grep.

## Hints:

grep [tutorial](https://ryanstutorials.net/linuxtutorial/grep.php)

## Solution:

```python
#!/usr/bin/env python

from pwn import *


user = 'RoeeSefi'
pw = 'UTTE9CQN2idX28W'

s = ssh(host='2019shell1.picoctf.com', user=user, password=pw)

s.set_working_directory('/problems/first-grep--part-ii_4_ca16fbcd16c92f0cb1e376a6c188d58f/files')
p = s.run('grep -r picoCTF .')

print p.recv()
```

Flag: picoCTF{grep_r_to_find_this_0e28f3ee}
