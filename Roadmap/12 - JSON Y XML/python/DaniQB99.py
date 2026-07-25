'''
EJERCICIO:
Desarrolla un programa capaz de crear un archivo XML y JSON que guarde
los siguientes datos (hacindo uso de la sintaxis correcta en cada caso):

- Nombre
- Edad
- Fecha de nacimiento
- Listado de Lenguajes de programación
Muestra el contenido de los archivos.
Borra los archivos.
'''

import xml.etree.ElementTree as xml
import json
import os

# OBJETO
data = {
    "name" : "Dani",
    "age" : "25",
    "birth_date" : "26-07-1999",
    "programming_languages" : ['Python', 'Java', 'HTML', 'CSS']
}

xml_file = "DaniQB99.xml"

# XML

# ESCRIBIR XML
def save_xml():
    
    with open(xml_file, "w") as file:
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

save_xml()

# LEER XML
def read_xml():
    
    with open(xml_file, "r") as xml_data:
        print('XML')
        print(xml_data.read())
        

        
read_xml()

# BORRAR XML
os.remove(xml_file)

# JSON

json_file = "DaniQB99.json"

# ESCRIBIR JSON
def save_json():

    with open(json_file, "w") as json_data:
        json.dump(data, json_data)

save_json()

# LEER JSON
def read_json():

    with open(json_file, "r") as json_data:
        print('JSON')
        print(json_data.read())
        
read_json()

# BORRAR JSON
os.remove(json_file)

'''
DIFICULTAD EXTRA (opcional):
Utilizando la lógica de creación de los archivos anteriores, crea un
programa capaz de leer y transformar en una misma clase custom de tu 
lenguaje los datos almacenados en el XML y el JSON.
Borra los archivos.
'''

print("\nEJERCICIO EXTRA\n")

save_xml()
save_json()

# CLASE CUSTOM
class Data():       
    def __init__(self, name, age, birth_date, programming_languages) -> None:
        self.name = name
        self.age = age
        self.birth_date = birth_date
        self.programming_languages = programming_languages  
        

# CLASE XML
with open (xml_file, 'r') as xml_data:
    
    root = xml.fromstring(xml_data.read()) # xml.fromstring() es un metodo de xml para leer el xml
    name = root.find("name").text
    age =root.find("age").text
    birth_date = root.find("birth_date").text
    programming_languages = []
    for item in root.find("programming_languages"):
        programming_languages.append(item.text)
     
    xml_class = Data(name, age, birth_date, programming_languages)
    print('XML')
    print(xml_class.__dict__)


# ClASE JSON
with open (json_file, 'r') as json_data:

    json_dict = json.load(json_data) # json.load() es un metodo de json para leer el diccionario
    json_class = Data(
        json_dict['name'],
        json_dict['age'],
        json_dict['birth_date'],
        json_dict['programming_languages']
    )
    print('JSON')
    print(json_class.__dict__)
        
os.remove(xml_file)
os.remove(json_file)