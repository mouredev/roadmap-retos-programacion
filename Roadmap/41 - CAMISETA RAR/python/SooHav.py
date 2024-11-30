# 41 - CAMISETA RAR
import zipfile
import os
import gzip
import shutil


# ZIPFILE
"""
zipfile - Módulo para trabajar con archivos ZIP

Este módulo proporciona herramientas para crear, leer, escribir, agregar y listar archivos ZIP.
Permite manipular archivos comprimidos utilizando diferentes algoritmos de compresión.

CLASE: class zipfile.ZipFile(file, mode='r', compression=ZIP_STORED, allowZip64=True,
                  compresslevel=None, *, strict_timestamps=True)

Esta clase permite abrir, crear y manipular archivos ZIP. Los archivos ZIP pueden ser comprimidos
utilizando diferentes algoritmos de compresión.

Parámetros del constructor:
---------------------------
file : str
    El nombre del archivo ZIP que se va a abrir o crear.

mode : str, opcional
    Especifica cómo se debe abrir el archivo. Los valores posibles son:
    - 'r': Leer un archivo ZIP existente.
    - 'w': Truncar y escribir un nuevo archivo ZIP. Esto sobrescribirá
      cualquier archivo ZIP existente con el mismo nombre.
    - 'a': Agregar archivos a un archivo ZIP existente. Si el archivo no
      existe, se creará.
    - 'x': Crear y escribir un nuevo archivo ZIP, pero fallará si el
      archivo ya existe.

compression : int, opcional
    Define el método de compresión a utilizar al escribir el archivo. Las
    opciones disponibles son:
    - ZIP_STORED: No comprime los archivos. Simplemente almacena los
      archivos sin comprimirlos.
    - ZIP_DEFLATED: Utiliza el algoritmo de compresión DEFLATE (el más
      común y utilizado).
    - ZIP_BZIP2: Utiliza el algoritmo BZIP2 para la compresión.
    - ZIP_LZMA: Utiliza el algoritmo LZMA para la compresión, que ofrece
      una mejor tasa de compresión que DEFLATE, pero puede ser más lento.

allowZip64 : bool, opcional
    Si se establece en True, permite crear archivos ZIP de más de 4 GiB.
    Por defecto, está habilitado.

compresslevel : int, opcional
    Permite especificar el nivel de compresión (de 0 a 9) cuando se usa
    ZIP_DEFLATED. Un nivel más alto implica más compresión pero más tiempo
    de procesamiento.

strict_timestamps : bool, opcional
    Si se establece en True, el código se apegará estrictamente a las
    marcas de tiempo al crear archivos ZIP.

MÉTODOS PRINCIPALES:
---------------------
extract(self, member, path=None, pwd=None):
    Extrae el contenido de un archivo ZIP específico y lo guarda en
    el directorio especificado. Si no se proporciona un directorio, se utilizará
    el directorio de trabajo actual.

    Parámetros:
    -----------
    member : str o ZipInfo
        El nombre completo del miembro a extraer o un objeto ZipInfo que
        representa el archivo dentro del archivo ZIP.

    path : str, opcional
        El directorio donde se extraerá el archivo. Si no se proporciona, el
        archivo se extraerá en el directorio de trabajo actual.

    pwd : bytes, opcional
        La contraseña utilizada para archivos ZIP cifrados. Si el archivo no
        está cifrado, este parámetro se puede omitir.

close(self):
    Cierra el archivo ZIP.

extractall(self, path=None, members=None, pwd=None):
    Extrae todos los miembros del archivo ZIP al directorio especificado.

getinfo(self, name):
    Devuelve un objeto ZipInfo para el miembro especificado.

namelist(self):
    Devuelve una lista de nombres de los miembros del archivo ZIP.

printdir(self):
    Imprime en la consola la lista de miembros del archivo ZIP.

read(self, name, pwd=None):
    Lee el contenido del miembro especificado y lo devuelve como bytes.

write(self, filename, arcname=None, compress_type=None):
    Añade un archivo al archivo ZIP.

writestr(self, zinfo_or_arcname, data, compress_type=None):
    Escribe una cadena de texto como un miembro en el archivo ZIP.

setpassword(self, pwd):
    Establece una contraseña para el archivo ZIP.

infolist(self):
    Devuelve una lista de objetos ZipInfo que representan los miembros
    del archivo ZIP. Esto permite iterar sobre los archivos dentro del ZIP.

testzip(self):
    Prueba todos los miembros del archivo ZIP y devuelve el nombre
    del primer archivo que falla.

"""


