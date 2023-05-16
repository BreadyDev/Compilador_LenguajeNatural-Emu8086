.model small
.stack 100h

.data

    salto db 10, 13, "$"     
    var_var1  db 100 dup('$')
	var1 db 'Texto de prueba', "$"
	len_var1 equ $-var1
.code
main proc
    mov ax, @data
    mov ds, ax     
                   
    mov si, offset var1
    mov di, offset var_var1 
    mov cx, len_var1
    
    ciclo:
        mov al, [si]
        mov [di], al
        inc si
        inc di
        loop ciclo:
          
    mov dx, offset var1
    mov ah, 09h
    int 21h
    
    mov dx, offset salto
    mov ah, 09h
    int 21h 
    
    mov dx, offset var_var1
    mov ah, 09h
    int 21h


    mov ah, 4Ch
    int 21h
main endp
end main
	
