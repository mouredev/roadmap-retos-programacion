'''
* EJERCICIO:
* Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los
* siguientes datos (haciendo uso de la sintaxis correcta en cada caso):
* - Nombre
* - Edad
* - Fecha de nacimiento
* - Listado de lenguajes de programación
* Muestra el contenido de los archivos.
* Borra los archivos.
*
'''
import os
import xml.etree.ElementTree as ET
import json

info = {
    "name": "Ricardo",
    "age": 60,
    "languages": ["Python", "JavaScript", "Go"]
}

#XML. Dos funciones. Escribe y lee. Para ller hay que recurrir al nombre de la etiqueta
#del diccionario y recorrer todo el hijo de la etiqueta.


file_xml = "ricardo.xml"

root = ET.Element("info")          # <info> será el nodo principal


def dict_to_xml(parent,xml_file):
    for key, value in info.items():
        child = ET.SubElement(parent, key)
        if isinstance(value, list):
            for item in value:
                ET.SubElement(child, "item").text = item
        else:
            child.text = str(value)

    tree = ET.ElementTree(parent)
    tree.write(xml_file, encoding="utf-8", xml_declaration=True)


def mostrar_xml(xml_file):
    
    tree = ET.parse(xml_file)
    root = tree.getroot()

    for child in root:
        if child.tag == "languages":
            print(f"{child.tag} ->")
            for lang in child:
                print(f"- {lang.text}")
        else:
            print(f"{child.tag} -> {child.text}")

dict_to_xml(root, file_xml)
print(50*"=")               
mostrar_xml(file_xml)


#JSON. Una función para rellenar el fichero usando .dump y otra para leerlo 

file_js = "ricardo.json"

dict = info

def dict_to_json(file, dict):
    with open (file, "w") as js:
        json.dump(dict, js, indent=1)

def mostrar_json(file):
    with open (file, "r") as js:
        print(js.read())

dict_to_json(file_js, dict)
print(50*"=")
mostrar_json(file_js)

'''
* DIFICULTAD EXTRA (opcional):
* Utilizando la lógica de creación de los archivos anteriores, crea un
* programa capaz de leer y transformar en una misma clase custom de tu 
* lenguaje los datos almacenados en el XML y el JSON.
* Borra los archivos.
'''

class Info:
    def __init__(self, nombre , edad, lenguajes:list):
        self.nombre = nombre
        self.edad = edad
        self.lenguajes = lenguajes
        self.pintar = print(f"Mi nombre {nombre}, edad {edad} y lenguajes {', '.join(self.lenguajes)}")

with open (file_xml, "r") as file:
    root = ET.fromstring(file.read())
    nombre = root.find("name").text
    edad = int(root.find("age").text)
    lenguajes = [item.text for item in root.find("languages")] #languages es el nombre de la
    #variable en info que es el nodo principal
    xml_class = Info(nombre, edad, lenguajes)
    print(50*"-")
    xml_class.pintar

with open (file_js, "r") as file:
    json_dic = json.load(file)
    json_class = Info (
        json_dic["name"],
        json_dic["age"],
        json_dic["languages"]
    )
    print(50*"-")
    json_class.pintar

os.remove(file_xml)
os.remove(file_js)