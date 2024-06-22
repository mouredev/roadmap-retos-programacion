import os
import xml.etree.ElementTree as xml
import json

data = {
    "name": "Brais Moure",
    "age": 36,
    "birth_date": "29-04-1987",
    "programming_languages": ["Python", "Kotlin", "Swift"]
}

xml_file="gringoam.xml"


#XML

def create_xml():
    root=xml.Element("data")
    for llave, valor in data.items():
        hijo=xml.SubElement(root, llave)
        if isinstance(valor, list):
            for item in valor:
                  xml.SubElement(hijo, "item").text=item

        else:
            hijo.text= str(valor)

    tree=xml.ElementTree(root)
    tree.write(xml_file)
    

create_xml()
with open(xml_file, "r") as file:
    print(file.read())
os.remove(xml_file)

#JSON
json_file="gringoam.json"
def create_jason():
    with open(json_file, "w")as file:
        json.dump(data, file)

create_jason()

with open(json_file, "r") as file:
    print(file.read())


os.remove(json_file)

"""
Extra
"""
create_xml()
create_jason()
class Data:

    def __init__(self, name, age, birth_date, programming_language ) -> None:
        self.name= name
        self.age= age 
        self.birth_date= birth_date
        self.programming_language= programming_language

with open(xml_file, "r") as xml_data:
        root= xml.fromstring(xml_data.read())

        name= root.find("name").text    
        age= root.find("age").text
        birth_date= root.find("birth_date").text
        programming_language= []

        for item in root.find("programming_languages"):
           programming_language.append(item.text)
    
        xml_calss= Data(name, age, birth_date, programming_language)
        print(xml_calss.__dict__)


with open(json_file, "r") as json_data:
    dicc=json.load(json_data)
    json_class= Data(
        dicc["name"],
        dicc["age"],
        dicc["birth_date"],
        dicc["programming_languages"]
    )

    print(json_class.__dict__)

    os.remove(json_file)
    os.remove(xml_file)

    