
 # EJERCICIO:
 # ¿Has visto la camiseta.rar?
 # https://x.com/MoureDev/status/1841531938961592740
 #
 # Crea un programa capaz de comprimir un archivo 
 # en formato .zip (o el que tú quieras).
 # - No subas el archivo o el zip.
 #/


import zipfile
import os


directorio_actual = os.path.dirname(__file__)
nombre_fichero="MiFichero.txt"
nombre_Zip="FicheroComprimido.zip"

fileToZip = os.path.join(directorio_actual,nombre_fichero)
ZipFile = os.path.join(directorio_actual,nombre_Zip)

with zipfile.ZipFile(ZipFile, 'w') as ficheroComprimido:
    ficheroComprimido.write(fileToZip, arcname=nombre_fichero)
    

    
