.model small
.stack 100h

.data

    salto db 10, 13, "$"
	var_var1 dw ?
	msg0 db 10, 13, "Escribe un numero", "$"
	msg1 db 10, 13, "Escribiste", "$"
	msg2 db 10, 13, "La variable ahora vale 0", "$"

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
	sub al, 30h
	mov var_var1, ax

	mov ah, 09h
	mov dx, offset salto
	int 21h

	mov ah, 09h
	mov dx, offset msg1
	int 21h

	mov ah, 09h
	mov dx, offset salto
	int 21h

	mov ah, 02h
	mov dx, var_var1
	add dx, 30h
	int 21h

	mov ah, 09h
	mov dx, offset salto
	int 21h

	mov ax, 0

	mov var_var1, ax

	mov ah, 09h
	mov dx, offset msg2
	int 21h

	mov ah, 09h
	mov dx, offset salto
	int 21h

	mov ah, 02h
	mov dx, var_var1
	add dx, 30h
	int 21h

	mov ah, 09h
	mov dx, offset salto
	int 21h

    mov ah, 4Ch
    int 21h
main endp
end main
