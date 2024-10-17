import os, platform, zipfile
from datetime import datetime
if (platform.platform().startswith("macOS") or platform.platform().startswith("Linux")):
    os.system('clear')
else:
    os.system('cls')

""" * EJERCICIO:
 * ¿Has visto la camiseta.rar?
 * https://x.com/MoureDev/status/1841531938961592740
 *
 * Crea un programa capaz de comprimir un archivo 
 * en formato .zip (o el que tú quieras).
 * - No subas el archivo o el zip."""

current_datetime = datetime.today().strftime("%Y_%m_%d_%H_%M_%S")#Creamos un objeto datetime
zip_name = "python_zip" + current_datetime + ".zip"#Guardamos en una variable el nombre del zip a crear
new_folder = "files"                             # añadiendo la fecha y hora para que siempre sea un fichero único
relative_path = "#41 - ZIP/" + new_folder + "/" 

if not os.path.exists("./" + new_folder):#Si no existe creamos una carpeta dentro del directorio del ejercicio
    os.mkdir("./" + new_folder)
else:
    print("El directorio ya existe en esta ubicación")

for i in range(5):#Generamos 5 archivos txt numerados dentro de la carpeta creada
    with open(f"#41 - ZIP/{new_folder}/file{i+1}.txt", "w") as file: 
        file.write(f"Este es el fichero nº {i+1}")#Añadimos texto descriptivo en cada fichero



def zip_files(zip_name, relative_path):#Creamos una función para generar el zip
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zip_file:#Creamos el zip
        os.chdir(relative_path)#Cambiamos el directorio al de la nueva carpeta
        for file in os.listdir("./"):#Recorremos el contenido de la nueva carpeta con los 5 ficheros txt
            zip_file.write(file)     # y los añadimos al zip


zip_files(zip_name, relative_path)

























# current_datetime = datetime.today().strftime("%Y_%m_%d_%H_%M_%S")
# backup = "#41 - ZIP/files/"
# zip_name = "#41 - ZIP/files/python_zip" + current_datetime + ".zip"
# os.chdir(backup)
# files_folder = os.listdir("./")
# with zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED) as zip_file:

#     for root, dir, files in os.walk(backup):
#         for file in file:
#             path = os.path.join(root, file)
#             zip_file.write(backup+file, compress_type=zipfile.ZIP_DEFLATED)