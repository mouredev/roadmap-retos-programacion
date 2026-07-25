"""
/*
 * EJERCICIO:
 * ¿Has visto la camiseta.rar?
 * https://x.com/MoureDev/status/1841531938961592740
 *
 * Crea un programa capaz de comprimir un archivo 
 * en formato .zip (o el que tú quieras).
 * - No subas el archivo o el zip.
 */
"""

import zipfile
import os
import logging

def zip_file(path: str, file: str):

    file_path = os.path.join(path, file)

    if os.path.exists(file_path):       
        zip_file = f"{file}.zip"
        zip_file_path = os.path.join(path, zip_file)     
        
        with zipfile.ZipFile(zip_file_path, "w", zipfile.ZIP_DEFLATED) as zfile:
            zfile.write(file_path, file)
            print(f"Archivo {file} comprimido en {zip_file_path}!")
            return zip_file
    else:
        print(f"El archivo {file} no existe en la ruta {path}")

    return None

def unzip_file(path: str, file: str):
    
    file_path = os.path.join(path, file)

    if os.path.exists(file_path):
        with zipfile.ZipFile(file_path, "r") as zfile:
            zfile.extractall(path)
            print(f"Archivo {file} descomprimido en {path}!")
    else:
        print(f"El archivo {file} no existe en la ruta {path}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    path = os.path.dirname(os.path.abspath(__file__))
    file = "Notes_Git.pdf"
    zip = zip_file(path, file)

    if zip != None:

        # Erase the original file
        os.remove(os.path.join(path, file))
        
        unzip_file(path, f"{file}.zip")

