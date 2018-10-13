# Problem
Crpyto can often be done by hand, here's a message you got from a friend, ```llkjmlmpadkkc``` with the key of ```thisisalilkey```. Can you use this [table](https://2018shell1.picoctf.com/static/7e80900bd1afae76845553d895e271e1/table.txt) to solve it?.

## Hints:
Submit your answer in our competition's flag format. For example, if you answer was 'hello', you would submit 'picoCTF{HELLO}' as the flag.

Please use all caps for the message.

## Solution:

First we need to download the table:
```bash
wget https://2018shell1.picoctf.com/static/7e80900bd1afae76845553d895e271e1/table.txt
```

And then we open the file
```python
#!/usr/bin/env python

message = 'llkjmlmpadkkc'
key = 'thisisalilkey'

s = ''
for m,k in zip(message, key):
	s += chr((ord(m) - ord(k) + 26) % 26 + ord('a'))

print 'picoCTF{{{}}}'.format(s.upper())
```

Flag: picoCTF{SECRETMESSAGE}
