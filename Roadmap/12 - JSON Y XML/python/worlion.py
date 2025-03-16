import json
import os
import xml.etree.ElementTree as ET

"""
    EJERCICIO: XML y JSON
"""

developer = {
    "Nombre": "Imanol",
    "Edad" : 40,
    "Fecha_de_nacimiento" : "20/04/1984",
    "lenguajes" : ["Java", "Python", "Ada", "C#", "C/C++"]
}

xml_file = "developer.xml"
json_file = "developer.json"

def write_xml_file(dicionary: dict, file_path: str):
    root = ET.Element("root")
    
    for key, value in dicionary.items():
        print(f"k:{key} - v:{value}")
        child = ET.SubElement(root, key)
        if isinstance(value, list):
            for item in value:
                ET.SubElement(child, "item").text = item
        else:
            child.text = str(value)
            
    print(f"\nwriting XML file in {file_path}...")
    tree = ET.ElementTree(root)
    ET.indent(tree, space="\t", level=0)
    tree.write(file_path)

def read_xml_file(file_path:str) -> str:
    print(f"\nreading XML from {file_path}:")
    with open(file_path , "r") as xfile:
        return  xfile.read()

write_xml_file(developer, xml_file)
print(read_xml_file(xml_file))
os.remove(xml_file)

def write_json_file(dicionary: dict, file_path: str):
    print(f"\nwriting JOSN file in {file_path}...")
    with open(file_path, "w") as jfile:
        json.dump(dicionary, jfile, indent="\t")

def read_json_file(file_path: str) -> str:
    print(f"\nreading JOSN from {file_path}...")
    with open(file_path, "r") as jfile:
        return jfile.read()

write_json_file(developer, json_file)
print(read_json_file(json_file))
os.remove(json_file)

"""
* DIFICULTAD EXTRA (opcional):
"""

print("\n ---- 🌩 DIFICULTAD EXTRA 🌩 ----\n")

# Developer Class
class Developer:
    def __init__(self, name: str, age: int, birth_date: str, languajes: list) -> None:
        self.name = name
        self.age = age
        self.birth_date = birth_date
        self.languajes = languajes
    
    def __str__(self) -> str:
        str_self = "Developer:"
        str_self += f"\n\t-Name = {self.name}"
        str_self += f"\n\t-Age = {self.age}"
        str_self += f"\n\t-Birth_date = {self.birth_date}"
        str_self += f"\n\t-Languages = {self.languajes}"
        return str_self
        

def test_load_dev_from_xml():
    write_xml_file(developer, xml_file)
    tree = ET.parse(xml_file)
    root = tree.getroot()

    name = root.find("Nombre").text
    age = root.find("Edad").text
    birth_date = root.find("Fecha_de_nacimiento").text
    languajes = []
    for lang in root.find("lenguajes"):
        print(f"lang: {lang.text}")
        languajes.append(lang.text)

    my_developer_1 = Developer(name, age, birth_date, languajes)
    
    print(f"My developer from XML:\n{str(my_developer_1)}")
    print(f"num of languages: {len(my_developer_1.languajes)}")
    
    os.remove(xml_file)
    
test_load_dev_from_xml()
    
    

def test_load_dev_from_json():
    write_json_file(developer, json_file)
    
    with open(json_file, "r") as json_data:
        my_json = json.load(json_data)
        my_developer_2 = Developer(
            my_json["Nombre"],
            my_json["Edad"],
            my_json["Fecha_de_nacimiento"],
            my_json["lenguajes"])
    
    print(f"My developer from JSON:\n{str(my_developer_2)}")
    print(f"num of languages: {len(my_developer_2.languajes)}")
    
    os.remove(json_file)
    
test_load_dev_from_json()