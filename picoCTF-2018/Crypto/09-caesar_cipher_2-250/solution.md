# Problem
Can you help us decrypt this [message](https://2018shell1.picoctf.com/static/9edfb0ed867d63fa924e91166c69b78b/ciphertext)? We believe it is a form of a caesar cipher. You can find the ciphertext in /problems/caesar-cipher-2_2_d9c42f8026f320079f3d4fcbaa410615 on the shell server.

## Hints:
You'll have figure out the correct alphabet that was used to encrypt the ciphertext from the ascii character set

[ASCII Table](https://www.asciitable.com/)

## Solution:

First, we need to download the ciphertext:
```bash
wget https://2018shell1.picoctf.com/static/9edfb0ed867d63fa924e91166c69b78b/ciphertext
```

We got ```PICO#4&[C!ESA2?#I0H%R3?JU34?A2%N4?S%C5R%]```.


Now, using the following script, we can decrypt the message
```python
#!/usr/bin/env python

ciphertext = open('ciphertext', 'r').read()

plain = ''

for c in ciphertext:
	plain += chr((ord(c) - ord('A') + ord('a')))
	#plain += chr((ord(c) - ord('a') + i) % 26 + ord('a'))

print '{}'.format(plain)
```

Flag: picoCTF{cAesaR_CiPhErS_juST_aREnT_sEcUrE}
