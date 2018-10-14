# Problem
If I told you your grade was 0x41 in hexadecimal, what would it be in ASCII?

## Hints:
Submit your answer in our competition's flag format. For example, if you answer was 'hello', you would submit 'picoCTF{hello}' as the flag.

## Solution:

A simple python script:
```python
#!/usr/bin/env python

print 'picoCTF{{{}}}'.format('41'.decode('hex'))
```

Flag: picoCTF{A}
