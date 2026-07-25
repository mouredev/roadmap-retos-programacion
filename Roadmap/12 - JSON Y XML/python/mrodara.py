#############################  JSON Y XML CON PYTHON  ######################################


### TEORÍA MANEJO DE FICHEROS JSON CON PYTHON
'''
JSON (JavaScript Object Notation) es un formato de intercambio de datos muy utilizado por su sencillez y legibilidad. 
Python ofrece el módulo estándar json para trabajar con este formato.
'''
#import json
#
## Creación de un fichero json con datos
#data = {
#    "name" : "manu",
#    "age" : 44,
#    "teacher" : True,
#    "subjects" : ["PIA", "SRI", "IAW"],
#    "detail" : {
#        "high_school" : "IES Al-Andalus",
#        "year" : 2024
#    }
#}
#
#with open("data.json", "w", encoding="utf-8") as file:
#    json.dump(data, file, indent=4, ensure_ascii=False)
#    
#print("Archivo json generado con éxito")
#
## Leer un fichero json
#with open("data.json", "r", encoding="utf-8") as file:
#    content = json.load(file)
#
#print(type(content))
#print(content)
#
## Añadir una nueva clave al diccionario a partir del contenido descargado
#content["detail"]["experience"] = 7
#
#with open("data.json", "w", encoding="utf-8") as file:
#    json.dump(content, file, indent=4, ensure_ascii=False)
#
#print("Fichero actualizado desde el volcado")
#
#### FIN TEORÍA MANEJO DE FICHEROS JSON CON PYTHON
#
#### TEORÍA MANEJO DE FICHEROS XML CON PYTHON
#'''
#XML (eXtensible Markup Language) es un formato estructurado y extensible usado principalmente para datos jerárquicos. 
#Python ofrece el módulo xml.etree.ElementTree para trabajar con este formato.
#'''
#
### Crear un archivo xml con python
#import xml.etree.ElementTree as ET
#
## Crear el elemento raíz
#raiz = ET.Element("curso")
#
## Añadir subelementos
#ET.SubElement(raiz, "nombre").text = "Servicios de Red e Internet"
#ET.SubElement(raiz, "profesor").text = "Manuel Jesús Rodríguez Arabi"
#ET.SubElement(raiz, "año").text = "2024"
#
## Añadir un subelemento con atributos
#materias = ET.SubElement(raiz, "materias")
#materias.set("tipo", "obligatorias")
#ET.SubElement(materias, "materia").text = "Python"
#ET.SubElement(materias, "materia").text = "IA"
#
## Crear un árbol y guardar el archivo
#arbol = ET.ElementTree(raiz)
#arbol.write("datos.xml", encoding="utf-8", xml_declaration=True)
#
#print("Archivo XML creado con éxito.")
#
## Leer un archivo XML
#arbol = ET.parse("datos.xml")
#raiz = arbol.getroot()
#
## Recorrer los elementos
#print("Contenido del archivo XML:")
#for elem in raiz:
#    print(f"{elem.tag}: {elem.text}")
#
## Añadir un nuevo subelemento
#nuevo_campo = ET.SubElement(raiz, "duración")
#nuevo_campo.text = "100 horas"
#
## Guardar los cambios
#arbol.write("datos_actualizados.xml", encoding="utf-8", xml_declaration=True)
#
#print("Archivo XML actualizado.")

### FIN TEORÍA MANEJO DE FICHEROS XML CON PYTHON

## EJERCICIO PROPUESTO
import json
import os
from os.path import exists

if exists("user_data.json"):
    os.remove("user_data.json")
if exists("user_data.xml"):
    os.remove("user_data.xml")

user_data = {
    "name" : "Manuel J. Rodríguez",
    "age" : 44,
    "birthday" : "03/01/1980",
    "programming-lamgs" : ["Python", "PHP", "C++", "Java"]
}

with open("user_data.json", "w", encoding="utf-8") as file:
    json.dump(user_data, file, indent=4, ensure_ascii=False)

print(f"Fichero {file.name} creado con éxito!!!")

print()

print("Mostrando datos almacenados")

with open("user_data.json", "r", encoding="utf-8") as file:
    content = json.load(file)

print(type(content))

print("Fin del contenido del fichero JSON")

print()

print("Inicio de borrado del fichero JSON")
#os.remove("user_data.json")
print("Fichero eliminado con éxito!!!")

import xml.etree.ElementTree as ET

root = ET.Element("user_data")

ET.SubElement(root, "name").text = "Manuel J. Rodríguez"
ET.SubElement(root, "age").text = "44"
ET.SubElement(root, "birthdate").text = "03/01/1980"

languages = ET.SubElement(root, "languages")
lang1 = ET.SubElement(languages, "language")
lang1.text = "Python"
lang2 = ET.SubElement(languages, "language")
lang2.text = "PHP"
lang3 = ET.SubElement(languages, "language")
lang3.text = "Java"
lang4 = ET.SubElement(languages, "language")
lang4.text = "C++"


tree = ET.ElementTree(root)
tree.write("user_data.xml", encoding="utf-8", xml_declaration=True)

print("Archivo XML creado con éxito.")
print()
print("Lectura del fichero")
read_tree = ET.parse("user_data.xml")
read_root = read_tree.getroot()

for data in read_root:
    if data.tag != "languages":
        print(f"Etiqueta: {data.tag}, texto: {data.text}")
    else:
        for lang in data:
            print(f"Etiqueta: {lang.tag}, texto: {lang.text}")

print("Fin de lectura del fichero")
print()
print("Borrado del fichero")
#os.remove("user_data.xml")
print("Fichero eliminado con éxito!!!")

#############################  EJERCICIO EXTRA  ######################################

# Usaremos los ejemplos creados en el anterior ejercicio.

json_to_dict = {}
xml_to_dict = {}
users = []

with open ('user_data.json', "r", encoding="utf-8") as file:
    json_to_dict = json.load(file) # Devuelve un diccionario

my_tree = ET.parse("user_data.xml")
my_root = my_tree.getroot()
#xml_to_dict = {data.tag : data.text for data in my_root} #Generamos el diccionario
i = 1
for data in my_tree.getroot():
    if data.tag != "languages":
        xml_to_dict[data.tag] = data.text
    else:
        for lang in data:
            xml_to_dict[lang.tag + str(i)] = lang.text
            i += 1

print(json_to_dict)
print()
print(xml_to_dict)
users.append(json_to_dict)
users.append(xml_to_dict)
print(users)
os.remove("user_data.json")
os.remove("user_data.xml")
    

#############################  FIN EJERCICIO EXTRA  ######################################








############################# FIN JSON Y XML CON PYTHON  ######################################