import re
import os

### Variables

# Numero de linea
i = 1

# Numero de mensaje, elevacion y ciclo
n_msj, n_elev, n_ciclo = 0, 0, 0

# Parentesis abiertos y ultimo bloque abierto
lin_par, fin_bloques = [], []

# Comprobar si se encontro el tipo de la linea
found = False

# Archivo de emu8086
nombre_archivo = "operaciones.txt"

with open("Compilador\\archivos\\base.txt", "r") as texto:
    codigo = texto.read().split("\n")
    
nom = nombre_archivo.replace(".txt","")

lin_var, lin_code = 6, 12

# Expresiones regulares

alpha = re.compile("[A-Za-zÑñ0-9=+-/()<>¿?,.^\"]+")
lenguaje = re.compile("(leer|escribir|si|mientras|para|fin|entero|texto)")
m_title = re.compile("(Title [A-Za-z0-9]+)")
var_dec = re.compile("((entero|decimal|texto) [a-z][a-z0-9]?)")
m_leer = re.compile("(leer [A-Za-z0-9]+)")
m_escribir_texto = re.compile("(escribir [\".*?\"])")
m_escribir_var = re.compile("(escribir [A-Za-z0-9]+)")
m_si = re.compile("si ([A-Za-z0-9]+|[0-9]+) (<|>|==|!=|<=|>=) ([A-Za-z0-9]+|[0-9]+)")
m_mientras = re.compile("mientras ([A-Za-z0-9]+|[0-9]+) (<|>|==|!=|<=|>=) ([A-Za-z0-9]+|[0-9]+)")
m_para = re.compile("para ([A-Za-z0-9]+) hasta ([A-Za-z0-9]+)")
m_valor_a_entero = re.compile("[A-Za-z0-9]+ = ([A-Za-z0-9]+|[0-9]+)( (\+|-|\*|/|%|^) ([A-Za-z0-9]+|[0-9]+))*")
m_valor_a_texto = re.compile("[A-Za-z0-9]+ = (\".*?\")")

# Tabla de variables
variables = [{"name":"", "tipe":"", "value":""}]

# Tabla de errores
errores = (
    "Err-01 : Linea mal declarada",
    "Err-02 : Variable ya declarada",
    "Err-03 : Valor ingresado no apto para la variable",
    "Err-04 : Variable no existente",
    "Err-05 : Caracter desconocido",
    "Err-06 : Declaracion desconocida",
    "Err-07 : Declaracion de inicio faltante",
    "Err-08 : Caracter desconocido",
    "Err-09 : Bloques de codigo no cerrados",
    "Err-10 : Variable sin valor",
    "Err-11 : Variable no apta para la operacion",
    "Err-12 : Bloque de codigo no abierto antes del fin",
    "Err-13 : Tipos no coincidentes"
)

### Funciones ###

def error(n_error, linea):
    print(f"\nError en la linea {i}: \n{linea} \n{errores[n_error]}")
    exit()

# Busca si la variable existe o no
def buscar_nombre_variable(palabra, variables):
    for var in variables:
        if var.get("name") == palabra and variables != [{"name":"", "tipe":"", "value":""}] and not lenguaje.match(palabra):
            return False
    return True

# Buscar posicion var

def buscar_posicion_variable(palabra, variables):
    for i in range(0, len(variables)):
        if variables[i]["name"] == palabra:
            return i

# Añade la variable y su tipo a la tabla de valores
def añadir_variables(linea, variables):
    if variables[0].get("name") == "":
        return [{"name":linea[1], "tipe":linea[0], "value":False}]
    elif buscar_nombre_variable(linea[1], variables):
        variables.append({"name":linea[1], "tipe":linea[0], "value":False})
        return variables
    else:
        error(0, linea)
        
# Leer

def f_leer(linea, variables):
    if not buscar_nombre_variable(linea[1], variables):
        variables[buscar_posicion_variable(linea[1], variables)]["value"] = True
        return variables
    else:
        error(3, linea)
        
