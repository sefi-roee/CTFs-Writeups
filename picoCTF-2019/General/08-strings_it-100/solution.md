# Problem
Can you find the flag in [file](https://2019shell1.picoctf.com/static/d97e691ff0842819be9dfcb767c074d9/strings) without running it? You can also find the file in /problems/strings-it_0_b76c77672f6285e3a39c188481cdff99 on the shell server.

## Hints:
[strings](https://linux.die.net/man/1/strings)

## Solution:

Let's download the file:
```bash
wget https://2019shell1.picoctf.com/static/d97e691ff0842819be9dfcb767c074d9/strings
```

Then we use strings (piped to grep) in order to find the flag:
```bash
#!/usr/bin/bash

strings strings | grep picoCTF
```

Flag: picoCTF{5tRIng5_1T_f1527258}
