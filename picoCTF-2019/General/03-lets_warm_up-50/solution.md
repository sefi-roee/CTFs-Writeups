# Problem
If I told you a word started with 0x70 in hexadecimal, what would it start with in ASCII?

## Hints:
Submit your answer in our competition's flag format. For example, if you answer was 'hello', you would submit 'picoCTF{hello}' as the flag.

## Solution:

A simple python script:
```python
#!/usr/bin/env python

print 'picoCTF{{{}}}'.format('70'.decode('hex'))
```

Flag: picoCTF{p}