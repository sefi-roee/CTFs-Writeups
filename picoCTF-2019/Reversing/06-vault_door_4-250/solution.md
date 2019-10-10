# Problem
This vault uses ASCII encoding for the password. The source code for this vault is here: [VaultDoor4.java](https://2019shell1.picoctf.com/static/8f755163931922b533492461c05b13f1/VaultDoor4.java)

## Hints:
Use a search engine to find an "ASCII table".

You will also need to know the difference between octal, decimal, and hexademical numbers.

## Solution:

First, we download the code
```bash
wget https://2019shell1.picoctf.com/static/8f755163931922b533492461c05b13f1/VaultDoor4.java
```

Let's take a look:
```java
import java.util.*;

class VaultDoor4 {
    public static void main(String args[]) {
        VaultDoor4 vaultDoor = new VaultDoor4();
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

    // I made myself dizzy converting all of these numbers into different bases,
    // so I just *know* that this vault will be impenetrable. This will make Dr.
    // Evil like me better than all of the other minions--especially Minion
    // #5620--I just know it!
    //
    //  .:::.   .:::.
    // :::::::.:::::::
    // :::::::::::::::
    // ':::::::::::::'
    //   ':::::::::'
    //     ':::::'
    //       ':'
    // -Minion #7781
    public boolean checkPassword(String password) {
        byte[] passBytes = password.getBytes();
        byte[] myBytes = {
            106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
            0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
            0142, 0131, 0164, 063 , 0163, 0137, 062 , 060 ,
            '1' , 'b' , '3' , '5' , '2' , 'd' , '6' , 'c' ,
        };
        for (int i=0; i<32; i++) {
            if (passBytes[i] != myBytes[i]) {
                return false;
            }
        }
        return true;
    }
}
```

We just need to convert numbers to characters. Using a simple script:
```python
pw = [106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
          0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
          0142, 0131, 0164, 063 , 0163, 0137, 062 , 060 ,
          '1' , 'b' , '3' , '5' , '2' , 'd' , '6' , 'c']

for i in range(24):
    pw[i] = chr(pw[i])

print 'picoCTF{{{}}}'.format(''.join(pw))
```

Flag: picoCTF{jU5t_4_bUnCh_0f_bYt3s_201b352d6c}
