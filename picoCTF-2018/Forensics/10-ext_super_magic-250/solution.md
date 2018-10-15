# Problem
We salvaged a ruined Ext SuperMagic II-class mech recently and pulled the [filesystem](https://2018shell1.picoctf.com/static/b9ff30ec03a9007fb1b1cd6ae15fae84/ext-super-magic.img) out of the black box. It looks a bit corrupted, but maybe there's something interesting in there. You can also find it in /problems/ext-super-magic_1_c544657e659accef770d3f2bc8384a8c on the shell server.

## Hints:
Are there any [tools](https://en.wikipedia.org/wiki/Fsck) for diagnosing corrupted filesystems? What do they say if you run them on this one?

How does a linux machine know what [type](https://www.garykessler.net/library/file_sigs.html) of file a [file](https://linux.die.net/man/1/file) is?

You might find this [doc](http://www.nongnu.org/ext2-doc/ext2.html) helpful.

Be careful with [endianness](https://en.wikipedia.org/wiki/Endianness) when making edits.

Once you've fixed the corruption, you can use /sbin/[debugfs](https://linux.die.net/man/8/debugfs) to pull the flag file out.

## Solution:

First, we download the filesystem and try to mount it
```bash
wget https://2018shell1.picoctf.com/static/b9ff30ec03a9007fb1b1cd6ae15fae84/ext-super-magic.img
mkdir mnt
sudo mount ./ext-super-magic.img ./mnt

mount: /home/roee/CTFs-Writeups/picoCTF-2018/Forensics/10-ext_super_magic-250/mnt: wrong fs type, bad option, bad superblock on /dev/loop0, missing codepage or helper program, or other error.

debugfs ./ext-super-magic.img 

debugfs 1.43.5 (04-Aug-2017)
Checksum errors in superblock!  Retrying...

./ext-super-magic.img: Bad magic number in super-block while opening filesystem
```

Bad superblock.
Lets try to create such superblock and compare:
```bash
cp ext-super-magic.img ext-super-magic-fixed.img
mke2fs ext-super-magic-fixed.img
colordiff -y <(xxd ext-super-magic.img) <(xxd ext-super-magic-fixed.img)

...
000003e0: 0000 0000 0000 0000 0000 0000 0000 0000  ..........	000003e0: 0000 0000 0000 0000 0000 0000 0000 0000  ..........
000003f0: 0000 0000 0000 0000 0000 0000 0000 0000  ..........	000003f0: 0000 0000 0000 0000 0000 0000 0000 0000  ..........
00000400: 0005 0000 0014 0000 0001 0000 6a05 0000  .......... |	00000400: 0005 0000 0014 0000 0001 0000 3a13 0000  ..........
00000410: 0003 0000 0100 0000 0000 0000 0000 0000  .......... |	00000410: f504 0000 0100 0000 0000 0000 0000 0000  ..........
00000420: 0020 0000 0020 0000 0005 0000 d8da ad5b  . ... .... |	00000420: 0020 0000 0020 0000 0005 0000 0000 0000  . ... ....
00000430: deda ad5b 0100 ffff 0000 0100 0100 0000  ...[...... |	00000430: 8077 c45b 0000 ffff 53ef 0100 0100 0000  .w.[....S.
00000440: d8da ad5b 0000 0000 0000 0000 0100 0000  ...[...... |	00000440: 8077 c45b 0000 0000 0000 0000 0100 0000  .w.[......
00000450: 0000 0000 0b00 0000 8000 0000 3802 0000  .......... |	00000450: 0000 0000 0b00 0000 8000 0000 3800 0000  ..........
00000460: 0200 0000 0300 0000 f571 19a5 29d5 4d7a  .........q |	00000460: 0200 0000 0300 0000 1f76 e55a 0520 4807  .........v
00000470: ae5d ad35 73a9 375f 0000 0000 0000 0000  .].5s.7_.. |	00000470: 9399 0f62 9b7d 79be 0000 0000 0000 0000  ...b.}y...
...
```

We can see a differenct at address 0x438, we have 0x0000 instead of [0x53ef](https://ext4.wiki.kernel.org/index.php/Ext4_Disk_Layout)

Lets try to change it and then to mount again:
```bash
dd if=ext-super-magic.img of=ext-super-magic-fixed.img bs=1 count=$((0x438))
echo -n -e '\x53\xef' >> ext-super-magic-fixed.img
dd if=ext-super-magic.img bs=1 skip=$((0x43a)) >> ext-super-magic-fixed.img
sudo mount ./ext-super-magic-fixed.img ./mnt
cp ./mnt/flag.jpg .
xdg-open ./flag.jpg
```

![flag](./flag.jpg)

Got the flag!

Flag: picoCTF{B3a388F85f93246B9DBA7Cc0fbBA5eE0}