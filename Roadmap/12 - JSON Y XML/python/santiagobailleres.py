'''EJERCICIO:
Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los
siguientes datos (haciendo uso de la sintaxis correcta en cada caso):
- Nombre
- Edad
- Fecha de nacimiento
- Listado de lenguajes de programación
Muestra el contenido de los archivos.
Borra los archivos.
DIFICULTAD EXTRA (opcional):
Utilizando la lógica de creación de los archivos anteriores, crea un
programa capaz de leer y transformar en una misma clase custom de tu 
lenguaje los datos almacenados en el XML y el JSON.
Borra los archivos.'''

import json
import xml.etree.ElementTree as xml
import os

data = {
    'name': 'Santiago Bailleres',
    'age': 25,
    'birth_date': '25-06-1999',
    'programming_languages': ['Python', 'JavaScript', 'Java']
}

xml_file = 'santiagobailleres.xml'
json_file = 'santiagobailleres.json'

# Crear archivo XML
def create_xml():
    root = xml.Element('data') # Crear elemento raíz
    
    for key, value in data.items(): # Recorrer diccionario
        child = xml.SubElement(root, key) # Crear elemento hijo para cada par clave-valor
        if isinstance(value, list): # isinstance() devuelve True si el objeto es una instancia de la clase especificada
            for item in value: # Si el valor es una lista, recorrerla
                xml.SubElement(child, 'item').text = item # Crear un elemento hijo para cada item de la lista
        else:
            child.text = str(value) # Si no es una lista, asignar el valor como texto del elemento hijo
    tree = xml.ElementTree(root) # Crear árbol XML. un arbol XML es un objeto que representa la estructura de un documento XML
    tree.write(xml_file) # Escribir árbol XML en archivo

create_xml()

with open(xml_file, 'r') as xml_data:
    print(xml_data.read())

os.remove(xml_file)

# Crear archivo JSON
def create_json():
    with open(json_file, 'w') as json_data:
        json.dump(data, json_data) # json.dump() escribe un objeto JSON en un archivo

create_json()

with open(json_file, 'r') as json_data:
    print(json_data.read())

os.remove(json_file)

# la libreria os permite interactuar con el sistema operativo, en este caso se utiliza para borrar los archivos creados

# EXTRA

create_json()
create_xml()

class Data:
    def __init__(self, name, age, birth_date, programming_languages):
        self.name = name
        self.age = age
        self.birth_date = birth_date
        self.programming_languages = programming_languages

with open(xml_file, 'r') as xml_data:
    root = xml.fromstring(xml_data.read()) # fromstring() convierte una cadena XML en un objeto Element
    name = root.find('name').text
    age = int(root.find('age').text)
    birth_date = root.find('birth_date').text
    programming_languages = [item.text for item in root.find('programming_languages')] # Recorrer los elementos hijos de la lista y guardar su texto en una lista
    
    xml_class = Data(name, age, birth_date, programming_languages) 
    print(xml_class.__dict__) # __dict__ devuelve un diccionario que contiene los atributos de la clase

with open(json_file, 'r') as json_data:
    json_class = Data(**json.load(json_data)) # **kwargs desempaqueta el diccionario y pasa sus elementos como argumentos a la clase
    print(json_class.__dict__)

os.remove(xml_file)
os.remove(json_file)