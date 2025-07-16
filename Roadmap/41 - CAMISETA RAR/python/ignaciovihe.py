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

input_texts = { "1":{ "input": "Introcuce el nombre del archivo o carpeta a comprimir: ",
                    "output": "Introcuce el nombre del archivo zip de salida: "},
                "2":{ "input": "Introcuce el nombre del archivo o carpeta zip a descomprimir: ",
                    "output": "Introcuce el path de salida: "},
                "3":{ "input": "Introcuce el nombre del archivo zip a descomprimir: ",
                    "output": "Introcuce el path de salida: ",
                    "inside": "Introduce el nombre del archivo concreto a descomprimir: "},    
                "4":{ "input": "Introcuce el nombre del archivo zip: ",
                    "inside": "Introcuce el path del archivo a leer dentro del zip: "},
                "5":{ "input": "Introcuce el nombre del archivo zip a abrir: "}
                    }


def get_input_data(opt: str):

    result=[]

    try:
        if opt in {"1", "2", "3", "4", "5"}:
            input_path = input(f"{input_texts[opt]['input']}")
            if os.path.exists(input_path):
                result.append(input_path)
            else:
                print(f"El archivo de entrada {input_path} no se encuentra/ no existe.")
        if opt in {"1", "2", "3"}:
            output_path = input(f"{input_texts[opt]['output']}")
            if opt == "1":
                output_path = check_output_name(output_path)
            result.append(output_path)
        if opt in {"3", "4"}:
            print_files_in_path(input_path)
            indise_path = input(f"{input_texts[opt]['inside']}")
            result.append(indise_path)

        return result
    
    except Exception as e :
        print(e)


def compress(input_path: str, zip_file_output: str):
    if os.path.exists(input_path):
        with zipfile.ZipFile(zip_file_output, 'w', compression=zipfile.ZIP_DEFLATED) as zipf:# Abro archivo en modo w
            if os.path.isfile(input_path):                                    # Si es un archivo
                zipf.write(input_path, arcname=os.path.basename(input_path))        #Lo escribo con su basename(su nombre) arcname= es la ruta 
                                                                        #con que se guradara dentro del zip.
            if os.path.isdir(input_path):                                     # Si es un directorio
                for current_folder, subfolder, files in os.walk(input_path):  # recorre todos los archivos y carpetas paso a paso.
                                                                        #os.walk(Sólo funciona con carpetas, no con archivos)
                    for file in files:
                        full_path = os.path.join(current_folder, file)  #Crea la el path completo concatenendo la carpeta act, y el file.
                        rel_path = os.path.relpath(full_path, os.path.dirname(input_path)) # relpath es como full_path - os.path.dirname(path)
                        zipf.write(full_path, arcname=rel_path)         # Se escribe cada fichelo con su estructura
    else:
        print(f"El archivo de entrada {input_path} no se encuentra/ no existe.")

def extraxt_all(zip_file: str, output_path: str = ''):
    with zipfile.ZipFile(zip_file, 'r') as zipf:
        zipf.extractall(output_path)

def extract_file(zip_file, file_to_extract, output_path):
    with zipfile.ZipFile(zip_file, 'r') as zipf:
        zipf.extract(file_to_extract, path=output_path)

def read_file_zip(zip_file: str, file_to_read):
    with zipfile.ZipFile(zip_file, 'r') as zipf:
        with zipf.open(file_to_read) as f:
            content = f.read().decode('utf-8')
            print(content)

def open_zip(input_path: str):
    print_files_in_path(input_path)

def check_output_name(file_name: str):
    if not file_name.lower().endswith('.zip'):
        file_name += '.zip'
    return file_name

def print_files_in_path(path: str):
    print("Contenido del archivo zip:")
    with zipfile.ZipFile(path, 'r') as z:
        for name in z.namelist():
            print(" -", name)

def main():
    while True:
        print(f"8zip")
        print(f"Opciones:")
        print(f"1. Comprimir archivo/carpeta")
        print(f"2. Extraer todo.")
        print(f"3. Extraer archivo.")
        print(f"4. Leer archivo")
        print(f"5. Abrir zip - Ver archivos contenidos en el zip")
        print(f"6. Salir")

        try:
            option = input("Elige una opción: ")
            if option == "6":
                break
            input_data = get_input_data(option)
            if input_data:
                match option:
                    case "1":
                        if len(input_data) == 2:
                            compress(input_data[0],input_data[1])
                    case "2":
                        if len(input_data) == 2:
                            extraxt_all(input_data[0],input_data[1])
                    case "3":
                        if len(input_data) == 3:
                            extract_file(input_data[0], input_data[2], input_data[1])
                    case "4":
                        if len(input_data) == 2:
                            read_file_zip(input_data[0], input_data[1])
                    case "5":
                        if len(input_data) == 1:
                            open_zip(input_data[0])

        except Exception as e:
            print(e)

main()