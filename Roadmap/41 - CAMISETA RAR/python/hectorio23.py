# Autor: Héctor Adán
# GitHub: https://github.com/hectorio23

import argparse
import zipfile
import gzip
import bz2
import os

# Argumentos mediante ArgumentParser
parser = argparse.ArgumentParser(description='Comprimir un archivo en diferentes formatos.')
parser.add_argument('archivo', help='El archivo que se desea comprimir')
parser.add_argument('formato', choices=['zip', 'gzip', 'bzip'], help='Formato de compresión (zip, gzip, bzip)')
args = parser.parse_args()

def comprimir_archivo(archivo, formato):
    """Comprime un archivo usando la librería estándar de Python según el formato indicado."""
    
    if formato == "zip":
        with zipfile.ZipFile(f"{archivo}.zip", 'w') as zipf:
            zipf.write(archivo, os.path.basename(archivo))
        print(f"Archivo comprimido como: {archivo}.zip")

    elif formato == "gzip":
        with open(archivo, 'rb') as f_in, gzip.open(f"{archivo}.gz", 'wb') as f_out:
            f_out.writelines(f_in)
        print(f"Archivo comprimido como: {archivo}.gz")

    elif formato == "bzip":
        with open(archivo, 'rb') as f_in, bz2.open(f"{archivo}.bz2", 'wb') as f_out:
            f_out.writelines(f_in)
        print(f"Archivo comprimido como: {archivo}.bz2")

    else:
        raise ValueError("Formato de compresión no soportado.")

# Llamar a la función de compresión
comprimir_archivo(args.archivo, args.formato)


