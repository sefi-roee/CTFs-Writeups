# Problem
In the last challenge, you mastered octal (base 8), decimal (base 10), and hexadecimal (base 16) numbers, but this vault door uses a different change of base as well as URL encoding! The source code for this vault is here: [VaultDoor5.java](https://2019shell1.picoctf.com/static/3b515f470e1151cb2af0777a7a6becf3/VaultDoor5.java)

## Hints:

You may find an encoder/decoder tool helpful, such as https://encoding.tools/

Read the wikipedia articles on URL encoding and base 64 encoding to understand how they work and what the results look like.

## Solution:

First, we download the code
```bash
wget https://2019shell1.picoctf.com/static/3b515f470e1151cb2af0777a7a6becf3/VaultDoor5.java
```

Let's take a look:
```java
import java.net.URLDecoder;
import java.util.*;

class VaultDoor5 {
    public static void main(String args[]) {
        VaultDoor5 vaultDoor = new VaultDoor5();
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

    // Minion #7781 used base 8 and base 16, but this is base 64, which is
    // like... eight times stronger, right? Riiigghtt? Well that's what my twin
    // brother Minion #2415 says, anyway.
    //
    // -Minion #2414
    public String base64Encode(byte[] input) {
        return Base64.getEncoder().encodeToString(input);
    }

    // URL encoding is meant for web pages, so any double agent spies who steal
    // our source code will think this is a web site or something, defintely not
    // vault door! Oh wait, should I have not said that in a source code
    // comment?
    //
    // -Minion #2415
    public String urlEncode(byte[] input) {
        StringBuffer buf = new StringBuffer();
        for (int i=0; i<input.length; i++) {
            buf.append(String.format("%%%2x", input[i]));
        }
        return buf.toString();
    }

    public boolean checkPassword(String password) {
        String urlEncoded = urlEncode(password.getBytes());
        String base64Encoded = base64Encode(urlEncoded.getBytes());
        String expected = "JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVm"
                        + "JTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2"
                        + "JTM0JTVmJTM3JTM1JTM3JTY1JTMxJTY0JTMwJTMw";
        return base64Encoded.equals(expected);
    }
}
```

We just need to revert the operations:
```python
#!/usr/bin/env python
from pwn import *


expected = "JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVmJTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2JTM0JTVmJTM3JTM1JTM3JTY1JTMxJTY0JTMwJTMw"

urlEncoded = b64d(expected)
password = urldecode(urlEncoded)

print 'picoCTF{{{}}}'.format(password)
```

Flag: picoCTF{c0nv3rt1ng_fr0m_ba5e_64_757e1d00}
