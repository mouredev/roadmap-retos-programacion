"""
 * EJERCICIO:
 * ¿Has visto la camiseta.rar?
 * https://x.com/MoureDev/status/1841531938961592740
 *
 * Crea un programa capaz de comprimir un archivo 
 * en formato .zip (o el que tú quieras).
 * - No subas el archivo o el zip.
"""

import zipfile
import os

def compress_file(file_path, zip_name):
    # Crea un archivo zip
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        # Agrega el archivo al zip
        zipf.write(file_path, os.path.basename(file_path))
    print(f'{file_path} ha sido comprimido en {zip_name}')

# Uso del programa
file_path = 'ruta/del/archivo.ext'  # Reemplaza con la ruta de tu archivo
zip_name = 'archivo_comprimido.zip'  # Nombre del archivo zip que se va a crear
compress_file(file_path, zip_name)
