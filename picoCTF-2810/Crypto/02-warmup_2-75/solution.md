# Problem
Cryptography doesn't have to be complicated, have you ever heard of something called rot13? ```cvpbPGS{guvf_vf_pelcgb!}```

## Hints:
This can be solved online if you don't want to do it by hand!

## Solution:

Using a simple python script
```python
#!/usr/bin/env python

message = 'cvpbPGS{guvf_vf_pelcgb!}'

s = ''
for m in message:
	if 'a' <= m <= 'z':
		s += chr((ord(m) - ord('a') + 13) % 26 + ord('a'))
	elif 'A' <= m <= 'Z':
		s += chr((ord(m) - ord('A') + 13) % 26 + ord('A'))
	else:
		s += m

print '{}'.format(s)
```

Flag: picoCTF{this_is_crypto!}
