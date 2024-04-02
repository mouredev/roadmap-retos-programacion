#12 JSON & XML
"""
 * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
 *
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los siguientes datos (haciendo uso de la sintaxis correcta en cada caso):
 * - Nombre
 * - Edad
 * - Fecha de nacimiento
 * - Listado de lenguajes de programación
 * Muestra el contenido de los archivos.
 * Borra los archivos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la lógica de creación de los archivos anteriores, crea un programa capaz de leer y transformar en una misma clase custom de tu 
 lenguaje los datos almacenados en el XML y el JSON.
 * Borra los archivos.
"""

import xml.etree.ElementTree as ET
import os

abspath = os.path.abspath(__file__) #get the file directory
dname = os.path.dirname(abspath)
os.chdir(dname) #change to file directory

#Create XML file
root = ET.Element("ContactsXML")
contact = ET.SubElement(root, "Contact")
name = ET.SubElement(contact, "Name")
name.text = "Saul"
age = ET.SubElement(contact, "Age")
age.text = "25"
birthdate = ET.SubElement(contact, "Birthdate")
birthdate.text = "02/12/2010"
coddingList = ET.SubElement(contact, "Coddinglist")
coddingList.text = "Pyhton, VBA, GOlang, JavaScript"

#Write to XML file
tree = ET.ElementTree(root)
tree.write("contacts.xml")

#Print XML as string
xml_string = ET.tostring(root)
print(xml_string)

#Remove file XML
os.remove("contacts.xml")


import json

filename = 'contacts.json'
isFile = os.path.isfile(filename)
 
emps = {"contactsJSON" :[{"Name": "Saul Saez", "Age": "22", "BirthDate":"02/12/2010", "Coddinglist":"Pyhton, VBA, GOlang, JavaScript"}, 
                     ]}

#Save JSON as file
with open(filename, 'w') as fp:
    json.dump(emps, fp, indent=4)

#Print JSON as string
print(emps)

#Delete JSON
os.remove("contacts.json")
