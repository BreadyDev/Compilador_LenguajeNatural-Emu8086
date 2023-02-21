import subprocess

nom = "Suma"

with open("Compilador\\archivos\\base.txt", "r") as texto:
    archivo = texto.read().split("\n")

lin_var = 5
lin_cod = 35

archivo[0] = "Title " + nom

archivo.insert(lin_var, "NUM1 DW ?")
lin_var += 1
lin_cod += 1
archivo.insert(lin_var, "NUM2 DW ?")
lin_var += 1
lin_cod += 1
archivo.insert(lin_var, "RES DW ?")

archivo.insert(lin_cod, "MOV AX, NUM1\nADD AX, NUM2\nADD AX, NUM3\nMOV RES, AX")

with open(f"Compilador\\archivos\\{nom}.asm", "w") as f:
    for item in archivo:
        f.write(f"{item}\n")

subprocess.run([r"C:\Users\juant\OneDrive\Documentos\VisualStudioProyects\Compilador\archivos\Suma.asm"])