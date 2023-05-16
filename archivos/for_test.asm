.model small
.stack 100h

.data

    salto db 10, 13, "$"
	var_num1 dw ?
	texvar_num1 db 10, 13, 3 dup('$')
	var_num2 dw ?
	texvar_num2 db 10, 13, 3 dup('$')
	msg0 db 10, 13, "desde", "$"
	msg1 db 10, 13, "hasta", "$"

.code
main proc
    mov ax, @data
    mov ds, ax

	mov ax, 1
	mov var_num1, ax

	mov ax, var_num1
	mov bx, 10
	xor dx, dx
	div bx
	add dl, '0'
	add al, '0'
	mov texvar_num1[2], al
	mov texvar_num1[3], dl

	mov ax, 10
	mov var_num2, ax

	mov ax, var_num2
	mov bx, 10
	xor dx, dx
	div bx
	add dl, '0'
	add al, '0'
	mov texvar_num2[2], al
	mov texvar_num2[3], dl

	mov ah, 09h
	mov dx, offset msg0
	int 21h

	mov ah, 09h
	mov dx, offset salto
	int 21h

	mov ah, 09h
	mov dx, offset texvar_num1+2
	int 21h

	mov ah, 09h
	mov dx, offset salto
	int 21h

	mov ah, 09h
	mov dx, offset msg1
	int 21h

	mov ah, 09h
	mov dx, offset salto
	int 21h

	mov ah, 09h
	mov dx, offset texvar_num2+2
	int 21h

	mov ah, 09h
	mov dx, offset salto
	int 21h

	for_0:
	mov ax, 10
	mov bx, var_num1
	cmp ax, bx
	jl end_for_0
		mov ah, 09h
		mov dx, offset texvar_num1+2
		int 21h

		mov ah, 09h
		mov dx, offset salto
		int 21h

		inc var_num1

		mov ax, var_num1
		mov bx, 10
		xor dx, dx
		div bx
		add dl, '0'
		add al, '0'
		mov texvar_num1[2], al
		mov texvar_num1[3], dl

		jmp for_0

		end_for_0:

    mov ah, 4Ch
    int 21h
main endp
end main
	
	
