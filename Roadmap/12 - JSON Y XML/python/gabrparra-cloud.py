"""
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
 """

import xml.etree.ElementTree as xml
import os
import json

data ={
"name" : "Gabriel",
"age" : 39,
"birth_date" : "08-09-87",
"programing_languages" : ["Python", "Ladder","Otro"]
}



# XML

xml_file = "gabrparra-cloud.xml"

def save_xml():

    root = xml.Element("data")

    for key, value in data.items():
        child = xml.SubElement(root,key)
        if isinstance(value, list):
            for item in value:
                xml.SubElement(child,"item").text = item

        else:
            child.text = str(value)

    tree = xml.ElementTree(root)
    tree.write(xml_file)

save_xml()

with open(xml_file) as xml_data:
    print(xml_data.read())

#os.remove(xml_file)

# JSON

json_file = "gabrparra-cloud.json"

def save_json():
    with open(json_file,"w") as json_data:
        json.dump(data,json_data)

save_json()

with open(json_file) as json_data:
    print(json_data.read())

#os.remove(json_file)

class Data:

    def __init__(self,name,age,birth_date,programing_languages)-> None:
        self.name = name
        self.age = age
        self.birth_date = birth_date
        self.programing_language=self = programing_languages

with open(xml_file,"r") as xml_data:

    root = xml.fromstring(xml_data.read())
    name = root.find("name").text
    age = root.find("age").text
    birth_date = root.find("birth_date").text
    programing_languages = []
    for item in root.find("programing_languages"):
        programing_languages.append(item.text)

    data_class_xml = Data(name,age, birth_date,programing_languages)
    print(data_class_xml.__dict__)

with open(json_file, "r") as json_data:

    data = json.load(json_data)
    json_class = Data(data["name"],data["age"],data["birth_date"],data["programing_languages"])

    print(json_class.__dict__)

os.remove(xml_file)
os.remove(json_file)