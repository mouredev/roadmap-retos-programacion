# @Author Daniel Grande (Mhayhem)

# EJERCICIO:
# ¿Has visto la camiseta.rar?
# https://x.com/MoureDev/status/1841531938961592740
#
# Crea un programa capaz de comprimir un archivo 
# en formato .zip (o el que tú quieras).
# - No subas el archivo o el zip.

import zipfile

def crate_zip_file(file):
    with zipfile.ZipFile("rar.zip", "w") as zipf:
        zipf.write(file)
