# Problem
What does asm0(0xc9,0xb0) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. [Source](https://2018shell1.picoctf.com/static/c443175680c19595c828108c26f48b9f/intro_asm_rev.S) located in the directory at /problems/assembly-0_4_0f197369bfc00a9211504cf65ac31994.

## Hints:
basical assembly [tutorial](https://www.tutorialspoint.com/assembly_programming/assembly_basic_syntax.htm)

assembly [registers](https://www.tutorialspoint.com/assembly_programming/assembly_registers.htm)

## Solution:

First download the source and look at it
```bash
wget https://2018shell1.picoctf.com/static/c443175680c19595c828108c26f48b9f/intro_asm_rev.S
cat intro_asm_rev.S
```

```asm
.intel_syntax noprefix
.bits 32
	
.global asm0

asm0:
	push	ebp
	mov	ebp,esp
	mov	eax,DWORD PTR [ebp+0x8]
	mov	ebx,DWORD PTR [ebp+0xc]
	mov	eax,ebx
	mov	esp,ebp
	pop	ebp	
	ret

```

We can see that the function get 2 parameters: [ebp+0x8], [ebp+0xc].

It just load those parameters, and then override $eax with the second parameter.

If we run asm0(0xc9,0xb0), we will just get 0xb0!

Flag: 0xb0
