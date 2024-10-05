import os
import xml.etree.ElementTree as xml
import json

os.system("clear")

data = {
    "nombre": "Marcos Robles",
    "edad": 42,
    "fecha_nacimiento": "20-02-1982",
    "lenguajes": ["Python", "Javascript", "PHP"]
}

xml_file = "Lumanet.xml"
json_file = "Lumanet.json"

# XML

def create_xml():

    root = xml.Element("data")

    for key, value in data.items():
        child = xml.SubElement(root, key)
        if isinstance(value, list):
            for item in value:
                xml.SubElement(child, "item").text = item
        else:
            child.text = str(value)

    tree = xml.ElementTree(root)
    tree.write(xml_file)

create_xml()

with open(xml_file, "r") as xml_data:
    print(xml_data.read())

os.remove(xml_file)

# JSON

def create_json():
    with open(json_file, "w") as json_data:
        json.dump(data, json_data)

create_json()

with open(json_file, "r") as json_data:
    print(json_data.read())

os.remove(json_file)

"""
DIFICULTAD EXTRA (opcional):
Utilizando la lógica de creación de los archivos anteriores, crea un
programa capaz de leer y transformar en una misma clase custom de tu 
lenguaje los datos almacenados en el XML y el JSON.
Borra los archivos.
"""

class Custom:
    def __init__(self, file) -> None:
        self.file = file

    def write_json(self, datas):
        with open(self.file, "w") as f:
            json.dump(datas, f, indent=4)

    def read_json(self):
        with open(self.file, "r") as f:
            load = json.load(f)
            print(load)

    def write_xml(self, datas):
        root = xml.Element("Informacion")
        information = xml.SubElement(root, "Datos")

        information.set("id", "1")
        nombre = xml.SubElement(information, "nombre")
        nombre.text = datas["nombre"]
        age = xml.SubElement(information, "edad")
        age.text = str(datas["edad"])
        birth_date = xml.SubElement(information, "fecha_nacimiento")
        birth_date.text = datas["fecha_nacimiento"]
        languages = xml.SubElement(information, "lenguajes")
        for lang in datas["lenguajes"]:
            xml.SubElement(languages, "lenguaje").text = lang

        tree = xml.ElementTree(root)
        tree.write(self.file)

    def read_xml(self):
      with open(self.file, "r") as xml_data:
        print(xml_data.read())

    def delete_file(self):
        os.remove(self.file)
        print("\nArchivos borrados exitosamente.")

# Ejemplo de uso
datos = {
    "nombre": "Marcos",
    "edad": 42,
    "fecha_nacimiento": "1982-02-20",
    "lenguajes": ["Python", "PHP", "Javascript"]
}

custom_instance = Custom("Lumanet.xml")
custom_instance.write_xml(datos)
custom_instance.read_xml()
#custom_instance.delete_file()

custom_instance = Custom("Lumanet.json")
custom_instance.write_json(datos)
custom_instance.read_json()
#custom_instance.delete_file()
