"""/*
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
 */"""

import xml.etree.ElementTree as xml #libreria para los xml
import os #libreria del sistema
import json #libreria de json

data={
"name" : "angel",
"age" : "35",
"birth_date" : "16/11/1989",
"programming_languages" : ["Python","Javascrip", "Css"]
}

#xml

xml_file="angel_xml.xml"

def save_xml():
    
    root = xml.Element("data") #creamos el directorio raiz

    for key, value in data.items(): #recorremos los valores y los vamos añadiendo al xml
        child = xml.SubElement(root,key) #creamos un hijo por cada clave dependiente del root
        if isinstance(value, list): #si es una instancia creamos un sub valor
            for item in value:
                xml.SubElement(child,"item").text = item
        else:
            child.text = str(value)
    
    tree = xml.ElementTree(root) #creamos el arbol
    tree.write(xml_file) #escribimos el arbol

save_xml()

with open(xml_file) as xml_data:
    print("**Mostrando el archivo xml")
    print(xml_data.read())

#os.remove(xml_file) #descomentar para borrar el archivo al salir

#JSON

json_file="angel_json.json"

def save_json():
    with open(json_file, "w") as json_data: #abrimos el archivo con escitura
        json.dump(data, json_data) #añadimos los datos

save_json()

with open(json_file, "r") as json_data:
    print("**Mostrando el archivo json")
    print(json_data.read()) #leemos los datos

#os.remove(json_file) #descomentar para borrar el archivo al salir

#Extra

#**XML**
class Data:

    def __init__(self, name, age, birth_date, programming_languages) ->None: #creacion de clase
        self.name = name
        self.age = age
        self.birth_date = birth_date
        self.programming_languages = programming_languages
    
with open(xml_file, "r") as xml_data:
    
    root = xml.fromstring(xml_data.read())
    name = root.find("name").text
    age = root.find("age").text
    birth_date = root.find("birth_date").text
    programming_languages= []
    for item in root.find("programming_languages"):
        programming_languages.append(item.text)

    data_from_xml = Data(name, age, birth_date, programming_languages) 
    print("**Mostrando la clase desde el archivo xml")
    print(data_from_xml.__dict__)

#**json

with open(json_file, "r") as json_data:
    json_dict = json.load(json_data)
    json_data = Data(json_dict["name"], 
         json_dict["age"], 
         json_dict["birth_date"],
         json_dict["programming_languages"]
         )
    print("de json a clase")
    print(json_data.__dict__)

#os.remove(xml_file) #descomentar para borrar el archivo al salir