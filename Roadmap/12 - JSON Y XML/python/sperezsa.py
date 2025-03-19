#12 - JSON Y XML

#  * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
#  * 
#  * EJERCICIO:
#  * Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los
#  * siguientes datos (haciendo uso de la sintaxis correcta en cada caso):
#  * - Nombre
#  * - Edad
#  * - Fecha de nacimiento
#  * - Listado de lenguajes de programación
#  * Muestra el contenido de los archivos.
#  * Borra los archivos.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Utilizando la lógica de creación de los archivos anteriores, crea un
#  * programa capaz de leer y transformar en una misma clase custom de tu 
#  * lenguaje los datos almacenados en el XML y el JSON.
#  * Borra los archivos.


import xml.etree.ElementTree as ET
import json 
import os 

#XML
xml_file = "archivo.xml"

root = ET.Element("root")

campo_texto1 = ET.SubElement(root, "nombre")
campo_texto1.text = "Sergio"

campo_texto2 = ET.SubElement(root, "edad")
campo_texto2.text = "44"

campo_texto3 = ET.SubElement(root, "fx_nacimiento")
campo_texto3.text = "08/09/1979"

campo_lista = ET.SubElement(root, "lenguajes")

item1 = ET.SubElement(campo_lista, "item")
item1.text = "Python"

item2 = ET.SubElement(campo_lista, "item")
item2.text = "Java"

item3 = ET.SubElement(campo_lista, "item")
item3.text = "JavaScript"

tree = ET.ElementTree(root)
tree.write(xml_file)


with open(xml_file, "r") as file:
    print(file.read())

os.remove(xml_file)

#JSON
json_file = "archivo.json"

datos = {
    "nombre": "Sergio",
    "edad": 44,
    "fx_nacimiento": "08/09/1979",
    "lenguajes": ["Python", "Java", "JavaScript"]
    }


with open(json_file, "w") as archivo:
  json.dump(datos, archivo)

with open(json_file, "r") as file:
    print(file.read())

os.remove(json_file)


"""
Extra
"""
class Developer():
    def __init__(self, nombre, edad, fx_nacimiento, lenguajes) -> None:
        self.nombre = nombre
        self.edad =  edad
        self.fx_nacimiento = fx_nacimiento
        self.lenguajes = lenguajes
    
with open(json_file, "r") as file:
    dic = json.load(file)
    json_class = Developer(
        dic["nombre"],
        dic["edad"],
        dic["fx_nacimiento"],
        dic["lenguajes"]
    )
    print(json_class.__dict__)
        

with open(xml_file, "r") as file:
    root = ET.fromstring(file.read())
    nombre = root.find("nombre").text
    edad = root.find("edad").text
    fx_nacimiento = root.find("fx_nacimiento").text
    lenguajes = []
    for item in root.find("lenguajes"):
        lenguajes.append(item.text)
    xml_class = Developer(nombre, edad, fx_nacimiento, lenguajes)
    print(xml_class.__dict__)
    
os.remove(xml_file)
os.remove(json_file)
