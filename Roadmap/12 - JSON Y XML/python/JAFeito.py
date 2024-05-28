"""
 IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.

 EJERCICIO:
 Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los
 siguientes datos (haciendo uso de la sintaxis correcta en cada caso):
 - Nombre
 - Edad
 - Fecha de nacimiento
 - Listado de lenguajes de programación
 Muestra el contenido de los archivos.
 Borra los archivos.

 DIFICULTAD EXTRA (opcional):
 Utilizando la lógica de creación de los archivos anteriores, crea un
 programa capaz de leer y transformar en una misma clase custom de tu 
 lenguaje los datos almacenados en el XML y el JSON.
 Borra los archivos.
"""
import os
import xml.etree.ElementTree as xml
import json
# XML
datos = {
    "nombre":"Jose",
    "edad":45,
    "nacido":"01/03/79", 
    "aficiones":["videojuego", "anime", "programar"]
    }

def crear_xml():
    root = xml.Element("datos")
    for key, value in datos.items():
        child = xml.SubElement(root, key)
        if isinstance(value,list):
            for item in value:
               xml.SubElement(child, "item").text = item
        else:
            child.text = str(value)
    tree = xml.ElementTree(root)
    tree.write ("JAFeito.xml")
crear_xml()
with open("JAFeito.xml", "r") as archivo:
    print(archivo.read())
os.remove("JAFeito.xml")
#JSON
def crear_json():
    with open ("JAFeito.json", "w") as archivo:
        json.dump(datos, archivo)
crear_json()
with open ("JAFeito.json", "r") as archivo:    
    print(archivo.read())
os.remove("JAFeito.json")
#EXTRA
crear_xml()
crear_json()

class Datos:
    def __init__ (self, nombre, edad, fecha_nacimiento, aficiones) -> None:
        self.nombre = nombre
        self.edad = edad
        self.fecha_nacimiento = fecha_nacimiento
        self.aficiones = aficiones
        
#XML

with open("JAFeito.xml", "r") as archivo:
    root = xml.fromstring(archivo.read())
    nombre = root.find("nombre").text
    edad = root.find("edad").text
    fecha_nacimiento = root.find("nacido").text
    aficiones = []
    for item in root.find("aficiones"):
        aficiones.append(item.text)

datos_xml = Datos( nombre, edad, fecha_nacimiento, aficiones)
print(datos_xml.__dict__)
#JSON
with open("JAFeito.json", "r") as archivo:
    dic_json = json.load(archivo)
    nombre = dic_json["nombre"]
    edad = dic_json["edad"]
    fecha_nacimiento = dic_json["nacido"] 
    aciciones = dic_json["aficiones"]
    datos_json = Datos(nombre, edad, fecha_nacimiento, aficiones)   
print(datos_json.__dict__)
os.remove("JAFeito.xml")
os.remove("JAFeito.json")