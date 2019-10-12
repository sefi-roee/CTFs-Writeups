# Problem
What will asm4("picoCTF_e341d") return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. [Source](https://2019shell1.picoctf.com/static/9e2417680a6f550bd538ac05ccdce088/test.S) located in the directory at /problems/asm4_4_046c448fbb6c43457e9709d33d485bc2.

## Hints:

Treat the Array argument as a pointer

## Solution:

First download the source and look at it:
```bash
wget https://2019shell1.picoctf.com/static/9e2417680a6f550bd538ac05ccdce088/test.S
cat test.S
```

```asm
asm4:
    <+0>:   push   ebp
    <+1>:   mov    ebp,esp
    <+3>:   push   ebx
    <+4>:   sub    esp,0x10
    <+7>:   mov    DWORD PTR [ebp-0x10],0x280
    <+14>:  mov    DWORD PTR [ebp-0xc],0x0
    <+21>:  jmp    0x518 <asm4+27>
    <+23>:  add    DWORD PTR [ebp-0xc],0x1
    <+27>:  mov    edx,DWORD PTR [ebp-0xc]
    <+30>:  mov    eax,DWORD PTR [ebp+0x8]
    <+33>:  add    eax,edx
    <+35>:  movzx  eax,BYTE PTR [eax]
    <+38>:  test   al,al
    <+40>:  jne    0x514 <asm4+23>
    <+42>:  mov    DWORD PTR [ebp-0x8],0x1
    <+49>:  jmp    0x587 <asm4+138>
    <+51>:  mov    edx,DWORD PTR [ebp-0x8]
    <+54>:  mov    eax,DWORD PTR [ebp+0x8]
    <+57>:  add    eax,edx
    <+59>:  movzx  eax,BYTE PTR [eax]
    <+62>:  movsx  edx,al
    <+65>:  mov    eax,DWORD PTR [ebp-0x8]
    <+68>:  lea    ecx,[eax-0x1]
    <+71>:  mov    eax,DWORD PTR [ebp+0x8]
    <+74>:  add    eax,ecx
    <+76>:  movzx  eax,BYTE PTR [eax]
    <+79>:  movsx  eax,al
    <+82>:  sub    edx,eax
    <+84>:  mov    eax,edx
    <+86>:  mov    edx,eax
    <+88>:  mov    eax,DWORD PTR [ebp-0x10]
    <+91>:  lea    ebx,[edx+eax*1]
    <+94>:  mov    eax,DWORD PTR [ebp-0x8]
    <+97>:  lea    edx,[eax+0x1]
    <+100>: mov    eax,DWORD PTR [ebp+0x8]
    <+103>: add    eax,edx
    <+105>: movzx  eax,BYTE PTR [eax]
    <+108>: movsx  edx,al
    <+111>: mov    ecx,DWORD PTR [ebp-0x8]
    <+114>: mov    eax,DWORD PTR [ebp+0x8]
    <+117>: add    eax,ecx
    <+119>: movzx  eax,BYTE PTR [eax]
    <+122>: movsx  eax,al
    <+125>: sub    edx,eax
    <+127>: mov    eax,edx
    <+129>: add    eax,ebx
    <+131>: mov    DWORD PTR [ebp-0x10],eax
    <+134>: add    DWORD PTR [ebp-0x8],0x1
    <+138>: mov    eax,DWORD PTR [ebp-0xc]
    <+141>: sub    eax,0x1
    <+144>: cmp    DWORD PTR [ebp-0x8],eax
    <+147>: jl     0x530 <asm4+51>
    <+149>: mov    eax,DWORD PTR [ebp-0x10]
    <+152>: add    esp,0x10
    <+155>: pop    ebx
    <+156>: pop    ebp
    <+157>: ret    
```

This time we just compile and run it...

Let's beautify the asm file (test1.S):
```asm

SECTION .TEXT
    global asm4

asm4:
    push   ebp
    mov    ebp,esp
    push   ebx
    sub    esp,0x10
    mov    DWORD  [ebp-0x10],0x280
    mov    DWORD  [ebp-0xc],0x0
    jmp    label2
label1:
    add    DWORD  [ebp-0xc],0x1
label2:
    mov    edx,DWORD  [ebp-0xc]
    mov    eax,DWORD  [ebp+0x8]
    add    eax,edx
    movzx  eax,BYTE  [eax]
    test   al,al
    jne    label1
    mov    DWORD  [ebp-0x8],0x1
    jmp    label4
label3:
    mov    edx,DWORD  [ebp-0x8]
    mov    eax,DWORD  [ebp+0x8]
    add    eax,edx
    movzx  eax,BYTE  [eax]
    movsx  edx,al
    mov    eax,DWORD  [ebp-0x8]
    lea    ecx,[eax-0x1]
    mov    eax,DWORD  [ebp+0x8]
    add    eax,ecx
    movzx  eax,BYTE  [eax]
    movsx  eax,al
    sub    edx,eax
    mov    eax,edx
    mov    edx,eax
    mov    eax,DWORD  [ebp-0x10]
    lea    ebx,[edx+eax*1]
    mov    eax,DWORD  [ebp-0x8]
    lea    edx,[eax+0x1]
    mov    eax,DWORD  [ebp+0x8]
    add    eax,edx
    movzx  eax,BYTE  [eax]
    movsx  edx,al
    mov    ecx,DWORD  [ebp-0x8]
    mov    eax,DWORD  [ebp+0x8]
    add    eax,ecx
    movzx  eax,BYTE  [eax]
    movsx  eax,al
    sub    edx,eax
    mov    eax,edx
    add    eax,ebx
    mov    DWORD  [ebp-0x10],eax
    add    DWORD  [ebp-0x8],0x1
label4:
    mov    eax,DWORD  [ebp-0xc]
    sub    eax,0x1
    cmp    DWORD  [ebp-0x8],eax
    jl     label3
    mov    eax,DWORD  [ebp-0x10]
    add    esp,0x10
    pop    ebx
    pop    ebp
    ret    
```

Let's wrap it with a ```c``` code (main.c):
```c
#include <stdio.h>

int main() {
    extern int asm4(char *);
    int ret = asm4("picoCTF_e341d");

    printf("0x%x\n", ret);

    return 0;
}
```

```bash
nasm -f elf test1.S
gcc -m32 test1.o main.c -o test1
./test1
```

Flag: 0x23c
