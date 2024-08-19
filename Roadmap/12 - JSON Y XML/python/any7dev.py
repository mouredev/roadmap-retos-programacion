""" /*
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
 */ """

#EJERCICIO
import json
import xml.etree.ElementTree as ET
import os

#JSON
contenido = {
    "Nombre": "Ana",
    "Edad": 36,
    "Fecha Nacimiento": "11/03/1988",
    "Lenguajes": ["Cobol", "Python"]
}

with open ("archivo.json", 'w') as archivo:
    json.dump(contenido, archivo, indent=3)

with open ("archivo.json", 'r') as archivo:
    print(json.load(archivo))

os.remove("archivo.json")

#XML
archivo = "archivo.xml"

#Creamos el árbol con los datos
contenido = ET.Element("contenido")
datos = ET.SubElement(contenido, "datos")
ET.SubElement(datos, "Nombre").text = "Ana"
ET.SubElement(datos, "Edad").text = "36"
ET.SubElement(datos, "Fecha_Nacimiento").text = "11/03/1988"
ET.SubElement(datos, "Lenguajes").text = "Cobol, Python"

#Creamos el fichero
ET.indent(contenido)
et = ET.ElementTree(contenido)
et.write(archivo, xml_declaration=True, encoding="UTF-8")

with open (archivo, 'r') as a:
    print(a.read())

os.remove("archivo.xml")





