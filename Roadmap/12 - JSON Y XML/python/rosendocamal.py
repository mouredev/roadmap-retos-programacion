"""
 * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
 * 
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los
 * siguientes datos (haciendo uso de la sintaxis correcta en cada caso):
 * - Nombre
 * - Edad
 * - Fecha de nacimiento
 * - Listado de lenguajes de programación
 * Muestra el contenido de los archivos.
 * Borra los archivos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la lógica de creación de los archivos anteriores, crea un
 * programa capaz de leer y transformar en una misma clase custom de tu 
 * lenguaje los datos almacenados en el XML y el JSON.
 * Borra los archivos.
"""
import xml.etree.ElementTree as xml; import os

data = {
    "name": "Swokowski Perelman",
    "age": 36,
    "birth_date": "2026-08-31",
    "programming_language": ["Python", "Rust", "Bash", "PowerShell", "TypeScript"]
}
name_file_xml = "rosendocamal.xml"

# XML

def save_xml():
    root = xml.Element("data")

    for key, value in data.items():
        child = xml.SubElement(root, key)
        if isinstance(value, list):
            for item in value:
                xml.SubElement(child, "item").text = item
        else:
            child.text = str(value)

    tree = xml.ElementTree(root)
    tree.write(name_file_xml)

save_xml()

with open(name_file_xml) as data_xml:
    print(data_xml.read())

os.remove(name_file_xml)

# JSON

import json

name_file_json = "rosendocamal.json"

def save_json():
    with open(name_file_json, "w") as data_json:
        json.dump(data, data_json)

with open(name_file_json, "r") as data_json:
    print(data_json.read())

os.remove(name_file_json)

#### EXTRA ####

save_xml(); save_json()

class Data():
    def __init__(self, name, age, birth_date, programming_language) -> None:
        self.name = name
        self.age = age
        self.birth_date = birth_date
        self.programming_language = programming_language

print()

with open(name_file_xml, "r") as f_xml:
    root = xml.fromstring(f_xml.read())
    name = root.find("name").text
    age = root.find("age").text
    birth_date = root.find("birth_date").text
    programming_language = []
    for item in root.find("programming_language"):
        programming_language.append(item.text)

    data_class_from_xml = Data(name, age, birth_date, programming_language)
    print(data_class_from_xml.__dict__)

with open(name_file_json, "r") as f_json:
    data = json.load(f_json)
    name = data["name" ]
    age = data["age"]
    birth_date = data["birth_date"]
    programming_language = data["programming_language"]

    data_class_from_json = Data(name, age, birth_date, programming_language)
    print(data_class_from_json.__dict__)

os.remove(name_file_json); os.remove(name_file_xml)