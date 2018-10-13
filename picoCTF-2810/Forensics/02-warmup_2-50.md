# Problem
Hmm for some reason I can't open this [PNG](https://2018shell1.picoctf.com/static/b96c236db4c32ed47e9958c7e461b3c4/flag.png)? Any ideas?


## Hints:
How do operating systems know what kind of file it is? (It's not just the ending!

Make sure to submit the flag as picoCTF{XXXXX}

## Solution:

First we try to open the file:
```bash
xdg-open flag.png
```

We get an error.

Lets investigate:
```bash
file flag.jpg
flag.png: JPEG image data, JFIF standard 1.01, resolution (DPI), density 75x75, segment length 16, baseline, precision 8, 909x190, frames 3
```

We can just rename and open it:
```bash
mv flag.png flag.jpg
xdg-open flag.jpg
```
