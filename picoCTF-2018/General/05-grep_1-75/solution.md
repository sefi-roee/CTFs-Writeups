# Problem
Can you find the flag in [file](https://2018shell1.picoctf.com/static/d7d1b6b0a64801c499a5eea393224811/file)? This would be really obnoxious to look through by hand, see if you can find a faster way. You can also find the file in /problems/grep-1_3_8d9cff3d178c231ab735dfef3267a1c2 on the shell server.

## Hints:
grep [tutorial](https://ryanstutorials.net/linuxtutorial/grep.php)

## Solution:

First we need to download the file
```bash
wget https://2018shell1.picoctf.com/static/d7d1b6b0a64801c499a5eea393224811/file
```

And then
```bash
cat file | grep picoCTF
```

Flag: picoCTF{grep_and_you_will_find_cdf2e7c2}
