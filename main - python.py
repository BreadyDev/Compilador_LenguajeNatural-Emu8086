# arreglar ciclo for

import re

### Variables

# Numero de linea
i = 1

# parentesis abiertos
lin_par = []

# Comprobar si se encontro el tipo de la linea
found = False

nombre_archivo = "clase_villa.txt"

nom = nombre_archivo.replace(".txt","")

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
            elif linea[i].isdecimal():
                ciclo_tipe[i] = "decimal"
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
            
    elif tipo == "decimal":
        for i in range(2, len(linea), 2):
                if str(linea[i]).isdecimal():
                    print("digito")
                elif not buscar_nombre_variable(linea[i],variables): 
                    if variables[buscar_posicion_variable(linea[i], variables)]["tipe"] == tipo:
                        print("variable decimal")
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
                
                f_para(palabra, variables, linea)
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
    
codigo = []
lin_cod = ""
tabs = 0
    
for linea in archivo:
    palabra = linea.split(" ")
    lin_cod = ""
    
    for t in range(tabs):
        lin_cod += "\t"
        
    if linea == "":
        codigo.append(lin_cod)
    
    if palabra[0] in ["entero", "decimal","texto"]:
        if var_dec.match(linea):
            lin_cod += palabra[1]
            if palabra[0] == "entero":
                lin_cod += ":int = 0"
            if palabra[0] == "decimal":
                lin_cod += ":float = 0"
            if palabra[0] == "texto":
                lin_cod += ":str =\"\""
            
            codigo.append(lin_cod)

    if palabra[0] == "leer":
        if m_leer.match(linea):
            tipo = variables[buscar_posicion_variable(palabra[1], variables)]["tipe"] 
            if tipo == "entero":
                lin_cod += palabra[1] + " = int(input())"
            elif tipo == "decimal":
                lin_cod += palabra[1] + " = float(input())"
            elif tipo == "texto":
                lin_cod += palabra[1] + " = str(input())"
                
            codigo.append(lin_cod)

    if palabra[0] == "escribir":
        if m_escribir_texto.match(linea):
            lin_cod += linea.replace("escribir ", "print (") + ")"
            codigo.append(lin_cod)

        elif m_escribir_var.match(linea):
            lin_cod += "print(" + palabra[1]+")"
            codigo.append(lin_cod)
    
    if palabra[0] == "si":
        if m_si.match(linea):
            tabs += 1
            lin_cod += linea.replace("si", "if") + " :"
            codigo.append(lin_cod)

    if palabra[0] == "mientras":
        if m_mientras.match(linea):
            tabs += 1
            lin_cod += linea.replace("mientras", "while ") + " :"
            codigo.append(lin_cod)
        
    if palabra[0] == "para":
        if m_para.match(linea):
            tabs += 1
            lin_cod += "for c" + palabra[1] + " in range(" + palabra[1] + "):"
            codigo.append(lin_cod)
            
    if palabra[0] == "fin":
        if linea == "fin":
            tabs -= 1
                
    if not buscar_nombre_variable(palabra[0], variables):
        
        tipo = variables[buscar_posicion_variable(palabra[0], variables)]["tipe"] 
        if tipo == "entero":
            lin_cod += linea.replace(" = ", " = int( ") + " )"
        elif tipo == "decimal":
            lin_cod += linea.replace(" = ", " = float( ") + " )"
        elif tipo == "texto":
            lin_cod += linea.replace(" = ", " = str( ") + " )"
        
        codigo.append(lin_cod)

### Creacion del archivo ###    

with open(f"Compilador\\archivos\\{nom}.py", "w") as f:
    for item in codigo:
        f.write(f"{item}\n")