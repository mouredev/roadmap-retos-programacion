# _____________________________________
# https://github.com/kenysdev
# 2024 - Python
# _____________________________________
# 41 CAMISETA RAR
# ------------------------------------

"""
 * EJERCICIO:
 * ¿Has visto la camiseta.rar?
 * https://x.com/MoureDev/status/1841531938961592740
 *
 * Crea un programa capaz de comprimir un archivo 
 * en formato .zip (o el que tú quieras).
 * - No subas el archivo o el zip.
"""

import zipfile # https://docs.python.org/es/3.13/library/zipfile.html
import os

def compress_file(source_file, zip_file):
    if not os.path.exists(source_file):
        raise FileNotFoundError(f"El archivo fuente '{source_file}' no existe.")

    if not os.access(source_file, os.R_OK):
        raise PermissionError(f"No tienes permiso de lectura para '{source_file}'")

    zip_dir = os.path.dirname(zip_file) or '.'
    if not os.path.exists(zip_dir):
        raise FileNotFoundError(f"El directorio '{zip_dir}' no existe.")

    if os.path.exists(zip_file):
        raise FileExistsError(f"El archivo zip '{zip_file}' ya existe.")

    try:
        with zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(source_file, arcname=os.path.basename(source_file))
        
        print(f"Comprimido exitosamente '{source_file}' a '{zip_file}'")
    
    except PermissionError:
        raise PermissionError(f"No tienes permiso de escritura para '{zip_file}'")
    except Exception as e:
        raise RuntimeError(f"Se produjo un error al comprimir el archivo.: {e}")


compress_file('tmp.mp4', 'file.zip')
