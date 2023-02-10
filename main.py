import re

### Lectura del archivo ###

with open("Compilador/archivos/texto.txt", "r") as texto:
    archivo = texto.read().split("\n")

# Quitar espacios vacios

solo_line_count = 0

for linea in archivo:
    if linea == "":
        solo_line_count += 1

for i in range(solo_line_count):
    archivo.remove("")

### Iteracion del archivo ###

for linea in archivo:
    print(linea)