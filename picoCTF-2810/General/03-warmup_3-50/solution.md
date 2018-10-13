# Problem
What is 0x3D (base 16) in decimal (base 10).

## Hints:
Submit your answer in our competition's flag format. For example, if you answer was '22', you would submit 'picoCTF{22}' as the flag.

## Solution:

A simple python script:
```python
#!/usr/bin/env python

print 'picoCTF{{{}}}'.format(int('0x3D', 16))
```

Flag: picoCTF{61}
