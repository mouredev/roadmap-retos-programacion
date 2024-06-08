"""	
12 - JSON Y XML
Autor de la solución: Oriaj3	
Teoría:	
JSON (JavaScript Object Notation) y XML (eXtensible Markup Language) son dos
formatos de texto utilizados para el intercambio de datos entre aplicaciones.

JSON es un formato ligero y fácil de leer, basado en JavaScript. Se utiliza
comúnmente en aplicaciones web y servicios web para enviar y recibir datos.

XML es un formato más complejo y flexible, basado en etiquetas. Se utiliza en
aplicaciones más antiguas y en servicios web SOAP.

En Python, se pueden leer y escribir datos en formato JSON y XML utilizando
las bibliotecas json y xml.etree.ElementTree, respectivamente.
"""
import json
import xml.etree.ElementTree as ET
import os

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
 *
"""

# Datos
datos = {
    "nombre": "Juan",
    "edad": 25,
    "fecha_nacimiento": "01/01/1996",
    "lenguajes": ["Python", "JavaScript", "Java"]
}

# Crear archivo JSON
with open("datos.json", "w") as f:
    json.dump(datos, f, indent=4) # indent=4 para dar formato
    
# Mostrar contenido del archivo JSON
with open("datos.json", "r") as f:
    print(f.read())

# Crear archivo XML
root = ET.Element("datos")
for key, value in datos.items():
    if isinstance(value, list):
        subroot = ET.SubElement(root, key)
        for item in value:
            ET.SubElement(subroot, "lenguaje").text = item
    else:
        ET.SubElement(root, key).text = str(value)
tree = ET.ElementTree(root)

tree.write("datos.xml")

# Mostrar contenido del archivo XML
with open("datos.xml", "r") as f:
    print(f.read())

 
"""
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la lógica de creación de los archivos anteriores, crea un
 * programa capaz de leer y transformar en una misma clase custom de tu 
 * lenguaje los datos almacenados en el XML y el JSON.
 * Borra los archivos.
"""

class Datos():
    def __init__(self, nombre, edad, fecha_nacimiento, lenguajes) -> None:
        self.nombre = nombre
        self.edad = edad
        self.fecha_nacimiento = fecha_nacimiento
        self.lenguajes = lenguajes

    def __str__(self) -> str:
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Fecha de nacimiento: {self.fecha_nacimiento}, Lenguajes: {self.lenguajes}"
    
    @staticmethod
    def from_json(json_file):
        with open(json_file, "r") as f:
            datos = json.load(f)
        return Datos(datos["nombre"], datos["edad"], datos["fecha_nacimiento"], datos["lenguajes"])
    
    @staticmethod
    def from_xml(xml_file):
        datos = {}
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for child in root:
            if child.tag == "lenguajes":
                datos[child.tag] = [lenguaje.text for lenguaje in child]
            else:
                datos[child.tag] = child.text
        return Datos(datos["nombre"], datos["edad"], datos["fecha_nacimiento"], datos["lenguajes"])
    
    def to_json(self, json_file):
        with open(json_file, "w") as f:
            json.dump(self.__dict__, f, indent=4)
    
    def to_xml(self, xml_file):
        root = ET.Element("datos")
        for key, value in self.__dict__.items():
            if key == "lenguajes":
                subroot = ET.SubElement(root, key)
                for item in value:
                    ET.SubElement(subroot, "lenguaje").text = item
            else:
                ET.SubElement(root, key).text = str(value)
        tree = ET.ElementTree(root)
        tree.write(xml_file)
        
# Crear objeto Datos a partir de JSON
datos_json = Datos.from_json("datos.json")
print(datos_json)

# Crear objeto Datos a partir de XML
datos_xml = Datos.from_xml("datos.xml")
print(datos_xml)

# Borrar archivos
os.remove("datos.json")
os.remove("datos.xml")
print("Archivos borrados")
