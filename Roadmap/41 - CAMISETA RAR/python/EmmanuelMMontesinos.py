"""
/*
 * EJERCICIO:
 * ¿Has visto la camiseta.rar?
 * https://x.com/MoureDev/status/1841531938961592740
 *
 * Crea un programa capaz de comprimir un archivo 
 * en formato .zip (o el que tú quieras).
 * - No subas el archivo o el zip.
 */
"""

import zipfile
import os

class ZipFileManager:
    def __init__(self, path):
        self.path = path
        self.name = os.path.splitext(os.path.basename(self.path))[0]

    def compress(self):
        with zipfile.ZipFile(f"{self.name}.zip", mode="w") as archive:
            archive.write(self.path)

# prueba
if __name__ == "__main__":
    manager = ZipFileManager("RUTA_DE_ARCHIVO_O_CARPETA")
    manager.compress()