# Problem
This [.tar file](https://2019shell1.picoctf.com/static/8694f84879d3b7c0dcf775930f4665fc/1000.tar) got tarred alot. Also available at /problems/like1000_0_369bbdba2af17750ddf10cc415672f1c.

## Hints:

Try and script this, it'll save you alot of time

## Solution:

First, let's download the file:
```bash
wget https://2019shell1.picoctf.com/static/8694f84879d3b7c0dcf775930f4665fc/1000.tar
```

It's just a tarball we need to extract from over and over.

Using a simple script:
```bash
for i in $(seq 1000 -1 1); do tar -xf ${i}.tar; rm ${i}.tar; done
```

![flag](./flag.png)

Flag: picoCTF{l0t5_0f_TAR5}
