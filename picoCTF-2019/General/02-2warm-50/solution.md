# Problem
Can you convert the number 42 (base 10) to binary (base 2)?

## Hints:
Submit your answer in our competition's flag format. For example, if you answer was '11111', you would submit 'picoCTF{11111}' as the flag.

## Solution:

A simple python script:
```python
#!/usr/bin/env python

print 'picoCTF{{{0:b}}}'.format(42)
```

Flag: picoCTF{101010}