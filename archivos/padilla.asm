.model small
.stack 100h

.data

    salto db 10, 13, "$"
	var_var_a dw ?
	var_var_b dw ?
	msg0 db 10, 13, "adasdas", "$"
	msg1 db 10, 13, "aksjfdkajskfd", "$"
	msg2 db 10, 13, " asdas das 2", "$"
	msg3 db 10, 13, "El valor de b", "$"

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

	mov ah, 09h
	mov dx, offset msg1
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
	mov ah, 0
	sub al, 30h
	mov var_var_a, ax

	mov ah, 09h
	mov dx, offset salto
	int 21h

	mov ah, 09h
	mov dx, offset msg3
	int 21h

	mov ah, 09h
	mov dx, offset salto
	int 21h

	mov ah, 01h
	int 21h
	mov ah, 0
	sub al, 30h
	mov var_var_b, ax

	mov ah, 09h
	mov dx, offset salto
	int 21h

	mov ah, 02h
	mov dx, var_var_a
	add dx, 30h
	int 21h

	mov ah, 09h
	mov dx, offset salto
	int 21h

	mov ax, 8

	add ax, 9

	mov var_var_a, ax

	mov ax, 5

	mov var_var_b, ax

	mov ah, 02h
	mov dx, var_var_a
	add dx, 30h
	int 21h

	mov ah, 09h
	mov dx, offset salto
	int 21h

	mov ah, 02h
	mov dx, var_var_b
	add dx, 30h
	int 21h

	mov ah, 09h
	mov dx, offset salto
	int 21h

    mov ah, 4Ch
    int 21h
main endp
end main
