# EJERCICIO:
# Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los
# siguientes datos (haciendo uso de la sintaxis correcta en cada caso):
# - Nombre
# - Edad
# - Fecha de nacimiento
# - Listado de lenguajes de programación
# Muestra el contenido de los archivos.
# Borra los archivos.

import json
import os
import xml.etree.ElementTree as xml

name = "Cristian"
age = 48
birth_date = "1978-01-01"
programming_languages = ["Python", "Java", "PHP"]

xml_file = "cristianfloyd.xml"
json_file = "cristianfloyd.json"

# XML

data = {
    "name": name,
    "age": age,
    "birth_date": birth_date,
    "programming_languages": programming_languages,
}


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


def read_xml():
    with open(xml_file, "r") as file:
        print(file.read())


def delete_xml():
    os.remove(xml_file)


create_xml()
read_xml()
delete_xml()

# JSON


def create_json():
    with open(json_file, "w") as file:
        json.dump(data, file)


def read_json():
    with open(json_file, "r") as file:
        print(file.read())


def delete_json():
    os.remove(json_file)


create_json()
read_json()
delete_json()


#
# DIFICULTAD EXTRA (opcional):
# Utilizando la lógica de creación de los archivos anteriores, crea un
# programa capaz de leer y transformar en una misma clase custom de tu
# lenguaje los datos almacenados en el XML y el JSON.
# Borra los archivos.

create_xml()
read_xml()


class UserData:
    def __init__(self, name: str, age, birth_date, programming_languages) -> None:
        self.name = name
        self.age = age
        self.birth_date = birth_date
        self.programming_languages = programming_languages

    def display(self):
        print(f"Nombre: {self.name}")
        print(f"Edad: {self.age}")
        print(f"Fecha de nacimiento: {self.birth_date}")
        print(f"Lenguajes de programación: {self.programming_languages}")

    @classmethod
    def from_xml(cls, xml_data):
        name = xml_data.find("name").text
        age = xml_data.find("age").text
        birth_date = xml_data.find("birth_date").text
        programming_languages = []
        for item in xml_data.find("programming_languages"):
            programming_languages.append(item.text)
        return cls(name, age, birth_date, programming_languages)

    @classmethod
    def from_json(cls, json_data):
        return cls(
            name=json_data["name"],
            age=json_data["age"],
            birth_date=json_data["birth_date"],
            programming_languages=json_data["programming_languages"],
        )


def my_app(json_file, xml_file):

    with open(xml_file, "r") as file:
        root = xml.fromstring(file.read())
        xml_class = UserData.from_xml(root)
        print("XML desde clase custom")
        xml_class.display()

    with open(json_file, "r") as file:
        json_data = json.load(file)
        json_class = UserData.from_json(json_data)
        print("JSON desde clase custom")
        json_class.display()
        
create_json()
create_xml()
my_app(json_file, xml_file)
delete_xml()
delete_json()