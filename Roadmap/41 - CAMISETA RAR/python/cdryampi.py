# /*
#  * EJERCICIO:
#  * ¿Has visto la camiseta.rar?
#  * https://x.com/MoureDev/status/1841531938961592740
#  *
#  * Crea un programa capaz de comprimir un archivo 
#  * en formato .zip (o el que tú quieras).
#  * - No subas el archivo o el zip.
#  */
import gzip
import zipfile
import tarfile
import os 
import tkinter as tk
from tkinter import filedialog


class ControlFiles():
    __PATH_COMPRESS = ''
    __FILES_NAMES = []

    def __init__(self) ->None:
        self.__PATH_COMPRESS = ''
        self.__FILES_NAMES = []

    def clear(self)-> None:
        """Limpia los atributos de la clase."""
        self.__PATH_COMPRESS = ''
        self.__FILES_NAMES = []
        print("Se han limpiado la ruta de salida y los ficheros seleccionados.")

    def compress_files(self, system)->None:
        """Comprime los archivos en el formato indicado."""
        output_file = self.__PATH_COMPRESS

        self.check_files()
        self.check_folder()
        if len(self.__FILES_NAMES) > 0:
            match system:
                case 'gzip':
                    output_file = os.path.join(
                        self.__PATH_COMPRESS,
                        'archivo_comprimido.gz'
                    )
                    self.compress_gzip(output_file)
                case 'zipfile':
                    output_file = os.path.join(
                        self.__PATH_COMPRESS,
                        'archivo_comprimido.zip'
                    )
                    self.compress_zip(output_file)
                case 'bz2':
                    output_file = os.path.join(
                        self.__PATH_COMPRESS,
                        'archivo_comprimido.tar.bz2'
                    )
                    self.compress_tar_bz2(output_file)
                case _:
                    print("No se ha seleccionado un formato correcto para la compresión.")
                    return
        else:
            print(f'Aún no tenemos ningún fichero seleccionado')
    
    def check_files(self)->None:
        """Elimina archivos de la lista si las rutas son inválidas."""
        for index, file in enumerate(list(self.__FILES_NAMES)):
            if not os.path.isfile(file):
                self.__FILES_NAMES.pop(index)
                print(f'Se ha eliminado el fichero "{file}" porque la ruta esta corrupta.')

    def check_folder(self)->None:
        """Establece una carpeta por defecto si no se ha seleccionado ninguna."""
        if not os.path.isdir(self.__PATH_COMPRESS):
            self.__PATH_COMPRESS = os.getcwd()
            print(f"Al no haber ruta hemos asignado la caperta por defecto.")

    def select_folder_output(self)-> None:
        """Selecciona la carpeta de salida para el archivo comprimido."""
        output_folder = self.select_foler_tk()
        
        if output_folder:
            print(f"Ruta seleccionada: {output_folder}")
            self.__PATH_COMPRESS = output_folder
        else:
            print("No se seleccionó ninguna carpeta.")

    def select_files(self)->None:
        """Selecciona los archivos que se quieren comprimir."""
        files = self.select_files_tk()
        if files:
            for file in files:
                self.__FILES_NAMES.append(
                    file
                )

    def select_foler_tk(self)-> str:
        """Utiliza tkinter para seleccionar la carpeta de salida."""
        root = tk.Tk()
        root.withdraw()
        ruta = filedialog.askdirectory(
            title="Selecciona la carpeta de salida"
        )
        return ruta
    
    def select_files_tk(self)-> str:
        """Utiliza tkinter para seleccionar los archivos a comprimir."""
        root = tk.Tk()
        root.withdraw()
        archivos = filedialog.askopenfilenames(
            title="Selecciona los ficheros"
        )
        return archivos
    
    def compress_zip(self, outputname) -> None:
        """Comprime los archivos seleccionados en un archivo ZIP."""
        with zipfile.ZipFile(outputname, 'w') as zipFile:
            for file in self.__FILES_NAMES:
                zipFile.write(
                    file
                )
        print("Compresión con zip completada")

    def compress_gzip(self, output_file):
        """Comprime los archivos seleccionados en formato GZIP."""
        for file in self.__FILES_NAMES:
            with open(file, 'rb') as f_in:
                with gzip.open(output_file, 'wb') as f_out:
                    f_out.writelines(f_in)
        print(f'Se ha comprimido los ficheros en {output_file}')

    def compress_tar_bz2(self, output_file):
        """Comprime los archivos seleccionados en formato TAR.BZ2."""
        with tarfile.open(output_file, 'w:bz2') as bz2_tar:
            for file in self.__FILES_NAMES:
                bz2_tar.add(
                    file
                )

def main():
    gestion_ficheros = ControlFiles()

    while True:
        print("\n--- Menú de compresión de ficheros ---")
        print("1. Seleccionar ficheros a comprimir")
        print("2. Seleccionar carpeta de salida")
        print("3. Comprimir archivos (elige formato)")
        print("   a) gzip")
        print("   b) zipfile")
        print("   c) bz2")
        print("4. Limpiar")
        print("5. Salir")

        opcion = input("Elige una opción (1-5): ").strip()
        match opcion:
            case '1':
                gestion_ficheros.select_files()
                if len(gestion_ficheros._ControlFiles__FILES_NAMES) > 0:
                    print("Archivos seleccionados:")
                    for file in gestion_ficheros._ControlFiles__FILES_NAMES:
                        print(f" - {file}")
                else:
                    print("No se seleccionaron archivos.")
            case '2':
                gestion_ficheros.select_folder_output()
                if gestion_ficheros._ControlFiles__PATH_COMPRESS:
                    print(f"Carpeta de salida seleccionada: {gestion_ficheros._ControlFiles__PATH_COMPRESS}")
                else:
                    print("No se seleccionó ninguna carpeta.")
            case '3':
                formato = input("Elige el formato de compresión (a=gzip, b=zipfile, c=bz2): ").strip().lower()
                if formato == 'a':
                    gestion_ficheros.compress_files('gzip')
                elif formato == 'b':
                    gestion_ficheros.compress_files('zipfile')
                elif formato == 'c':
                    gestion_ficheros.compress_files('bz2')
                else:
                    print("Formato de compresión no válido.")
            case '4':
                gestion_ficheros.clear()
            case '5':
                print("Saliendo del programa.")
                break

            case _:
                print("Opción no válida, por favor elige una opción entre 1 y 4.")


if __name__ == '__main__':
    main()