'''
 * IMPORTANTE: Solo debes subir el fichero de codigo como parte del ejercicio.
 * 
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los
 * siguientes datos (haciendo uso de la sintaxis correcta en cada caso):
 * - Nombre
 * - Edad
 * - Fecha de nacimiento
 * - Listado de lenguajes de programacion
 * Muestra el contenido de los archivos.
 * Borra los archivos.
'''

import json
import xml.etree.ElementTree as ET
import os

# Archivo json

user = {
    "name": input(str("Por favor indica tu nombre: ")),
    "nick": input(str("Indica tu nick de usuario: ")),
    "age": input(str("Confirma tu edad: ")),
    "languages": [input(str("Enumera los lenguajes de programacion que conoces: " ))]
}

with open("datos.json", "w") as file:
    json.dump(user, file)
    
with open("datos.json", "r") as file:
    data = json.load(file)
    print(data)
    
with open("datos.json", "r") as file:
    data = json.load(file)
    print(data["name"]) # Para imprimir solo un elemento del archivo (en este caso el nombre)
    
if os.path.exists("datos.json"):
    os.remove("datos.json")
    print("[+] El archivo 'datos.json' ha sido eliminado ....")
else:
    print("[!] El archivo no existe ...." )

       
# Archivo XML

root = ET.Element("datos.xml")

name = ET.SubElement(root, "Luis")
nick = ET.SubElement(root, "rantamplan")
age = ET.SubElement(root, "88")
languages = ET.SubElement(root, "python, bash, java")

tree = ET.ElementTree(root)
tree.write("datos.xml")

    
with open("datos.xml", "r") as file:
    data = file.read()
    print(data)



if os.path.exists("datos.xml"):
    os.remove("datos.xml")
    print("[+] El archivo 'datos.json' ha sido eliminado ....")
else:
    print("[!] El archivo no existe ...." )



'''
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la logica de creacion de los archivos anteriores, crea un
 * programa capaz de leer y transformar en una misma clase custom de tu 
 * lenguaje los datos almacenados en el XML y el JSON.
 * Borra los archivos.
'''
2
class Archivos:
    def __init__(self, file_json, file_xml):
        self.file_json = file_json
        self.file_xml = file_xml
        
def create_json():
    user2 = {
        "name": str("Juan"),
        "nick": str("rantamplan"),
        "age": str("61"),
        "languages": ["python, bash, java"]
    }
    with open("file_json", "w") as file:
        json.dump(user2, file)
    
    with open("file_json", "r") as file:
        data = json.load(file)
        print(data)
        
    os.remove("file_json")
    print("[!] El archivo 'file_json' ha sido eliminado ....")
        
        
def create_xml():
    
    root = ET.Element("file_xml")
    
    name = ET.SubElement(root, "Luis")
    nick = ET.SubElement(root, "rantam")
    age = ET.SubElement(root, "92")
    languages = ET.SubElement(root, "python, bash, java")

    tree = ET.ElementTree(root)
    tree.write("file_xml")

        
    with open("file_xml", "r") as file:
        data = file.read()
    print(data)
    
    os.remove("file_xml")
    print("[!] El archivo 'file_xml' ha sido eliminado ....")
    
        
        
create_json()
create_xml()
