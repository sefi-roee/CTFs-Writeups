# Problem
Can you spot the difference? [kitters](https://2019shell1.picoctf.com/static/473cf765877f28edf95140f90cd76b59/kitters.jpg) [cattos](https://2019shell1.picoctf.com/static/473cf765877f28edf95140f90cd76b59/cattos.jpg). They are also available at /problems/whats-the-difference_0_00862749a2aeb45993f36cc9cf98a47a on the shell server

## Hints:

How do you find the difference between two files?

Dumping the data from a hex editor may make it easier to compare.

## Solution:

First, let's get the files:
```bash
wget https://2019shell1.picoctf.com/static/473cf765877f28edf95140f90cd76b59/kitters.jpg
wget https://2019shell1.picoctf.com/static/473cf765877f28edf95140f90cd76b59/cattos.jpg
```

Let's try a simple script:
```python
kitters = open('./kitters.jpg', 'rb').read()
cattos  = open('./cattos.jpg', 'rb').read()

s = ''                                                           
for i in range(len(cattos)):                                                                                                                                                                      
    if kitters[i] != cattos[i]:
        s += cattos[i]

print s
```

Nice.

Flag: picoCTF{th3yr3_a5_d1ff3r3nt_4s_bu773r_4nd_j311y_aslkjfdsalkfslkflkjdsfdszmz10548}
