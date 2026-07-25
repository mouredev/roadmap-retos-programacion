'''
IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
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
 * Utilizando la lógica de creación de los archivos anteriores, crea un programa capaz de leer y transformar en una misma clase custom de tu lenguaje los datos almacenados en el XML y el JSON.
 * Borra los archivos.
 '''

import xml.etree.ElementTree as xml
import os

#creamos un diccionario
data = {
    'name': 'Adolfo Loza',
    'edad': 56,
    'birth_date': '12-07-1968',
    'languages':['Pyhton', 'Basic', 'C']
}

xml_file = 'adolfolozaa.xml'
#xml
def save_xml():

    root = xml.Element('data')
    for key, value in data.items():
        child = xml.SubElement(root, key)
        if isinstance(value, list):
            for item in value:
                xml.SubElement(child, 'item').text = item
        else:
            child.text = str(value)

    tree = xml.ElementTree(root)
    tree.write(xml_file)


save_xml()

#leer el archivo
'''with open(xml_file) as xml_data:
    print(xml_data.read())
'''


#JSON
import json

print('------------------')

json_file = 'data.json'
# convert into JSON
def create_json():
    y = json.dumps(data)

    #print(y)
    with open(json_file, 'w') as f:
        json.dump(data, f)

create_json()

'''with open('data.json') as data_json:
    print(data_json.read())'''

'''
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la lógica de creación de los archivos anteriores, crea un
 * programa capaz de leer y transformar en una misma clase custom de tu 
 * lenguaje los datos almacenados en el XML y el JSON.
 * Borra los archivos.
'''



#leer 

class Data:
    def __init__(self, name, age, birth_date, language) -> None:
        self.name = name
        self.age = age
        self.birth_date = birth_date
        self.language = language

with open(xml_file, 'r') as xml_data:
    root = xml.fromstring(xml_data.read())
    name = root.find('name').text
    age = root.find('edad').text
    birth_date =root.find('birth_date').text
    languages = []
    for item in root.find('languages'):
        languages.append(item.text)

    xml_class = Data(name, age, birth_date, languages)
    print('From XML -----------')
    print(xml_class.__dict__)

    #From JSON

with open(json_file, 'r') as json_data:
    print('From JSON -----------')
    json_dict = json.load(json_data)
    json_class = Data(
        json_dict['name'], 
        json_dict['edad'], 
        json_dict['birth_date'], 
        json_dict['languages'])
    print(json_class.__dict__)


os.remove(xml_file)
os.remove(json_file)

