
import json
import os

datos = {"Nombre": "Sergio",
         "Edad": "46",
         "Fecha_Nacimiento": "04/10/1979",
         "Lenguaje": "Python"}

with open("./datos.json", "w", encoding="utf-8") as archivo:
    json.dump(datos, archivo, ensure_ascii=False, indent=4)

with open("./datos.json", "r", encoding="utf-8") as archivo:
    persona = json.load(archivo)
    print(persona)

#if os.path.exists("./datos.json"):
#    os.remove("./datos.json")


import xml.etree.ElementTree as xml

root = xml.Element("datos")
for llave, valor in datos.items():
    child = xml.SubElement(root, llave)
    child.text = valor
tree = xml.ElementTree(root)
tree.write("./datos.xml")

with open("./datos.xml", "r") as archivo_xml:
    print(archivo_xml.read())

#if os.path.exists("./datos.xml"):
#    os.remove("./datos.xml")


# DIFICULTAD EXTRA:

class Datos:
    def __init__(self, nombre, edad, fecha_nacimiento, lenguaje):
        self.nombre = nombre
        self.edad = edad
        self.fecha_nacimiento = fecha_nacimiento
        self.lenguaje = lenguaje

with open("./datos.json", "r", encoding="utf-8") as archivo_json:
    persona = json.load(archivo_json)
    clase_json = Datos(
        persona["Nombre"], 
        persona["Edad"], 
        persona["Fecha_Nacimiento"], 
        persona["Lenguaje"])
    print(clase_json.__dict__)

if os.path.exists("./datos.json"):
    os.remove("./datos.json")

with open("./datos.xml", "r") as archivo_xml:
    root = xml.fromstring(archivo_xml.read())
    nombre = root.find("Nombre").text
    edad = root.find("Edad").text
    fecha_nacimiento = root.find("Fecha_Nacimiento").text
    lenguaje = root.find("Lenguaje").text
    clase_xml = Datos(nombre, edad, fecha_nacimiento, lenguaje)
    print(clase_xml.__dict__)

if os.path.exists("./datos.xml"):
    os.remove("./datos.xml")


