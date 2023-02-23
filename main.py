import re

### Variables

found = False

# Lectura de la base

nom = ""

with open("Compilador\\archivos\\base.txt", "r") as texto:
    ensamblador = texto.read().split("\n")

lin_var = 5
lin_cod = 35

# Expresiones regulares

alpha = re.compile("[A-Za-zÑñ0-9=+-/()<>¿?,.\"]+")
lenguaje = re.compile("(leer|escribir|si|mientras|para|fin|entero|decimal|texto)")
m_title = re.compile("(Title [A-Za-z0-9]+)")
var_dec = re.compile("((entero|decimal|texto) [a-z][a-z0-9]?)")
m_leer = re.compile("(leer [A-Za-z0-9]+)")
m_escribir_texto = re.compile("(escribir [\".*?\"])")
m_escribir_var = re.compile("(escribir [A-Za-z0-9]+)")
m_si = re.compile("si ([A-Za-z0-9]+|[0-9]+) (<|>|==|<=|>=) ([A-Za-z0-9]+|[0-9]+)")
m_mientras = re.compile("mientras ([A-Za-z0-9]+|[0-9]+) (<|>|==|<=|>=) ([A-Za-z0-9]+|[0-9]+)")
m_para = re.compile("para ([A-Za-z0-9]+|[0-9]+)")
m_valor_a_entero = re.compile("[A-Za-z0-9]+ = ([A-Za-z0-9]+|[0-9]+)( (\+|-|\*|/) ([A-Za-z0-9]+|[0-9]+))*")
m_valor_a_decimal = re.compile("[A-Za-z0-9]+ = ([A-Za-z0-9]+|([0-9]+.[0-9]+|[0-9]+))( (\+|-|\*|/) ([A-Za-z0-9]+|([0-9]+.[0-9]+|[0-9]+)))*")
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
    "Err-11 : Variable no apta para la operacion"
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

# Si

def f_si(linea, variables, lin):
    
    for i in range(1,4,2):   
    
        if buscar_nombre_variable(linea[i], variables):
            if not linea[i].isdigit() or not linea[i].isdecimal():
                #Es un numero
            #else:
                error(10, lin)
        else:
            
            if not (variables[buscar_posicion_variable(linea[i], variables)]["value"]):
                error(9, lin)
                
            elif variables[buscar_posicion_variable(linea[i], variables)]["tipe"] == "texto":
                error(10, lin)
            
# Mientras

def f_mientras(linea, variables, lin):
        
    for i in range(1,4,2):   
    
        if buscar_nombre_variable(linea[i], variables):
            if not linea[i].isdigit() or not linea[i].isdecimal():
                #Es un numero
            #else:
                error(10, lin)
        else:
            
            if not (variables[buscar_posicion_variable(linea[i], variables)]["value"]):
                error(9, lin)
                
            elif variables[buscar_posicion_variable(linea[i], variables)]["tipe"] == "texto":
                error(10, lin)

# Para

def f_para(linea, variables, lin):
    if buscar_nombre_variable(linea[1], variables):
        error(3, lin)
    if not (variables[buscar_posicion_variable(linea[1], variables)]["value"]):
        error(9, lin)
        
# Variables
def f_var_dec(linea, variables, lin):
    tipo = variables[buscar_posicion_variable(linea[0], variables)]["tipe"]
    for i in range(2, len(linea), 2):  
        if not variables[buscar_posicion_variable(linea[i], variables)]["tipe"] == tipo:
            error(3, lin)

# Numero de linea
i = 1

# parentesis abiertos
par_a = 0

### Lectura del archivo ###

with open("Compilador/archivos/variables.txt", "r") as texto:
    archivo = texto.read().split("\n")
    
### Iteracion del archivo ###
    
if archivo[0].startswith("Title"):
    if m_title.match(archivo[0]):
        print("titulo")
        nom = archivo[0].replace("Title ", "")
        ensamblador[0] = "Title \'" + nom + "\'"
        found = True
    else:
        error(0, archivo[0])
else:
    error(6, archivo[0])
    
for linea in archivo:
    palabra = linea.split(" ")
    
    if alpha.match(palabra[0]):
    
        if palabra[0] in ["entero", "decimal","texto"]:
            if var_dec.match(linea):
                variables = añadir_variables(palabra, variables)
                
                ensamblador.insert(lin_var, f"{palabra[1]} DW ?")
                
                lin_var += 1
                lin_cod += 1 
                
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
                
                f_si(palabra, variables, linea)
                par_a += 1
            else:
                error(0, linea)
                
        if palabra[0] == "mientras":
            if m_mientras.match(linea):
                print("mientras")
                found = True
                
                f_mientras(palabra, variables, linea)
                par_a += 1
            else:
                error(0, i)
            
        if palabra[0] == "para":
            if m_para.match(linea):
                print("para")
                found = True
                
                f_para(palabra, variables, linea)
                par_a += 1
            else:
                error(0, i)
                
        if palabra[0] == "fin":
            if linea == "fin":
                print("fin")
                found = True
                
                par_a -= 1
            else:
                error(0, i)
                    
        if not buscar_nombre_variable(palabra[0], variables):
            print("valor var")
            found = True
            
            f_var_dec(palabra, variables, linea)
                
        if not found and linea != "":
            error(5, i) 
                
        i += 1
        found = False
        
    elif linea != "":
        error(4, linea)
# Verificacion de ciclos cerrados

if par_a != 0:
    print(f"\nError en el programa\n{errores[8]}")
    exit()
    
### Creacion del archivo para ensamblador ###    

with open(f"Compilador\\archivos\\{nom}.asm", "w") as f:
    for item in ensamblador:
        f.write(f"{item}\n")