import json
import os
import xml.etree.ElementTree as xml

data = {
    "name" : "Mario",
    "age" : 40,
    "birth_date" : "01/01/2000",
    "programming_languages" : ["Python", "C#"]
}

# XML
xml_file = "mvidalb.xml"

def create_xml():

    root = xml.Element("data")

    for key, value in data.items():
        child = xml.SubElement(root, key)
        if isinstance(value, list):
            for item in value:
                child_child = xml.SubElement(child, "item")
                child_child.text = item
        else:
            child.text = str(value)

    tree = xml.ElementTree(root)
    tree.write(xml_file)

create_xml()

with open(xml_file, "r") as xml_data:
    print("XML file:")
    print(xml_data.read())

os.remove(xml_file)


# JSON
json_file = "mvidalb.json"

def create_json():
    with open(json_file, "w") as json_data:
        json.dump(data, json_data)

create_json()

# Shift + Alt + F para formatear el archivo a formato JSON!

with open(json_file, "r") as json_data:
    print("JSON file:")
    print(json_data.read())

os.remove(json_file)


'''
Ejercicio extra
'''
create_xml()
create_json()

class Data:

    def __init__(self, name, age, birth_date, programming_languages) -> None:
        self.name = name
        self.age = age
        self.birth_date = birth_date
        self.programming_languages = programming_languages

def extract_xml():
    with open(xml_file, "r") as xml_data:

        root = xml.fromstring(xml_data.read())
        name = root.find("name").text
        age = root.find("age").text
        birth_date = root.find("birth_date").text
        
        programming_languages = []
        for item in  root.find("programming_languages"):
            programming_languages.append(item.text)

        xml_class = Data(name, age, birth_date, programming_languages)
        print("DATA CLASS: XML FILE")
        print(xml_class.__dict__)

def extract_json():
    with open(json_file, "r") as json_data:

        json_dict = json.load(json_data)
        
        name = json_dict["name"]
        age = json_dict["age"]
        birth_date = json_dict["birth_date"]
        programming_languages = json_dict["programming_languages"]

        json_class = Data(name, age, birth_date, programming_languages)
        print("DATA CLASS: JSON FILE")
        print(json_class.__dict__)

extract_xml()
extract_json()

os.remove(xml_file)
os.remove(json_file)

