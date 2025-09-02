# 41 - Camiseta RAR

import zipfile
import os

def zip_file(path:str, file: str) -> str:
    
    file_path = os.path.join(path, file)

    if os.path.exists(file_path):

        zip_file_name = f"{file}.zip"
        zip_file_path = os.path.join(path, zip_file_name)

        with zipfile.ZipFile(zip_file_path, "w", zipfile.ZIP_DEFLATED) as zip_file:
            zip_file.write(file_path, file)
            print(f"Archivo {file} comprimido como {zip_file_name}")
            return file

    else:
        print(f"El archivo {file} no existe en el directorio {path}")
    
    return None

def unzip_file(path: str, file: str):

    file_path = os.path.join(path, file)

    if os.path.exists(file_path):

        zip_path = os.path.join(path, file)

        with zipfile.ZipFile(zip_path, "r") as zipf:
            zipf.extractall(path)
            print(f"Archivo {file} descomprimido como {path}")

    else:
        print(f"El archivo {file} no existe en el directorio {path}")


path = os.path.dirname(os.path.abspath(__file__))
file = "text.txt"

zip = zip_file(path,file)

if zip != None:

    # Borro el fichero original antes de descomprimir el zip
    os.remove(os.path.join(path,zip))

    unzip_file(path,zip)