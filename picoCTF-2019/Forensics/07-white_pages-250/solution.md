# Problem
I stopped using YellowPages and moved onto WhitePages... but [the page they gave me](https://2019shell1.picoctf.com/static/d7068f4c75d7b4a3e342cc57d528c5ce/whitepages.txt) is all blank!

## Hints:

## Solution:

First, let's download the file:
```bash
wget https://2019shell1.picoctf.com/static/d7068f4c75d7b4a3e342cc57d528c5ce/whitepages.txt
```

When printing the file it's all whitespaces :(

After some googling I understood its a 'utf-8' encoded.
From now on it's pretty simple.

Using a simple python script:
```python
#!/usr/bin/env python

f = open('./whitepages.txt', 'r').read()

s = hex(int(f.decode('utf-8').replace(u'\u2003', '0').replace(' ', '1'), 2))[3:-1].decode('hex')

print s
```

And we got:
```bash
        picoCTF

        SEE PUBLIC RECORDS & BACKGROUND REPORT
        5000 Forbes Ave, Pittsburgh, PA 15213
        picoCTF{not_all_spaces_are_created_equal_178d720252af1af29369e154eca23a95}
```

Nice!

Flag: picoCTF{not_all_spaces_are_created_equal_178d720252af1af29369e154eca23a95}
