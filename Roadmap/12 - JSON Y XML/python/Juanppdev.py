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

import json
import xml.etree.ElementTree as ET
import os

# Datos a guardar
datos = {
    "Nombre": "Juan Pablo",
    "Edad": 25,
    "Fecha de nacimiento": "1998-09-24",
    "Lenguajes de programación": ["Python", "Kotlin", "C++"]
}

# Crear archivo JSON
with open("datos.json", "w") as json_file:
    json.dump(datos, json_file, indent=4)

# Crear archivo XML
root = ET.Element("Persona")
ET.SubElement(root, "Nombre").text = datos["Nombre"]
ET.SubElement(root, "Edad").text = str(datos["Edad"])
ET.SubElement(root, "Fecha_de_nacimiento").text = datos["Fecha de nacimiento"]
lenguajes = ET.SubElement(root, "Lenguajes_de_programacion")
for lenguaje in datos["Lenguajes de programación"]:
    ET.SubElement(lenguajes, "Lenguaje").text = lenguaje

tree = ET.ElementTree(root)
with open("datos.xml", "wb") as xml_file:
    tree.write(xml_file)

# Mostrar contenido de los archivos
with open("datos.json", "r") as json_file:
    print("Contenido de datos.json:")
    print(json_file.read())

with open("datos.xml", "r") as xml_file:
    print("\nContenido de datos.xml:")
    print(xml_file.read())

# Borrar los archivos
# os.remove("datos.json")
# os.remove("datos.xml")


"""
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la lógica de creación de los archivos anteriores, crea un
 * programa capaz de leer y transformar en una misma clase custom de tu 
 * lenguaje los datos almacenados en el XML y el JSON.
 * Borra los archivos.
"""

import json
import xml.etree.ElementTree as ET
import os

class Persona:
    def __init__(self, nombre, edad, fecha_nacimiento, lenguajes):
        self.nombre = nombre
        self.edad = edad
        self.fecha_nacimiento = fecha_nacimiento
        self.lenguajes = lenguajes

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Fecha de nacimiento: {self.fecha_nacimiento}, Lenguajes de programación: {', '.join(self.lenguajes)}"

# Función para leer datos desde JSON
def leer_json(file_path):
    with open(file_path, "r") as json_file:
        datos = json.load(json_file)
    return Persona(datos["Nombre"], datos["Edad"], datos["Fecha de nacimiento"], datos["Lenguajes de programación"])

# Función para leer datos desde XML
def leer_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    nombre = root.find("Nombre").text
    edad = int(root.find("Edad").text)
    fecha_nacimiento = root.find("Fecha_de_nacimiento").text
    lenguajes = [lenguaje.text for lenguaje in root.find("Lenguajes_de_programacion")]
    return Persona(nombre, edad, fecha_nacimiento, lenguajes)

# Crear archivos JSON y XML (como en el ejercicio anterior)
datos = {
    "Nombre": "Juan Pablo",
    "Edad": 25,
    "Fecha de nacimiento": "1998-09-24",
    "Lenguajes de programación": ["Python", "Java", "C++"]
}

with open("datos.json", "w") as json_file:
    json.dump(datos, json_file, indent=4)

root = ET.Element("Persona")
ET.SubElement(root, "Nombre").text = datos["Nombre"]
ET.SubElement(root, "Edad").text = str(datos["Edad"])
ET.SubElement(root, "Fecha_de_nacimiento").text = datos["Fecha de nacimiento"]
lenguajes = ET.SubElement(root, "Lenguajes_de_programacion")
for lenguaje in datos["Lenguajes de programación"]:
    ET.SubElement(lenguajes, "Lenguaje").text = lenguaje

tree = ET.ElementTree(root)
with open("datos.xml", "wb") as xml_file:
    tree.write(xml_file)

# Leer y transformar los datos en una clase custom
persona_desde_json = leer_json("datos.json")
persona_desde_xml = leer_xml("datos.xml")

print("Datos desde JSON:")
print(persona_desde_json)

print("\nDatos desde XML:")
print(persona_desde_xml)

# Borrar los archivos
# os.remove("datos.json")
# os.remove("datos.xml")
