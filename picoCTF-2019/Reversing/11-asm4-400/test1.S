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