Title 'Suma numeros 1'

DATOS SEGMENT
;DECLARAR VARIABLES----------------------
                                                                          
num1 DW ?
num2 DW ?
res DW ?
tex DW ?
                                         
;----------------------------------------

DATOS ENDS 


PILA SEGMENT

    DB 64 DUP(0)
    
PILA ENDS 


CODIGO SEGMENT
                              
INICIO PROC FAR
    
ASSUME DS:DATOS, CS:CODIGO, SS:PILA 

PUSH DS
MOV AX, 0
PUSH AX

MOV AX, DATOS
MOV DS, AX
MOV ES, AX  

;CODIGO DEL PROGRAMA---------------------- 


;----------------------------------------- 

RET
INICIO ENDP
CODIGO ENDS

END INICIO
