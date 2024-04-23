"""
* IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
* 
* EJERCICIO:
* Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los
* siguientes datos (haciendo uso de la sintaxis correcta en cada caso):
* - Nombre
* - Edad
* - Fecha de nacimiento
* - Listado de lenguajes de programación
* Muestra el contenido de los archivos.
* Borra los archivos.
"""
import json
import os
import time
import xml.etree.ElementTree as xml

xml_file = "Nightblockchain30.xml"
json_file = "Nightblockchain30.json"


# <<<< XML >>>>
datos = {
    "Nombre": "Alonso",
    "Edad": "26",
    "Fecha_nacimiento": "10/05/1997",
    "Listado_de_lenguajes": ["Python", "JavaScript", "CSS"]
}

# SAVE DATA
def create_xml():
    root = xml.Element("Parent_Node")

    #print(type(root))  # -> class 'xml.etree.ElementTree.Element'

    for key,value in datos.items():
        child = xml.SubElement(root, key)
        if isinstance(value,list):
            for item in value:
                xml.SubElement(child,"item").text = item
        else:
            child.text = str(value)

    tree = xml.ElementTree(root)
    #print(type(tree)) # <class 'xml.etree.ElementTree.ElementTree'>
    tree.write(xml_file)


create_xml()


#READ DATA
with open(xml_file, "r") as file:
    print(file.read())

#time.sleep(2)

# Borramos el archivo XML
if os.path.exists(xml_file):
    os.remove(xml_file)
else:
    print("El arhivo XML no existe")


# <<<< JSON >>>>

json_data = {
    "Nombre": "Alonso",
    "Edad": "26",
    "Fecha_nacimiento": "10/05/1997",
    "Listado_de_lenguajes": ["Python", "JavaScript", "CSS"]
}


# Guardamos los datos usando DUMP
def create_json():
    with open(json_file,"w") as file:
        json.dump(json_data,file,indent=4)

create_json()


# Mostramos el contenido usando LOAD
with open(json_file,"r") as file:
    contenido = json.load(file) # type(contenido) -> LIST
    for clave , valor in contenido.items():
        print(f"Clave:{clave} - Valor:{valor}")


#time.sleep(2) # compruebo como se crea y se borra el documento

# Borramos el archivo JSON
if os.path.exists(json_file):
    os.remove(json_file)
else:
    print("El arhivo JSON no existe")


print("<<<< EXTRA >>>>")

'''
* DIFICULTAD EXTRA (opcional):
* Utilizando la lógica de creación de los archivos anteriores, crea un
* programa capaz de leer y transformar en una misma clase custom de tu 
* lenguaje los datos almacenados en el XML y el JSON.
* Borra los archivos.
'''
create_xml()
create_json()


class Data():

    def __init__(self, Nombre, Edad, Fecha_nacimiento, Listado_de_lenguajes) -> None:
        self.Nombre = Nombre
        self.Edad = Edad
        self.Fecha_nacimiento = Fecha_nacimiento
        self.Listado_de_lenguajes = Listado_de_lenguajes

with open(json_file, "r") as json_data:
    string_data = json.load(json_data)
    custom_class_json = Data(string_data["Nombre"],string_data["Edad"],string_data["Fecha_nacimiento"],string_data["Listado_de_lenguajes"])

    print(custom_class_json.__dict__)


with open(xml_file, "r") as xml_data:

    root = xml.fromstring(xml_data.read())
    
    Nombre = root.find("Nombre").text
    Edad = root.find("Edad").text
    Fecha_nacimiento = root.find("Fecha_nacimiento").text

    Listado_de_lenguajes = []
    for item in root.find("Listado_de_lenguajes"):
        Listado_de_lenguajes.append(item.text)

    custom_class_xml = Data(Nombre,Edad,Fecha_nacimiento,Listado_de_lenguajes)
    print(custom_class_xml.__dict__)


