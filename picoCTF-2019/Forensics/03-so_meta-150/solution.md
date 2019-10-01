# Problem
Find the flag in this [picture](https://2019shell1.picoctf.com/static/ddffae2f670f7c822c4f878e932bf6c5/pico_img.png). You can also find the file in /problems/so-meta_0_7c0b2ae7a38b024c6b1c68cf50970a88.

## Hints:
What does meta mean in the context of files?

Ever hear of metadata?

## Solution:

First, let's download the file:
```bash
wget https://2019shell1.picoctf.com/static/ddffae2f670f7c822c4f878e932bf6c5/pico_img.png
```

Let's take a look:
![pico_img](./pico_img.png)

Nothing...
Let's look at the meta:
```bash
exiftool pico_img.png

ExifTool Version Number         : 11.16
File Name                       : pico_img.png
Directory                       : .
File Size                       : 106 kB
File Modification Date/Time     : 2019:09:29 00:50:57+03:00
File Access Date/Time           : 2019:09:29 16:53:26+03:00
File Inode Change Date/Time     : 2019:09:29 16:53:24+03:00
File Permissions                : rw-r--r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 600
Image Height                    : 600
Bit Depth                       : 8
Color Type                      : RGB
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Software                        : Adobe ImageReady
XMP Toolkit                     : Adobe XMP Core 5.3-c011 66.145661, 2012/02/06-14:56:27
Creator Tool                    : Adobe Photoshop CS6 (Windows)
Instance ID                     : xmp.iid:A5566E73B2B811E8BC7F9A4303DF1F9B
Document ID                     : xmp.did:A5566E74B2B811E8BC7F9A4303DF1F9B
Derived From Instance ID        : xmp.iid:A5566E71B2B811E8BC7F9A4303DF1F9B
Derived From Document ID        : xmp.did:A5566E72B2B811E8BC7F9A4303DF1F9B
Artist                          : picoCTF{s0_m3ta_dc38ce45}
Image Size                      : 600x600
Megapixels                      : 0.360
```

Got it!

Flag: picoCTF{s0_m3ta_dc38ce45}
