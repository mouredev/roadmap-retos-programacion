### 12 - JSON y XML
import os
import xml.etree.ElementTree as xml
import json


file_name_1 = "./xml_file.xml"
file_name_2 = "./json_file.json"


def to_xml(name, age, date, languagues):

    x = ""
    for i in languagues:
        x += f'\n{" "*8}<languague>{i}</languague>'
    
    file = f'<?xml version="1.0" encoding="UTF-8"?>\n<data>\n{" "*4}<name>{name}</name>\n{" "*4}<age>{age}</age>\n{" "*4}<date>{date}</date>\n{" "*4}<languagues>{x}\n{" "*4}</languagues>\n</data>'
    with open(file_name_1,"w") as f:
        f.write(file)


def to_json(name, age, date, languagues):

    x = f'["{'","'.join(languagues)}"]'

    file = f'{{\n{" "*4}"name":"{name}",\n{" "*4}"age":"{age}",\n{" "*4}"date":"{date}",\n{" "*4}"languagues":{x}\n}}'
    
    with open(file_name_2,"w") as f:
        f.write(file)

def to_print(file_name):
    print()
    with open (file_name, "r") as f:
        
        x = f.readlines()

        for i in x:
            if not i.startswith("<?"):
                print (i,end="")


to_xml("Gordo","Master","08-05-1995",["C++","Python"])
to_json("Gordo","Master","08-05-1995",["C++","Python"])


to_print(file_name_1)
to_print(file_name_2)


os.remove(file_name_1)
os.remove(file_name_2)

#############################################################################################
#Forma numero 2#
#############################################################################################

file_name_3 = "./xml_file_v2.xml"
file_name_4 = "./json_file_v2.json"

data = {
        "name" : "Gordo",
        "age" : "29",
        "date" : "08-05-1995",
        "languagues" : ["C++","Python"]
    }

def to_xml_v2():
    
    root = xml.Element("data")

    for key, value in data.items():
        
        child = xml.SubElement(root,key)

        if isinstance(value, list):
            for item in value:
                xml.SubElement(child,"item").text = item
        
        else:
            child.text = str(value)
    
    tree = xml.ElementTree(root)
    tree.write(file_name_3)



def to_json_v2():

    file = json.dumps(data,indent=4)

    with open(file_name_4,"w") as f:
            f.write(file)

to_xml_v2()
to_json_v2()

to_print(file_name_3)
to_print(file_name_4)


### Ejercicio Extra ###

class Data():

    def __init__(self, name, age, date, languagues) -> None:
        self.name = name
        self.age = age
        self.date = date
        self.languagues = languagues


with open(file_name_3,"r") as xml_data:

    root = xml.fromstring(xml_data.read())
    name = root.find("name").text
    age = root.find("age").text
    date = root.find("date").text
    languagues = []
    for i in root.find("languagues"):
        languagues.append(i.text)

    xml_class = Data(name,age,date,languagues)
    print(xml_class.__dict__)

with open(file_name_4,"r") as json_data:

    json_dict = json.load(json_data)
    json_class = Data(
        json_dict["name"],
        json_dict["age"],
        json_dict["date"],
        json_dict["languagues"]
    )
    print(json_class.__dict__)

os.remove(file_name_3)
os.remove(file_name_4)
