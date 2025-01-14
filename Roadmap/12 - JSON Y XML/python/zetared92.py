# RETO 12 JSON Y XML

import os
import xml.etree.ElementTree as xml
import json

"Desarrolla un programa para crear archivo XML y JSON"

data = {
    "name": "Zeta Vega",
    "age": 31,
    "birth_date": "03-12-1992",
    "languages": ["Python", "Swift", "Rust"]
}

xml_file = "zetared.xml"
json_file = "zetared.json"

"""
EJERCICIO
"""

# XML

def create_xml():

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

create_xml()

with open(xml_file, "r") as xml_data:
    print(xml_data.read())

os.remove(xml_file)

# JSON

def create_json():
    with open(json_file, "w") as json_data:
        json.dump(data, json_data)


create_json()

with open(json_file, "r") as json_data:
    print(json_data.read())

os.remove(json_file)


# Extra

print("🧩 DIFICULTAD EXTRA - ARCHIVOS 🧩")

create_xml()
create_json()

class Data:

    def __init__(self, name, age, birth_date, languages) -> None:
        self.name = name
        self.age = age
        self.birth_date = birth_date
        self.languages = languages

with open(xml_file, "r") as xml_data:

    root = xml.fromstring(xml_data.read())
    name = root.find("name").text
    age = root.find("age").text
    birth_date = root.find("birth_date").text
    languages = []
    for item in root.find("languages"):
        languages.append(item.text)
    
    xml_class = Data(name, age, birth_date, languages)
    print(xml_class.__dict__)

with open(json_file, "r") as json_data:
    json_dict = json.load(json_data)
    json_class = Data(
        json_dict["name"],
        json_dict["age"],
        json_dict["birth_date"],
        json_dict["languages"]
    )
    print(json_class.__dict__)

os.remove(xml_file)
os.remove(json_file)