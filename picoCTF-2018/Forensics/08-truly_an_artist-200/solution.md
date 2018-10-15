# Problem
Can you help us find the flag in this [Meta-Material](https://2018shell1.picoctf.com/static/9b8863e30054675ce78328df28c601db/2018.png)? You can also find the file in /problems/truly-an-artist_4_cdd9e325cf9bacd265b98a7fe336e840.

## Hints:
Try looking beyond the image.

Who created this?

## Solution:

First, we download the image
```bash
wget https://2018shell1.picoctf.com/static/9b8863e30054675ce78328df28c601db/2018.png
```

Lets try to open the file:
```bash
xdg-open ./2018.png
```

![picture](./2018.png)


Not helping us... lets try to extract some meta data. We can use [exiftool](https://linoxide.com/linux-how-to/install-use-exiftool-linux-ubuntu-centos/)
```bash
exiftool ./2018.png

ExifTool Version Number         : 10.80
File Name                       : 2018.png
Directory                       : .
File Size                       : 13 kB
File Modification Date/Time     : 2018:09:28 11:26:38+03:00
File Access Date/Time           : 2018:10:15 08:07:50+03:00
File Inode Change Date/Time     : 2018:10:15 08:07:47+03:00
File Permissions                : rw-r--r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 1200
Image Height                    : 630
Bit Depth                       : 8
Color Type                      : RGB
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Artist                          : picoCTF{look_in_image_13509d38}
Image Size                      : 1200x630
Megapixels                      : 0.756
```

We can see the flag at the "Artist" field.

One liner:
```bash
exiftool -Artist ./2018.png | awk '{split($0, a, ":"); print a[2]}' | awk '{$1=$1};1'
```

Flag: picoCTF{look_in_image_13509d38}