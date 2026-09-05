"""Cómo se representan y transportan datos estructurados"""

#JSON: JavaScript Object Notation
#XML: Extensible Markup Language

#TANTO JSON COMO XML se usan para representar datos estructurados.

"""Data Histórica"""

#XML nace en los años 90's derivado de una tecnología anterior llamada SGML.
#JSON es bastante más joven. 2001-2006.

"""
1960s–1980s
        │
        ▼
   SGML
        │
        │ "Necesitamos estructurar documentos"
        ▼
     XML
   ~1998
        │
        │ "Necesitamos intercambiar datos"
        ▼
     JSON
   ~2000s
"""
import os
import xml.etree.ElementTree as xml
import json

data = {
"name": "Carla",
"age":25,
"birth_date": "25-08-2000",
"programming_languages":  ["python", "java", "react"]
}

xml_file = "carladev.xml"
json_file = "carladev.json"

def create_xml():
  root =  xml.Element("data")

  for key, value in data.items():
    child= xml.SubElement(root,key)
    if isinstance(value,list):
        for item in value:
           xml.SubElement(child, "item").text = item
    else:
        child.text = str(value)

    tree = xml.ElementTree(root)
    tree.write(xml_file)

create_xml()

with open(xml_file) as xml_data:
   print(xml_data.read())

os.remove(xml_file)

#JSON


def create_json():
    with open (json_file, "w") as json_data:
        json.dump(data, json_data)

create_json()


with open(json_file, "r") as json_data:
   print(json_data.read())

#Extra

create_xml()
create_json()

class Data:

   def __init__(self, name, age, birth_date, programming_languages) -> None:
      self.name = name
      self.age = age
      self.birth_date = birth_date
      self.programming_languages = programming_languages

with open(xml_file, "r") as xml_data:

    root = xml.fromstring(xml_data.read())
    name=root.find("name").text
    age=root.find("age").text
    birth_date=root.find("birth_date").text
    programming_languages = []

    for item in root.find("programming_languages"):
        programming_languages.append(item.text)

    xml_class = Data(name,age, birth_date,programming_languages)
    print(xml_class.__dict__)

with open(json_file, "r") as json_data:
   json_dict = json.load(json_data)
   json_class = Data(name = json_dict["name"],
      age =  json_dict["age"],
      birth_date = json_dict["birth_date"],
      programming_languages = json_dict["programming_languages"])
   print(json_class.__dict__)

   os.remove(xml_file)
   os.remove(json_file)

    