import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
import json
import os

# EJERCICIO
# Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los
# siguientes datos (haciendo uso de la sintaxis correcta en cada caso):
# - Nombre
# - Edad
# - Fecha de nacimiento
# - Listado de lenguajes de programación
# Muestra el contenido de los archivos.
# Borra los archivos.

os.chdir(r'Roadmap\12 - JSON Y XML\python')

xml_filename = 'data.xml'
json_filename = 'data.json'

data_dict = {
    'name': 'Gabriel',
    'age': 26,
    'birthday': '19-09-2000',
    'programming_languages': [
        'Java',
        'C#',
        'Python'
    ]
}

def create_xml_file(filename: str, data: dict):
    root = ET.Element('data')

    for k, v in data.items():
        if type(v) == list:
            child = ET.Element(k)
            root.append(child)

            for item in v:
                grandchild = ET.SubElement(child, 'item')
                grandchild.text = item
        else:
            tag = ET.SubElement(root, k)
            tag.text = str(v)

    raw_string = ET.tostring(root, 'utf-8')
    parsed = minidom.parseString(raw_string)

    clean_xml = parsed.toprettyxml()

    with open(filename, 'w') as f:
        f.write(clean_xml)

    print(f'¡Archivo \'{filename}\' creado!')

def create_json_file(filename: str, data: dict):

    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

    print(f'¡Archivo \'{filename}\' creado!')

def get_root_from_xml(filename: str):
    tree = ET.parse(filename)
    return tree.getroot()

def get_dict_from_json(filename: str):
    with open(filename, 'r') as f:
        return json.load(f)

def print_file_data(filename: str, file_type: str = 'json'):
    if file_type == 'json':
        data = get_dict_from_json(filename)

        for k, v in data.items():
            if type(v) == list:
                print(f"{k}:")
                for item in v:
                    print(f"> {item}")
            else:
                print(f"{k}: {v}")
    elif file_type == 'xml':
        root = get_root_from_xml(filename)

        for child in root:
            if len(child) > 0:
                print(f"{child.tag}:")
                for grandchild in child:
                    print(f"> {grandchild.text}")
            else:
                print(f"{child.tag}: {child.text}")
    else:
        print(f'Tipo \'{file_type}\' no aceptado.')

def delete_file(filename: str):
    if os.path.exists(filename):
        os.remove(filename)
        print(f'¡Archivo \'{filename}\' eliminado!')

print('=== CREAR Y LEER ARCHIVO XML ===')

create_xml_file(xml_filename, data_dict)

print_file_data(xml_filename, 'xml')

delete_file(xml_filename)

print('\n=== CREAR Y LEER ARCHIVO JSON ===')
create_json_file(json_filename, data_dict)

print_file_data(json_filename, 'json')

delete_file(json_filename)

# DIFICULTAD EXTRA (opcional)
# Utilizando la lógica de creación de los archivos anteriores, crea un
# programa capaz de leer y transformar en una misma clase custom de tu
# lenguaje los datos almacenados en el XML y el JSON.
# Borra los archivos.

class Data():
    def __init__(self, name: str, age: int,
                 birthday: str, programming_languages: list):
        self.__name = name
        self.__age = age
        self.__birthday = birthday
        self.__programming_languages = programming_languages

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_birthday(self):
        return self.__birthday

    def get_programming_languages(self):
        return self.__programming_languages

    def print_data(self):
        print("DATA:")
        print(f"Name: {self.get_name()}")
        print(f"Age: {self.get_age()} years old")
        print(f"Birthday: {self.get_birthday()}")
        print("Programming languages:")
        for item in self.get_programming_languages():
            print(f"> {item}")

def get_data_from_xml(filename: str):
    root = get_root_from_xml(filename)

    name = None
    age = None
    birthday = None
    programming_languages = []

    for child in root:
        match child.tag:
            case 'name':
                name = child.text
            case 'age':
                age = int(child.text)
            case 'birthday':
                birthday = child.text
            case 'programming_languages':
                for grandchild in child:
                    programming_languages.append(grandchild.text)

    return Data(name, age, birthday, programming_languages)

def get_data_from_json(filename: str):
    data = get_dict_from_json(filename)

    name = None
    age = None
    birthday = None
    programming_languages = []

    for k, v in data.items():
        match k:
            case 'name':
                name = v
            case 'age':
                age = int(v)
            case 'birthday':
                birthday = v
            case 'programming_languages':
                programming_languages = v

    return Data(name, age, birthday, programming_languages)

print('\n=== OBTENER DATOS DE XML EN CLASE ===')
create_xml_file(xml_filename, data_dict)

data = get_data_from_xml(xml_filename)
data.print_data()

delete_file(xml_filename)

print('\n=== OBTENER DATOS DE JSON EN CLASE ===')
create_json_file(json_filename, data_dict)

data = get_data_from_json(json_filename)
data.print_data()

delete_file(json_filename)