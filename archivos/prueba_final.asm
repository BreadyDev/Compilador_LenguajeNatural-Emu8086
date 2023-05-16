.model small
.stack 100h

.data

    salto db 10, 13, "$"
	var_num dw ?
	texvar_num db 10, 13, 3 dup('$')
	var_cont dw ?
	texvar_cont db 10, 13, 3 dup('$')
	var_res dw ?
	texvar_res db 10, 13, 3 dup('$')
	var_div dw ?
	texvar_div db 10, 13, 3 dup('$')
	msg0 db 10, 13, "Ingresa un numero", "$"
	msg1 db 10, 13, "Tabla de multiplicar del", "$"
	msg2 db 10, 13, "--------------", "$"
	msg3 db 10, 13, "veces es", "$"
	msg4 db 10, 13, "Es par", "$"
	msg5 db 10, 13, "Es impar", "$"

.code
main proc
    mov ax, @data
    mov ds, ax

	mov ax, 1
	mov var_cont, ax

	mov ax, var_cont
	mov bx, 10
	xor dx, dx
	div bx
	add dl, '0'
	add al, '0'
	mov texvar_cont[2], al
	mov texvar_cont[3], dl

	mov ah, 09h
	mov dx, offset msg0
	int 21h

	mov ah, 09h
	mov dx, offset salto
	int 21h

	mov ah, 01h
	int 21h
	mov ah, 0
	sub al, 30h
	mov var_num, ax

	mov ax, var_num
	mov bx, 10
	xor dx, dx
	div bx
	add dl, '0'
	add al, '0'
	mov texvar_num[2], al
	mov texvar_num[3], dl

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
	mov dx, offset texvar_num+2
	int 21h

	mov ah, 09h
	mov dx, offset salto
	int 21h

	for_0:
	mov ax, 10
	mov bx, var_cont
	cmp ax, bx
	jl end_for_0
		mov ax, var_num
		mov var_res, ax

		mov bx, var_cont
		imul bx
		mov var_res, ax

		mov ax, var_res
		mov bx, 10
		xor dx, dx
		div bx
		add dl, '0'
		add al, '0'
		mov texvar_res[2], al
		mov texvar_res[3], dl

		mov ah, 09h
		mov dx, offset msg2
		int 21h

		mov ah, 09h
		mov dx, offset salto
		int 21h

		mov ah, 09h
		mov dx, offset texvar_cont+2
		int 21h

		mov ah, 09h
		mov dx, offset salto
		int 21h

		mov ah, 09h
		mov dx, offset msg3
		int 21h

		mov ah, 09h
		mov dx, offset salto
		int 21h

		mov ah, 09h
		mov dx, offset texvar_res+2
		int 21h

		mov ah, 09h
		mov dx, offset salto
		int 21h

		mov ax, var_res
		mov var_div, ax

		mov bx, 2
		xor dx, dx
		div bx
		mov var_div, dx

		mov ax, var_div
		mov bx, 10
		xor dx, dx
		div bx
		add dl, '0'
		add al, '0'
		mov texvar_div[2], al
		mov texvar_div[3], dl

		mov ax, var_div
		cmp ax, 0
		jne if_1

			mov ah, 09h
			mov dx, offset msg4
			int 21h

			mov ah, 09h
			mov dx, offset salto
			int 21h

			if_1:

		mov ax, var_div
		cmp ax, 1
		jne if_2

			mov ah, 09h
			mov dx, offset msg5
			int 21h

			mov ah, 09h
			mov dx, offset salto
			int 21h

			if_2:

		inc var_cont

		mov ax, var_cont
		mov bx, 10
		xor dx, dx
		div bx
		add dl, '0'
		add al, '0'
		mov texvar_cont[2], al
		mov texvar_cont[3], dl

		jmp for_0

		end_for_0:

    mov ah, 4Ch
    int 21h
main endp
end main
	
	
		
		
		
		
