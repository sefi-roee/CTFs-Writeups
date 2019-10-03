# Problem
Sometimes you need to handle process data outside of a file. Can you find a way to keep the output from this program and search for the flag? Connect to 2019shell1.picoctf.com 21550.

## Hints:

Remember the flag format is picoCTF{XXXX}

What's a pipe? No not that kind of pipe... This [kind](http://www.linfo.org/pipes.html)

## Solution:

Easy, a simple ```grep```:
```bash
nc 2019shell1.picoctf.com 21550 | grep picoCTF
```

Flag: picoCTF{digital_plumb3r_8f946c69}
