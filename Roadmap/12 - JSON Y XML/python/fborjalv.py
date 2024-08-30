import xml.etree.ElementTree as xml
import json
import os

data = {
    "nombre": "Borja",
    "edad": 32,
    "fecha_nacimiento": "29/04/1992",
    "lenguajes_programacion": ['Python', 'JavaScript']
}

# JSON

json_file = "fborjalv.json"

with open(json_file, "w") as file:
    json.dump(data, file)

with open(json_file, "r") as file:
    print(file.read())

#os.remove(json_file)


# XML
xml_file = "fborjalv.xml"

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


with open(xml_file, "r") as xml_data:
    print(xml_data.read())


# ejercicio 

"""
* DIFICULTAD EXTRA (opcional):
 * Utilizando la lógica de creación de los archivos anteriores, crea un
 * programa capaz de leer y transformar en una misma clase custom de tu 
 * lenguaje los datos almacenados en el XML y el JSON.
 * Borra los archivos.
 */

"""

class User:
    def __init__(self, nombre, edad, fecha_nacimiento, lenguajes_programacion) -> None:
        self.nombre = nombre
        self.edad = edad
        self.fecha_nacimiento = fecha_nacimiento
        self.lenguajes_programación = lenguajes_programacion



with open(json_file ,"r") as json_data: 
    json_dict = json.load(json_data)
    my_user = User(json_dict["nombre"],
                    json_dict["edad"],
                    json_dict["fecha_nacimiento"],
                    json_dict["lenguajes_programacion"])
    print(my_user.__dict__)