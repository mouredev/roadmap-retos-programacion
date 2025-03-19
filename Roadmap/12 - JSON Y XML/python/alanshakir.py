"""
/*
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
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la lógica de creación de los archivos anteriores, crea un
 * programa capaz de leer y transformar en una misma clase custom de tu 
 * lenguaje los datos almacenados en el XML y el JSON.
 * Borra los archivos.
 */
"""
import xml.etree.ElementTree as ET
import json
import os


my_file_xml = "alanshakir.xml"
root = ET.Element("person_xml")
name = ET.SubElement(root, "name")
name.text = "Alan Ramirez"

age = ET.SubElement(root, "age")
age.text= "39"

birthdate = ET.SubElement(root, "birthdate")
birthdate.text = "1985-01-20"

languages =ET.SubElement(root, "languages")
languages_1 = ET.SubElement(languages, "Language")
languages_1.text = "Python"
languages_2 = ET.SubElement(languages, "Language")
languages_2.text = "Java"
languages_3 = ET.SubElement(languages, "Language")
languages_3.text = "SQL"

tree = ET.ElementTree(root)
tree.write(my_file_xml, "utf-8", True)

with open(my_file_xml, "r") as xml_data:
    print(xml_data.read())

#os.remove(my_file_xml)

person_json = {"name":"Alan Ramirez",
               "age":"39",
               "birthdate": "1985-01-20",
               "language":["Python", "Java", "SQL"]}

with open("alanshakir.json", "w+") as my_file_json:
    json.dump(person_json, my_file_json, indent=2)

with open("alanshakir.json", "r") as file:
    print(file.read())

#os.remove("alanshakir.json")


#Extra


class Custom:
    def __init__(self, name, age, birthdate, languages):
        self.name = name
        self.age = age
        self.birthdate = birthdate
        self.languages = languages

with open("alanshakir.xml", "r") as my_file_xml:
        root = ET.fromstring(my_file_xml.read())
        name = root.find("name").text
        age = root.find("age").text
        birthdate = root.find("birthdate").text
        languages = []
        for element in root.find("languages"):
            languages.append(element.text)
        
        xml_class = Custom(name, age, birthdate, languages)
        print(xml_class.__dict__)

with open("alanshakir.json", "r") as my_file_json:
     json_dict = json.load(my_file_json)
     json_class = Custom(
          json_dict["name"],
          json_dict["age"],
          json_dict["birthdate"],
          json_dict["language"]
     )
     print(json_class.__dict__)

os.remove("alanshakir.xml")
os.remove("alanshakir.json")
