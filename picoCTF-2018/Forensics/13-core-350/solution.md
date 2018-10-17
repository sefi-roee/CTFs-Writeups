# Problem
This [program](https://2018shell1.picoctf.com/static/21896a776bfc5ba11a69a98c03e616e2/print_flag) was about to print the flag when it died. Maybe the flag is still in this [core](https://2018shell1.picoctf.com/static/21896a776bfc5ba11a69a98c03e616e2/core) file that it dumped? Also available at /problems/core_0_28700fe29cea151d6a3350f244f342b2 on the shell server.

## Hints:
What is a core file?

You may find this [reference](http://darkdust.net/files/GDB%20Cheat%20Sheet.pdf) helpful.

Try to figure out where the flag was read into memory using the disassembly and [strace](https://linux.die.net/man/1/strace).

You should study the format options on the cheat sheet and use the examine (x) or print (p) commands. disas may also be useful.

## Solution:
First, we download the files:
```bash
wget https://2018shell1.picoctf.com/static/21896a776bfc5ba11a69a98c03e616e2/print_flag
wget https://2018shell1.picoctf.com/static/21896a776bfc5ba11a69a98c03e616e2/core
chmod +x ./print_flag
```

A core file is a dump of the process memory at the moment of a crash (probably).

Lets debug using this file
```bash
gdb ./print_flag ./core

gdb-peda$ disas
Dump of assembler code for function print_flag:
=> 0x080487c1 <+0>:	push   ebp
   0x080487c2 <+1>:	mov    ebp,esp
   0x080487c4 <+3>:	sub    esp,0x18
   0x080487c7 <+6>:	mov    DWORD PTR [ebp-0xc],0x539
   0x080487ce <+13>:	mov    eax,DWORD PTR [ebp-0xc]
   0x080487d1 <+16>:	mov    eax,DWORD PTR [eax*4+0x804a080]
   0x080487d8 <+23>:	sub    esp,0x8
   0x080487db <+26>:	push   eax
   0x080487dc <+27>:	push   0x804894c
   0x080487e1 <+32>:	call   0x8048410 <printf@plt>
   0x080487e6 <+37>:	add    esp,0x10
   0x080487e9 <+40>:	nop
   0x080487ea <+41>:	leave  
   0x080487eb <+42>:	ret    
End of assembler dump.
```

We can see that ```printf()``` is about to being called with parameters: ```0x804894c```, ```[eax*4+0x804a080]```.

Lets examine those.

```bash
gdb-peda$ x/s 0x804894c
0x804894c:	"your flag is: picoCTF{%s}\n"
gdb-peda$ x/wx $eax*4+0x804a080
0x8053cbc <strs+39996>:	0x080b5a60
gdb-peda$ x/s 0x080b5a60
0x80b5a60:	"b87e064dba532c386f964435e5e65fc0"
```

Got the flag!

Flag: picoCTF{b87e064dba532c386f964435e5e65fc0}