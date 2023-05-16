.MODEL SMALL
.STACK 100h
.DATA
    num DW ?   ; define a word-sized variable
    message DB 'Enter a number: $'
.CODE
    MOV AX, @DATA
    MOV DS, AX  ; initialize data segment
    
    ; display message asking for input
    MOV AH, 09h
    LEA DX, message
    INT 21h
    
    ; read input from user
    MOV AH, 01h
    INT 21h
    SUB AL, 30h  ; convert ASCII value to numeric value
    MOV num, AX  ; store numeric value in variable
    
    ; display the value
    MOV AH, 02h
    MOV Dx, num
    ADD Dx, 30h  ; convert numeric value to ASCII value
    INT 21h  
    
    ; exit program
    MOV AH, 4Ch
    INT 21h
END