# Problem
What does asm1(0x76) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. [Source](https://2018shell1.picoctf.com/static/fa95fab402722fc45d8a61ca98cc211d/eq_asm_rev.S) located in the directory at /problems/assembly-1_0_cfb59ef3b257335ee403035a6e42c2ed.

## Hints:
assembly [conditions](https://www.tutorialspoint.com/assembly_programming/assembly_conditions.htm)

## Solution:

First download the source and look at it
```bash
wget https://2018shell1.picoctf.com/static/fa95fab402722fc45d8a61ca98cc211d/eq_asm_rev.S
cat eq_asm_rev.S
```

```asm
.intel_syntax noprefix
.bits 32
	
.global asm1

asm1:
	push	ebp
	mov	ebp,esp
	cmp	DWORD PTR [ebp+0x8],0x98
	jg 	part_a	
	cmp	DWORD PTR [ebp+0x8],0x8
	jne	part_b
	mov	eax,DWORD PTR [ebp+0x8]
	add	eax,0x3
	jmp	part_d
part_a:
	cmp	DWORD PTR [ebp+0x8],0x16
	jne	part_c
	mov	eax,DWORD PTR [ebp+0x8]
	sub	eax,0x3
	jmp	part_d
part_b:
	mov	eax,DWORD PTR [ebp+0x8]
	sub	eax,0x3
	jmp	part_d
	cmp	DWORD PTR [ebp+0x8],0xbc
	jne	part_c
	mov	eax,DWORD PTR [ebp+0x8]
	sub	eax,0x3
	jmp	part_d
part_c:
	mov	eax,DWORD PTR [ebp+0x8]
	add	eax,0x3
part_d:
	pop	ebp
	ret
```

We can see that the function takes one parameter: [ebp+0x8].

Lets try to reverse it:
```c
asm1(int v) {
	if (v > 0x98)
		GOTO part_a

	if (v != 0x8)
		GOTO part_b

	a = v + 0x3

	GOTO part_d

part_a:
	if (v != 0x16)
		GOTO part_c

	a = v - 3

	GOTO part_d

part_b:
	a = v - 3

	GOTO part_d

	... some unreachable code

part_c:
	a = v + 3

part_d:
	return a	
}
```

Now, if we call asm1 with 0x76 it will flow to part_b and return 0x73!

Flag: 0x73
