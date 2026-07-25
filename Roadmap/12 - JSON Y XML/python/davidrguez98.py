
""" /*
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
 */ """

#EJERCICIO

import os

#XML

import xml.etree.ElementTree as xml

data = {
    "name" : "David",
    "age" : 26,
    "birth_date" : "10/03/1998",
    "languages" : ["Python", "HTML", "CSS"]
}

xml_file = "davidrguez98.xml"

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
    tree.write(xml_file)

save_xml()

with open(xml_file, "r") as xml_data:
    print(xml_data.read())

os.remove(xml_file)

#JSON

import json

json_file = "davidrguez98.json"

def save_json():
    with open(json_file, "w") as json_data:
        json.dump(data, json_data)

save_json()

with open(json_file, "r") as json_data:
    print(json_data.read())

os.remove(json_file)

#DIFICULTAD EXTRA

save_xml()

class Data():

    def __init__(self, name, age, birth_date, languages):
        self.name = name
        self.age = age
        self.birth_date = birth_date
        self.languages = languages

with open(xml_file, "r") as xml_data:
    root = xml.fromstring(xml_data.read())
    name = root.find("name").text
    age = root.find("age").text
    birth_date = root.find("birth_date").text
    languages = []
    for item in root.find("languages"):
        languages.append(item.text)
    
    xml_class = Data(name, age, birth_date, languages)
    print(xml_class.__dict__)

os.remove(xml_file)

save_json()

with open(json_file, "r") as json_data:
    json_dict = json.load(json_data)
    json_class = Data(json_dict["name"], json_dict["age"], json_dict["birth_date"], json_dict["languages"])

    print(json_class.__dict__)

os.remove(json_file)