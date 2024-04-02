#12 JSON & XML
"""
 * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
 *
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los siguientes datos (haciendo uso de la sintaxis correcta en cada caso):
 * - Nombre
 * - Edad
 * - Fecha de nacimiento
 * - Listado de lenguajes de programación
 * Muestra el contenido de los archivos.
 * Borra los archivos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la lógica de creación de los archivos anteriores, crea un programa capaz de leer y transformar en una misma clase custom de tu 
 lenguaje los datos almacenados en el XML y el JSON.
 * Borra los archivos.
"""

import xml.etree.ElementTree as ET
import os

abspath = os.path.abspath(__file__) #get the file directory
dname = os.path.dirname(abspath)
os.chdir(dname) #change to file directory

#Create XML file
root = ET.Element("ContactsXML")
contact = ET.SubElement(root, "Contact")
name = ET.SubElement(contact, "Name")
name.text = "Saul"
age = ET.SubElement(contact, "Age")
age.text = "25"
birthdate = ET.SubElement(contact, "Birthdate")
birthdate.text = "02/12/2010"
coddingList = ET.SubElement(contact, "Coddinglist")
coddingList.text = "Pyhton, VBA, GOlang, JavaScript"

#Write to XML file
tree = ET.ElementTree(root)
tree.write("contacts.xml")

#Print XML as string
xml_string = ET.tostring(root)
print(xml_string)

#Remove file XML
os.remove("contacts.xml")


#XML 
xml_file = "contacts002.xml"

data = {
    "name" : "SSM",
    "age" : 22,
    "birth_date" : "22/12/2010",
    "programming_languages" : ["Pyhton", "VBA", "GOlang", "JavaScript"]
}

def save_xml():

    root = ET.Element("data")

    for key, value in data.items():
        child = ET.SubElement(root, key)
        if isinstance(value, list):
            for item in value:
                ET.SubElement(child, "item").text = item
        else:
            child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(xml_file)

save_xml()

with open(xml_file, "r") as xml_data:
    print(xml_data.read())

os.remove(xml_file)

#Create JOSN file
import json

filename = 'contacts.json'
isFile = os.path.isfile(filename)
 
person = {"contactsJSON" :[{"Name": "Saul Saez", "Age": "22", "BirthDate":"02/12/2010", "Coddinglist":"Pyhton, VBA, GOlang, JavaScript"}, 
                     ]}

#Save JSON as file
with open(filename, 'w') as fp:
    json.dump(person, fp, indent=4)

#Print JSON as string
print(person)

#Delete JSON
os.remove("contacts.json")


#JSON
json_file = "contacts002.json"

def save_json():
    with open(json_file, "w") as json_data:
        json.dump(data, json_data, indent=4)

save_json()

with open(json_file, "r") as json_data:
    print(json_data.read())

os.remove(json_file)

##EXTRA:

save_xml()
save_json()

class Data:
    
    def __init__(self, name, age, birth_date, programming_languages) -> None:
        self.name = name
        self.age = age
        self.birth_date = birth_date
        self.programming_languages = programming_languages

with open(xml_file, "r") as xml_data:

    root = ET.fromstring(xml_data.read())
    name = root.find("name").text
    age = root.find("age").text
    birth_date = root.find("birth_date").text
    programming_languages = []
    for item in root.find("programming_languages"):
        programming_languages.append(item.text)

    data_from_xml = Data(name, age, birth_date, programming_languages)
    print(data_from_xml.__dict__)

with open(json_file, "r") as json_data:
    json_dict = json.load(json_data)
    json_class = Data(
        json_dict["name"],
        json_dict["age"],
        json_dict["birth_date"], 
        json_dict["programming_languages"]
    )
    print(json_class.__dict__)

os.remove(xml_file)
os.remove(json_file)
