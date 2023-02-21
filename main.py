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
lenguaje = re.compile("(leer|escribir|si|finsi|mientras|finmientras|entero|decimal|texto)")
m_title = re.compile("(Title [A-Za-z0-9]+)")
var_dec = re.compile("((entero|decimal|texto) [A-Za-z0-9]+)")
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
    "Err-08 : Caracter desconocido"
)

### Funciones ###

def error(n_error, linea):
    print(f"\nError en la linea {i}: \n{linea} \n{errores[n_error]}")
    exit()

# Busca si la variable existe o no
def buscar_nombre_variable(palabra, variables):
    for var in variables:
        if var.get("name") == palabra and variables != [{"name":"", "tipe":"", "value":""}]:
            return False
    return True

# Añade la variable y su tipo a la tabla de valores
def añadir_variables(linea, variables, i):
    if variables[0].get("name") == "":
        return [{"name":linea[1], "tipe":linea[0], "value":False}]
    elif buscar_nombre_variable(linea[1], variables):
        variables.append({"name":linea[1], "tipe":linea[0], "value":False})
        return variables
    else:
        error(0, i)

# Numero de linea
i = 1

### Lectura del archivo ###

with open("Compilador/archivos/texto.txt", "r") as texto:
    archivo = texto.read().split("\n")
    
### Iteracion del archivo ###
    
if archivo[0].startswith("Title"):
    if m_title.match(archivo[0]):
        print("titulo")
        nom = archivo[0].replace("Title ", "")
        ensamblador[0] = "Title \'" + nom + "\'"
        found = True
    else:
        error(0, linea)
else:
    error(6, linea)
    
for linea in archivo:
    palabra = linea.split(" ")
    
    if palabra[0] in ["entero", "decimal","texto"]:
        if var_dec.match(linea):
            variables = añadir_variables(palabra, variables, i)
            
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
        else:
            error(0, linea)
            
    if palabra[0] == "escribir":
        if m_escribir_texto.match(linea):
            print("escribir")
            found = True
        elif m_escribir_var.match(linea):
            print("escribir")
            found = True
        else:
            error(0, linea)
    
    if palabra[0] == "si":
        if m_si.match(linea):
            print("si")
            found = True
        else:
            error(0, linea)
    
    if palabra[0] == "finsi":
        if linea == "finsi":
            print("fin del si")
            found = True
        else:
            error(0, linea)
           
    if palabra[0] == "para":
        if m_para.match(linea):
            print("para")
            found = True
        else:
            error(0, i)
            
    if palabra[0] == "finpara":
        if linea == "finpara":
            print("fin del para")
            found = True
        else:
            error(0, i)
            
    if palabra[0] == "mientras":
        if m_mientras.match(linea):
            print("mientras")
            found = True
        else:
            error(0, i)
            
    if palabra[0] == "finmientras":
        if linea == "finmientras":
            print("fin del mientras")
            found = True
        else:
            error(0, i)
                
    if not buscar_nombre_variable(palabra[0], variables):
        print("valor var")
        found = True
            
    if not found and linea != "":
        error(5, i) 
            
    i += 1
    found = False
    
### Creacion del archivo para ensamblador ###    

with open(f"Compilador\\archivos\\{nom}.asm", "w") as f:
    for item in ensamblador:
        f.write(f"{item}\n")