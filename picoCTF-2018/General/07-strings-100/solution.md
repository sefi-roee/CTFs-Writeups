# Problem
Can you find the flag in this [file](https://2018shell1.picoctf.com/static/22ef75638cf590f5fad3db45463883bb/strings) without actually running it? You can also find the file in /problems/strings_2_b7404a3aee308619cb2ba79677989960 on the shell server.


## Hints:
[strings](https://linux.die.net/man/1/strings)

## Solution:

First, we download the file
```bash
wget https://2018shell1.picoctf.com/static/22ef75638cf590f5fad3db45463883bb/strings
```

Then we use strings (piped to grep) in order to find the flag:
```bash
#!/usr/bin/bash

strings strings | grep picoCTF
```

Flag: picoCTF{sTrIngS_sAVeS_Time_3f712a28}
