"""
----------
JSON Y XML
----------
IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.

EJERCICIO:
Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los
siguientes datos (haciendo uso de la sintaxis correcta en cada caso):
- Nombre
- Edad
- Fecha de nacimiento
- Listado de lenguajes de programación
Muestra el contenido de los archivos.
Borra los archivos.

DIFICULTAD EXTRA (opcional):
Utilizando la lógica de creación de los archivos anteriores, crea un
programa capaz de leer y transformar en una misma clase custom de tu 
lenguaje los datos almacenados en el XML y el JSON.
Borra los archivos.
"""
# Ejercicio

# JSON

import json, os

filename_json = "myinfo.json"

myinfo = {
    "name": "Sergio",
    "age": "24",
    "birthdate": "04/05/1999",
    "languages": [
        "Python",
        "CSS",
        "JavaScript"
    ]
}

with open(filename_json, "w") as write_json:
    json.dump(myinfo, write_json)
write_json.close

with open(filename_json, "r") as read_json:
    json_data = json.load(read_json)
    print(json_data)

# XML

import xml.etree.ElementTree as ET

filename_xml = "myinfo.xml"

root = ET.Element("info")

ET.SubElement(root, "name").text="David"
ET.SubElement(root, "age").text="33"
ET.SubElement(root, "birthdate").text="07/03/1991"
lang = ET.SubElement(root, "languages")
ET.SubElement(lang, "language").text="Python"
ET.SubElement(lang, "language").text="CSS"
ET.SubElement(lang, "language").text="JavaScript"

xml_file = ET.ElementTree(root)
xml_file.write(filename_xml)

with open(filename_xml, "r") as read_xml:
    print(read_xml.read())

# Extra

class Persona:
    def __init__(self, name=None, age=None, birth=None, lang=[]):
        self.__name = name
        self.__age = age
        self.__birth = birth
        self.__lang = lang
    def show_info(self):
        print(f"{self.__name}\n{self.__age}\n{self.__birth}\n{self.__lang}")      

print("\nClase con json:\n---------------")

with open(filename_json, "r") as read_json:
    info_json = json.load(read_json)

name = info_json["name"]
age = info_json["age"]
birth = info_json["birthdate"]
lang = info_json["languages"]

sergio = Persona(name, age, birth, lang)

sergio.show_info()

print("\nClase con XML:\n--------------")

info_xml = ET.parse(filename_xml)

name = info_xml.find("name").text
age = info_xml.find("age").text
birth = info_xml.find("birthdate").text
languages = []
for item in info_xml.find("languages"):
    languages.append(item.text)

david = Persona(name, age, birth, languages)

david.show_info()
    
os.remove(filename_json)
os.remove(filename_xml)