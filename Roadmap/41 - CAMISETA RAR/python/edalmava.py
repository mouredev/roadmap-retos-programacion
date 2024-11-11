import zipfile
import os

def crear_y_comprimir_archivo(mensaje, nombre_txt="mensaje.txt", nombre_zip="archivo_comprimido.zip"):
    # Crear archivo de texto con el mensaje
    with open(nombre_txt, 'w') as archivo:
        archivo.write(mensaje)
    
    print(f"Archivo de texto '{nombre_txt}' creado con el mensaje.")

    # Comprimir el archivo en un archivo .zip
    with zipfile.ZipFile(nombre_zip, 'w') as archivo_zip:
        archivo_zip.write(nombre_txt, os.path.basename(nombre_txt), compress_type=zipfile.ZIP_DEFLATED)
    
    print(f"Archivo comprimido como '{nombre_zip}'")

    # Eliminar el archivo de texto después de comprimirlo
    os.remove(nombre_txt)
    print(f"Archivo de texto '{nombre_txt}' eliminado después de la compresión.")

# Ejemplo de uso
mensaje = "Este es un mensaje corto dentro del archivo de texto."
crear_y_comprimir_archivo(mensaje)
