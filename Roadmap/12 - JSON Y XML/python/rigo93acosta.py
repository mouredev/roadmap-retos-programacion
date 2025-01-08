'''
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
'''
import xml.etree.ElementTree as ET
import json
import os

data = {
    "name" : 'Rigoberto Acosta',
    "age" : 30,
    "birth_date" : '25-05-1993',
    "programming_languages" : ['Python', 'C++', 'Matlab']
}

## XML

def create_xml():

    root = ET.Element('data')
    
    for key, value in data.items():
        child = ET.SubElement(root, key)
        if isinstance(value, list):
            for item in value:
                ET.SubElement(child, 'item').text = item
        else:
            child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write('data.xml')

create_xml()

def read_xml():
    tree = ET.parse('data.xml')
    root = tree.getroot()

    data = {}
    for child in root:
        if child.tag == 'programming_languages':
            data[child.tag] = [item.text for item in child]
        else:
            data[child.tag] = child.text

    return data

print(read_xml())

os.remove('data.xml')

## JSON

def create_json():
    with open('data.json', 'w') as file:
        json.dump(data, file)

def read_json():
    with open('data.json', 'r') as file:
        return json.load(file)

create_json()
print(read_json())

os.remove('data.json')

'''
Extra
'''

create_xml()
create_json()

class CustomData:
    def __init__(self, name, age, birth_date, programming_languages) -> None:
        self.name = name
        self.age = age
        self.birth_date = birth_date
        self.programming_languages = programming_languages

    def __str__(self):
        return f'Name: {self.name}\nAge: {self.age}\nBirth Date: {self.birth_date}\nProgramming Languages: {", ".join(self.programming_languages)}'
    

with open('data.xml', 'r') as file:

    print("\nXML")
    root = ET.fromstring(file.read())
    name = root.find('name').text
    age = int(root.find('age').text)
    birth_date = root.find('birth_date').text
    programming_languages = [item.text for item in root.find('programming_languages')]

    custom_data = CustomData(name, age, birth_date, programming_languages)

    print(custom_data)

with open('data.json', 'r') as file:
    print("\nJSON")
    data = json.load(file)
    custom_data = CustomData(data['name'], data['age'], data['birth_date'], data['programming_languages'])
    print(custom_data)