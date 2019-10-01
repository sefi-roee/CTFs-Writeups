# Problem
This is a really weird text file [TXT](https://2019shell1.picoctf.com/static/45886ed4b6d5d1dc74c4944fcf4b4041/flag.txt)? Can you find the flag?

## Hints:
How do operating systems know what kind of file it is? (It's not just the ending!

Make sure to submit the flag as picoCTF{XXXXX}

## Solution:

First, let's download the file:
```bash
wget https://2019shell1.picoctf.com/static/45886ed4b6d5d1dc74c4944fcf4b4041/flag.txt
```

Let's check the file's type:
```bash
file flag.txt 

flag.txt: PNG image data, 1697 x 608, 8-bit/color RGB, non-interlaced
```

It is a PNG

```bash
mv flag.txt flag.png
```

Let's take a look:
![flag](./flag.png)

Flag: picoCTF{now_you_know_about_extensions}
