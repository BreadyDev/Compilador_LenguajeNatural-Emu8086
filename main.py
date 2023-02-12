import re

### Objetos a usar

# Variables

alpha = re.compile("[A-Za-zÑñ0-9=+-/()<>¿?,.\"]+")
lenguaje = re.compile("(leer|escribir|si|finsi|mientras|finmientras|entero|decimal|texto)")
var_dec = re.compile("((entero|decimal|texto) [A-Za-z0-9]+)")
m_leer = re.compile("(leer [A-Za-z0-9]+)")
m_escribir_texto = re.compile("(escribir [\".*?\"])")
m_escribir_var = re.compile("(escribir [A-Za-z0-9]+)")
m_string = re.compile("\".*?\"")
m_decimal = re.compile("([0-9]+.[0-9]+)|([0-9]+)")
m_valor_a_entero = re.compile("[A-Za-z0-9]+ = ([A-Za-z0-9]+|[0-9]+)( (\+|-|\*|/) ([A-Za-z0-9]+|[0-9]+))*")
m_valor_a_decimal = re.compile("[A-Za-z0-9]+ = ([A-Za-z0-9]+|([0-9]+.[0-9]+|[0-9]+))( (\+|-|\*|/) ([A-Za-z0-9]+|([0-9]+.[0-9]+|[0-9]+)))*")
m_valor_a_texto = re.compile("[A-Za-z0-9]+ = (\".*?\")")

variables = [{"name":"", "tipe":"", "value":""}]
errores = (
    "Err-01 : Variable ya declarada",
    "Err-02 : Variable no existente",
    "Err-03 : Valor ingresado no apto para la variable",
    "Err-04 : Linea no valida",
    "Err-05 : Valores no coincidentes"
)

i = 1 #numero de linea

# Funciones

def error(n_error, linea):
    print(f"\nError en la linea {i}: \n{linea} \n{errores[n_error]}")
    exit()

def buscar_nombre_variable(palabra):
    for var in variables:
        if var.get("name") == palabra:
            return False
    return True

def añadir_variables(palabra, variables, linea):
    if variables[0].get("name") == "":
        return [{"name":palabra[1], "tipe":palabra[0], "value":"null"}]
    elif buscar_nombre_variable(palabra[1]):
        variables.append({"name":palabra[1], "tipe":palabra[0], "value":"null"})
        return variables
    else:
        error(0, linea)
        
def mostrar_variables(vars):
    print("\n**************VARIABLES**************\n")  
    for var in vars:
        print("\nNombre: " + str(dict(var).get("name")))
        print("Tipo: " + str(dict(var).get("tipe")))
        print("Valor: " + str(dict(var).get("value")) + "\n")
        
def buscar_var(palabra, variables, linea):
    i = 0
    for var in variables:
        if str(var.get("name")) == palabra:
            return i
        i += 1
    error(1, linea)
    
def leer_var(palabra, variables, linea):
    valor = str(input())
    tipo = str(variables[buscar_var(palabra, variables, linea)]["tipe"])
    
    if tipo == "entero" and valor.isnumeric():
        variables[buscar_var(palabra, variables, linea)]["value"] = valor
        
    elif tipo == "decimal" and m_decimal.match(valor):
        if valor.isdecimal():
            valor += ".0"
        else:
            valor = valor.replace(",", ".")
        variables[buscar_var(palabra, variables, linea)]["value"] = valor
       
    elif tipo == "texto":
        variables[buscar_var(palabra, variables, linea)]["value"] = valor
        
    else:
        error(2, linea)
        
    return variables

def escribir_var(palabra, variables, linea):
    return str(variables[buscar_var(palabra, variables, linea)]["value"]).replace("\"","")

def escribir_tex(linea):
    linea = linea.replace("escribir ", "")
    linea = linea.replace("\"", "")
    return linea

def valor_a_variable(palabra, variables, linea, palabra_list):

    tipo = str(variables[buscar_var(palabra, variables, linea)]["tipe"])
    valor = str(variables[buscar_var(palabra, variables, linea)]["value"])
    
    if tipo == "entero":
        if valor == "null":
            valor = 0
        else:
            valor = int(valor)
            
        for i in range(2, len(palabra_list), 2):
            if not buscar_nombre_variable(palabra_list[i]):
                if variables[buscar_var(palabra_list[i], variables, linea)]["tipe"] == "entero":
                    valor += int(variables[buscar_var(palabra_list[i], variables, linea)]["value"])
                else:
                    error(4, linea)
            else:
                if palabra_list[i].isnumeric():
                    valor += int(palabra_list[i])
                else:
                    error(4, linea)
    elif tipo == "decimal":
        if valor == "null":
            valor = 0.0
        else:
            valor = float(valor)
            
        for i in range(2, len(palabra_list), 2):
            if not buscar_nombre_variable(palabra_list[i]):
                if variables[buscar_var(palabra_list[i], variables, linea)]["tipe"] == "decimal":
                    valor += float(variables[buscar_var(palabra_list[i], variables, linea)]["value"])
                else:
                    error(4, linea)
            else:
                if m_decimal.match(palabra_list[i]):
                    valor += float(palabra_list[i])
                else:
                    error(4, linea)
                    
    elif tipo == "texto":
        valor = linea.replace(palabra + " = ", "")
            
    variables[buscar_var(palabra, variables, linea)]["value"] = str(valor)
        

### Lectura del archivo ###

with open("Compilador/archivos/texto.txt", "r") as texto:
    archivo = texto.read().split("\n")

### Iteracion del archivo ###

for linea in archivo:
    palabra = linea.split(" ")
    
    if(alpha.match(linea)):
        if(lenguaje.match(palabra[0])):
            if var_dec.match(linea):
                variables = añadir_variables(palabra, variables, linea)
                
            elif m_leer.match(linea):
                variables = leer_var(palabra[1], variables, linea)
                
            elif m_escribir_var.match(linea):
                print(escribir_var(palabra[1], variables, linea))
                
            elif m_escribir_texto.match(linea):
                print(escribir_tex(linea))
                
        elif not buscar_nombre_variable(palabra[0]) or m_valor_a_decimal.match(linea) or m_valor_a_texto.match(linea):
                valor_a_variable(palabra[0], variables, linea, palabra)

        else:
            error(3, linea)
            
    i += 1
  
mostrar_variables(variables)