.model small
.stack 100h

.data

    salto db 10, 13, "$"
	var_var1 db 100 dup('$')
	msg0 db 10, 13, "Escribe un texto: ", "$"
	msg1 db 10, 13, "escribiste: ", "$"
	var_var2 dw ?
	msg2 db 10, 13, "Escribe un numero: ", "$"
	msg3 db 10, 13, "escribiste: ", "$"

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

	mov ah, 0Ah
	mov dx, offset var_var1
	mov cx, 99
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
	mov dx, offset var_var1+2
	int 21h

	mov ah, 09h
	mov dx, offset salto
	int 21h

	mov ah, 09h
	mov dx, offset msg2
	int 21h

	mov ah, 09h
	mov dx, offset salto
	int 21h

	mov ah, 01h
	int 21h
	sub al, 30h
	mov var_var2, ax

	mov ah, 09h
	mov dx, offset salto
	int 21h

	mov ah, 09h
	mov dx, offset msg3
	int 21h

	mov ah, 09h
	mov dx, offset salto
	int 21h

	mov ah, 02h
	mov dx, var_var2
	add dx, 30h
	int 21h

	mov ah, 09h
	mov dx, offset salto
	int 21h

    mov ah, 4Ch
    int 21h
main endp
end main
	
