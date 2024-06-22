# #12 JSON Y XML
#### Dificultad: Difícil | Publicación: 18/03/24 | Corrección: 25/03/24

## Ejercicio


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

import os
import xml.etree.ElementTree as xml
import json

data = {
'name' : 'Daniel',
'age' : 33,
'birth_date' : '19-11-1990',
'languages' : ['python', 'sql'],
'countries' : {
    'live_in' : 'Mexico', 'lived_in' : 'USA'
    }
}

xml_file = 'Daniel.xml'
json_file = 'Daniel.json'

def create_xml():
    # nombre de la raiz
    root = xml.Element('programmer')

    # Extraemos el key y value en data
    for key, value in data.items():
        '''Creamos un child
        root es el padre y key es el tag (nombre del sub elemento)
        Aqui el tag toma el nombre de los keys o sub elementos'''
        child = xml.SubElement(root, key)
        
        # Si el value es una instancia de la clase lista (['python', 'sql']):
        if isinstance(value, list):
            # Se itera entre los elementos de value (lista)
            for item in value:
                
                '''se crea un sub elemento.
                child es el padre e 'item' el nombre de los tags.
                cada tag es decir, cada 'item' contendra un elemento de la lista en formato str
                (text)
                .text en un elemento XML se utiliza para asignar o recuperar el contenido de texto de ese elemento
                '''
                xml.SubElement(child, 'item').text = item

        # Creo un sub-sub elemento 'grand_child' 
        elif isinstance(value, dict):
            for sub_key, sub_value in value.items():
                grand_child = xml.SubElement(child, 'item')
                xml.SubElement(grand_child, sub_key).text = sub_value
        
        # Muestra el value como tal en formato string
        else:
            child.text = str(value)

    tree = xml.ElementTree(root)
    tree.write(xml_file)

create_xml()
#Lo abro y lo leo
with open(xml_file, 'r') as xml_data:
    print(xml_data.read())

#os.remove(xml_file)

# JSON
def create_json():
    with open(json_file, 'w') as json_data: 
        # Tomo el dicc data, lo convierto a json y lo guardo en json_data
        json.dump(data, json_data)
create_json()

with open(json_file, 'r') as json_data:
    print(json_data.read())

#os.remove(json_file)



'''Extra'''

create_xml()
create_json()

class modify:
    def __init__(self, name, age, birth_date, languages, countries) -> None:
        self.name = name
        self.age = age
        self.birth_date = birth_date
        self.languages = languages
        self.countries = countries
with open(xml_file, 'r') as xml_data:
    # Obtengo y guardo el texto de mi archivo
    root = xml.fromstring(xml_data.read())
    # Encuentra el tag y guarda su contenido (en este caso texto)
    name = root.find('name').text
    age = root.find('age').text
    birth_date = root.find('birth_date').text
    # languages = root.find('languages').text
    languages = []
    for item in root.find('languages'):
        languages.append(item.text)
    countries = root.find('countries').text

data_from_xml = modify(name, age, birth_date, languages, countries)
print(data_from_xml.__dict__)

with open(json_file, 'r') as json_data:
    json_dict = json.load(json_data)
    json_class = modify(
        json_dict['name'],
        json_dict['age'],
        json_dict['birth_date'],
        json_dict['languages'],
        json_dict['countries']
    )
    print(json_class.__dict__)

os.remove(xml_file)
os.remove(json_file)
    

