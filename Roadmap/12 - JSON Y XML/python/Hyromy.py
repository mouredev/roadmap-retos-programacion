import os
import xml.etree.ElementTree as ET
import json

# ---- xml ----
root = ET.Element("root") # Crear el nodo raíz

nombre = ET.SubElement(root, "nombre") # Crear un nodo hijo
nombre.text = "Hyromy" # Asignar un valor al nodo hijo

edad = ET.SubElement(root, "edad")
edad.text = "20"

fecha_nacimiento = ET.SubElement(root, "fecha_nacimiento")
fecha_nacimiento.text = "2004-12-04"

lenguajes = ET.SubElement(root, "lenguajes")
lenguajes_list = ["Java", "PHP", "C#", "Python", "JavaScript"]
for lenguaje in lenguajes_list:
    lenguaje_node = ET.SubElement(lenguajes, "item")
    lenguaje_node.text = lenguaje

xml_file_name = __file__[:-3] + ".xml"
tree = ET.ElementTree(root)
tree.write(xml_file_name, encoding = "utf-8", xml_declaration = True)
del tree
del root

tree = ET.parse(xml_file_name)
root = tree.getroot()

def read_xml(root : ET.Element, ident = 0):
    for child in root:
        if not len(child):
            print(f"{'\t' * ident}<{child.tag}>{child.text}</{child.tag}>")
        else:
                print(f"{'\t' * ident}<{child.tag}>")
                read_xml(child, ident + 1)
                print(f"{'\t' * ident}</{child.tag}>")

read_xml(root)
os.remove(xml_file_name)

print("\n\n")

# ---- json ----
json_data = {
    "nombre": "Hyromy",
    "edad": 20,
    "fecha_nacimiento": "2004-12-04",
    "lenguajes": [
        "Java",
        "PHP",
        "C#",
        "Python",
        "JavaScript"
    ],
}

json_file_name = __file__[:-3] + ".json"

with open(json_file_name, "w", encoding = "utf-8") as f:
    json.dump(json_data, f, indent = 4)
del json_data

with open(json_file_name, "r", encoding = "utf-8") as f:
    json_data = json.load(f)
print(json_data)

os.remove(json_file_name)