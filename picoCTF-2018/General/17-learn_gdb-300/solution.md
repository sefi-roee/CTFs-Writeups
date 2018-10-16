# Problem
Using a debugging tool will be extremely useful on your missions. Can you run this [program](https://2018shell1.picoctf.com/static/999e37c9737d95c105ea29ae5b3fac1f/run) in gdb and find the flag? You can find the file in /problems/learn-gdb_3_f1f262d9d48b9ff39efc3bc092ea9d7b on the shell server.

## Hints:
Try setting breakpoints in gdb

Try and find a point in the program after the flag has been read into memory to break on

Where is the flag being written in memory?

## Solution:

First, we download the file and try to execute it
```bash
wget https://2018shell1.picoctf.com/static/999e37c9737d95c105ea29ae5b3fac1f/run
chmod +x ./run
./run

Decrypting the Flag into global variable 'flag_buf'
.....................................
Finished Reading Flag into global variable 'flag_buf'. Exiting.
```

After few seconds it's done.

Lets look at the disassembly:
```bash
gdb-peda$ disas main
Dump of assembler code for function main:
   0x00000000004008c9 <+0>:	push   rbp
   0x00000000004008ca <+1>:	mov    rbp,rsp
   0x00000000004008cd <+4>:	sub    rsp,0x10
   0x00000000004008d1 <+8>:	mov    DWORD PTR [rbp-0x4],edi
   0x00000000004008d4 <+11>:	mov    QWORD PTR [rbp-0x10],rsi
   0x00000000004008d8 <+15>:	mov    rax,QWORD PTR [rip+0x200af9]        # 0x6013d8 <stdout@@GLIBC_2.2.5>
   0x00000000004008df <+22>:	mov    ecx,0x0
   0x00000000004008e4 <+27>:	mov    edx,0x2
   0x00000000004008e9 <+32>:	mov    esi,0x0
   0x00000000004008ee <+37>:	mov    rdi,rax
   0x00000000004008f1 <+40>:	call   0x400650 <setvbuf@plt>
   0x00000000004008f6 <+45>:	mov    edi,0x4009d0
   0x00000000004008fb <+50>:	call   0x400600 <puts@plt>
   0x0000000000400900 <+55>:	mov    eax,0x0
   0x0000000000400905 <+60>:	call   0x400786 <decrypt_flag>
   0x000000000040090a <+65>:	mov    edi,0x400a08
   0x000000000040090f <+70>:	call   0x400600 <puts@plt>
   0x0000000000400914 <+75>:	mov    eax,0x0
   0x0000000000400919 <+80>:	leave  
   0x000000000040091a <+81>:	ret    
End of assembler dump.
gdb-peda$ disas decrypt_flag 
Dump of assembler code for function decrypt_flag:
   0x0000000000400786 <+0>:	push   rbp
   0x0000000000400787 <+1>:	mov    rbp,rsp
   0x000000000040078a <+4>:	sub    rsp,0x30
   0x000000000040078e <+8>:	mov    rax,QWORD PTR fs:0x28
   0x0000000000400797 <+17>:	mov    QWORD PTR [rbp-0x8],rax
   0x000000000040079b <+21>:	xor    eax,eax
   0x000000000040079d <+23>:	mov    edi,0x2f
   0x00000000004007a2 <+28>:	call   0x400640 <malloc@plt>
   0x00000000004007a7 <+33>:	mov    QWORD PTR [rip+0x200c3a],rax        # 0x6013e8 <flag_buf>
   0x00000000004007ae <+40>:	mov    rax,QWORD PTR [rip+0x200c33]        # 0x6013e8 <flag_buf>
   0x00000000004007b5 <+47>:	test   rax,rax
   0x00000000004007b8 <+50>:	jne    0x4007ce <decrypt_flag+72>
   0x00000000004007ba <+52>:	mov    edi,0x4009a8
   0x00000000004007bf <+57>:	call   0x400600 <puts@plt>
   0x00000000004007c4 <+62>:	mov    edi,0xffffffff
   0x00000000004007c9 <+67>:	call   0x400660 <exit@plt>
   0x00000000004007ce <+72>:	mov    BYTE PTR [rbp-0xe],0x0
   0x00000000004007d2 <+76>:	mov    DWORD PTR [rbp-0x24],0x2
   0x00000000004007d9 <+83>:	mov    DWORD PTR [rbp-0x20],0x0
   0x00000000004007e0 <+90>:	mov    DWORD PTR [rbp-0x1c],0x0
   0x00000000004007e7 <+97>:	jmp    0x400889 <decrypt_flag+259>
   0x00000000004007ec <+102>:	mov    edi,0x2e
   0x00000000004007f1 <+107>:	call   0x4005f0 <putchar@plt>
   0x00000000004007f6 <+112>:	mov    edi,0x3d090
   0x00000000004007fb <+117>:	mov    eax,0x0
   0x0000000000400800 <+122>:	call   0x400670 <usleep@plt>
   0x0000000000400805 <+127>:	mov    eax,DWORD PTR [rbp-0x1c]
   0x0000000000400808 <+130>:	cdqe   
   0x000000000040080a <+132>:	movzx  eax,BYTE PTR [rax+0x601080]
   0x0000000000400811 <+139>:	mov    BYTE PTR [rbp-0x10],al
   0x0000000000400814 <+142>:	movzx  eax,BYTE PTR [rbp-0x10]
   0x0000000000400818 <+146>:	cmp    al,0x30
   0x000000000040081a <+148>:	jne    0x400834 <decrypt_flag+174>
   0x000000000040081c <+150>:	mov    eax,DWORD PTR [rbp-0x1c]
   0x000000000040081f <+153>:	add    eax,0x1
   0x0000000000400822 <+156>:	cdqe   
   0x0000000000400824 <+158>:	movzx  eax,BYTE PTR [rax+0x601080]
   0x000000000040082b <+165>:	mov    BYTE PTR [rbp-0x10],al
   0x000000000040082e <+168>:	mov    BYTE PTR [rbp-0xf],0x0
   0x0000000000400832 <+172>:	jmp    0x400846 <decrypt_flag+192>
   0x0000000000400834 <+174>:	mov    eax,DWORD PTR [rbp-0x1c]
   0x0000000000400837 <+177>:	add    eax,0x1
   0x000000000040083a <+180>:	cdqe   
   0x000000000040083c <+182>:	movzx  eax,BYTE PTR [rax+0x601080]
   0x0000000000400843 <+189>:	mov    BYTE PTR [rbp-0xf],al
   0x0000000000400846 <+192>:	lea    rax,[rbp-0x10]
   0x000000000040084a <+196>:	mov    edx,0x10
   0x000000000040084f <+201>:	mov    esi,0x0
   0x0000000000400854 <+206>:	mov    rdi,rax
   0x0000000000400857 <+209>:	call   0x400630 <strtol@plt>
   0x000000000040085c <+214>:	mov    QWORD PTR [rbp-0x18],rax
   0x0000000000400860 <+218>:	mov    rdx,QWORD PTR [rip+0x200b81]        # 0x6013e8 <flag_buf>
   0x0000000000400867 <+225>:	mov    eax,DWORD PTR [rbp-0x20]
   0x000000000040086a <+228>:	cdqe   
   0x000000000040086c <+230>:	add    rax,rdx
   0x000000000040086f <+233>:	mov    rdx,QWORD PTR [rbp-0x18]
   0x0000000000400873 <+237>:	add    edx,0x2b
   0x0000000000400876 <+240>:	mov    BYTE PTR [rax],dl
   0x0000000000400878 <+242>:	add    DWORD PTR [rbp-0x20],0x1
   0x000000000040087c <+246>:	add    DWORD PTR [rbp-0x24],0x1
   0x0000000000400880 <+250>:	mov    eax,DWORD PTR [rbp-0x24]
   0x0000000000400883 <+253>:	add    eax,0x2
   0x0000000000400886 <+256>:	add    DWORD PTR [rbp-0x1c],eax
   0x0000000000400889 <+259>:	cmp    DWORD PTR [rbp-0x1c],0x352
   0x0000000000400890 <+266>:	jle    0x4007ec <decrypt_flag+102>
   0x0000000000400896 <+272>:	mov    rdx,QWORD PTR [rip+0x200b4b]        # 0x6013e8 <flag_buf>
   0x000000000040089d <+279>:	mov    eax,DWORD PTR [rbp-0x20]
   0x00000000004008a0 <+282>:	cdqe   
   0x00000000004008a2 <+284>:	add    rax,rdx
   0x00000000004008a5 <+287>:	mov    BYTE PTR [rax],0x0
   0x00000000004008a8 <+290>:	mov    edi,0xa
   0x00000000004008ad <+295>:	call   0x4005f0 <putchar@plt>
   0x00000000004008b2 <+300>:	nop
   0x00000000004008b3 <+301>:	mov    rax,QWORD PTR [rbp-0x8]
   0x00000000004008b7 <+305>:	xor    rax,QWORD PTR fs:0x28
   0x00000000004008c0 <+314>:	je     0x4008c7 <decrypt_flag+321>
   0x00000000004008c2 <+316>:	call   0x400610 <__stack_chk_fail@plt>
   0x00000000004008c7 <+321>:	leave  
   0x00000000004008c8 <+322>:	ret    
End of assembler dump.
```

We can set a breakpoint right before ```decrypt_flag()``` returns, and print the flag from the buffer.

Using this gdbinit file
```
break *0x00000000004008c8
run
print (char *)flag_buf
```

```bash
gdb -x ./gdbinit ./run

Breakpoint 1, 0x00000000004008c8 in decrypt_flag ()
$1 = 0x602260 "picoCTF{gDb_iS_sUp3r_u53fuL_efaa2b29}"
```

OK!

Flag: picoCTF{gDb_iS_sUp3r_u53fuL_efaa2b29}