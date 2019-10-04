asm1:
	push   ebp
	mov    ebp,esp
	cmp    DWORD PTR [ebp+0x8],0x35d
	jg     0x512 <asm1+37>
	cmp    DWORD PTR [ebp+0x8],0x133
	jne    0x50a <asm1+29>
	mov    eax,DWORD PTR [ebp+0x8]
	add    eax,0xb
	jmp    0x529 <asm1+60>
	mov    eax,DWORD PTR [ebp+0x8]
	sub    eax,0xb
	jmp    0x529 <asm1+60>
	cmp    DWORD PTR [ebp+0x8],0x53e
	jne    0x523 <asm1+54>
	mov    eax,DWORD PTR [ebp+0x8]
	sub    eax,0xb
	jmp    0x529 <asm1+60>
	mov    eax,DWORD PTR [ebp+0x8]
	add    eax,0xb
	pop    ebp
	ret    