def compress_with_zipfile(filename, output_dir):
    if not os.path.exists(filename):
        print(f"Error: No se encontró el archivo '{filename}'.")
        return

    # Asegurar que el directorio de salida existe
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Definir la ruta completa del archivo comprimido
    output_path = os.path.join(output_dir, os.path.basename(filename) + ".zip")

    # Verificar si el archivo comprimido ya existe
    if os.path.exists(output_path):
        respuesta = input(
            f"El archivo '{output_path}' ya existe. ¿Deseas reemplazarlo? (s/n): ")
        if respuesta.lower() != 's':
            print("Operación cancelada. No se ha comprimido el archivo.")
            return

    try:
        # Comprimir el archivo
        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED, compresslevel=8) as zipf:
            zipf.write(filename, os.path.basename(filename))
        print(f"Archivo comprimido guardado en: {output_path}")
    except Exception as e:
        print(f"Error al comprimir el archivo: {e}")


def decompress_with_zipfile(zip_filename, output_dir):
    if not os.path.exists(zip_filename):
        print(f"Error: No se encontró el archivo '{zip_filename}'.")
        return

    # Asegurar de que el directorio de salida exista
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    try:
        with zipfile.ZipFile(zip_filename, 'r') as zipf:
            # Descomprimir uno o varios archivos del zip
            for item in zipf.infolist():
                extracted_file_path = os.path.join(output_dir, item.filename)

                # Verificar si el archivo a descomprimir ya existe
                if os.path.exists(extracted_file_path):
                    respuesta = input(
                        f"El archivo '{extracted_file_path}' ya existe. ¿Deseas reemplazarlo? (s/n): ")
                    if respuesta.lower() != 's':
                        print(f"Archivo '{item.filename}' no reemplazado.")
                        continue

                # Extraer el archivo
                zipf.extract(item, output_dir)
                print(f"Archivo '{item.filename}' descomprimido en: {
                      output_dir}")

    except Exception as e:
        print(f"Error al descomprimir el archivo: {e}")


# Uso
filename = "/home/sofiah/Documentos/temporal/clientes-exportados.csv"
output_dir = "/home/sofiah/Documentos/temporal/comprimidos"
compress_with_zipfile(filename, output_dir)

zip_filename = "/home/sofiah/Documentos/temporal/aglomerados_eph_json.zip"
output_dir = "/home/sofiah/Documentos/temporal/descompresion"
decompress_with_zipfile(zip_filename, output_dir)