# Escribir

def f_escribir(linea, variables, lin):
    if buscar_nombre_variable(linea[1], variables):
        error(3, lin)
    if not (variables[buscar_posicion_variable(linea[1], variables)]["value"]):
        error(9, lin)

# Si y Mientras

def f_comparativo(linea, variables, lin):
    
    ciclo_tipe = [0,0,0,0]
    
    for i in range(1,4,2): 

        if buscar_nombre_variable(linea[i], variables):
            if linea[i].isdigit():
                ciclo_tipe[i] = "entero"
            else:
                error(10, lin)
        else:
            ciclo_tipe[i] = variables[buscar_posicion_variable(linea[i], variables)]["tipe"]
            if not (variables[buscar_posicion_variable(linea[i], variables)]["value"]):
                error(9, lin)
                
            elif ciclo_tipe[i] == "texto":
                error(10, lin)

    if ciclo_tipe[1] != ciclo_tipe[3]:
        error(12, lin)    

# Para

def f_para(linea, variables, lin):#no sea texto la variable
    if buscar_nombre_variable(linea[1], variables):
        error(3, lin)
    if buscar_nombre_variable(linea[3], variables) or linea[3].isnumeric():
        error(3, lin)
    if not (variables[buscar_posicion_variable(linea[1], variables)]["value"]):
        error(9, lin)
        
# Variables

def f_var_dec(linea, variables, lin):
    tipo = variables[buscar_posicion_variable(linea[0], variables)]["tipe"]
    
    if tipo == "entero":
        if m_valor_a_entero.match(lin):
            for i in range(2, len(linea), 2):
                if str(linea[i]).isdigit():
                    print("digito")
                elif not buscar_nombre_variable(linea[i],variables): 
                    if variables[buscar_posicion_variable(linea[i], variables)]["tipe"] == tipo:
                        print("variable entera")
                    else:
                        error(2, lin)
                else:
                    error(3, lin)
            
    elif tipo == "texto":   
        if m_valor_a_texto.match(lin):
            print("texto a variable")
        else:
            error(3, lin)
            
    variables[buscar_posicion_variable(linea[0], variables)]["value"] = True
    return variables

### Lectura del archivo ###

with open(f"Compilador/archivos/{nombre_archivo}", "r") as texto:
    archivo = texto.read().split("\n")
    
### Iteracion del archivo - Analisis lexico/semantico ###
    
for linea in archivo:
    palabra = linea.split(" ")
    
    if alpha.match(palabra[0]):
    
        if palabra[0] in ["entero", "decimal","texto"]:
            if var_dec.match(linea):
                variables = añadir_variables(palabra, variables)
                
                print("variable")
                found = True
            else:
                error(0, linea)
        
        if palabra[0] == "leer":
            if m_leer.match(linea):
                print("leer")
                found = True
            
                variables = f_leer(palabra, variables)
            else:
                error(0, linea)
                
        if palabra[0] == "escribir":
            if m_escribir_texto.match(linea):
                print("escribir")
                found = True
                
            elif m_escribir_var.match(linea):
                print("escribir var")
                found = True
                
                f_escribir(palabra, variables, linea)
            else:
                error(0, linea)
        
        if palabra[0] == "si":
            if m_si.match(linea):
                print("si")
                found = True
                
                f_comparativo(palabra, variables, linea)
                lin_par.append(i)
            else:
                error(0, linea)
                
        if palabra[0] == "mientras":
            if m_mientras.match(linea):
                print("mientras")
                found = True
                
                f_comparativo(palabra, variables, linea)
                lin_par.append(i)
            else:
                error(0, linea)
            
        if palabra[0] == "para":
            if m_para.match(linea):
                print("para")
                found = True
                
                #f_para(palabra, variables, linea)
                lin_par.append(i)
            else:
                error(0, linea)
                
        if palabra[0] == "fin":
            if linea == "fin":
                print("fin")
                found = True
                
                try:
                    lin_par.remove(lin_par[-1])
                except:
                    error(11, linea)
            else:
                error(0, linea)
                    
        if not buscar_nombre_variable(palabra[0], variables):
            print("valor var")
            found = True
            
            variables = f_var_dec(palabra, variables, linea)
                
        if not found and linea != "":
            error(5, linea) 
        
    elif linea != "":
        error(4, linea)
        
    i += 1
    found = False
    
