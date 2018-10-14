# Problem
This is one of the older ciphers in the books, can you decrypt the [message](https://2018shell1.picoctf.com/static/2b49cc4b04ae2bc8ea4dcdf8016b10d6/ciphertext)? You can find the ciphertext in /problems/caesar-cipher-1_4_e4dc6dcfb004bdade0b9ce8e44f1bac4 on the shell server.

## Hints:
caesar cipher [tutorial](https://learncryptography.com/classical-encryption/caesar-cipher)

## Solution:

First, we need to download the ciphertext:
```bash
wget https://2018shell1.picoctf.com/static/2b49cc4b04ae2bc8ea4dcdf8016b10d6/ciphertext
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
0  picoCTF{domnuaiixifxwuymulwcjbylnivlpglc}
1  picoCTF{epnovbjjyjgyxvznvmxdkczmojwmqhmd}
2  picoCTF{fqopwckkzkhzywaownyeldanpkxnrine}
3  picoCTF{grpqxdllaliazxbpxozfmeboqlyosjof}
4  picoCTF{hsqryemmbmjbaycqypagnfcprmzptkpg}
5  picoCTF{itrszfnncnkcbzdrzqbhogdqsnaqulqh}
6  picoCTF{justagoodoldcaesarciphertobrvmri}
7  picoCTF{kvtubhppepmedbftbsdjqifsupcswnsj}
8  picoCTF{lwuvciqqfqnfecguctekrjgtvqdtxotk}
9  picoCTF{mxvwdjrrgrogfdhvduflskhuwreuypul}
10 picoCTF{nywxeksshsphgeiwevgmtlivxsfvzqvm}
11 picoCTF{ozxyflttitqihfjxfwhnumjwytgwarwn}
12 picoCTF{payzgmuujurjigkygxiovnkxzuhxbsxo}
13 picoCTF{qbzahnvvkvskjhlzhyjpwolyaviyctyp}
14 picoCTF{rcabiowwlwtlkimaizkqxpmzbwjzduzq}
15 picoCTF{sdbcjpxxmxumljnbjalryqnacxkaevar}
16 picoCTF{tecdkqyynyvnmkockbmszrobdylbfwbs}
17 picoCTF{ufdelrzzozwonlpdlcntaspcezmcgxct}
18 picoCTF{vgefmsaapaxpomqemdoubtqdfandhydu}
19 picoCTF{whfgntbbqbyqpnrfnepvcuregboeizev}
20 picoCTF{xighouccrczrqosgofqwdvsfhcpfjafw}
21 picoCTF{yjhipvddsdasrpthpgrxewtgidqgkbgx}
22 picoCTF{zkijqweetebtsquiqhsyfxuhjerhlchy}
23 picoCTF{aljkrxffufcutrvjritzgyvikfsimdiz}
24 picoCTF{bmklsyggvgdvuswksjuahzwjlgtjneja}
25 picoCTF{cnlmtzhhwhewvtxltkvbiaxkmhukofkb}
```

We can see the plaintext in i=6.

Flag: picoCTF{justagoodoldcaesarciphertobrvmri}
