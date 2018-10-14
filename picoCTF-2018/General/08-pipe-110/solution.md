# Problem
During your adventure, you will likely encounter a situation where you need to process data that you receive over the network rather than through a file. Can you find a way to save the output from this program and search for the flag? Connect with ```2018shell1.picoctf.com 34532```.

## Hints:
Remember the flag format is picoCTF{XXXX}

Ever heard of a pipe? No not that kind of pipe... This [kind](http://www.linfo.org/pipes.html)

## Solution:

```bash
#!/usr/bin/bash

nc 2018shell1.picoctf.com 34532 | grep picoCTF
```

Flag: picoCTF{almost_like_mario_b797f2b3}
