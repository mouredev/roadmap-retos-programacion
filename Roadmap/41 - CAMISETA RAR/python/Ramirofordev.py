'''
Ejercicio:

Crea un programa capaz de comprimir un archivo en formato .zip (o el que quiera).
    * No hay que subir el archivo
'''

import zipfile
import os

# Obtenemos la ruta del archivo que deseamos convertir a zip
ruta = os.path.abspath(input("Nombre del archivo: "))

if not os.path.exists(ruta):
    print("El archivo no existe.")
else:
    # Obtenemos el nombre del archivo.
    nombre_archivo = os.path.basename(ruta)

    with zipfile.ZipFile("archivo.zip", "w") as zip:
        zip.write(ruta, arcname = nombre_archivo)

    print(f"El archivo {nombre_archivo} fue comprimido correctamente en .zip")