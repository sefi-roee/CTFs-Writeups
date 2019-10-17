# Problem
This vault uses an XOR encryption scheme. The source code for this vault is here: [VaultDoor6.java](https://2019shell1.picoctf.com/static/baceedcb57993355ba6eac807ca041b0/VaultDoor6.java)

## Hints:

If X ^ Y = Z, then Z ^ Y = X. Write a program that decrypts the flag based on this fact.

## Solution:

First, we download the code
```bash
wget https://2019shell1.picoctf.com/static/baceedcb57993355ba6eac807ca041b0/VaultDoor6.java
```

Let's take a look:
```java
import java.util.*;

class VaultDoor6 {
    public static void main(String args[]) {
        VaultDoor6 vaultDoor = new VaultDoor6();
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter vault password: ");
        String userInput = scanner.next();
    String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
    if (vaultDoor.checkPassword(input)) {
        System.out.println("Access granted.");
    } else {
        System.out.println("Access denied!");
        }
    }

    // Dr. Evil gave me a book called Applied Cryptography by Bruce Schneier,
    // and I learned this really cool encryption system. This will be the
    // strongest vault door in Dr. Evil's entire evil volcano compound for sure!
    // Well, I didn't exactly read the *whole* book, but I'm sure there's
    // nothing important in the last 750 pages.
    //
    // -Minion #3091
    public boolean checkPassword(String password) {
        if (password.length() != 32) {
            return false;
        }
        byte[] passBytes = password.getBytes();
        byte[] myBytes = {
            0x3b, 0x65, 0x21, 0xa , 0x38, 0x0 , 0x36, 0x1d,
            0xa , 0x3d, 0x61, 0x27, 0x11, 0x66, 0x27, 0xa ,
            0x21, 0x1d, 0x61, 0x3b, 0xa , 0x2d, 0x65, 0x27,
            0xa , 0x34, 0x30, 0x31, 0x30, 0x36, 0x30, 0x31,
        };
        for (int i=0; i<32; i++) {
            if (((passBytes[i] ^ 0x55) - myBytes[i]) != 0) {
                return false;
            }
        }
        return true;
    }
}
```

We just need to XOR ```myBytes``` with ```0x55``` and we will get the ```passBytes```:
```python
#!/usr/bin/env python
from pwn import *


myBytes = [0x3b, 0x65, 0x21, 0xa , 0x38, 0x0 , 0x36, 0x1d, 0xa , 0x3d, 0x61, 0x27, 0x11, 0x66, 0x27, 0xa , 0x21, 0x1d, 0x61, 0x3b, 0xa , 0x2d, 0x65, 0x27, 0xa , 0x34, 0x30, 0x31, 0x30, 0x36, 0x30, 0x31]

passBytes = map(lambda x: x ^ 0x55, myBytes)

print 'picoCTF{{{}}}'.format(''.join(map(chr, passBytes)))
```

Flag: picoCTF{n0t_mUcH_h4rD3r_tH4n_x0r_aedeced}
