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
import re
import xml.etree.ElementTree as ET
from xml.dom import minidom
import json
from os import remove

def get_data():
    name_pattern = r"^[a-zA-ZÁ-Úá-ú]+(?:[\ |-]*[a-zA-ZÁ-Úá-ú]*)*$"
    date_pattern = r"^(?:[0-2][0-9]|3[0-1])\/(?:0[1-9]|1[0-2])\/(?:19[0-9]{2}|200[0-6])$"
    age_pattern = r"^(?:[2-9][0-9]|1[8-9])$"
    languages_pattern = r"^[a-zA-Z]+(?:[\ ]*,[\ ]*[a-zA-Z]+)*$"
    name = input("Dime el nombre: ")
    while True:
        match_name = re.match(name_pattern,name)
        if match_name != None:
            break
        else:
            name = input("Ups... parece que tu nombre no tiene un formato válido. Prueba de nuevo: ")

    age = input("Ahora dime la edad(se admitirán edades desde los 18 hasta los 99 años): ")
    while True:
        try:
            int(age)
        except:
            age = input("Por favor introduce un número dentro del rango 18-99: ")
        else:
            match_age = re.match(age_pattern,age)
            if match_age != None:
                break
            else:
                age = input("La edad no está en el rango de 18-99 años. Prueba de nuevo: ")
    date = input("A continuación dime la fecha de nacimiento (usa el formato DD/MM/AAAA): ")
    while True:
        match_date = re.match(date_pattern,date)
        if match_date != None:
            break
        else:
            date = input("Vaya, parece que la fecha no tiene un formato correcto. Prueba de nuevo: ")

    languages = input("Y por último dime qué lenguajes de programación son tus favoritos (escríbelos separados por coma): ")
    while True:
        match_languages = re.match(languages_pattern,languages)
        if match_languages != None:
            break
        else:
            languages = input ("Ups... revisa como has introducido la información. Debes separar cada lenguaje con una coma. Prueba de nuevo: ")
    languages = languages.replace(" ","")
    return name,age,date,languages

def format_xml(element):
    unformatted_string = ET.tostring(element,'utf-8',method='xml').decode('utf-8')
    reparsed = minidom.parseString(unformatted_string)
    return reparsed.toprettyxml(indent="  ")

def generate_archives():
    name,age,date,languages = get_data()
    birth_date = date.split("/")

#GENERACIÓN DEL XML
    person = ET.Element("person")
    ET.SubElement(person,"name").text = name
    ET.SubElement (person,"age").text = age
    ET.SubElement(person, "birth_date").text = date
    languages_array = languages.split(",")
    xml_languages = ET.SubElement(person,"languages")
    for element in languages_array:
        ET.SubElement(xml_languages,"language").text = element
    ET.indent(person)
    et = ET.ElementTree(person)
    et.write("data.xml",xml_declaration=True)

#GENERACIÓN DEL JSON
    person_dict = dict()
    person_dict["name"] = name
    person_dict["age"] = age
    person_dict["birth_date"] = date
    person_dict["languages"] = languages.split(",")
    with open("data.json","w+") as json_file:
        json.dump(person_dict,json_file,indent=2)
    json_file.close()

#LECTURA DEL XML
#para presentar datos por terminal tal y como aparecen en el fichero
    with open("data.xml","r+") as xml_file:
        xml_lines = xml_file.readlines()
    print("\n")
    xml_file.close()
    for line in xml_lines:
        print (line)
    print("\n")
#lectura y almacenamiento del XML - uso también un diccionario para poder retornar los valores de una manera eficiente
    xml_dict = dict()
    root = ET.parse("data.xml")
    root_node = root.getroot()
    for child in root_node:
        if child.tag == "name":
            xml_dict["name"] = child.text
        elif child.tag == "age":
            xml_dict["age"] = child.text
        elif child.tag == "birth_date":
            xml_dict["birth_date"] = child.text
        elif child.tag == "languages":
            xml_dict["languages"] = list()
            for sub_child in child:
                xml_dict["languages"].append(sub_child.text)

    

#LECTURA DEL JSON
    new_person_dict = dict()
    new_person_dict = json.load(open("data.json"))
    print(new_person_dict)
    json_file.close()

    return new_person_dict, xml_dict

    #remove("data.xml")
    #remove("data.json")

#generate_archives()

"""
* DIFICULTAD EXTRA (opcional):
 * Utilizando la lógica de creación de los archivos anteriores, crea un
 * programa capaz de leer y transformar en una misma clase custom de tu 
 * lenguaje los datos almacenados en el XML y el JSON.
 * Borra los archivos.
"""
#declarar una clase persona y dos persona_json y persona_xml que heredan

class Person():
    def __init__(self,name,age,date,languages) -> None:
        self.name = name
        self.age = age
        self.date = date
        self.languages = languages

class XML_Person(Person):
    pass

class JSON_Person(Person):
    pass
json_person_dict = dict()
xml_person_dict = dict()
json_person_dict, xml_person_dict = generate_archives()

#Creo JSON_Person con los datos del JSON
json_person = JSON_Person(json_person_dict["name"],json_person_dict["age"],json_person_dict["birth_date"],json_person_dict["languages"])
#Creo XML_Person con los datos del XML guardados en un diccionario previamente
xml_person = XML_Person(xml_person_dict["name"],xml_person_dict["age"],xml_person_dict["birth_date"],xml_person_dict["languages"])

print(json_person.date)
print(xml_person.languages)

remove("data.xml")
remove("data.json")
