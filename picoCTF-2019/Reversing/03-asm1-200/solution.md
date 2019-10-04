# Problem
What does asm1(0x53e) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. [Source](https://2019shell1.picoctf.com/static/646a8167294d5c95b6446576264f24ab/test.S) located in the directory at /problems/asm1_4_431c7088e03c0028398793773ccf89d7.


## Hints:

assembly [conditions](https://www.tutorialspoint.com/assembly_programming/assembly_conditions.htm)

## Solution:

First download the source and look at it:
```bash
wget https://2019shell1.picoctf.com/static/646a8167294d5c95b6446576264f24ab/test.S
cat test.S
```

```asm
asm1:
    <+0>:   push   ebp
    <+1>:   mov    ebp,esp
    <+3>:   cmp    DWORD PTR [ebp+0x8],0x35d
    <+10>:  jg     0x512 <asm1+37>
    <+12>:  cmp    DWORD PTR [ebp+0x8],0x133
    <+19>:  jne    0x50a <asm1+29>
    <+21>:  mov    eax,DWORD PTR [ebp+0x8]
    <+24>:  add    eax,0xb
    <+27>:  jmp    0x529 <asm1+60>
    <+29>:  mov    eax,DWORD PTR [ebp+0x8]
    <+32>:  sub    eax,0xb
    <+35>:  jmp    0x529 <asm1+60>
    <+37>:  cmp    DWORD PTR [ebp+0x8],0x53e
    <+44>:  jne    0x523 <asm1+54>
    <+46>:  mov    eax,DWORD PTR [ebp+0x8]
    <+49>:  sub    eax,0xb
    <+52>:  jmp    0x529 <asm1+60>
    <+54>:  mov    eax,DWORD PTR [ebp+0x8]
    <+57>:  add    eax,0xb
    <+60>:  pop    ebp
    <+61>:  ret    
```

We can see that the function get 1 parameters: [ebp+0x8]. Let's try to write this as a high-level code:

```c
asm1(int arg) {
    if (arg > 0x35d)
        goto l2;

    if (arg != 0x133)
        goto l1;

    arg += 0xb;
    goto l4;

l1: // asm1+29
    arg -= 0xb;
    goto l4;

l2: // asm1+37
    if (arg != 0x53e)
        goto l3;

    arg -= 0xb;
    goto l4;
    
l3: // asm1+54
    arg += 0xb;

l4: // asm1+60
    return arg;
}

Following this flow, asm1(0x53e) = 0x53e - 0xb = 0x533

Flag: 0x533
