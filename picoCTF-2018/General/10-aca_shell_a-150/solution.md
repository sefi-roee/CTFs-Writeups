# Problem
It's never a bad idea to brush up on those linux skills or even learn some new ones before you set off on this adventure! Connect with ```nc 2018shell1.picoctf.com 33158```.

## Hints:
Linux for [Beginners](https://maker.pro/education/basic-linux-commands-for-beginners)

## Solution:

Lets connect to the server:
```bash
nc 2018shell1.picoctf.com 33158

Sweet! We have gotten access into the system but we aren't root.
It's some sort of restricted shell! I can't see what you are typing
but I can see your output. I'll be here to help you along.
If you need help, type "echo 'Help Me!'" and I'll see what I can do
There is not much time left!
~/$ 
```

Lets list the directory:
```bash
~/$ ls
blackmail
executables
passwords
photos
secret
~/$
```

I love secrets, lets look there:
```bash
~/$ cd secret
Now we are cookin'! Take a look around there and tell me what you find!
~/secret$ ls
intel_1
intel_2
intel_3
intel_4
intel_5
profile_ahqueith5aekongieP4ahzugi
profile_ahShaighaxahMooshuP1johgo
profile_aik4hah9ilie9foru0Phoaph0
profile_AipieG5Ua9aewei5ieSoh7aph
profile_bah9Ech9oa4xaicohphahfaiG
profile_ie7sheiP7su2At2ahw6iRikoe
profile_of0Nee4laith8odaeLachoonu
profile_poh9eij4Choophaweiwev6eev
profile_poo3ipohGohThi9Cohverai7e
profile_Xei2uu5suwangohceedaifohs
Sabatoge them! Get rid of all their intel files!
```

OK, we know how to delete files:
```bash
~/secret$ rm intel_1
Nice! Once they are all gone, I think I can drop you a file of an exploit!
Just type "echo 'Drop it in!' " and we can give it a whirl!
~/secret$ rm intel_2
~/secret$ rm intel_3
~/secret$ rm intel_4
~/secret$ rm intel_5
~/secret$ echo 'Drop it in!'
Drop it in!
I placed a file in the executables folder as it looks like the only place we can execute from!
Run the script I wrote to have a little more impact on the system!
```

Lets go back to the ```executables``` directory:
```bash
~/secret$ cd ..
~/$ cd executables
~/executables$ ls
dontLookHere
~/executables$ ./dontLookHere
 a9ce 7dc4 c936 20c3 9446 3f9b 8b73 0d93 150d af70 b85c 692f ff15 24f3 8821 1906 d8b8 0ec7 490d 4550 d235 6ec1 2964 15a9 07aa
 67ec bd2a fb31 b903 f4b2 d9a2 a509 db8f 52c6 ed34 c886 a4b8 1b54 e4f7 8486 8a27 c607 ca01 2616 e3b7 7c63 1b7c 9281 cd00 8478
 6c49 cde3 c200 1981 405d 83a1 11e0 8024 ee82 7982 cef2 e60e 20ba 7a82 c600 f5c0 4555 0287 ad4a a8b8 8cfc 00f9 30c1 c116 c11b
 1d65 d94a c0d2 b99e 591e 05f7 c849 2106 e0bd 7993 35ca 777c 908e 0a13 a25e d50c 8a8b de86 87e2 0efc 8b39 3520 e8b6 b9f2 fe0c
 5402 1cd4 9130 64d7 4ae3 7e97 dd97 0438 5b63 ea79 ef32 9b2f d252 c35b 2dcf d75d 62a2 b9e8 55ad 2e49 d417 8714 7798 afca 79c7
 b164 740f e3b6 7f95 823c e1fd f04f 1aa1 7356 8747 8e10 975b 663b 219c 95f3 f18f ef41 2737 4ef5 24e2 de04 ec58 125e 8f0a d4bb
 13ef c041 70d6 2937 c11e e2e8 bd3a 700f 73ae 1d44 13c0 c571 4f0f 6a63 0e96 d76a 11ca 05ea c2e5 3e05 361a 7431 8fb7 8c13 2393
 d886 29b0 d8a9 0b62 4c0d 375a fbc8 078e 02e4 2917 e61f ff63 4dbc 5004 6c2a fdd0 d48c d31d 7fa1 de63 db42 f25d 24ad ed61 2481
 461b 5d5e ae64 5ebc f260 114d b9c7 621a 30d9 40f3 87d8 5eea 4881 34bc 24f1 475c b3c8 f5ce af0b 7ccb ea9c 4369 9513 e31f d417
 dc3d 9ed0 641e 29c1 f2fb 7cbf 231a f1b4 6a76 0ef6 3277 9327 d955 43b3 826f 61cf 8308 69f2 b8cd 3743 b872 13a9 18e3 5c8f d79a
 1ed0 9099 9a7a 3c0e 85c5 88e3 1ee6 b990 d0a6 9d1a dd64 51f4 13d9 3d41 0f45 027b 1a20 4720 be6f 61e4 6321 70b3 691f 6690 12a6
 78cd 2453 a4bc b137 2544 638d 63ad b5e8 6706 6540 82bc 9ea4 0d2d 5411 9ca9 50f6 43a4 adc4 af5c 579c f482 a2d2 ac0e f98c 1f4f
 a1fc fb1c cde9 1ad8 8d86 33b1 8edb c445 5862 ea91 7b84 e97c de95 e2f5 3f9c 6b68 1130 3fd0 e6e3 071b 4a8e d6f2 a17c d82e b28e
 9281 2103 dd90 973f c178 6907 daa0 bb3f d4f6 c3a4 630a 4768 772d f36b 910d 9935 37e3 5c28 c83a fa3c d00b 522d fa4a be13 f692
 d342 44c0 faae 375b f6a1 aed7 baed c33e 9cc3 c7fb 8b1f 9ca6 c568 62a9 23a2 3400 db05 16e4 47c0 5075 ecfa 2f82 ebc8 0ae8 c8f9
 98b8 5484 4111 d701 0189 47b9 9f79 6f9c 5bdf 1bf5 e705 cad5 aa2d 6b54 6e71 e8ef 659e 2484 f47b 78b3 f58c a67f f8e8 5612 5cf7
 caa1 135b 3d54 5556 f5f2 483a 9aec 8e1e 2c70 cc68 cc3a 21de bf89 58eb 0700 433b 680e f622 fb4c 21c7 2787 6481 9a89 4eba 8f26
 2861 bdbc 067e 8895 6b5e 269e 132c 7e08 8cc8 0714 4191 2f58 3d0c ce7e cb20 ca12 122a 5242 b9f3 b054 84fe f205 670a 116d 7f25
 907c f9ee 82a1 3369 aa86 0041 f72d 636d db98 1892 f3ef 80b3 c6e7 d4b7 872a 3ef3 7d42 da49 7041 0990 ccbe b4f1 d098 8c1a 9bad
 0cbd 582a 5aa4 382b 83fb 6bc3 ccb8 2fc7 9799 e925 13ca 6f0e 901c 59c0 c77f f631 9b8c ae93 b61f 1766 4d2b d950 a213 e9a6 3a8c
 a4d0 a5ef 68d3 2dce 99e8 5218 c649 ece3 53f4 5f0c 5fbd ced4 d928 35fd bb9f d126 dad8 4a6b 9ead f7ae 8be1 92b9 fd0d b5ec 10ee
 710f 26ee f300 0d51 5299 22a4 264b 62d6 70ae 3a12 0397 c82f 9036 2a59 a500 b182 c5c4 29ec 7750 ef48 283f c875 bddb 98b8 346a
 817d 37c7 5024 9db3 2201 0840 04be 946c 5fc8 281f 977f 308f ca2b b3c2 52c6 1c13 c8c1 1202 f57c 714b 1a63 b8ad 8a04 8b1b e330
 883a 16e6 81be 4251 03e6 87cd 0e16 4907 ae9d 94f5 63c9 0ee5 937d ab21 3383 028b 01b3 f1c1 7eb1 7864 913a 75ce 2536 bfa5 2dbf
 9c39 dba8 9953 b289 6c23 2571 bc40 e3a0 0ed1 56cc dcd0 2895 b1b3 2ff7 7dbb cfdc cd58 c7e3 430e d898 3748 3dc2 fb61 0912 7b12
 bb50 e2d4 22b8 49b4 c1f1 f376 6979 fc4b 84e2 fad5 2430 5ee0 3b78 dc24 b8bd 76e5 af94 81bf 12f1 50b1 5f5e b4ff 3ce5 15ef 57bb
 c36b e051 47ab 0eba 30ea 55d4 1339 97c3 fd36 e846 bd54 f3cc 6339 6d54 830e c088 8b1f cce9 be9f b4e4 7a87 12ea 988a 6aad de69
 40cd 89a9 1228 1d90 b77d a6a6 c2b4 7066 ee2e 4ebb cd71 f1d5 bbc2 a0f1 d33e 4fb3 938f a6ff 2333 8b7e 52de 0213 8a9f a0e7 7b46
 d767 9883 211c 6739 7530 e343 7949 4aa2 30e3 9035 1255 c7c4 18a6 d26e 3567 dcf8 eac3 a77c 9ce6 998d c684 dd32 b9d0 cd9e f0ce
 d5b9 a43c 2954 4e14 9859 369e 99af ac9e c255 706a 5fc8 db64 930b 1d5e 7f9f 3a70 ff57 2ec1 0a37 b08f 3908 fa3f c458 3c1f 214d
Looking through the text above, I think I have found the password. I am just having trouble with a username.
Oh drats! They are onto us! We could get kicked out soon!
Quick! Print the username to the screen so we can close are backdoor and log into the account directly!
You have to find another way other than echo!
```

Well, there is a command for showing the username ```whoami``` (man page says: "print effective userid"):
```bash
~/executables$ whoami
l33th4x0r
Perfect! One second!
Okay, I think I have got what we are looking for. I just need to to copy the file to a place we can read.
Try copying the file called TopSecret in tmp directory into the passwords folder.
~/$ cp /tmp/TopSecret passwords/
Server shutdown in 10 seconds...
Quick! go read the file before we lose our connection!
```

Lets hurry up now:
```bash
~/$ cd passwords
~/passwords$ ls
TopSecret
~/passwords$ cat TopSecret
Major General John M. Schofield's graduation address to the graduating class of 1879 at West Point is as follows: The discipline which makes the soldiers of a free country reliable in battle is not to be gained by harsh or tyrannical treatment.On the contrary, such treatment is far more likely to destroy than to make an army.It is possible to impart instruction and give commands in such a manner and such a tone of voice as to inspire in the soldier no feeling butan intense desire to obey, while the opposite manner and tone of voice cannot fail to excite strong resentment and a desire to disobey.The one mode or other of dealing with subordinates springs from a corresponding spirit in the breast of the commander.He who feels the respect which is due to others, cannot fail to inspire in them respect for himself, while he who feels,and hence manifests disrespect towards others, especially his subordinates, cannot fail to inspire hatred against himself.
picoCTF{CrUsHeD_It_9edaa84a}
```

We can do it all with a single python script:
```python
#!/usr/bin/env python

from pwn import *
from time import sleep

r = remote('2018shell1.picoctf.com', 33158)

print r.recvuntil('$ ')
r.sendline('ls')
print r.recvuntil('$ ')
r.sendline('cd secret')
print r.recvuntil('$ ')
r.sendline('ls')
print r.recvuntil('$ ')
r.sendline('rm intel_1')
print r.recvuntil('$ ')
r.sendline('rm intel_2')
r.sendline('rm intel_3')
r.sendline('rm intel_4')
r.sendline('rm intel_5')
r.sendline('echo \'Drop it in!\'')
sleep(3)
r.sendline('cd ..')
r.sendline('cd executables')
r.sendline('ls')
print r.recvuntil('$ ')
r.sendline('./dontLookHere')
print r.recvuntil('$ ')
r.sendline('whoami')
print r.recvuntil('$ ')
r.sendline('cd ..')
r.sendline('cp /tmp/TopSecret passwords')
r.sendline('cd passwords')
r.sendline('cat TopSecret')
print r.recvall()
```

Flag: picoCTF{CrUsHeD_It_9edaa84a}
