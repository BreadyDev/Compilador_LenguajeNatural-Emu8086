.model small
.stack 100h

.data

    salto db 10, 13, "$"
	var_num1 dw ?
	texvar_num1 db 10, 13, 3 dup('$')
	var_num2 dw ?
	texvar_num2 db 10, 13, 3 dup('$')
	var_res dw ?
	texvar_res db 10, 13, 3 dup('$')
	msg0 db 10, 13, "Ingresa el primer numero", "$"
	msg1 db 10, 13, "Ingresa el segundo numero", "$"
	msg2 db 10, 13, "La suma es:", "$"
	msg3 db 10, 13, "La resta es:", "$"
	msg4 db 10, 13, "La multiplicacion es:", "$"
	msg5 db 10, 13, "La division es:", "$"
	msg6 db 10, 13, "El residio es:", "$"
	msg7 db 10, 13, "La elevacion es:", "$"

.code
main proc
    mov ax, @data
    mov ds, ax

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
	mov var_num1, ax

	mov ax, var_num1
	mov bx, 10
	xor dx, dx
	div bx
	add dl, '0'
	add al, '0'
	mov texvar_num1[2], al
	mov texvar_num1[3], dl

	mov ah, 09h
	mov dx, offset salto
	int 21h

	mov ah, 09h
	mov dx, offset msg1
	int 21h

	mov ah, 09h
	mov dx, offset salto
	int 21h

	mov ah, 01h
	int 21h
	mov ah, 0
	sub al, 30h
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
	mov dx, offset salto
	int 21h

	mov ax, var_num1
	mov var_res, ax

	add ax, var_num2
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
	mov dx, offset texvar_res+2
	int 21h

	mov ah, 09h
	mov dx, offset salto
	int 21h

	mov ax, var_num1
	mov var_res, ax

	sub ax, var_num2
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

	mov ax, var_num1
	mov var_res, ax

	mov bx, var_num2
	mul bx
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
	mov dx, offset msg4
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

	mov ax, var_num1
	mov var_res, ax

	mov bx, var_num2
	xor dx, dx
	div bx
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
	mov dx, offset msg5
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

	mov ax, var_num1
	mov var_res, ax

	mov bx, var_num2
	xor dx, dx
	div bx
	mov var_res, dx

	mov ax, var_res
	mov bx, 10
	xor dx, dx
	div bx
	add dl, '0'
	add al, '0'
	mov texvar_res[2], al
	mov texvar_res[3], dl

	mov ah, 09h
	mov dx, offset msg6
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

	mov ax, var_num1
	mov var_res, ax

	mov bx, var_num1
	mov cx, var_num2

	cmp cx, 1
	je elevar_uno_0

	cmp cx, 0
	je elevar_cero_0

	sub cx, 1

	elevar_0:
		mul bx
		loop elevar_0
		jmp fin_elevar_0

	elevar_uno_0:
		mov ax, var_num1
		jmp fin_elevar_0

	elevar_cero_0:
		mov ax, 1
		jmp fin_elevar_0

	fin_elevar_0:

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
	mov dx, offset msg7
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

    mov ah, 4Ch
    int 21h
main endp
end main
	
	
	
	
	
	
	
	
