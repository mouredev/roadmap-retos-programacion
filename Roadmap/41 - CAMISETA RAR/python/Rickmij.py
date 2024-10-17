
import os
import zipfile

# Comprimir 1 archivo
def archive_to_zip(archive, destiny):
    zip_archive = zipfile.ZipFile(destiny, "w")
    #con basename aseguramos que añada el último elemento y no toda la ruta
    zip_archive.write(archive, os.path.basename(archive))

# Comprimir varios archivos
def archives_to_zip(archives, destiny):
    zip_archive = zipfile.ZipFile(destiny, "w")
    for archiv in archives:
        zip_archive.write(archiv, os.path.basename(archiv))

# Comprimir una carpeta
def folder_to_zip(folder, destiny):
    zip_archive = zipfile.ZipFile(destiny, "w")
    # _ es para variables que no hay por qué declarar porque no vamos a usar.
    # Aquí serían las subcarpetas 
    for root, _, files in os.walk(folder):
        for file in files:
            # recorremos los archivos y combinamos en un path la raíz (root) con el archivo en cuestión
            file_path = os.path.join(root, file)

            # cogemos una ruta relativa dentro del archivo zip
            archive_name = os.path.relpath(file_path, os.path.dirname(folder))
        
            zip_archive.write(file_path, archive_name)

archive = "" #archivo que queramos (incluyendo el .txt final)

archives = ["", ""] #ponemos en la lista los archivos que queramos añadir

folder = "" #dirección de la carpeta (con nombre incluído)

destiny = "" #ubicación del destino (con nombre del .zip incluído)
