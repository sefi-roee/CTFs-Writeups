# Problem
Theres something in the [building](https://2019shell1.picoctf.com/static/aec3861fc4d5bce4d39dc0db196426de/buildings.png). Can you retrieve the flag?

## Hints:
There is data encoded somewhere, there might be an online decoder

## Solution:

First, let's download the file:
```bash
wget https://2019shell1.picoctf.com/static/aec3861fc4d5bce4d39dc0db196426de/buildings.png
```

Let's take a look:
![buildings](./buildings.png)

Now, lets use some public tools to obtain the flag, try [zsteg](https://github.com/zed-0xff/zsteg).
```bash
../../../tools/zsteg/bin/zsteg ./buildings.png 

b1,r,lsb,xy         .. text: "^5>R5YZrG"
b1,rgb,lsb,xy       .. text: "picoCTF{h1d1ng_1n_th3_b1t5}"
b1,abgr,msb,xy      .. file: PGP\011Secret Sub-key -
b2,b,lsb,xy         .. text: "XuH}p#8Iy="
b3,abgr,msb,xy      .. text: "t@Wp-_tH_v\r"
b4,r,lsb,xy         .. text: "fdD\"\"\"\" "
b4,r,msb,xy         .. text: "%Q#gpSv0c05"
b4,g,lsb,xy         .. text: "fDfffDD\"\""
b4,g,msb,xy         .. text: "f\"fff\"\"DD"
b4,b,lsb,xy         .. text: "\"$BDDDDf"
b4,b,msb,xy         .. text: "wwBDDDfUU53w"
b4,rgb,msb,xy       .. text: "dUcv%F#A`"
b4,bgr,msb,xy       .. text: " V\"c7Ga4"
b4,abgr,msb,xy      .. text: "gOC_$_@o"
```

There it is!

Flag: picoCTF{h1d1ng_1n_th3_b1t5}
