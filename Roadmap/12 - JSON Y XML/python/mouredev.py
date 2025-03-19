import os
import xml.etree.ElementTree as xml
import json

data = {
    "name": "Brais Moure",
    "age": 36,
    "birth_date": "29-04-1987",
    "programming_languages": ["Python", "Kotlin", "Swift"]
}

xml_file = "mouredev.xml"
json_file = "mouredev.json"

"""
Ejercicio
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

"""
Extra
"""

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
    name = root.find("name").text
    age = root.find("age").text
    birth_date = root.find("birth_date").text
    programming_languages = []
    for item in root.find("programming_languages"):
        programming_languages.append(item.text)

    xml_class = Data(name, age, birth_date, programming_languages)
    print(xml_class.__dict__)


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
