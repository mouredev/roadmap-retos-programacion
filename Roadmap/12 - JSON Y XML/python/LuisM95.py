"""
Ejercicio
"""

import xml.etree.ElementTree as xml
import xml.dom.minidom as minidom
import os

data = {
    "name" : "Luis",
    "age" : 25,
    "birthday" : "1995-09-19",
    "programming_languages" : ["Python", "HTML", "JavaScript"]
}

def create_xml():
    root = xml.Element("data")

    for key, value in data.items():

        child = xml.SubElement(root, key)
        if isinstance(value, list):
            for item in value:
                xml.SubElement(child, "Item").text = item
        else:
            child.text = str(value)

        tree = xml.ElementTree(root)
        tree.write("programador.xml")

        #Convert the tree to a string
        xml_str = xml.tostring(root, encoding='unicode')

        #Parse the string using a minidom for pretty printing
        dom = minidom.parseString(xml_str)
        pretty_xml_as_string = dom.toprettyxml()

        with open("programador.xml", "w") as f:
            f.write(pretty_xml_as_string)

create_xml()

with open("programador.xml", 'r') as xml_data:
    print(xml_data.read())

#os.remove("programador.xml")


"""
Json
"""

import json

json_file = "programador1.json"

def create_json():
    with open(json_file, "w") as f:
        json.dump(data, f, indent=4)

create_json()

with open(json_file, "r") as f:
    print(f.read())

#os.remove(json_file)

"""
Extra
"""

create_xml()
create_json()

class Data:
    
    def __init__(self, name, age, birthday, programming_languages) -> None:
        self.name = name
        self.age = age
        self.birthday = birthday
        self.programming_languages = programming_languages


with open("programador.xml", "r") as f:
    root = xml.fromstring(f.read())
    name = root.find("name").text
    age = root.find("age").text
    birthday = root.find("birthday").text
    programming_languages = []
    for item in root.find("programming_languages"):
        programming_languages.append(item.text)

    data_class = Data(name, age, birthday, programming_languages)
    print(data_class.__dict__)


#json

with open(json_file, "r") as f:
    json_dict = json.load(f)
    json_class = Data(
        json_dict["name"], 
        json_dict["age"], 
        json_dict["birthday"], 
        json_dict["programming_languages"]
        )
    print(json_class.__dict__)


os.remove("programador.xml")
os.remove(json_file)
