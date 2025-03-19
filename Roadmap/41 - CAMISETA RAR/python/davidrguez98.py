""" /*
 * EJERCICIO:
 * ¿Has visto la camiseta.rar?
 * https://x.com/MoureDev/status/1841531938961592740
 *
 * Crea un programa capaz de comprimir un archivo 
 * en formato .zip (o el que tú quieras).
 * - No subas el archivo o el zip.
 */ """

#EJERCICIO

import zipfile
import os

def zip_file(path: str, file: str) -> str:

    file_path = os.path.join(path, file)

    if os.path.exists(file_path):

        zip_file = f"{file}.zip"

        zip_path = os.path.join(path, zip_file)

        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(file_path, file)
            print(f"El archivo {file} comprimido como {zip_file}.")
            return zip_file
    
    else: 
        print(f"El archivo {file} no existe en el directorio {path}")

    return None

def unzip_file(path: str, file: str):
    
    file_path = os.path.join(path, file)

    if os.path.exists(file_path):

        zip_path = os.path.join(path, file)

        with zipfile.ZipFile(zip_path, "r") as zipf:
            zipf.extractall(path)
            print(f"El archivo {file} descomprimido en {path}.")

    else: 
        print(f"El archivo {file} no existe en el directorio {path}")


path = os.path.dirname(os.path.abspath(__file__))
file = "Matisseprint3.pdf"

zip = zip_file(path, file)

if zip != None:

    os.remove(os.path.join(path, file))

    unzip_file(path, zip)