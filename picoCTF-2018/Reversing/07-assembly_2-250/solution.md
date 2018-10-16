# Problem
What does asm2(0x6,0x28) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. [Source](https://2018shell1.picoctf.com/static/69e4ae9f3b62f70070a97e58168be574/loop_asm_rev.S) located in the directory at /problems/assembly-2_0_24775b87ffbbe8e643da10e71018f275.

## Hints:
assembly [conditions](https://www.tutorialspoint.com/assembly_programming/assembly_conditions.htm)

## Solution:

First download the source and look at it
```bash
wget https://2018shell1.picoctf.com/static/69e4ae9f3b62f70070a97e58168be574/loop_asm_rev.S
cat loop_asm_rev.S
```

```asm
.intel_syntax noprefix
.bits 32
	
.global asm2

asm2:
	push   	ebp
	mov    	ebp,esp
	sub    	esp,0x10
	mov    	eax,DWORD PTR [ebp+0xc]
	mov 	DWORD PTR [ebp-0x4],eax
	mov    	eax,DWORD PTR [ebp+0x8]
	mov	DWORD PTR [ebp-0x8],eax
	jmp    	part_b
part_a:	
	add    	DWORD PTR [ebp-0x4],0x1
	add	DWORD PTR [ebp+0x8],0x8f
part_b:	
	cmp    	DWORD PTR [ebp+0x8],0x8f90
	jle    	part_a
	mov    	eax,DWORD PTR [ebp-0x4]
	mov	esp,ebp
	pop	ebp
	ret

```

We can see that the function takes one parameter: [ebp+0x8]. [ebp+0xc].

Lets try to reverse it:
```c
asm2(int v1, v2) {
	local2 = v2
	local1 = v1

	GOTO part_b

part_a:
	local2++;
	v1 += 0x8f

part_b:
	if (v1 <= 0x8f90)
		GOTO part_a

	return local2;
}
```

Now, if we call asm2(0x6, 0x28), the loop will iterate [(0x8f90 - 0x6) / 0x8f] times, which is 0x128. In the last iteration local2 will be increased to 0x129 and the program will return.

Flag: 0x129
