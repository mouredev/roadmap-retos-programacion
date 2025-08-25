import xml.etree.ElementTree as xml
import os
import json
xml_file = "juanma.xml"

data = {
    "name" : "Juanma",
    "edad" : 32,
    "fecha_nacimiento" : "13-11-1992",
    "lenguajes_programacion" : ["Python", "HTML"]      
    
}
# XML

def save_xml():
    
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

with open(xml_file, "r") as xml_data:
    print(xml_data.read())

os.remove(xml_file)

# JSON

json_file = "juanma.json"
def save_json():
    with open(json_file, "w") as json_data:
        json.dump(data, json_data)
save_json()

with open(json_file, "r") as json_data:
    print(json_data.read())
os.remove(json_file)

"""
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la lógica de creación de los archivos anteriores, crea un
 * programa capaz de leer y transformar en una misma clase custom de tu 
 * lenguaje los datos almacenados en el XML y el JSON.
 * Borra los archivos.
"""
save_xml()
save_json()

class Data:
    
    def __init__(self, name, edad, fecha_nacimiento, lenguajes_programacion : list):
        self.name = name
        self.edad = edad
        self.fecha_nacimiento = fecha_nacimiento
        self.lenguajes_programacion = lenguajes_programacion

with open(xml_file, "r") as xml_data:
    
    root = xml.fromstring(xml_data.read())
    name = root.find("name").text
    edad = root.find("edad").text
    fecha_nacimiento = root.find("fecha_nacimiento").text
    lenguajes_programacion = []
    for item in root.find("lenguajes_programacion"):
        lenguajes_programacion.append(item.text)
        
    data_from_xml = Data(name, edad, fecha_nacimiento, lenguajes_programacion)
    print(data_from_xml.__dict__)
    
with open(json_file, "r") as json_data:
    json_dict = json.load(json_data)
    json_class = Data(json_dict["name"], json_dict["edad"], json_dict["fecha_nacimiento"], json_dict["lenguajes_programacion"])
    print(json_class.__dict__)

os.remove(xml_file)
os.remove(json_file)