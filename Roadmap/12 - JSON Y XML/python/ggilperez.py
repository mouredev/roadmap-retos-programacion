# 12 JSON & XML
import json
import os
import xml.etree.cElementTree as ET
from dataclasses import dataclass

json_file = "freddy.json"
xml_file = "data.xml"

data = {
    "name": "Guillermo",
    "age": "31",
    "birth_date": "4/6/1993",
    "languages": ["Python"]
}

# JSON

# Write file
def write_json_file():
    with open(json_file, "w") as file:
        json.dump(data, file)

write_json_file()

# Read file
with open(json_file, "r") as file:
    print(json.load(file))

# Remove file
os.remove(json_file)

# XML

# Write file
def write_xml_file():
    root = ET.Element("data")
    for key, value in data.items():
        child = ET.SubElement(root, key)
        if isinstance(value, list):
            for item in value:
                ET.SubElement(child, "lang").text = item
        else:
            child.text = value

    tree = ET.ElementTree(root)
    tree.write(xml_file)

write_xml_file()

# Read file
with open(xml_file, "r") as file:
    print(file.read())

# Remove file
os.remove(xml_file)

# Extra

@dataclass
class Data:
    name: str
    age: int
    birth_date: str
    languages: list

write_json_file()
write_xml_file()

# Transform from JSON
with open(json_file, "r") as file:
    data = json.load(file)
    obj_data = Data(**data)
    print(obj_data)

# Transform from XML
with open(xml_file, "r") as file:
    data = file.read()
    xml_data = ET.fromstring(data)

    name = xml_data.find("name").text
    age = xml_data.find("age").text
    birth_date = xml_data.find("birth_date").text
    languages = []
    for item in xml_data.find("languages"):
        languages.append(item.text)

    obj_data = Data(name, age, birth_date, languages)
    print(obj_data)


