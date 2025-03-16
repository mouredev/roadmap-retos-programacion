import json
import os
import xml.etree.ElementTree as ET


#JSON file 
data = {

    "nombre":"raul",
    "edad": "32",
    "fecha_nacimiento": "11/09/1991",
    "lenguajes": ["Python","Javascript","Abap"]
}

#Parse dictionay to JSON
data_json = json.dumps(data)

path = os.path.join(os.path.dirname(__file__),"fichero.json")

with open(path,"w") as file:
    file.write(data_json)

data_file = ""
with open(path,"r") as file:
    data_file = file.read()

#Parse document into dictionay 
decoder_info = json.JSONDecoder().decode(s=data_file)

#Remove file
os.remove(path)


#XML 
path_xml = ""

path_xml = os.path.join(os.path.dirname(__file__),"fichero.xml")

#Create xml

root = ET.Element("data")
name = ET.SubElement(root,"name")
name.text = "Raul"
age = ET.SubElement(root,"age")
age.text = "33"
birthDate = ET.SubElement(root,"birth_date")
birthDate.text = "11/0971991"
languages = ET.SubElement(root,"languages")
item1 = ET.SubElement(languages,"item")
python = ET.SubElement(item1,"language")
python.text = "python"
item2 = ET.SubElement(languages,"item")
abap  = ET.SubElement(item2,"language")
abap.text = "abap"
item3 = ET.SubElement(languages,"item")
javascript = ET.SubElement(item3,"language")
javascript.text = "javascript"

#Build xml tree
tree = ET.ElementTree(root)
#Write xml tree to file
tree.write(path_xml,encoding="UTF-8")

#Read XML 

tree = ET.parse(source=path_xml)

root = tree.getroot()

#Iterate over elements
for element in root:
    print(f'{element.tag}: {element.text}')

os.remove(path_xml)

