import xml.etree.ElementTree as xml
import os
import json

"""
JSON Y XML
"""

data = {
    "name" : "Yenner Alayon",
    "age" : 21,
    "happy_date" : "30/05/2003",
    "languages" : ["PYTHON", "CSHARP"]
}

xml_file = "yenneralayon.xml"
json_file = "yenneralayon.json"


#XML
def create_xml():  
    root = xml.Element("data")
    for key, value in data.items():
        child = xml.SubElement(root,key)
        if isinstance(value,list):
            for item in value:
                xml.SubElement(child, "item").text = item
        else:
            child.text = str(value)
    tree = xml.ElementTree(root)
    tree.write(xml_file)

create_xml()

#Leer Fichero XML
with open(xml_file, "r") as data_xml:
    print(data_xml.read())
#Eliminar  Fichero XML
#os.remove(xml_file)

#JSON

def create_json():
    with open(json_file, "w") as data_json:
         json.dump(data, data_json)
create_json()

with open(json_file, "r") as data_json:
    print(data_json.read())

#os.remove(json_file)

"""
Extra
"""
class Data:

    def __init__(self, name:str, age:int, happy_date:str,languages:list):
        self.name = name
        self.age = age
        self.happy_date = happy_date
        self.languages = languages

# Trabajando con fichero XML desde una clase
with open(xml_file, "r") as xml_data:
    root = xml.fromstring(xml_data.read())
    name = root.find("name").text
    age = root.find("age").text
    happydate = root.find("happy_date").text
    languages = []
    for item in root.find("languages"):
        languages.append(item.text)
    xml_class = Data(name,age,happydate,languages)
    print(xml_class.__dict__)        

# Trabajando con Fichero Json desde una clase
with open(json_file, "r") as json_data:
    json_dict = json.load(json_data)
    json_class = Data(
        json_dict["name"],
        json_dict["age"],
        json_dict["happy_date"],
        json_dict["languages"],
    )
    print(data_json.__dict__)

os.remove(xml_file)
os.remove(json_file)