# EJERCICIO:
# Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los
# siguientes datos (haciendo uso de la sintaxis correcta en cada caso):
# - Nombre
# - Edad
# - Fecha de nacimiento
# - Listado de lenguajes de programación
# Muestra el contenido de los archivos.
# Borra los archivos.

import os
import json
import xml.etree.ElementTree as et

def create_info() -> dict:
    name = input("Intriduzca su nombre: \n").capitalize()
    age = int(input("Introduzca su edad : \n"))
    birth_date = input("Introduzca su fecha de nacimiento (dd/mm/aaaa): \n")
    programing_languages = input("Introduzca sus lenguajes de programación (separados por comas): \n").split(", ")
    personal_info = {
        "nombre": name,
        "edad": age,
        "fecha_de_nacimiento": birth_date,
        "lenguajes_de_programacion": programing_languages,
        }
    return personal_info

def create_json_file_and_remove(data: dict):
    with open("mhayhem.json", "w") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    with open("mhayhem.json", "r", encoding="utf-8") as f:
        print(f.read())
        print()
    
    #os.remove("mhayhem.json")

def create_xml_file_and_remove(data: dict):
    root = et.Element("mhayhem")
    
    for key, value in data.items():
        if isinstance(value, list):
            child = et.SubElement(root, key)
            for item in value:
                et.SubElement(child, "item").text = item
        else:
            child = et.SubElement(root, key).text = str(value)
    
    tree = et.ElementTree(root)
    tree.write("mhayhem.xml", encoding="utf-8", xml_declaration=True)
    
        
    #os.remove("mhayhem.xml")
 
create_xml_file_and_remove(create_info())

#os.remove("mhayhem.xml")


# DIFICULTAD EXTRA (opcional):
# Utilizando la lógica de creación de los archivos anteriores, crea un
# programa capaz de leer y transformar en una misma clase custom de tu 
# lenguaje los datos almacenados en el XML y el JSON.
# Borra los archivos.
class DeveloperInfo:
    def __init__(self, name: str, age: int, birth_date : str, languages: list):
        self.name = name
        self.age = age
        self.birth_date = birth_date
        self.languages = languages
    
    def __repr__(self) -> str:
        return f"DeveloperInfo(name={self.name}, age={self.age}, birth_date ={self.birth_date}, lanfuages={self.languages})"
    

def json_to_class(json_file: str):
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)
        return DeveloperInfo(data["nombre"], data["edad"], data["fecha_de_nacimiento"], data["lenguajes_de_programacion"])

def xml_to_class(xml_file: str):
    tree = et.parse(xml_file)
    root = tree.getroot()
    return DeveloperInfo(
        root.find("nombre").text,
        int(root.find("edad").text),
        root.find("fecha_de_nacimiento").text,
        [item.text for item in root.find("lenguajes_de_programacion").findall("item")]
    )

