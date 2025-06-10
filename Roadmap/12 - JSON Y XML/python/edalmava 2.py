import os
import json
import xml.etree.ElementTree as ET

# Datos
name = "Edwin Alberto Martinez Vanegas"
age = 30
birthdate = "1994-08-11"
languages = ["Python", "Pascal", "JavaScript"]

# Crear archivo XML
person = ET.Element("person")

name_element = ET.SubElement(person, "name")
name_element.text = name

age_element = ET.SubElement(person, "age")
age_element.text = str(age)

birthdate_element = ET.SubElement(person, "birthdate")
birthdate_element.text = birthdate

languages_element = ET.SubElement(person, "languages")
for lang in languages:
    language_element = ET.SubElement(languages_element, "language")
    language_element.text = lang

tree = ET.ElementTree(person)
tree.write("data.xml", encoding="utf-8", xml_declaration=True)

# Crear archivo JSON
data = {
    "name": name,
    "age": age,
    "birthdate": birthdate,
    "languages": languages
}

with open("data.json", "w", encoding="utf-8") as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

# Mostrar contenido de los archivos
print("Contenido del archivo XML:")
with open("data.xml", "r", encoding="utf-8") as xml_file:
    print(xml_file.read())

print("\nContenido del archivo JSON:")
with open("data.json", "r", encoding="utf-8") as json_file:
    print(json_file.read())

# Borrar los archivos
if os.path.exists("data.xml"):
    os.remove("data.xml")
    print("\nArchivo XML borrado con éxito.")
else:
    print("\nError al borrar el archivo XML.")

if os.path.exists("data.json"):
    os.remove("data.json")
    print("Archivo JSON borrado con éxito.")
else:
    print("Error al borrar el archivo JSON.")
