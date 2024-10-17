import os
from zipfile import ZipFile

try:

    with ZipFile(file="file.zip",mode='w') as my_zip:
        my_zip.write("file.txt")
except :
    print("Error creating ZIP file")        