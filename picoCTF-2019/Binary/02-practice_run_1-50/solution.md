# Problem
You're going to need to know how to run programs if you're going to get out of here. Navigate to /problems/practice-run-1_0_62b61488e896645ebff9b6c97d0e775e on the shell server and run this [program](https://2019shell1.picoctf.com/static/6eba3b66e7a2b786c6c9769711d85663/run_this) to receive a flag.

## Hints:
How do you execute a program in a command line?

## Solution:

Lets download the file:
```bash
wget https://2019shell1.picoctf.com/static/6eba3b66e7a2b786c6c9769711d85663/run_this
```

Let's execute it:
```bash
chmod +x ./run_this
./run_this

ERROR: ld.so: object 'libgtk3-nocsd.so.0' from LD_PRELOAD cannot be preloaded (cannot open shared object file): ignored.
picoCTF{g3t_r3adY_2_r3v3r53}
```

Now lets wrap it with a simple python script:
```python
#!/usr/bin/env python

from pwn import *


debug = 0

user = 'RoeeSefi'
pw = 'UTTE9CQN2idX28W'

if debug:
  p = process('./run_this')
else:
  s = ssh(host = '2019shell1.picoctf.com', user=user, password=pw)

  s.set_working_directory('/problems/practice-run-1_0_62b61488e896645ebff9b6c97d0e775e')
  p = s.process('./run_this')

print p.recvall()
```

Flag: picoCTF{g3t_r3adY_2_r3v3r53}