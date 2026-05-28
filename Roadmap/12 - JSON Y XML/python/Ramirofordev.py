# Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los siguientes datos:
'''
* Nombre
* Edad 
* Fecha de nacimiento
* Listado de lenguajes de programacion
'''
import os
import json
import xml.etree.ElementTree as xml

datos = {"name": input("Inserte su nombre: "), "age": 18, "birth_date": "22-12-2006", "programming_languages": ["Python, JavaScript, SQL"]}

# XML

xml_file = "nacho.xml"

def save_xml():
    root = xml.Element("data")
    for key, value in datos.items():
        child = xml.SubElement(root, key)
        if isinstance(value, list):
            for item in value:
                xml.SubElement(child, "item").text = item
        else:    
            child.text = str(value)

    tree = xml.ElementTree(root)
    tree.write("nacho.xml")    

save_xml()

with open("nacho.xml", "r") as f:
    print(f.readlines())

# os.remove(xml_file)

# JSON

json_file = "nacho.json"

with open(json_file, "w+") as json_data:
    json.dump(datos, json_data)

with open(json_file, "r") as f:
    print(f.readlines())

# os.remove(json_file)

# Dificultad extra

'''
Utilizando la logica de creacion de los archivos anteriores, crea un programa capaz de leer y transformar en una misma clase de custom de tu lenguaje de datos almacenados en el XML y el JSON.
'''

class Data:
    def __init__(self, name, age, birth_date, programming_language):
        self.name = name
        self.age = age
        self.birth_date = birth_date
        self.programming_language = programming_language

with open(xml_file, "r") as f:
    root = xml.fromstring(f.read())
    print(xml.tostring(root, encoding='unicode'))
    name = root.find("name").text
    age = root.find("age").text
    birth_date = root.find("birth_date").text
    programming_languages = [
        item.text for item in root.find("programming_languages").findall("item")
    ]

    data_from_xml = Data(name, age, birth_date, programming_languages)
    print(data_from_xml.__dict__)

with open(json_file, "r") as f:
    json_dict = json.load(f)
    json_class = Data(
        json_dict["name"],
        json_dict["age"],
        str(json_dict["birth_date"]),
        json_dict["programming_languages"]
        )
    print(json_class.__dict__)

os.remove(xml_file)
os.remove(json_file)