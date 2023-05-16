.model small
.stack 100h

.data

    salto db 10, 13, "$"
	var_var1 db 100 dup('$')
	var0 db 10, 13, 'Texto de prueba', "$"
	len_var0 equ $-var0
	var_var2 dw ?
	var_var3 dw ?

.code
main proc
    mov ax, @data
    mov ds, ax

	mov si, offset var0
	mov di, offset var_var1
	mov cx, len_var0

	ciclo0:
		mov al, [si]
		mov [di], al
		inc si
		inc di
		loop ciclo0:

	mov ah, 09h
	mov dx, offset var_var1+2
	int 21h

	mov ah, 09h
	mov dx, offset salto
	int 21h

	mov ax, 2

	mov bx, 2
	imul bx

	mov var_var2, ax

	mov ax, var_var2

	add ax, 2

	mov var_var3, ax

	mov ah, 02h
	mov dx, var_var2
	add dx, 30h
	int 21h

	mov ah, 09h
	mov dx, offset salto
	int 21h

	mov ah, 02h
	mov dx, var_var3
	add dx, 30h
	int 21h

	mov ah, 09h
	mov dx, offset salto
	int 21h

    mov ah, 4Ch
    int 21h
main endp
end main
	