# Verificacion de ciclos cerrados

if lin_par != []:
    print(f"\nError en el programa\n{errores[8]}\nBloque no cerrado en la linea: {lin_par[0]}")
    exit()
    
### Creacion del programa - Añadir lineas al archivo ###
    
lin_cod = ""
tabs = 1
        
for linea in archivo:
    palabra = linea.split(" ")
    lin_cod = "\t"*tabs
        
    if linea == "":
        codigo.append(lin_cod)
    
    if palabra[0] in ["entero","texto"]:
        if var_dec.match(linea):
            if variables[buscar_posicion_variable(palabra[1],variables)]["tipe"] == "texto":
                lin_cod = "\tvar_" + palabra[1] + " db 100 dup('$')"
            else:
                lin_cod = "\tvar_" + palabra[1] + " dw ?\n\ttexvar_" + palabra[1] + " db 10, 13, 3 dup('$')"
            codigo.insert(lin_var, lin_cod)
            lin_code += 1
            lin_var += 1

    if palabra[0] == "leer":
        if m_leer.match(linea):
            if variables[buscar_posicion_variable(palabra[1],variables)]["tipe"] == "texto":
                lin_cod += "mov ah, 0Ah\n" + "\t"*tabs + "mov dx, offset var_" + palabra[1] +"\n" + "\t"*tabs + "mov cx, 99\n" + "\t"*tabs +  "int 21h\n"
            else:
                lin_cod += "mov ah, 01h\n" + "\t"*tabs + "int 21h\n" + "\t"*tabs +  "mov ah, 0\n" + "\t"*tabs +  "sub al, 30h\n" + "\t"*tabs + "mov var_" + palabra[1] + ", ax\n\n" + "\t"*tabs + "mov ax, var_" + palabra[1] + "\n" + "\t"*tabs + "mov bx, 10\n"  + "\t"*tabs + "xor dx, dx\n"  + "\t"*tabs + "div bx\n" + "\t"*tabs + "add dl, '0'\n" + "\t"*tabs + "add al, '0'\n" + "\t"*tabs + "mov texvar_" + palabra[1] + "[2], al\n"  + "\t"*tabs + "mov texvar_" + palabra[1] + "[3], dl\n"
            codigo.insert(lin_code, lin_cod)
            lin_code += 1         
            
            lin_cod = "\t"*tabs + "mov ah, 09h\n" + "\t"*tabs + "mov dx, offset salto\n" + "\t"*tabs + "int 21h\n"
            codigo.insert(lin_code, lin_cod)
            lin_code += 1   

    if palabra[0] == "escribir":
        if m_escribir_texto.match(linea):
            lin_cod = "\tmsg" + str(n_msj) + " db 10, 13, " +linea.replace("escribir ", "")+", \"$\""
            codigo.insert(lin_var, lin_cod)
            lin_code += 1
            lin_var += 1
            lin_cod = "\t"*tabs + "mov ah, 09h\n" + "\t"*tabs + "mov dx, offset msg" + str(n_msj) +"\n" + "\t"*tabs + "int 21h\n"
            codigo.insert(lin_code, lin_cod)
            lin_code += 1
            n_msj += 1

        elif m_escribir_var.match(linea):
            if variables[buscar_posicion_variable(palabra[1],variables)]["tipe"] == "texto":
                lin_cod += "mov ah, 09h\n" + "\t"*tabs + "mov dx, offset var_" + palabra[1] +"+2\n" + "\t"*tabs + "int 21h\n"
            else:
                lin_cod += "mov ah, 09h\n" + "\t"*tabs + "mov dx, offset texvar_" + palabra[1] +"+2\n" + "\t"*tabs + "int 21h\n"
            codigo.insert(lin_code, lin_cod)
            lin_code += 1
            
        lin_cod = "\t"*tabs + "mov ah, 09h\n" + "\t"*tabs + "mov dx, offset salto\n" + "\t"*tabs + "int 21h\n"
        codigo.insert(lin_code, lin_cod)
        lin_code += 1  
    
    if palabra[0] == "si":

        if m_si.match(linea):
            if (palabra[1].isnumeric()):
                lin_cod += "mov ax, " + palabra[1] + "\n"
            else:
                lin_cod += "mov ax, var_" + palabra[1] + "\n"
                
            if (palabra[3].isnumeric()):
                lin_cod += "\t"*tabs + "cmp ax, " + palabra[3] + "\n"
            else:
                lin_cod += "\t"*tabs + "cmp ax, var_" + palabra[3] + "\n"
                
            if (palabra[2] == "<"):
                lin_cod += "\t"*tabs + "jge if_" + str(n_ciclo) + "\n"
            elif (palabra[2] == ">"):
                lin_cod += "\t"*tabs + "jle if_" + str(n_ciclo) + "\n"
            elif (palabra[2] == "<="):
                lin_cod += "\t"*tabs + "jg if_" + str(n_ciclo) + "\n"
            elif (palabra[2] == ">="):
                lin_cod += "\t"*tabs + "jl if_" + str(n_ciclo) + "\n"
            elif (palabra[2] == "=="):
                lin_cod += "\t"*tabs + "jne if_" + str(n_ciclo) + "\n"
            elif (palabra[2] == "!="):
                lin_cod += "\t"*tabs + "je if_" + str(n_ciclo) + "\n"
                
            fin_bloques.append("if_" + str(n_ciclo) + ":\n")
            
            codigo.insert(lin_code, lin_cod)
            lin_code += 1
            n_ciclo += 1    
            
            tabs += 1

    if palabra[0] == "mientras":
        if m_mientras.match(linea):
            
            lin_cod += "while_" + str(n_ciclo) + ":\n"
            
            if (palabra[1].isnumeric()):
                lin_cod += "\t"*tabs + "mov ax, " + palabra[1] + "\n"
            else:
                lin_cod += "\t"*tabs + "mov ax, var_" + palabra[1] + "\n"
                
            if (palabra[3].isnumeric()):
                lin_cod += "\t"*tabs + "cmp ax, " + palabra[3] + "\n"
            else:
                lin_cod += "\t"*tabs + "cmp ax, var_" + palabra[3] + "\n"
                
            if (palabra[2] == "<"):
                lin_cod += "\t"*tabs + "jge end_while_" + str(n_ciclo) + "\n"
            elif (palabra[2] == ">"):
                lin_cod += "\t"*tabs + "jle end_while_" + str(n_ciclo) + "\n"
            elif (palabra[2] == "<="):
                lin_cod += "\t"*tabs + "jg end_while_" + str(n_ciclo) + "\n"
            elif (palabra[2] == ">="):
                lin_cod += "\t"*tabs + "jl end_while_" + str(n_ciclo) + "\n"
            elif (palabra[2] == "=="):
                lin_cod += "\t"*tabs + "jne end_while_" + str(n_ciclo) + "\n"
            elif (palabra[2] == "!="):
                lin_cod += "\t"*tabs + "je end_while_" + str(n_ciclo) + "\n"
                
            fin_bloques.append("jmp while_" + str(n_ciclo) + "\n" +  "\t"*tabs + "\tend_while_" + str(n_ciclo) + ":\n")
            
            codigo.insert(lin_code, lin_cod)
            lin_code += 1
            n_ciclo += 1    
            
            tabs += 1
        
    if palabra[0] == "para":
        if m_para.match(linea):
            lin_cod += "for_" + str(n_ciclo) + ":\n" + "\t"*tabs + "mov ax, "
            if not palabra[3].isnumeric():
                lin_cod += "var_"
            lin_cod += palabra[3] + "\n" + "\t"*tabs + "mov bx, var_" + palabra[1] + "\n" + "\t"*tabs + "cmp ax, bx\n" + "\t"*tabs + "jl end_for_" + str(n_ciclo)
            tabs += 1
            fin_bloques.append("inc var_" + palabra[1] + "\n\n" + "\t"*tabs + "mov ax, var_" + palabra[1] + "\n" + "\t"*tabs + "mov bx, 10\n"  + "\t"*tabs + "xor dx, dx\n"  + "\t"*tabs + "div bx\n" + "\t"*tabs + "add dl, '0'\n" + "\t"*tabs + "add al, '0'\n" + "\t"*tabs + "mov texvar_" + palabra[1] + "[2], al\n"  + "\t"*tabs + "mov texvar_" + palabra[1] + "[3], dl\n\n" + "\t"*tabs + "jmp for_" + str(n_ciclo) + "\n\n" + "\t"*tabs + "end_for_" + str(n_ciclo) + ":\n")         
            
            codigo.insert(lin_code, lin_cod)
            lin_code += 1
            n_ciclo += 1    
                       
    if palabra[0] == "fin":
        if linea == "fin":
            lin_cod = "\t"*tabs + fin_bloques[-1]
            fin_bloques.pop()
            codigo.insert(lin_code, lin_cod)
            lin_code += 1
            tabs -= 1
                
    if not buscar_nombre_variable(palabra[0], variables):
        if variables[buscar_posicion_variable(palabra[0],variables)]["tipe"] == "texto": 
            lin_cod = "\tvar" + str(n_msj) + " db 10, 13, " + linea.replace(palabra[0] + " = ","").replace("\"", "'") + ", \"$\""
            codigo.insert(lin_var, lin_cod)
            lin_code += 1
            lin_var += 1
            lin_cod = "\tlen_var" + str(n_msj) + " equ $-var" + str(n_msj)
            codigo.insert(lin_var, lin_cod)
            lin_code += 1
            lin_var += 1
            lin_cod = "\t"*tabs + "mov si, offset var" + str(n_msj) + "\n" + "\t"*tabs + "mov di, offset var_" + palabra[0] + "\n" + "\t"*tabs + "mov cx, len_var" + str(n_msj) + "\n\n" + "\t"*tabs + "ciclo" + str(n_ciclo) +":\n" + "\t"*(tabs + 1) + "mov al, [si]\n" + "\t"*(tabs + 1) + "mov [di], al\n" + "\t"*(tabs + 1) + "inc si\n" + "\t"*(tabs + 1) + "inc di\n" + "\t"*(tabs + 1) + "loop ciclo" + str(n_ciclo) + ":\n"
            codigo.insert(lin_code, lin_cod)
            lin_code += 1
            n_msj += 1
            n_ciclo += 1
            
        else:
            for i in range(len(palabra)):
                pal = palabra[i]
                if pal.isdigit():
                    nom_value = pal
                else:
                    nom_value = "var_" + pal
                
                if i == 2:
                    lin_cod = "\t"*tabs + "mov ax, " + nom_value + "\n" + "\t"*tabs + "mov var_" + palabra[0] + ", ax\n"
                    codigo.insert(lin_code, lin_cod)
                    lin_code += 1
                elif palabra[i-1] == "+":
                    lin_cod = "\t"*tabs + "add ax, " + nom_value + "\n" + "\t"*tabs + "mov var_" + palabra[0] + ", ax\n"
                    codigo.insert(lin_code, lin_cod)
                    lin_code += 1
                elif palabra[i-1] == "-":
                    lin_cod = "\t"*tabs + "sub ax, " + nom_value + "\n" + "\t"*tabs + "mov var_" + palabra[0] + ", ax\n"
                    codigo.insert(lin_code, lin_cod)
                    lin_code += 1
                elif palabra[i-1] == "*":
                    lin_cod = "\t"*tabs + "mov bx, " + nom_value + "\n" + "\t"*tabs + "mul bx\n" + "\t"*tabs + "mov var_" + palabra[0] + ", ax\n"
                    codigo.insert(lin_code, lin_cod)
                    lin_code += 1
                elif palabra[i-1] == "/":
                    lin_cod = "\t"*tabs + "mov bx, " + nom_value + "\n" + "\t"*tabs + "xor dx, dx\n" + "\t"*tabs +  "div bx\n" +"\t"*tabs + "mov var_" + palabra[0] + ", ax\n"
                    codigo.insert(lin_code, lin_cod)
                    lin_code += 1
                elif palabra[i-1] == "%":
                    lin_cod = "\t"*tabs + "mov bx, " + nom_value + "\n" + "\t"*tabs + "xor dx, dx\n" + "\t"*tabs +  "div bx\n" + "\t"*tabs + "mov var_" + palabra[0] + ", dx\n"
                    codigo.insert(lin_code, lin_cod)
                    lin_code += 1
                elif palabra[i-1] == "^":
                    lin_cod = "\t"*tabs + "mov bx, "
                    if palabra[i-2].isdigit():
                        lin_cod += palabra[i-2]
                    else:
                        lin_cod += "var_" + palabra[i-2]
                    lin_cod += "\n" + "\t"*tabs + "mov cx, " + nom_value + "\n\n"  + "\t"*tabs + "cmp cx, 1\n" + "\t"*tabs + "je elevar_uno_" + str(n_elev) + "\n\n"   + "\t"*tabs + "cmp cx, 0\n" + "\t"*tabs + "je elevar_cero_" + str(n_elev) + "\n\n" + "\t"*tabs + "sub cx, 1\n\n" + "\t"*tabs + "elevar_" + str(n_elev) + ":\n" + "\t"*(tabs + 1) + "mul bx\n"  + "\t"*(tabs + 1) + "loop elevar_" + str(n_elev) + "\n"  + "\t"*(tabs+1) + "jmp fin_elevar_" + str(n_elev) + "\n\n" + "\t"*tabs + "elevar_uno_" + str(n_elev) + ":\n" + "\t"*(tabs+1) + "mov ax, "
                    if palabra[i-2].isdigit():
                        lin_cod += palabra[i-2]
                    else:
                        lin_cod += "var_" + palabra[i-2]
                    lin_cod += "\n"  + "\t"*(tabs+1) + "jmp fin_elevar_" + str(n_elev) + "\n\n"  + "\t"*tabs + "elevar_cero_" + str(n_elev) + ":\n" + "\t"*(tabs+1) + "mov ax, 1\n"  + "\t"*(tabs+1) + "jmp fin_elevar_" + str(n_elev) + "\n\n"  + "\t"*tabs + "fin_elevar_" + str(n_elev) + ":\n\n" + "\t"*tabs + "mov var_" + palabra[0] + ", ax\n"
                    codigo.insert(lin_code, lin_cod)
                    lin_code += 1
                    n_elev += 1
                        
            lin_cod = "\t"*tabs + "mov ax, var_" + palabra[0] + "\n" + "\t"*tabs + "mov bx, 10\n"  + "\t"*tabs + "xor dx, dx\n"  + "\t"*tabs + "div bx\n" + "\t"*tabs + "add dl, '0'\n" + "\t"*tabs + "add al, '0'\n" + "\t"*tabs + "mov texvar_" + palabra[0] + "[2], al\n"  + "\t"*tabs + "mov texvar_" + palabra[0] + "[3], dl\n"
            codigo.insert(lin_code, lin_cod)
            lin_code += 1

### Creacion del archivo ###    

with open(f"Compilador\\archivos\\{nom}.asm", "w") as f:
    for item in codigo:
        f.write(f"{item}\n")
        
print("\nArchivo guardado en: " + str(os.path.abspath(f"Compilador\\archivos\\{nom}.asm")) + "\n")