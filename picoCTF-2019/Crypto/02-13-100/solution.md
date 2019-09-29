# Problem
Cryptography can be easy, do you know what ROT13 is? cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}

## Hints:
This can be solved online if you don't want to do it by hand!

## Solution:

Using a simple script:
```python
#!/usr/bin/env python

cipher = 'cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}'

plain = ''

for c in cipher:
    if 'a' <= c <= 'z':
        plain += chr((ord(c) - ord('a') + 13) % 26 + ord('a'))
    elif 'A' <= c <= 'Z':
        plain += chr((ord(c) - ord('A') + 13) % 26 + ord('A'))
    else:
        plain += c

print '{}'.format(plain)
```

Flag: picoCTF{not_too_bad_of_a_problem}
