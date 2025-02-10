#12 { Retos para Programadores } JSON Y XML

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

# Bibliography reference
# Professional JavaScript for web developers by Matt Frisbie [Frisbie, Matt] (z-lib.org)
#Python Notes for Professionals. 800+ pages of professional hints and tricks (GoalKicker.com) (Z-Library)
# GPT

# JSON
# JSON stands for "JavaScript Object Notation", but it's not JavaScript. 
# Think of it as just a data serialization format that happens to be directly usable as a JavaScript literal. 
# However, it is not advisable to directly run (i.e. through eval()) JSON that is fetched from an external source. 
# Functionally, JSON isn't very different from XML or YAML – some confusion can be avoided if JSON is just imagined as some serialization format that looks very much like JavaScript.

import json
import os
import xml.etree.ElementTree as ET
from xml.dom import minidom
from datetime import datetime

# Short for print
log = print

# JSON string example
json_string = '[{"name":"Kox","age":51},{"name":"Fanny","age":17}]'
data = json.loads(json_string, object_hook=lambda d: {k: v.upper() if k == 'name' else v for k, v in d.items()})
log(data)  # [{'name': 'KOX', 'age': 51}, {'name': 'FANNY', 'age': 17}]

# Parsing with a reviver function for date
json_string2 = '{"date":"2024-10-12T12:28:40.143Z"}'
data2 = json.loads(json_string2, object_hook=lambda d: {k: (datetime.fromisoformat(v[:-1]) if k == 'date' else v) for k, v in d.items()})
log(data2)  # {'date': datetime.datetime(2024, 10, 12, 12, 28, 40, 143000)}

# JSON.stringify equivalent in Python
log(json.dumps(True))  # 'true'
log(json.dumps(154))  # '154'
log(json.dumps('roadmap'))  # '"roadmap"'
log(json.dumps({}))  # '{}'
log(json.dumps({'name': 'Any'}))  # '{"name": "Any"}'
log(json.dumps([41, True, 'System Engineering']))  # '[41, true, "System Engineering"]'
log(json.dumps({"x": 4, "y": 4}, indent=2))  # Pretty print with indentation:
''' 
{
  "x": 4,
  "y": 4
} 

'''

# Data to save
data1 = {
    "name": "Niko Zen",
    "age": 30,
    "birthDate": "1983-08-08",
    "languages": ["JavaScript", "Python", "Ruby", "Rust", "Bash"]
}

# Function to create a JSON file
def create_json(data):
    json_data = json.dumps(data, indent=2)
    with open('data.json', 'w') as json_file:
        json_file.write(json_data)
    log("Content of the JSON file:") # Content of the JSON file:
    log(json_data)

    ''' 
{
  "name": "Niko Zen",
  "age": 30,
  "birthDate": "1983-08-08",
  "languages": [
    "JavaScript",
    "Python",
    "Ruby",
    "Rust",
    "Bash"
  ]
}

 '''

# Function to create an XML file
def create_xml(data):
    person = ET.Element("person")
    ET.SubElement(person, "name").text = data["name"]
    ET.SubElement(person, "age").text = str(data["age"])
    ET.SubElement(person, "birthDate").text = data["birthDate"]
    languages = ET.SubElement(person, "languages")
    for lang in data["languages"]:
        ET.SubElement(languages, "language").text = lang

    # Convert the ElementTree to a string
    xml_data = ET.tostring(person, encoding='unicode')

    # Use minidom to pretty-print the XML
    pretty_xml = minidom.parseString(xml_data).toprettyxml(indent="  ")

    # Write the pretty-printed XML to a file
    with open('data.xml', 'w') as xml_file:
        xml_file.write(pretty_xml)

    log("Content of the XML file:") # Content of the XML file:
    log(pretty_xml)
    ''' 
<?xml version="1.0" ?>
<person>
  <name>Niko Zen</name>
  <age>30</age>
  <birthDate>1983-08-08</birthDate>
  <languages>
    <language>JavaScript</language>
    <language>Python</language>
    <language>Ruby</language>
    <language>Rust</language>
    <language>Bash</language>
  </languages>
</person>
 '''

# Function to delete files
def delete_files():
    os.remove('data.json')
    os.remove('data.xml')
    log("Files deleted.")

# Custom class
class Person:
    def __init__(self, name, age, birth_date, languages):
        self.name = name
        self.age = age
        self.birth_date = birth_date
        self.languages = languages

# Function to read and transform data
def read_and_transform():
    with open('data.json', 'r') as json_file:
        json_data = json.load(json_file)

    with open('data.xml', 'r') as xml_file:
        xml_data = xml_file.read()

    # Transform XML to object
    xml_doc = ET.fromstring(xml_data)
    name = xml_doc.find("name").text
    age = int(xml_doc.find("age").text)
    birth_date = xml_doc.find("birthDate").text
    languages = [lang.text for lang in xml_doc.find("languages").findall("language")]

    # Create an instance of Person
    person = Person(name, age, birth_date, languages)
    log("Data transformed to Person class:") # Data transformed to Person class:
    log(person.__dict__)  # {'name': 'Niko Zen', 'age': 30, 'birth_date': '1983-08-08', 'languages': ['JavaScript', 'Python', 'Ruby', 'Rust', 'Bash']}

if __name__ == "__main__":
    create_json(data1)
    create_xml(data1)
    read_and_transform()
    delete_files()  #Files deleted.
