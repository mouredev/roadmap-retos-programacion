"""
EJERCICIO:
Desarrolla un programa capaz de crear un archivo XML y JSON que guarde
los siguientes datos (hacindo uso de la sintaxis correcta en cada caso):

- Nombre
- Edad
- Fecha de nacimiento
- Listado de Lenguajes de programación
Muestra el contenido de los archivos.
Borra los archivos.

DIFICULTAD EXTRA (opcional):
Utilizando la lógica de creación de los archivos anteriores, crea un
programa capaz de leer y transformar en una misma clase custom de tu 
lenguaje los datos almacenados en el XML y el JSON.
Borra los archivos.

by adra-dev
"""

"""
Ejercicio:
"""


"""
XML:
XML es el acrónimo de Extensible Markup Language, es decir, es un 
lenguaje de marcado que define un conjunto de reglas para la 
codificación de documentos. 

Un archivo XML se divide en dos partes: prolog y body. La parte 
prolog consiste en metadatos administrativos, como declaración XML, 
instrucción de procesamiento opcional, declaración de tipo de 
documento y comentarios. La parte del body se compone de dos partes: 
estructural y de contenido (presente en los textos simples).
"""
import os
import xml.etree.ElementTree as xml

data = {
"name" : "Adrian Rodriguez",
"age" : "26",
"birth_date" : "12-02-1998",
"programing_languages" : ['Python', 'Rust']
}

xml_file = "adra-dev.xml"

# XML

def create_xml():

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

create_xml()

with open(xml_file) as xml_data:
    print(xml_data.read())
    
os.remove(xml_file)


"""
JSON: 
Es un formato omnipresente en el que se usa un esquema de documento 
jerárquico para definir entidades de datos (objetos) que tienen 
varios atributos. Cada atributo puede ser un objeto (o una colección 
de objetos ), lo que hace de JSON un formato flexible adecuado tanto 
para datos estructurados como semiestructurados.
"""

# JSON

import json

json_file = "adra-dev.json"

def create_json():

    with open(json_file, "w") as json_data:
        json.dump(data, json_data)


create_json()

with open(json_file, "r") as json_data:
    print(json_data.read())

os.remove(json_file)

"""
Extra
"""

create_xml()
create_json()

class Data():

    def __init__(self, name, age, birth_date, programing_languages) -> None:
        self.name = name
        self.age = age
        self.birth_date = birth_date
        self.programing_languages = programing_languages


with open(xml_file, "r") as xml_data:

    root = xml.fromstring(xml_data.read())
    name = root.find("name").text
    age = root.find("age").text
    birth_date = root.find("birth_date").text
    programing_languages = []
    for item in root.find("programing_languages"):
        programing_languages.append(item.text)

    xml_class = Data(name, age, birth_date, programing_languages)
    print(xml_class.__dict__)


with open(json_file, "r") as json_data:
    json_dict = json.load(json_data)
    json_class = Data(
        json_dict["name"],
        json_dict["age"],
        json_dict["birth_date"],
        json_dict["programing_languages"]
    )
    print(json_class.__dict__)

os.remove(xml_file)
os.remove(json_file)