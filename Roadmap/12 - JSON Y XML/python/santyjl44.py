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

import json
import os
import xml.etree.ElementTree as ET

archivo_json = "santyjl.json"
archivo_xml = "santyjl.xml"

#json
with open(archivo_json , "w" ) as archivo :
    datos = {
        "nombre" :"Santiago" ,
        "edad" :14 ,
        "fecha_de_nacimiento" :"20/01/2010" ,
        "lenguajes_de_programacion" : ["python" , "arduino"]
        }

    json.dump(datos , archivo) #escribe archivos python y lo combierte a json

#xml
raiz = ET.Element("Datos-Personales")

nombre = ET.SubElement(raiz , "nombre")
edad = ET.SubElement(raiz , "edad")
fecha_de_nacimiento = ET.SubElement(raiz , "fecha-de-nacimiento")
lenguajes_de_programacion = ET.SubElement(raiz , "lenguajes")

nombre.text = "santiago"
edad.text = "14"
fecha_de_nacimiento.text = "20/01/2010"
lenguajes_de_programacion.text = "python & arduino"

#creando archivo xml
xml = ET.ElementTree(raiz)
xml.write(archivo_xml , encoding="UTF-8" , xml_declaration=True)

#clase para leer archivos xml y json
class ManejadorArchivos:
    def __init__(self, archivo_json, archivo_xml):
        self.archivo_json = archivo_json
        self.archivo_xml = archivo_xml

    def leer_json(self):
        with open(self.archivo_json, "r") as archivo:
            return json.load(archivo)

    def leer_xml(self):
        parseo = ET.parse(self.archivo_xml)
        raiz = parseo.getroot()
        datos = {}

        for dato in raiz:
            datos[dato.tag] = dato.text
        return datos

    def eliminar_archivo_json(self):
        os.remove(self.archivo_json)

    def eliminar_archivo_xml(self):
        os.remove(self.archivo_xml)


# Crear instancia de la clase
manejador = ManejadorArchivos(archivo_json="santyjl.json", archivo_xml="santyjl.xml")
datos_json = manejador.leer_json()
datos_xml = manejador.leer_xml()
print(datos_json)
print(datos_xml)

# Eliminar archivo JSON
manejador.eliminar_archivo_json()
manejador.eliminar_archivo_xml()