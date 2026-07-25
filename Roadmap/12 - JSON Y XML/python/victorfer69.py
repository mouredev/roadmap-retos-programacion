import os
import xml.etree.ElementTree as xml
import json

#EJERCICIO

data = {
    "name" : "Victor",
    "age" : 21,
    "birthday" : "06-09-2003",
    "languages" : ["Python", "Java", "Swift"]
}

xml_file = "victorfer69.xml"
json_file = "victorfer69.json"


#XML
def save_xml():

    root = xml.Element("data")

    for key, value in data.items():
        child = xml.SubElement(root, key)
        if isinstance(value, list):
            for item in value:
                child2 = xml.SubElement(child, "item").text = item
        else:
            child.text = str(value)
    
    tree = xml.ElementTree(root)
    tree.write(xml_file)

save_xml()

with open(xml_file, "r") as xml_data:
    print (xml_data.read())

os.remove(xml_file)


#JSON
def save_json():
    with open(json_file, "w") as json_data:
        json.dump(data, json_data)

save_json()

with open(json_file, "r") as json_data:
    print(json_data.read())

os.remove(json_file)


#EJERCICIO EXTRA

save_xml()
save_json()

class Data:
    
    def __init__(self, name, age, birthday, languages):
        self.name = name
        self.age = age
        self.birthday = birthday
        self.languages = languages


with open(xml_file, "r") as xml_data:

    root = xml.fromstring(xml_data.read())
    name = root.find("name").text
    age = root.find("age").text
    birth_date = root.find("birthday").text
    programming_languages = []
    for item in root.find("languages"):
        programming_languages.append(item.text)

    xml_class = Data(name, age, birth_date, programming_languages)
    print(f"XML: {xml_class.__dict__}")


with open(json_file, "r") as json_data:
    json_dict = json.load(json_data)
    json_class = Data(
        json_dict["name"],
        json_dict["age"],
        json_dict["birthday"],
        json_dict["languages"]
    )
    print(f"JSON: {json_class.__dict__}")

os.remove(xml_file)
os.remove(json_file)