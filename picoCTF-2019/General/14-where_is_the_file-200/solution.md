# Problem
I've used a super secret mind trick to hide this file. Maybe something lies in /problems/where-is-the-file_0_cc140a3ba634658b98122a1954c1316a.

## Hints:

What command can see/read files?

What's in the manual page of ls?

## Solution:

Just a hidden file...

```python
#!/usr/bin/env python

from pwn import *


user = 'RoeeSefi'
pw = 'UTTE9CQN2idX28W'

s = ssh(host = '2019shell1.picoctf.com', user=user, password=pw)
s.set_working_directory('/problems/where-is-the-file_0_cc140a3ba634658b98122a1954c1316a')
p = s.run('ls -a')

files = p.recv().split()

log.info('Found: {}'.format(files))

p = s.run('cat {}'.format(files[-1]))

print p.recvall()
```

Flag: picoCTF{w3ll_that_d1dnt_w0RK_b2dab472}
