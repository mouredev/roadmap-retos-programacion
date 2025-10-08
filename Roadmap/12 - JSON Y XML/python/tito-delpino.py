#  * EJERCICIO:
#  * Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los
#  * siguientes datos (haciendo uso de la sintaxis correcta en cada caso):
#  * - Nombre
#  * - Edad
#  * - Fecha de nacimiento
#  * - Listado de lenguajes de programación
#  * Muestra el contenido de los archivos.
#  * Borra los archivos.

import xml.etree.ElementTree as ET
import json
import os


def crear_mostrar_xml():
    """CREAR"""
    root = ET.Element("persona")
    print(f"Elemento raiz '{root.tag}' creado")

    # subelementos
    name = ET.SubElement(root, "name")
    name.text = "tito"
    age = ET.SubElement(root, "age")
    age.text = "38"
    birth_date = ET.SubElement(root, "birth-date")
    birth_date.text = "26-03-1988"
    # lista de lenguajes
    languages_element = ET.SubElement(root, "languages")
    for lang in programming_languages:
        lang_element = ET.SubElement(languages_element, "language")
        lang_element.text = lang

    # guardar XML en el archivo
    tree = ET.ElementTree(root)  # creamos objeto
    tree.write("personaXML.xml")  # guardamos el archivo
    print("Archivo creado y guardado")

    """MOSTRAR"""
    tree = ET.parse("personaXML.xml")  # leer el archivo
    root = tree.getroot()  # obtener la raíz

    print("----Contenido del archivo .xml:")
    for child in root:
        if child.tag == "languages":
            print(f"{child.tag} :")
            for lang in child:
                print(f"- {lang.text}")
        else:
            print(f"{child.tag} : {child.text}")


def crear_mostrar_json():
    """CREAR"""
    # datos
    persona = {
        "name": "pepe",
        "age": 35,
        "birth-date": "14-07-1995",
        "languages": programming_languages,
    }

    """GUARDAR"""
    with open("personaJSON.json", "w") as file:
        json.dump(persona, file)  # datos del diccionario agregados a un json nuevo
        print("Archivo .json creado y relleno")

    """MOSTRAR"""
    with open("personaJSON.json", "r") as file:
        datos = json.load(file)
        print("----Contenido del archivo .json:")
        for clave, valor in datos.items():
            print(f"{clave} - {valor}")


programming_languages = ["python", "html"]

crear_mostrar_xml()
print("/" * 60)
crear_mostrar_json()


#  * DIFICULTAD EXTRA (opcional):
#  * Utilizando la lógica de creación de los archivos anteriores, crea un
#  * programa capaz de leer y transformar en una misma clase custom de tu
#  * lenguaje los datos almacenados en el XML y el JSON.
#  * Borra los archivos.


class Persona:
    def __init__(self, name, age, birth_date, languages):
        self.name = name
        self.age = age
        self.birth_date = birth_date
        self.languages = languages

    @classmethod
    def from_xml(cls, filename):
        root = ET.parse(filename).getroot()
        name = root.find("name").text # type: ignore
        age = int(root.find("age").text) # type: ignore
        birth_date = root.find("birth-date").text # type: ignore
        languages = [lang.text for lang in root.find("languages")] # type: ignore
        return cls(name, age, birth_date, languages)

    @classmethod
    def from_json(cls, filename):
        data = json.load(open(filename))
        return cls(data["name"], data["age"], data["birth-date"], data["languages"])

    def __str__(self):
        return f"{self.name}, {self.age} años, nacido el {self.birth_date}, lenguajes: {', '.join(self.languages)}"

print("/" * 60)
persona_xml = Persona.from_xml("personaXML.xml")
persona_json = Persona.from_json("personaJSON.json")

print("Objeto desde XML:", persona_xml)
print("Objeto desde JSON:", persona_json)


print("/" * 60)
"""BORRAR ARCHIVOS"""
os.remove("personaXML.xml")
print(f"Archivo XML borrado del directorio")
os.remove("personaJSON.json")
print(f"Archivo .json borrado del directorio")
