# Problem
To be successful on your mission, you must be able read data represented in different ways, such as hexadecimal or binary. Can you get the flag from this program to prove you are ready? Connect with ```nc 2018shell1.picoctf.com 15853```.

## Hints:
I hear python is a good means (among many) to convert things.

It might help to have multiple windows open

## Solution:

Lets connect:
```bash
nc 2018shell1.picoctf.com 15853

We are going to start at the very beginning and make sure you understand how data is stored.
computer
Please give me the 01100011 01101111 01101101 01110000 01110101 01110100 01100101 01110010 as a word.
To make things interesting, you have 30 seconds.
Input:
```

We need to convert data between bases etc.

After investigation I got this script:
```python
#!/usr/bin/env python

from pwn import *


r = remote('2018shell1.picoctf.com', 15853)

lines = r.recv()
print lines

ans = ''.join([chr(int(x, 2)) for x in lines.split('\n')[-4].split('the')[1].split('as')[0].strip().split()])
print 'Sending: {}'.format(ans)
r.sendline('{}'.format(ans))

lines = r.recv()
print lines

ans = lines.split('\n')[-3].split('the')[1].split('as')[0].strip().decode('hex')
print 'Sending: {}'.format(ans)
r.sendline('{}'.format(ans))

lines = r.recv()
print lines

ans = ''.join([chr(int(x, 8)) for x in lines.split('\n')[-3].split('the')[1].split('as')[0].strip().split()])
print 'Sending: {}'.format(ans)
r.sendline('{}'.format(ans))

print r.recvall()
```

Flag: picoCTF{delusions_about_finding_values_3cc386de}