"""
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

from pathlib import Path
import xml.etree.ElementTree as XML
import json

xml_file = "ignaciovihe.xml"
json_file = "ignaciovihe.json"

programmer = {
    "name": "ignacio",
    "age": "40",
    "date_of_birth": "23/02/1985",
    "languages": ["python", "Javascript", "GO"]
}


def create_xml():

    #Creo la estructura XML
    root = XML.Element("programmer")# Creo el elemento raiz <programmer>

    #Crear los subelementos
    for key, value in programmer.items():
        child = XML.SubElement(root, key)
        if isinstance(value, list):
            for language in value:
                XML.SubElement(child, "language").text = language
        else:
            child.text = value

    tree = XML.ElementTree(root) # Convertimos la estructura en un árbol XML
    tree.write(xml_file, encoding="utf-8", xml_declaration=True) # Guardamos el XML en un archivo.

def print_xml():

    # Cargar el archivo XML
    tree = XML.parse(xml_file) # Abre y analiza el archivo XML
    root = tree.getroot()  # Obtiene el elemento raíz del XML (<programmer> en este caso)

    # Recorrer los elementos 'libro' y extraer información
    for child in root:
        if len(child) == 0:
            print(f"{child.tag}: {child.text}")
        else:
            languages = ""
            for language in child:
                languages += (language.text + ", ")
            print(f"{child.tag}: {languages.strip(", ")}")

def delete_file(file_name):

    file = Path(file_name)
    if file.exists():
        file.unlink()

create_xml()
print_xml()
delete_file(xml_file)


def create_json():
    with open(json_file, "w") as file:
        json.dump(programmer, file, indent=4) # Le paso un diccionario(programmer)

def print_json():
    with open(json_file,"r") as file:
        data = json.load(file) # me devulve un diccionario(data)

    for key, value in data.items():
        if isinstance(value, list):
            print(f"{key}: {" ".join(value)}")
        else:
            print(f"{key}: {value}")

create_json()
print_json()
delete_file(json_file)


"""
* DIFICULTAD EXTRA (opcional):
 * Utilizando la lógica de creación de los archivos anteriores, crea un
 * programa capaz de leer y transformar en una misma clase custom de tu 
 * lenguaje los datos almacenados en el XML y el JSON.
 * Borra los archivos.
"""

class Programmer:
    def __init__(self,):
        self.name = None
        self.age = None
        self.date = None
        self.languages = None

    def set_attribute(self, key:str, value):
        setattr(self, key, value)

    def print_data(self):
        print(f"Name: {self.name}\nAge: {self.age}\nDate of birth: {self.date}\nLanguajes:")
        for language in self.languages:
            print(f"\t{language}")

def read_xml():

    tree = XML.parse(xml_file)
    root = tree.getroot()

    my_programmer = Programmer()

    for child in root:
        if len(child) == 0:
            my_programmer.set_attribute(child.tag, child.text)
        else:
            languages = [language.text for language in child]
            my_programmer.set_attribute(child.tag, languages)
    return my_programmer


def read_json():
    with open(json_file, "r") as file:
        data = json.load(file)

    my_programmer = Programmer()
    for key, value in data.items():
        my_programmer.set_attribute(key, value)
    
    return my_programmer

print("-------Lee XML-------")
create_xml()
my_programmer = read_xml()
my_programmer.print_data()
delete_file(xml_file)

print("-----Lee JSON-----")
create_json()
my_programmer = read_json()
my_programmer.print_data()
delete_file(json_file)