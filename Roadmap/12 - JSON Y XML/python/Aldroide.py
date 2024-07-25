"""
    EJERCICIO:
    Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los
    siguientes datos (haciendo uso de la sintaxis correcta en cada caso):
        - Nombre
        - Edad
        - Fecha de nacimiento
        - Listado de lenguajes de programación
    Muestra el contenido de los archivos.
    Borra los archivos
"""

import json
import xml.etree.ElementTree as ET
import os

# Datos para crear los archivos JSON y XML
data = {
    "nombre": "Aldroide",
    "edad": 40,
    "fecha_nacimiento": "1983-09-24",
    "lenguajes_programacion": ["Python", "C", "C++"]
}

# Creamos el archivo JSON
with open("datos.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

# Creamos el archivo XML
root = ET.Element("datos")
for key, value in data.items():
    if isinstance(value, list):
        subelement = ET.SubElement(root, key)
        for item in value:
            ET.SubElement(subelement, "lenguaje").text = item
    else:
        ET.SubElement(root, key).text = str(value)

tree = ET.ElementTree(root)
tree.write("datos.xml")

# Imprimir los archivos que se han creado
with open("datos.json", "r") as json_file:
    print("Contenido de datos.json:")
    print(json_file.read())

with open("datos.xml", "r") as xml_file:
    print("\nContenido de datos.xml:")
    print(xml_file.read())

# Borrar los archivos
# os.remove("datos.json")
# os.remove("datos.xml") Se comentan estas lineas para que funcione el codigo siguinte sin replicar el anterior

"""
    Utilizando la lógica de creación de los archivos anteriores, crea un
    programa capaz de leer y transformar en una misma clase custom de tu 
    lenguaje los datos almacenados en el XML y el JSON.
"""


class UserData:
    def __init__(self, nombre, edad, fecha_nacimiento, lenguajes_programacion):
        self.nombre = nombre
        self.edad = edad
        self.fecha_nacimiento = fecha_nacimiento
        self.lenguajes_programacion = lenguajes_programacion

    @classmethod
    def read_json(usr_data, na_file):
        # Leer archivo JSON
        with open("datos.json", "r") as json_file:
            json_data = json.load(json_file)
            # Crear instancia de UserData con los datos del JSON
            return usr_data(
                json_data["nombre"],
                json_data["edad"],
                json_data["fecha_nacimiento"],
                json_data["lenguajes_programacion"])

    @classmethod
    def read_xml(usr_data, na_file):
        # Leer archivo XML
        tree = ET.parse("datos.xml")
        root = tree.getroot()
        # Extraer datos del XML
        nombre = root.find("nombre").text
        edad = int(root.find("edad").text)
        fecha_nacimiento = root.find("fecha_nacimiento").text
        lenguajes_programacion = [
            elem.text for elem in root.find("lenguajes_programacion")]
        # Crear instancia de UserData con los datos del XML
        return usr_data(
            nombre, edad, fecha_nacimiento, lenguajes_programacion)

    def __str__(self):
        return f"Nombre: {self.nombre}\nEdad: {self.edad}\nFecha de nacimiento: {self.fecha_nacimiento}\nLenguajes de programación: {', '.join(self.lenguajes_programacion)}"


# Mostrar datos de ambas instancias
print("\nDatos del JSON:")
print(UserData.read_json("datos.json"))

print("\nDatos del XML:")
print(UserData.read_xml("datos.xml"))


os.remove("datos.json")
os.remove("datos.xml")
