""" 
# 41 - Zip 
"""
# Crea un programa capaz de comprimir un archivo en formato .zip (o el que tú quieras).

import zipfile
import os

# Archivo a comprimir
pdf_file = "GuiaPython.pdf"

# Nombre del archivo zip que se creara
zip_file = "GuiaPython.zip"

# Crear archivo zip
with zipfile.ZipFile(zip_file, "w", compression=zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(pdf_file)

# Comparar tamaños
tamaño_pdf = os.path.getsize(pdf_file)
tamaño_zip = os.path.getsize(zip_file)

print(f"El tamaño del pdf: {tamaño_pdf} bytes.")
print(f"El tamaño del zip: {tamaño_zip} bytes.")
print(f"El archivo {pdf_file}, ha sido comprimido en {zip_file}.")