my_dict = {
    "Name":[],
    "Type":[],
    "Value":[]
}

def error(err):
    print(f"Error: {err}")

def add_value(name, type, value):
    
    if name not in my_dict.get("Name"):
        my_dict.get("Name").append(name)
    else:
        error("Variable ya declarada")
        
    if type in ["int", "float", "string"]:
        my_dict.get("Type").append(type)        
    else:
        error("Tipo de variable no valida")

    my_dict.get("Value").append(value)

def search_var(var_name):
    var_place = 0
    for i in my_dict.get("Name"):
        if i == var_name:
            print("Nombre: " + str(my_dict.get("Name")[var_place]) + "\nTipo: " + str(my_dict.get("Type")[var_place]) + "\nValor: " + str(my_dict.get("Value")[var_place]))
        var_place += 1

add_value("int_1", "int", "3")
add_value("int_2", "int", "5")
add_value("float_1", "float", "3.14")
add_value("float_2", "float", "2.5")
add_value("string_1", "string", "Cadena de prueba")
add_value("string_2", "string", "Hola mundo")

print(my_dict)

search_var(input("Nombre de la variable? "))