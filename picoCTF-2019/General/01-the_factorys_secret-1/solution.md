# Problem
There appear to be some mysterious glyphs hidden inside this [abandoned factory](https://2019game.picoctf.com/game)... I wonder what would happen if you collected them all?

    ## Hints:
Submit your answer in our competition's flag format. For example, if you answer was 'hello', you would submit 'picoCTF{hello}' as the flag.

## Solution:

A simple python script:
```python
#!/usr/bin/env python

print 'picoCTF{{{}}}'.format('41'.decode('hex'))
```

Flag: picoCTF{A}