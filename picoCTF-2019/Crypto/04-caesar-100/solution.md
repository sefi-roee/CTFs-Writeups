# Problem
Decrypt this [message](https://2019shell1.picoctf.com/static/48df1c1cea3578bb350dd089a9f0bc10/ciphertext). You can find the ciphertext in /problems/caesar_0_22aa542fadadcc37b6ec6037c493ec9f on the shell server.

## Hints:
caesar cipher [tutorial](https://learncryptography.com/classical-encryption/caesar-cipher)

## Solution:

First, we need to download the ciphertext:
```bash
wget https://2019shell1.picoctf.com/static/48df1c1cea3578bb350dd089a9f0bc10/ciphertext
```

Now, using the following script, we can try to detect the secret key (probably only one key will decrypt the ciphertext to english)
```python
#!/usr/bin/env python

ciphertext = open('ciphertext', 'r').read()

cipher = ciphertext.split('{')[1].replace('}', '')

for i in range(26):
	plain = ''

	for c in cipher:
		plain += chr((ord(c) - ord('a') + i) % 26 + ord('a'))

	print '{:<3}picoCTF{{{}}}'.format(i, plain)
```

```bash
0  picoCTF{jyvzzpunaolybipjvunfzpthre}
1  picoCTF{kzwaaqvobpmzcjqkwvogaquisf}
2  picoCTF{laxbbrwpcqnadkrlxwphbrvjtg}
3  picoCTF{mbyccsxqdrobelsmyxqicswkuh}
4  picoCTF{nczddtyrespcfmtnzyrjdtxlvi}
5  picoCTF{odaeeuzsftqdgnuoazskeuymwj}
6  picoCTF{pebffvatgurehovpbatlfvznxk}
7  picoCTF{qfcggwbuhvsfipwqcbumgwaoyl}
8  picoCTF{rgdhhxcviwtgjqxrdcvnhxbpzm}
9  picoCTF{sheiiydwjxuhkrysedwoiycqan}
10 picoCTF{tifjjzexkyvilsztfexpjzdrbo}
11 picoCTF{ujgkkafylzwjmtaugfyqkaescp}
12 picoCTF{vkhllbgzmaxknubvhgzrlbftdq}
13 picoCTF{wlimmchanbylovcwihasmcguer}
14 picoCTF{xmjnndiboczmpwdxjibtndhvfs}
15 picoCTF{ynkooejcpdanqxeykjcuoeiwgt}
16 picoCTF{zolppfkdqeboryfzlkdvpfjxhu}
17 picoCTF{apmqqglerfcpszgamlewqgkyiv}
18 picoCTF{bqnrrhmfsgdqtahbnmfxrhlzjw}
19 picoCTF{crossingtherubicongysimakx}
20 picoCTF{dspttjohuifsvcjdpohztjnbly}
21 picoCTF{etquukpivjgtwdkeqpiaukocmz}
22 picoCTF{furvvlqjwkhuxelfrqjbvlpdna}
23 picoCTF{gvswwmrkxlivyfmgsrkcwmqeob}
24 picoCTF{hwtxxnslymjwzgnhtsldxnrfpc}
25 picoCTF{ixuyyotmznkxahoiutmeyosgqd}
```

We can see the plaintext in i=19.

Flag: picoCTF{crossingtherubicongysimakx}
