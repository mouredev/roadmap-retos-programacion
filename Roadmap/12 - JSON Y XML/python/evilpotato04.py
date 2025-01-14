#/*
# * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
# * 
# * EJERCICIO:
# * Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los
# * siguientes datos (haciendo uso de la sintaxis correcta en cada caso):
# * - Nombre
# * - Edad
# * - Fecha de nacimiento
# * - Listado de lenguajes de programación
# * Muestra el contenido de los archivos.
# * Borra los archivos.

import json
import os
import xml.etree.ElementTree as ET

def crear_archivo(extension: str):
    if extension == "json":
        with open(f"archivo.json", "w") as arc:
            contenido = {
                "Nombre": "Samy",
                "Edad": "19",
                "FechaNacimiento": "10/04/2004",
                "Lenguajes": ["Python", "C#", "Javascript", "Java", "PHP"]
            }
            json.dump(contenido, arc)
    elif extension == "xml":
        contenido = ET.Element("contenido")
        ET.SubElement(contenido, "Nombre").text = "Samy"
        ET.SubElement(contenido, "Edad").text = "19"
        ET.SubElement(contenido, "FechaNacimiento").text = "10/04/2004"
        ET.SubElement(contenido, "Lenguajes").text = "Python, C#, Javascript, Java, PHP"

        xml = ET.ElementTree(contenido)
        xml.write("archivo.xml" , encoding="UTF-8" , xml_declaration=True)
    else:
        print("Extención no válida")

crear_archivo("json")
crear_archivo("xml")
crear_archivo("samy")

with open("archivo.json", "r") as arc:
    print(arc.read())
with open("archivo.xml", "r") as arc:
    print(arc.read())

os.remove("archivo.json")
os.remove("archivo.xml")

# *
# * DIFICULTAD EXTRA (opcional):
# * Utilizando la lógica de creación de los archivos anteriores, crea un
# * programa capaz de leer y transformar en una misma clase custom de tu 
# * lenguaje los datos almacenados en el XML y el JSON.
# * Borra los archivos.
# */

class fabrica_de_archivos:
    def __init__(self, nombre_archivo: str, extension: str, datos: dict):
        self.nombre_archivo = nombre_archivo
        self.extension = extension
        self.datos = datos
        
    def crear_json(self):
        with open(f"{self.nombre_archivo}.json", "w") as arc:
            json.dump(self.datos, arc)
    
    def crear_xml(self):
        xml = ET.Element("datos")
        for llave, valor in self.datos.items():
            ET.SubElement(xml, llave).text = valor
        arc = ET.ElementTree(xml)
        arc.write(f"{self.nombre_archivo}.xml" , encoding="UTF-8" , xml_declaration=True)
    
    def crear_archivo(self):
        match self.extension:
            case "json":
                self.crear_json()
            case "xml":
                self.crear_xml()
            case _:
                print("Extención na válida")
    
    def leer_archivo(self):
        with open(f"{self.nombre_archivo}.{self.extension}", "r") as arc:
            print(arc.read())

    def borrar_archivo(self):
        os.remove(f"{self.nombre_archivo}.{self.extension}")

def programa():
    diccionario = {
        "Nombre": "Samy",
        "Edad": "19",
        "FechaNacimiento": "10/04/2004",
        "Lenguajes": "Python, C#, Javascript, Java, PHP"
    }

    fabrica_json = fabrica_de_archivos("evilpotato04", "json", diccionario)
    fabrica_json.crear_archivo()
    fabrica_json.leer_archivo()
    fabrica_json.borrar_archivo()

    fabrica_xml = fabrica_de_archivos("evilpotato04", "xml", diccionario)
    fabrica_xml.crear_archivo()
    fabrica_xml.leer_archivo()
    fabrica_xml.borrar_archivo()

programa()