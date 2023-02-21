import subprocess

emu_path = r"C:\emu8086\emu8086.exe"

file_path = r"Compilador\archivos\Sumas.asm"

subprocess.call([emu_path, file_path])