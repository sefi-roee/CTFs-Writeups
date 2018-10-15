# Problem
This [cat](https://2018shell1.picoctf.com/static/29531f8d0c0270a32bd186ffcb9271b8/hex_editor.jpg) has a secret to teach you. You can also find the file in /problems/hex-editor_1_10cafee5618ce2cfe32f2188ca1f472e on the shell server.

## Hints:
What is a hex editor?

Maybe google knows.

[xxd](http://linuxcommand.org/man_pages/xxd1.html)

[hexedit](http://linuxcommand.org/man_pages/hexedit1.html)

[bvi](http://manpages.ubuntu.com/manpages/natty/man1/bvi.1.html)

## Solution:

First, we download the file
```bash
wget https://2018shell1.picoctf.com/static/29531f8d0c0270a32bd186ffcb9271b8/hex_editor.jpg
```

Lets try to open the file:
```bash
xdg-open ./hex_editor.jpg
```

![hex editor](./hex_editor.jpg)


Nothing... lets print the contents of this file:
```bash
xxd ./hex_editor.jpg

00000000: ffd8 ffe0 0010 4a46 4946 0001 0100 0001  ......JFIF......
00000010: 0001 0000 ffdb 0043 0005 0304 0404 0305  .......C........
00000020: 0404 0405 0505 0607 0c08 0707 0707 0f0b  ................
00000030: 0b09 0c11 0f12 1211 0f11 1113 161c 1713  ................
00000040: 141a 1511 1118 2118 1a1d 1d1f 1f1f 1317  ......!.........
...
000128c0: e23f 92ab 940c 94f9 5e9c d4f7 5f9e 99b6  .?......^..._...
000128d0: 8008 befd 5a6a aab5 61ea c822 7fbf 4c6a  ....Zj..a.."..Lj
000128e0: 7bd3 256a 802b 4ad5 153a 5a6a d496 39d7  {.%j.+J..:Zj..9.
000128f0: e4a8 3857 ab88 bf25 412a d000 9f3d 5eb7  ..8W...%A*...=^.
00012900: 8ea9 c557 226a 2206 b5a7 cb57 16b3 2dda  ...W"j"....W..-.
00012910: af24 95bc 4863 65f9 6a9c ad56 66aa 370d  .$..Hce.j..Vf.7.
00012920: 4480 8a56 a4a8 5e4a 3ccd d520 4d45 43ba  D..V..^J<.. MEC.
00012930: 8a00 ffd9 596f 7572 2066 6c61 6720 6973  ....Your flag is
00012940: 3a20 2270 6963 6f43 5446 7b61 6e64 5f74  : "picoCTF{and_t
00012950: 6861 7473 5f68 6f77 5f75 5f65 6469 745f  hats_how_u_edit_
00012960: 6865 785f 6b69 7474 6f73 5f34 6245 3561  hex_kittos_4bE5a
00012970: 4362 387d 220a                           Cb8}".
```

We can see the flag at the end of the png file!

```bash
tail ./hex_editor.jpg -c 52

"picoCTF{and_thats_how_u_edit_hex_kittos_4bE5aCb8}"
```

Flag: picoCTF{and_thats_how_u_edit_hex_kittos_4bE5aCb8}