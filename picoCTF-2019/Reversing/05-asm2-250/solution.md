# Problem
What does asm2(0x10,0x18) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. [Source](https://2019shell1.picoctf.com/static/cc04ba2d1d8ac93ee11cc9a3d45f7064/test.S) located in the directory at /problems/asm2_0_a50f0b17a6f50b50a53305ebd71af535.

## Hints:

assembly [conditions](https://www.tutorialspoint.com/assembly_programming/assembly_conditions.htm)

## Solution:

First download the source and look at it:
```bash
wget https://2019shell1.picoctf.com/static/cc04ba2d1d8ac93ee11cc9a3d45f7064/test.S
cat test.S
```

```asm
asm2:
    <+0>:   push   ebp
    <+1>:   mov    ebp,esp
    <+3>:   sub    esp,0x10
    <+6>:   mov    eax,DWORD PTR [ebp+0xc]
    <+9>:   mov    DWORD PTR [ebp-0x4],eax
    <+12>:  mov    eax,DWORD PTR [ebp+0x8]
    <+15>:  mov    DWORD PTR [ebp-0x8],eax
    <+18>:  jmp    0x50c <asm2+31>
    <+20>:  add    DWORD PTR [ebp-0x4],0x1
    <+24>:  add    DWORD PTR [ebp-0x8],0xcb
    <+31>:  cmp    DWORD PTR [ebp-0x8],0xb693
    <+38>:  jle    0x501 <asm2+20>
    <+40>:  mov    eax,DWORD PTR [ebp-0x4]
    <+43>:  leave  
    <+44>:  ret 
```

We can see that the function gets 2 parameters: [ebp+0x8, ebp+0xc]. Let's try to write this as a high-level code:

```c
asm1(int arg1, int arg2) {
    int a = arg2; // ebp-0x4
    int b = arg1; // ebp-0x8

    while (b <= 0xb693) {
        a += 0x1;
        b += 0xcb;
    }

    return a;
}

Following this flow, asm2(0x10,0x18) = 0x18 + 0x1 * (0xb693 / 0xcb + 1) = 0x18 + 0xe7 = 0xff

Flag: 0xff
