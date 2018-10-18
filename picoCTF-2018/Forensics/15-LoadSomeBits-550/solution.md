# Problem
Can you find the flag encoded inside this [image](https://2018shell1.picoctf.com/static/826fc5f89e31773bf09914e568097d44/pico2018-special-logo.bmp)? You can also find the file in /problems/loadsomebits_3_8933ebe9085168b1e0bbb07884c2231f on the shell server.

## Hints:
Look through the Least Significant Bits for the image

If you interpret a binary sequence (seq) as ascii and then try interpreting the same binary sequence from an offset of 1 (seq[1:]) as ascii do you get something similar or completely different?

## Solution:
First, we download the image and look at it:
```bash
wget https://2018shell1.picoctf.com/static/826fc5f89e31773bf09914e568097d44/pico2018-special-logo.bmp
xdg-open ./pico2018-special-logo.bmp
```

![pico2018-special-logo](./pico2018-special-logo.bmp)

The hint tells us what to do. We just need to concatenate all to LSBs and try to decode:
```python
#!/usr/bin/env python

import binascii


image = open('pico2018-special-logo.bmp', 'rb').read()
s = ''

for c in image:
	s += str(ord(c) & 1)

for it in range(16):
	ss = ''
	try:
		ss = binascii.unhexlify('%x' % int(s[:-it], 2))

	except:
		pass

	if 'pico' in ss:
		print ss[ss.find('pico') : ss.find('pico') + 70]

		break
```

Flag: picoCTF{st0r3d_iN_tH3_l345t_s1gn1f1c4nT_b1t5_449088860}