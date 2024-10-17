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

def compress_file(file_path: str, zip_path: str):
    
    if os.path.exists(file_path):
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(file_path, os.path.basename(file_path))
            print(f"Archivo {file_path} comprimido como {zip_path}.")
            return zip_path
    else:
        print(f"El archivo {file_path} no existe.")
        return None
    
def decompress_file(zip_path: str, dest_path: str):
        
        if os.path.exists(zip_path):
            with zipfile.ZipFile(zip_path) as zipf:
                zipf.extractall(dest_path)
                print(f"Archivo {zip_path} descomprimido en {dest_path}.")
        else:
            print(f"El archivo {zip_path} no existe.")
    
path = os.path.dirname(os.path.abspath(__file__))  # Directorio actual
file = "prueba.txt"
zip_file = f"{file}.zip"

zip = compress_file(os.path.join(path, file), os.path.join(path, zip_file))

if zip != None:
    decompress_file(os.path.join(path, zip), path)
    #os.remove(os.path.join(path, zip))


