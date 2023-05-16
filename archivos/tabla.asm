.model small
.stack 100h

.data

    salto db 10, 13, "$"
	var_var_num dw ?
	texvar_var_num db 10, 13, 3 dup('$')
	var_cont dw ?
	texvar_cont db 10, 13, 3 dup('$')
	var_res dw ?
	texvar_res db 10, 13, 3 dup('$')
	msg0 db 10, 13, "Ingresa un numero", "$"
	msg1 db 10, 13, "Tabla multiplicar", "$"

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
	mov var_var_num, ax

	mov ax, var_var_num
	mov bx, 10
	xor dx, dx
	div bx
	add dl, '0'
	add al, '0'
	mov texvar_var_num[2], al
	mov texvar_var_num[3], dl

	mov ah, 09h
	mov dx, offset salto
	int 21h

	mov ah, 09h
	mov dx, offset msg1
	int 21h

	mov ah, 09h
	mov dx, offset salto
	int 21h

	mov ax, var_var_num

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

	mov ax, var_cont

	add ax, 1

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
	mov dx, offset texvar_res+2
	int 21h

	mov ah, 09h
	mov dx, offset salto
	int 21h

	mov ax, var_var_num

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

	mov ax, var_cont

	add ax, 1

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
	mov dx, offset texvar_res+2
	int 21h

	mov ah, 09h
	mov dx, offset salto
	int 21h

	mov ax, var_var_num

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

	mov ax, var_cont

	add ax, 1

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
	mov dx, offset texvar_res+2
	int 21h

	mov ah, 09h
	mov dx, offset salto
	int 21h

	mov ax, var_var_num

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

	mov ax, var_cont

	add ax, 1

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
	mov dx, offset texvar_res+2
	int 21h

	mov ah, 09h
	mov dx, offset salto
	int 21h

	mov ax, var_var_num

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

	mov ax, var_cont

	add ax, 1

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
	mov dx, offset texvar_res+2
	int 21h

	mov ah, 09h
	mov dx, offset salto
	int 21h

	mov ax, var_var_num

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

	mov ax, var_cont

	add ax, 1

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
	mov dx, offset texvar_res+2
	int 21h

	mov ah, 09h
	mov dx, offset salto
	int 21h

	mov ax, var_var_num

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

	mov ax, var_cont

	add ax, 1

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
	mov dx, offset texvar_res+2
	int 21h

	mov ah, 09h
	mov dx, offset salto
	int 21h

	mov ax, var_var_num

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

	mov ax, var_cont

	add ax, 1

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
	mov dx, offset texvar_res+2
	int 21h

	mov ah, 09h
	mov dx, offset salto
	int 21h

	mov ax, var_var_num

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

	mov ax, var_cont

	add ax, 1

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
	mov dx, offset texvar_res+2
	int 21h

	mov ah, 09h
	mov dx, offset salto
	int 21h

	mov ax, var_var_num

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

	mov ax, var_cont

	add ax, 1

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
	mov dx, offset texvar_res+2
	int 21h

	mov ah, 09h
	mov dx, offset salto
	int 21h

    mov ah, 4Ch
    int 21h
main endp
end main
	
	
	
	
	
	
	
	
	
	
	
