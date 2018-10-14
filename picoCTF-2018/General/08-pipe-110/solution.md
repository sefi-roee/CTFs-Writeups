# Problem
During your adventure, you will likely encounter a situation where you need to process data that you receive over the network rather than through a file. Can you find a way to save the output from this program and search for the flag? Connect with ```2018shell1.picoctf.com 34532```.

## Hints:
Remember the flag format is picoCTF{XXXX}

Ever heard of a pipe? No not that kind of pipe... This [kind](http://www.linfo.org/pipes.html)

## Solution:

```bash
#!/usr/bin/bash

nc 2018shell1.picoctf.com 34532 | grep picoCTF
```

We can do it all with a single python script:
```python
#!/usr/bin/env python

import requests

s = ''
for url in ['http://2018shell1.picoctf.com:56252/', 'http://2018shell1.picoctf.com:56252/mycss.css', 'http://2018shell1.picoctf.com:56252/myjs.js']:
	f = requests.get(url)

	lines = f.text.split('\n')

	for line in lines:
		if 'flag' in line:
			index = line.find('flag:') + 5

			s += line[index:].split()[0].replace('*', '').replace('/', '')

print s
```

Flag: picoCTF{almost_like_mario_b797f2b3}