# GZIP
"""
Este módulo proporciona una interfaz simple para comprimir y descomprimir archivos en formato gzip.

La compresión de datos es proporcionada por el módulo zlib. El formato gzip se usa
en sistemas Unix/Linux para la compresión de archivos, especialmente archivos de texto.

1. Funciones del módulo:
   - gzip.open(filename, mode='rb', compresslevel=9, encoding=None, errors=None, newline=None):
     Abre un archivo comprimido gzip en modo binario o de texto, retornando un objeto de archivo.
     - `filename`: Nombre de archivo.
     - `mode`: Puede ser 'r', 'rb', 'a', 'ab', 'w', 'wb', 'x', 'xb' para modo binario, o 'rt', 'at', 
     'wt', 'xt' para modo texto. El valor predeterminado es 'rb'.
     - `compresslevel`: Un entero de 0 a 9 que define el nivel de compresión.
     - Los argumentos `encoding`, `errors`, y `newline` son utilizados solo en modo texto.

   - gzip.compress(data, compresslevel=9):
     Comprime los datos proporcionados (bytes) y retorna los datos comprimidos. El argumento `compresslevel` 
     es un entero de 0 a 9 que controla el nivel de compresión, siendo 1 la compresión más rápida y 9 la más 
     lenta pero con la mayor compresión.

   - gzip.decompress(data):
     Descomprime los datos comprimidos (bytes) y retorna los datos originales. Se espera que los datos de 
     entrada sean un objeto bytes.

2. Clase `GzipFile`: gzip.GzipFile(filename=None, mode=None, compresslevel=9, fileobj=None, mtime=None):
    
    Constructor para la clase `GzipFile`, que simula la mayoría de los métodos de un objeto de archivo 
    (excepto `truncate()`). Debe proporcionarse al menos uno de `fileobj` o `filename`.

    - `filename`: Nombre del archivo a abrir.
    - `mode`: Modo de apertura ('r', 'rb', 'a', 'ab', 'w', 'wb', 'x', 'xb'). Por defecto es 'rb'.
    - `compresslevel`: Controla el nivel de compresión (0 a 9).
    - `fileobj`: Archivo, objeto `io.BytesIO` o cualquier objeto que simule un archivo. Si es `None`, 
      se abrirá `filename`.
    - `mtime`: Timestamp en formato Unix (segundos desde el 1 de enero de 1970). Por defecto, se usa 
      la hora actual.

    El método `close()` de un objeto `GzipFile` no cierra `fileobj`, permitiendo agregar más datos 
    después de la compresión. 
"""


def compress_with_gzip(filename, output_dir):
    if not os.path.exists(filename):
        print(f"Error: No se encontró el archivo '{filename}'.")
        return

    # Asegurar que el directorio de salida existe
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Definir la ruta completa del archivo comprimido
    output_path = os.path.join(output_dir, os.path.basename(filename) + ".gz")

    # Verificar si el archivo comprimido ya existe
    if os.path.exists(output_path):
        respuesta = input(
            f"El archivo '{output_path}' ya existe. ¿Deseas reemplazarlo? (s/n): ")
        if respuesta.lower() != 's':
            print("Operación cancelada. No se ha comprimido el archivo.")
            return

    try:
        # Comprimir el archivo
        with open(filename, 'rb') as f_in:
            with gzip.GzipFile(output_path, 'wb', compresslevel=9) as f_out:
                shutil.copyfileobj(f_in, f_out)
        print(f"Archivo comprimido guardado en: {output_path}")
    except Exception as e:
        print(f"Error al comprimir el archivo: {e}")


def decompress_with_gzip(gzip_filename, output_dir):
    if not os.path.exists(gzip_filename):
        print(f"Error: No se encontró el archivo '{gzip_filename}'.")
        return

    # Asegurar que el directorio de salida existe
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Definir la ruta completa del archivo descomprimido
    output_path = os.path.join(
        output_dir, os.path.basename(gzip_filename[:-3]))

    # Verificar si el archivo descomprimido ya existe
    if os.path.exists(output_path):
        respuesta = input(
            f"El archivo '{output_path}' ya existe. ¿Deseas reemplazarlo? (s/n): ")
        if respuesta.lower() != 's':
            print("Operación cancelada. No se ha descomprimido el archivo.")
            return

    try:
        # Descomprimir el archivo
        with gzip.GzipFile(gzip_filename, 'rb') as f_in:
            with open(output_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        print(f"Archivo descomprimido guardado en: {output_path}")
    except Exception as e:
        print(f"Error al descomprimir el archivo: {e}")


# Uso

filename = "/home/sofiah/Documentos/temporal/clientes-exportados.csv"
output_dir = "/home/sofiah/Documentos/temporal/comprimidos"
compress_with_gzip(filename, output_dir)

gzip_filename = "/home/sofiah/Documentos/temporal/comprimidos/clientes-exportados.csv.gz"
output_dir = "/home/sofiah/Documentos/temporal/descompresion"
decompress_with_gzip(gzip_filename, output_dir)
