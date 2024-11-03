import zipfile
import os

def comprimir_archivo_en_zip(ruta_archivo, nombre_zip):
    with zipfile.ZipFile(nombre_zip, 'w') as zipf:
        zipf.write(ruta_archivo, os.path.basename(ruta_archivo))
    print(f"Archivo comprimido con éxito en {nombre_zip}")

def comprimir_directorio_en_zip(ruta_directorio, nombre_zip):
    with zipfile.ZipFile(nombre_zip, 'w') as zipf:
        for foldername, subfolders, filenames in os.walk(ruta_directorio):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                zipf.write(file_path, os.path.relpath(file_path, ruta_directorio))
    print(f"Directorio comprimido con éxito en {nombre_zip}")

if __name__ == "__main__":
    tipo = input("Selecciona lo que quieres comprimir (archivo/directorio): ").strip().lower()
    ruta = input(f"Introduce la ruta del {tipo} que deseas comprimir: ").strip()
    nombre_salida = input("Introduce el nombre de salida (sin la extensión): ").strip() + '.zip'

    if tipo == 'archivo':
        comprimir_archivo_en_zip(ruta, nombre_salida)
    elif tipo == 'directorio':
        comprimir_directorio_en_zip(ruta, nombre_salida)
    else:
        print("Selección no válida")
