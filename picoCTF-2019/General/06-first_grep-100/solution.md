# Problem
Can you find the flag in [file](https://2019shell1.picoctf.com/static/20314c5941bbf36a5eaa2e0926fb1cb5/file)? This would be really tedious to look through manually, something tells me there is a better way. You can also find the file in /problems/first-grep_3_2e09f586a51352180a37e25913f5e5d9 on the shell server.

## Hints:

grep [tutorial](https://ryanstutorials.net/linuxtutorial/grep.php)

## Solution:

Let's download the file:
```bash
wget https://2019shell1.picoctf.com/static/20314c5941bbf36a5eaa2e0926fb1cb5/file
```

Using a simple ```grep```:
```bash
cat file | grep picoCTF

picoCTF{grep_is_good_to_find_things_eda8911c}
```

Flag: picoCTF{grep_is_good_to_find_things_eda8911c}
