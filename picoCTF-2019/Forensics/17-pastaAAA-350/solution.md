# Problem
This [pasta](https://2019shell1.picoctf.com/static/5d7af6690ab5672fa7a6caca6d4a48cc/ctf.png) is up to no good. There MUST be something behind it.

## Hints:

## Solution:

First, let's download the file:
```bash
wget https://2019shell1.picoctf.com/static/5d7af6690ab5672fa7a6caca6d4a48cc/ctf.png
```

We have this image of pasta:

![ctf](./ctf.png)

Using [stegSolve](https://github.com/zardus/ctf-tools/tree/master/stegsolve) and walking through the bitplains, we get this in `Red plain 1`:

![red_plain_1](./red_plain_1.bmp)

Flag: picoCTF{pa$ta_1s_lyf3}
