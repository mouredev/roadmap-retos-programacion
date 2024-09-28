"""EJERCICIO:
Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los
siguientes datos (haciendo uso de la sintaxis correcta en cada caso):
- Nombre
- Edad
- Fecha de nacimiento
- Listado de lenguajes de programación
Muestra el contenido de los archivos.
Borra los archivos."""

import json
import os
import xml.etree.ElementTree as ET


class JsonFile:
    def __init__(self, path):
        self.file_path = f'{path}.json'

    def create_json(self):
        data = {
            'name': "Brandon",
            'age': 20,
            'dob': "05/20/1994",
            'language': ['Python', 'Matlab', 'C#']
        }
        with open(self.file_path, "w") as json_file:
            json.dump(data, json_file, indent=4)

    def show_json(self):
        with open(self.file_path, "r") as json_file:
            data = json.load(json_file)
        print(json.dumps(data, indent=4))

    def remove_json(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
            print(f"The file '{self.file_path}' has been removed.")
        else:
            print(f"The file '{self.file_path}' does not exist.")


class XmlFile:
    def __init__(self, path):
        self.file_path = f'{path}.xml'

    def create_xml(self):
        root = ET.Element('data')

        name = ET.SubElement(root, 'name')
        name.text = 'Brandon'
        age = ET.SubElement(root,'age')
        age.text = '29'
        dob = ET.SubElement(root, 'dob')
        dob.text = '05/20/1994'
        language = ET.SubElement(root, 'language')
        language.text = str(['Python', 'Matlab', 'C#'])

        tree = ET.ElementTree(root)

        tree.write(self.file_path, encoding="utf-8", xml_declaration=True)

    def show_xml(self):
        tree = ET.parse(self.file_path)

        root = tree.getroot()

        for child in root:
            print(f'{child.tag}: {child.text}')

    def remove_xml(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
            print(f"The file '{self.file_path}' has been removed.")
        else:
            print(f"The file '{self.file_path}' does not exist.")

"""DIFICULTAD EXTRA (opcional):
Utilizando la lógica de creación de los archivos anteriores, crea un
programa capaz de leer y transformar en una misma clase custom de tu 
lenguaje los datos almacenados en el XML y el JSON.
Borra los archivos."""


def print_transformed_information(name, age, dob, language):
    print(f'Name: {name}\n'
          f'Age: {age}\n'
          f'Date of Birth: {dob}\n'
          f'Language: {language}')


def read_transform_json(path):
    file_path = f'{path}.json'

    with open(file_path, 'r') as json_file:
        data = json.load(json_file)

    name = data['name']
    age = data['age']
    dob = data['dob']
    languages = data['language']
    print_transformed_information(name, age, dob, languages)


def read_transform_xml(path):
    file_path = f'{path}.xml'
    tree = ET.parse(file_path)
    root = tree.getroot()

    name = root.find('name').text
    age = root.find('age').text
    dob = root.find('dob').text
    language = root.find('language').text
    print_transformed_information(name, age, dob, language)


json_path = 'myjson'
xml_path = 'myxml'

print('******** JSON ********')

json_file = JsonFile(json_path)
json_file.create_json()
print('\n**** Transformed values from the JSON file ****')
read_transform_json(json_path)
print('\n**** JSON File ****')
json_file.show_json()
json_file.remove_json()

print('\n******** XML ********')

xml_file = XmlFile(xml_path)
xml_file.create_xml()
print('\n**** Transformed values from the XML file ****')
read_transform_xml(xml_path)
print('\n**** XML File ****')
xml_file.show_xml()
xml_file.remove_xml()
