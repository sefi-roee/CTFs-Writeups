# Bandit Level 13

```bash
Username: bandit13
Password: 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL
Server:   bandit.labs.overthewire.org
Port:     2220
```

Lets connect to the server:
```bash
ssh bandit13@bandit.labs.overthewire.org -p2220
```

Lets take a look:
```bash
bandit13@bandit:~$ ls
sshkey.private
bandit13@bandit:~$ file sshkey.private 
sshkey.private: PEM RSA private key
```

We need to use this key to login as user ```bandit14```:
```bash
bandit13@bandit:~$ ssh -i sshkey.private bandit14@localhost
Could not create directory '/home/bandit13/.ssh'.
The authenticity of host 'localhost (127.0.0.1)' can't be established.
ECDSA key fingerprint is SHA256:98UL0ZWr85496EtCRkKlo20X3OPnyPSB5tB5RPbhczc.
Are you sure you want to continue connecting (yes/no)? yes
Failed to add the host to the list of known hosts (/home/bandit13/.ssh/known_hosts).
This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

Linux bandit 4.18.12 x86_64 GNU/Linux
               
      ,----..            ,----,          .---. 
     /   /   \         ,/   .`|         /. ./|
    /   .     :      ,`   .'  :     .--'.  ' ;
   .   /   ;.  \   ;    ;     /    /__./ \ : |
  .   ;   /  ` ; .'___,/    ,' .--'.  '   \' .
  ;   |  ; \ ; | |    :     | /___/ \ |    ' ' 
  |   :  | ; | ' ;    |.';  ; ;   \  \;      : 
  .   |  ' ' ' : `----'  |  |  \   ;  `      |
  '   ;  \; /  |     '   :  ;   .   \    .\  ; 
   \   \  ',  /      |   |  '    \   \   ' \ |
    ;   :    /       '   :  |     :   '  |--"  
     \   \ .'        ;   |.'       \   \ ;     
  www. `---` ver     '---' he       '---" ire.org     
               
              
Welcome to OverTheWire!

If you find any problems, please report them to Steven or morla on
irc.overthewire.org.

--[ Playing the games ]--

  This machine might hold several wargames. 
  If you are playing "somegame", then:

    * USERNAMES are somegame0, somegame1, ...
    * Most LEVELS are stored in /somegame/.
    * PASSWORDS for each level are stored in /etc/somegame_pass/.

  Write-access to homedirectories is disabled. It is advised to create a
  working directory with a hard-to-guess name in /tmp/.  You can use the
  command "mktemp -d" in order to generate a random and hard to guess
  directory in /tmp/.  Read-access to both /tmp/ and /proc/ is disabled
  so that users can not snoop on eachother. Files and directories with 
  easily guessable or short names will be periodically deleted!
    
  Please play nice:
      
    * don't leave orphan processes running
    * don't leave exploit-files laying around
    * don't annoy other players
    * don't post passwords or spoilers
    * again, DONT POST SPOILERS! 
      This includes writeups of your solution on your blog or website!

--[ Tips ]--

  This machine has a 64bit processor and many security-features enabled
  by default, although ASLR has been switched off.  The following
  compiler flags might be interesting:

    -m32                    compile for 32bit
    -fno-stack-protector    disable ProPolice
    -Wl,-z,norelro          disable relro 

  In addition, the execstack tool can be used to flag the stack as
  executable on ELF binaries.

  Finally, network-access is limited for most levels by a local
  firewall.

--[ Tools ]--

 For your convenience we have installed a few usefull tools which you can find
 in the following locations:

    * pwndbg (https://github.com/pwndbg/pwndbg) in /usr/local/pwndbg/
    * peda (https://github.com/longld/peda.git) in /usr/local/peda/
    * gdbinit (https://github.com/gdbinit/Gdbinit) in /usr/local/gdbinit/
    * pwntools (https://github.com/Gallopsled/pwntools)
    * radare2 (http://www.radare.org/)
    * checksec.sh (http://www.trapkit.de/tools/checksec.html) in /usr/local/bin/checksec.sh

--[ More information ]--

  For more information regarding individual wargames, visit
  http://www.overthewire.org/wargames/

  For support, questions or comments, contact us through IRC on
  irc.overthewire.org #wargames.

  Enjoy your stay!

bandit14@bandit:~$ cat /etc/bandit_pass/bandit14
4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e
```

We got the password for the next level: **4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e**

**A single script is:**
```python
#!/usr/bin/env python

from pwn import *


def main():
    shell = ssh(host='bandit.labs.overthewire.org',
                user='bandit13',
                password='8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL',
                port=2220
           )

    key_file = shell['ls | grep sshkey']
    shell.get(key_file)

    shell1 = ssh(host='bandit.labs.overthewire.org',
                user='bandit14',
                keyfile=key_file,
                port=2220
           )

    print shell1['cat /etc/bandit_pass/bandit14']
    os.remove(key_file)
    
if __name__ == "__main__":
    main()
```