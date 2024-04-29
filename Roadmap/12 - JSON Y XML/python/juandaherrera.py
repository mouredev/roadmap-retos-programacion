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
"""

import json
import logging
import os
import xml.etree.ElementTree as ET

logging.basicConfig(level=logging.INFO)

file_name = 'juandaherrera'

data = {
    'name': 'Juan David Herrera',
    'age': '24',
    'birth_date': '1999-12-05',
    'programming_languages': ['python', 'javascript', 'visual basic', 'bash', 'html', 'css'],
}

# Json
with open(f'{file_name}.json', 'w') as file:
    logging.info('Guardando archivo como .json')
    json.dump(data, file)

# XML
root = ET.Element('person')

ET.SubElement(root, 'name').text = data['name']
ET.SubElement(root, 'age').text = data['age']
ET.SubElement(root, 'birth_date').text = data['birth_date']

programming_languages = ET.SubElement(root, 'programming_languages')
for lang in data['programming_languages']:
    ET.SubElement(programming_languages, 'language').text = lang

# Crear el árbol de ElementTree y escribirlo a un archivo XML
tree = ET.ElementTree(root)
with open(f'{file_name}.xml', 'wb') as archivo:
    logging.info('Guardando archivo como .xml')
    tree.write(archivo, encoding='utf-8', xml_declaration=True)


logging.info('Leyendo archivos')
with open(f'{file_name}.json', 'r') as file:
    json_data = json.load(file)

tree = ET.parse(f'{file_name}.xml')
root = tree.getroot()

print('-' * 15, 'JSON', '-' * 15)
print(json_data)
print('-' * 15, 'XML', '-' * 15)
print(root)
print('-' * 40)
"""
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la lógica de creación de los archivos anteriores, crea un
 * programa capaz de leer y transformar en una misma clase custom de tu 
 * lenguaje los datos almacenados en el XML y el JSON.
 * Borra los archivos.
"""
from abc import ABC, abstractmethod


class FileReader(ABC):

    @abstractmethod
    def read() -> list[dict] | dict:
        pass


class JsonReader(FileReader):

    @staticmethod
    def read(file_path: str) -> list[dict] | dict:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data


class XmlReader(FileReader):

    @staticmethod
    def xml_to_dict(element):
        """Convierte un elemento XML y sus hijos en un diccionario de Python."""
        if not list(element):
            return element.text
        dicc = {}
        for child in element:
            if len(element.findall(child.tag)) > 1:
                if child.tag not in dicc:
                    dicc[child.tag] = []
                dicc[child.tag].append(XmlReader.xml_to_dict(child))
            else:
                dicc[child.tag] = XmlReader.xml_to_dict(child)
        return dicc

    @staticmethod
    def read(file_path: str) -> dict:
        tree = ET.parse(file_path)
        root = tree.getroot()
        return XmlReader.xml_to_dict(root)


class Person:
    name = None
    age = None
    birth_date = None
    lenguages = None

    def __init__(self, file_path: str = None) -> None:
        self.file_path = file_path

    def __str__(self) -> str:
        return f'{self.name = }, {self.age = }, {self.birth_date = }, {self.lenguages = }'

    def file_type(self) -> str:
        return os.path.splitext(self.file_path)[1]

    def read_file(self, reader: FileReader) -> list[dict] | dict:
        return reader.read(self.file_path)

    def read_and_load_file(self, reader: FileReader) -> None:
        data = self.read_file(reader)
        self.name = data.get('name', None)
        self.age = data.get('age', None)
        self.birth_date = data.get('birth_date', None)
        self.lenguages = data.get('programming_languages', None)


json_person = Person('juandaherrera.json')
print(json_person)
json_person.read_and_load_file(JsonReader)
print(json_person)

print('-' * 25, 'XML', '-' * 25)

xml_person = Person('juandaherrera.xml')
print(xml_person)
xml_person.read_and_load_file(XmlReader)
print(xml_person)

if os.path.exists(f'{file_name}.json'):
    os.remove(f'{file_name}.json')

if os.path.exists(f'{file_name}.xml'):
    os.remove(f'{file_name}.xml')
