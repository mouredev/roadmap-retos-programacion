import os
import xml.etree.ElementTree as xmll
import json



data = {
    "name" : "Rick Gonzales",
    "age" : 57,
    "birth_date" : "27-02-1969",
    "programming_languages" : ["Python", "Kotlin", "Swift"]
}

xml_file = "Lionheart7777.xml"
json_file = "Lionheart7777.json"
# XML

def create_xml ():
    
    root = xmll.Element("data")
    
    for key, value in data.items():
        child = xmll.SubElement(root, key)
        if isinstance(value, list):
            for item in value :
                xmll.SubElement(child, "item").text = item
        else:    
            child.text = str(value)
    
    arbol = xmll.ElementTree(root)
    xmll.indent(arbol, space="    ")   
    arbol.write(xml_file, encoding="utf-8", xml_declaration=True)
    
create_xml ()

# ABRIR ARCHIVO

with open (xml_file, encoding="utf-8") as xml_date :
    print(xml_date.read())

os.remove(xml_file)


# JSON

def create_json():
    with open(json_file, "w", encoding="utf-8") as json_datex :
        json.dump(data, json_datex, indent=4, ensure_ascii=False)
    
create_json()
    
with open(json_file, encoding="utf-8") as json_datex :
    print(json_datex.read())    

os.remove(json_file)

"""
EXTRA
"""
create_xml()
create_json()

class Data :
    
    def __init__(self, name, age, birth_date, programming_languages):
        self.name = name
        self.age = age
        self.birth_date = birth_date
        self.programming_languages = programming_languages
#JSON CLASS
with open(json_file, "r", encoding="utf-8") as json_data :
    json_dict = json.load(json_data)
    json_class = Data(
        json_dict["name"],
        json_dict["age"],
        json_dict["birth_date"],
        json_dict["programming_languages"])
    
    print(json_class.__dict__)
    
os.remove(xml_file)
os.remove(json_file)