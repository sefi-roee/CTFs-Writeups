# Problem
Our network administrator is having some trouble handling the tickets for all of of our incidents. Can you help him out by answering all the questions? Connect with nc ```2018shell1.picoctf.com 10493```. [incidents.json](https://2018shell1.picoctf.com/static/8eed8b873d59e897ae9dea0af40491f3/incidents.json)

## Hints:
If you need to code, python has some good libraries for it.

## Solution:

After trying manually, I write this script:
```python
#!/usr/bin/env python

import json
from collections import Counter
from pwn import *


data = json.loads(open('incidents.json').read())

ips = []

for ticket in data['tickets']:
	ips.append(ticket['dst_ip'])
	ips.append(ticket['src_ip'])

cnt = Counter(ips).most_common(1)

r = remote('2018shell1.picoctf.com', 10493)

lines = r.read()
print lines

ans = cnt[0][0]
print 'Sending: {}'.format(ans)
r.send('{}\n'.format(ans))

lines = r.read()
print lines

src = lines.split('\n')[-2].split()[-1][:-1]

ips = []
for ticket in data['tickets']:
	if ticket['src_ip'] == src:
		ips.append(ticket['dst_ip'])

ans = len(set(ips))
print 'Sending: {}'.format(ans)
r.send('{}\n'.format(ans))

lines = r.read()
print lines

hashes = []
for ticket in data['tickets']:
	hashes.append(ticket['file_hash'])

hashes = list(set(hashes))
c = []
for h in hashes:
	ips = []
	for ticket in data['tickets']:
		if ticket['file_hash'] == h:
			ips.append(ticket['dst_ip'])

	c.append(len(set(ips)))

ans = float(sum(c)) / len(c)
print 'Sending: {}'.format(ans)
r.send('{}\n'.format(ans))

lines = r.read()
print lines
```

Flag: picoCTF{J4y_s0n_d3rUUUULo_a062e5f8}
