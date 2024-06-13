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

import os
import json
import xml.etree.ElementTree as et


MY_DATA = {
    "name": "Naia",
    "age": 25,
    "bday": "1998-07-25",
    "languages": [
        "Python",
        "JavaScript",
        "C++",
    ],
}

XML_FILEPATH = "nlarrea.xml"
JSON_FILEPATH = "nlarrea.json"


def write_xml_tags() -> None:
    root = et.Element("data")

    for k, v in MY_DATA.items():
        node = et.SubElement(root, k)

        if isinstance(v, list):
            for item in v:
                et.SubElement(node, k.rstrip("s")).text = item

        else:
            node.text = str(v)

    tree = et.ElementTree(root)
    tree.write(XML_FILEPATH)


write_xml_tags()

with open(XML_FILEPATH, "r") as json_f:
    print(json_f.read())

# os.remove(XML_FILEPATH)


def write_json() -> None:
    with open(JSON_FILEPATH, "w") as f:
        json.dump(MY_DATA, f, indent=4)


write_json()

with open(JSON_FILEPATH, "r") as json_f:
    print(json_f.read())

# os.remove(JSON_FILEPATH)


"""
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la lógica de creación de los archivos anteriores, crea un
 * programa capaz de leer y transformar en una misma clase custom de tu 
 * lenguaje los datos almacenados en el XML y el JSON.
 * Borra los archivos.
"""


class Data:
    def __init__(self, name, age, bday, languages) -> None:
        self.name = name
        self.age = age
        self.bday = bday
        self.languages = languages


# Read from XML file
with open(XML_FILEPATH, "r") as xml_f:
    root = et.fromstring(xml_f.read())

    name = root.find("name").text
    age = root.find("age").text
    bday = root.find("bday").text
    languages = []
    for language in root.find("languages"):
        languages.append(language.text)

    xml_data = Data(name, age, bday, languages)
    print(xml_data.__dict__)


# Read from json
with open(JSON_FILEPATH, "r") as json_f:
    json_dict = json.load(json_f)
    json_data = Data(**json_dict)
    print(json_data.__dict__)


os.remove(XML_FILEPATH)
os.remove(JSON_FILEPATH)
