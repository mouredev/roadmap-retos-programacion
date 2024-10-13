"""
*JSON y XML
"""
import json
from xml.dom.minidom import Element
import xml.etree.ElementTree as xml
from os import remove

#!Json
#?persona es un objeto de python (diccionario)
persona = {
    "nombre" : "sorubadguy",
    "edad" : "30",
    "f_nac" : "27/03/94",
    "leng_progra" : "python"
}

#?convierto a persona en un JSON
def crear_json(persona):
    with open("archivo.json", "w") as j:
        json.dump(persona, j)

    #?leer y mostrar el archivo.json
    with open("archivo.json", "r") as j:
        #?Leo el archivo Json
        objson = json.load(j)

    print(objson)
    print(type(objson))

    remove("archivo.json")

#!XML

def crear_xml(persona):
    pers = xml.Element("informacion")
    nombre = xml.SubElement(pers, "nombre").text = persona["nombre"]
    edad = xml.SubElement(pers, "edad").text = persona["edad"]
    nacimiento = xml.SubElement(pers, "fecha_nacimiento").text = persona["f_nac"]
    progra = xml.SubElement(pers, "Lenguaje_programacion").text = persona["leng_progra"]
    
    xml.dump(pers)
    datos = xml.ElementTree(pers)
    datos.write("persona.xml")
    
crear_xml(persona)

with open("persona.xml", "r") as datos_xml:
    print(datos_xml.read())
remove("persona.xml")
