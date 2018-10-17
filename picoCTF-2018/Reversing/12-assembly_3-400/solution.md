# Problem
What does asm3(0xf238999b,0xda0f9ac5,0xcc85310c) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. [Source](https://2018shell1.picoctf.com/static/8574a4801ca14ef4666bc4a6e5f694c2/end_asm_rev.S) located in the directory at /problems/assembly-3_2_504fe35f4236db611941d162e2abc6b9.

## Hints:
more(?) [registers](https://wiki.skullsecurity.org/index.php?title=Registers)

## Solution:

Lets download the file:
```bash
wget https://2018shell1.picoctf.com/static/8574a4801ca14ef4666bc4a6e5f694c2/end_asm_rev.S
cat end_asm_rev.S
```

```asm
.intel_syntax noprefix
.bits 32
	
.global asm3

asm3:
	push   	ebp
	mov    	ebp,esp
	mov	eax,0xb6
	xor	al,al
	mov	ah,BYTE PTR [ebp+0x8]
	sal	ax,0x10
	sub	al,BYTE PTR [ebp+0xf]
	add	ah,BYTE PTR [ebp+0xd]
	xor	ax,WORD PTR [ebp+0x12]
	mov	esp, ebp
	pop	ebp
	ret
```

We can see that the function takes three parameters: [ebp+0x8], [ebp+0xc] and (probably) [ebp+0x10].

Lets try to reverse it:
```c
asm3(int v1, v2, v3) {
	a = 0xb6;				// mov	eax,0xb6
	a &= 0xFFFFFF00;		// xor	al,al

	// mov	ah,BYTE PTR [ebp+0x8]
	a &= 0xFFFF00FF;		
	a |= ((v1 & 0x000000FF) << 8);

	a &= 0xFFFF0000;		// effectively the outcome of - sal	ax,0x10

	// sub	al,BYTE PTR [ebp+0xf]
	a = a & 0xFFFFFF00 | (a & 0x000000FF - ((v2 & 0xFF000000) >> 24));

	// add	ah,BYTE PTR [ebp+0xd]
	a = a & 0xFFFF00FF | (((a & 0xFFFF00FF) >> 8) - ((v2 & 0x0000FF00) >> 8)) << 8;

	// xor	ax,WORD PTR [ebp+0x12]
	a ^= ((v3 & 0xFFFF0000) >> 16);

	return a;
}
```

Lets "debug" asm3(0xf238999b,0xda0f9ac5,0xcc85310c):
```c
asm3(int 0xf238999b, 0xda0f9ac5, 0xcc85310c) {
	a = 0xb6;				// mov	eax,0xb6
	a &= 0xFFFFFF00;		// xor	al,al

	// a now equals 0x0

	// mov	ah,BYTE PTR [ebp+0x8]
	a &= 0xFFFF00FF;		
	a |= (0xf238999b & 0x000000FF);

	// a now equals 0x00009b00

	a &= 0xFFFF0000;		// effectively the outcome of - sal	ax,0x10

	// a now equals 0x0 again

	// sub	al,BYTE PTR [ebp+0xf]
	a = a & 0xFFFFFF00 | (a & 0x000000FF - ((0xda0f9ac5 & 0xFF000000) >> 24));

	// a now is 0x26

	// add	ah,BYTE PTR [ebp+0xd]
	a = a & 0xFFFF00FF | (((a & 0xFFFF00FF) >> 8) - ((0xda0f9ac5 & 0x0000FF00) >> 8)) << 8;

	// a now is 0x9a26

	// xor	ax,WORD PTR [ebp+0x12]
	a ^= ((0xcc85310c & 0xFFFF0000) >> 16);

	// a gets 1001101000100110 ^ 
	//        1100110010000101 = 
	//        0101011010100011 = 0x56a3
	return a;
}
```

Flag: 0x56a3
