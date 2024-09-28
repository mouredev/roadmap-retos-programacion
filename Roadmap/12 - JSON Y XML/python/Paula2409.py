"""
/*
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
"""
import json
import xml.etree.ElementTree
import os

data = {
    'name': 'Paula Adgi Romano', 
    'age': 36, 'birth': '24/09/1987', 
    'languages': ['Python', 'Javascript', 'Java']
}

""" JSON: Javascript Object Notation """

# Create
def create_json():
    with open("C:/Users/pau87/OneDrive/Documentos/Roadmap/data.json", 'w') as file_json:
        read = json.dump(data,file_json)

# Read
def read_json():
    with open("C:/Users/pau87/OneDrive/Documentos/Roadmap/data.json", 'r') as file_json:
        print(file_json.read())

create_json()
read_json()

# Delete
os.remove("C:/Users/pau87/OneDrive/Documentos/Roadmap/data.json")

""" XML: Extensible Markup Language """

# Create
tree = xml.etree.ElementTree.parse("C:/Users/pau87/OneDrive/Documentos/Roadmap/data.xml")
root = tree.getroot()
print(root.tag)
print(root.attrib)

# Read
for node in root:
    print(node.tag, node.attrib)
print(root[0].text)
print(root[1].text)
print(root[2].text)

# Delete 
os.remove("C:/Users/pau87/OneDrive/Documentos/Roadmap/data.xml")