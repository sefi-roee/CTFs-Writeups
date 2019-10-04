# Problem
This vault uses for-loops and byte arrays. The source code for this vault is here: [VaultDoor3.java](https://2019shell1.picoctf.com/static/e3c91f3cd8fb4d926e10ec20ecf074b6/VaultDoor3.java)

## Hints:
Make a table that contains each value of the loop variables and the corresponding buffer index that it writes to.

## Solution:

First, we download the code
```bash
wget https://2019shell1.picoctf.com/static/e3c91f3cd8fb4d926e10ec20ecf074b6/VaultDoor3.java
```

Let's take a look:
```java
import java.util.*;

class VaultDoor3 {
    public static void main(String args[]) {
        VaultDoor3 vaultDoor = new VaultDoor3();
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

    // Our security monitoring team has noticed some intrusions on some of the
    // less secure doors. Dr. Evil has asked me specifically to build a stronger
    // vault door to protect his Doomsday plans. I just *know* this door will
    // keep all of those nosy agents out of our business. Mwa ha!
    //
    // -Minion #2671
    public boolean checkPassword(String password) {
        if (password.length() != 32) {
            return false;
        }
        char[] buffer = new char[32];
        int i;
        for (i=0; i<8; i++) {
            buffer[i] = password.charAt(i);
        }
        for (; i<16; i++) {
            buffer[i] = password.charAt(23-i);
        }
        for (; i<32; i+=2) {
            buffer[i] = password.charAt(46-i);
        }
        for (i=31; i>=17; i-=2) {
            buffer[i] = password.charAt(i);
        }
        String s = new String(buffer);
        return s.equals("jU5t_a_sna_3lpm13gc49_u_4_m0rf41");
    }
}
```

We just need to reverse the algorithm. Using a simple script:
```python
target = 'jU5t_a_sna_3lpm13gc49_u_4_m0rf41'

pw = [None] * 32

for i in range(17, 32, 2):
    pw[i] = target[i]

for i in range(30, 14, -2):
    pw[46 - i] = target[i]

for i in range(15, 7, -1):
    pw[23 - i] = target[i]

for i in range(7, -1, -1):
    pw[i] = target[i]

print 'picoCTF{{{}}}'.format(''.join(pw))
```

Flag: picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_90cf31}
