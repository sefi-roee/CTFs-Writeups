# Problem
Stego-Saurus hid a message for you in this [image](https://2018shell1.picoctf.com/static/9129761dbc4bf494c47429f85ddf7434/husky.png), can you retreive it?

## Hints:
Maybe you can find an online decoder?

## Solution:

First, we download the image
```bash
wget https://2018shell1.picoctf.com/static/9129761dbc4bf494c47429f85ddf7434/husky.png
```

Now, lets use pulic tools to obtain the flag, try [zsteg](https://github.com/zed-0xff/zsteg).
```bash
./zsteg/bin/zsteg ./husky.png

b1,r,lsb,xy         .. text: "^5>c[rvyzrf@"
b1,rgb,lsb,xy       .. text: "picoCTF{r34d1ng_b37w33n_7h3_by73s}"
b1,abgr,msb,xy      .. file: PGP\011Secret Sub-key -
b2,g,msb,xy         .. text: "ADTU@PEPA"
b3,abgr,msb,xy      .. text: "t@Wv!Wt\tGtA"
b4,r,msb,xy         .. text: "0Tt7F3Saf"
b4,g,msb,xy         .. text: "2g'uV `3"
b4,b,lsb,xy         .. text: "##3\"TC%\"2f"
b4,b,msb,xy         .. text: " uvb&b@f!"
b4,rgb,lsb,xy       .. text: "1C5\"RdWD"
b4,rgb,msb,xy       .. text: "T E2d##B#VuQ`"
b4,bgr,lsb,xy       .. text: "A%2RTdGG"
b4,bgr,msb,xy       .. text: "EPD%4\"c\"#CUVqa "
b4,rgba,lsb,xy      .. text: "?5/%/d_tO"
b4,abgr,msb,xy      .. text: "EO%O#/c/2/C_e_q"
```

*Please tell me if you know how to solve it without using tools*

Flag: picoCTF{r34d1ng_b37w33n_7h3_by73s}
