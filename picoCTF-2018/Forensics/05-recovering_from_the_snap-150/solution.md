# Problem
There used to be a bunch of [animals](https://2018shell1.picoctf.com/static/5d982298cdb725f9e23c6f25c8a37411/animals.dd) here, what did Dr. Xernon do to them?

## Hints:
Some files have been deleted from the disk image, but are they really gone?

## Solution:

First, we download the file
```bash
wget https://2018shell1.picoctf.com/static/5d982298cdb725f9e23c6f25c8a37411/animals.dd
```

Lets try to mount it:
```bash
file animals.dd

animals.dd: DOS/MBR boot sector, code offset 0x3c+2, OEM-ID "mkfs.fat", sectors/cluster 4, root entries 512, sectors 20480 (volumes <=32 MB), Media descriptor 0xf8, sectors/FAT 20, sectors/track 32, heads 64, serial number 0x9b664dde, unlabeled, FAT (16 bit)

mkdir ./mnt
mount ./animals.dd ./mnt
ls mnt
```

Only 4 photos, which wont help us.

Lets try to restore deleted photos, use [photorec])(https://www.cgsecurity.org/wiki/PhotoRec)

```bash
apt install testdisk/artful
photorec ./animals.dd
```

Follow instructions and restore 8 photos.

The flag is in the last one.

![restored flag file](./flag.jpg)

Flag: picoCTF{th3_5n4p_happ3n3d}
