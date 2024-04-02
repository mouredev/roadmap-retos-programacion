"""
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
"""

import json
import os

# Crear archivo json

datos_json = {
    "Nombre": "Christian",
    "Edad": "30",
    "Fecha de nacimiento": "01/05/1994",
    "Listado de lenguajes": ["Python", "JavaScript", "React"]
}

file_name = "Chrisdev00.json"

with open(file_name, "w") as file_json:
    json.dump(datos_json, file_json, indent=4) # (ident=) para que el archivo json tenga una apariencia mas legible con identaciones

# Mostrar el contenido
    
with open(file_name, "r") as file_json:
    lista_datos = json.load(file_json)

print("Datos en el archivo JSON")
for clave, valor in lista_datos.items():
    print(f"{clave}: {valor}")

# Borrar el archivo

if os.path.exists(file_name):
    #os.remove(file_name)  comentamos esta parte para que el ejercicio extra no de error
    pass
else:
    print("El archivo no existe")


# Crear archivo XML
    
import xml.etree.ElementTree as ET

root = ET.Element("datos")

nombre = ET.SubElement(root, "nombre")
nombre.text = "Christian"

edad = ET.SubElement(root, "edad")
edad.text = "30"

fecha_nacimiento = ET.SubElement(root, "fecha_nacimiento")
fecha_nacimiento.text = "01/05/1994"

lenguajes = ET.SubElement(root, "Listado_de_lenguajes")
lenguajes.text = "Python, JavaScript, React"

tree_xml = ET.ElementTree(root)
file_name_xml = "Chrisdev00.xml"

tree_xml.write(file_name_xml, encoding="utf-8", xml_declaration=True)

# mostrar datos

tree_xml = ET.parse(file_name_xml)

raiz = tree_xml.getroot()

print("Datos en el archivo XML")
for elemento in raiz:
    print(f"{elemento.tag}: {elemento.text}")

# borrar archivo
    
#os.remove(file_name_xml) comentamos esta parte para que funcione el ejercicio extra


##### -------------------------------- EXTRA -------------------------------------------- ########



class DatosPersonales:

    def __init__(self, nombre, edad, fecha_nacimiento, lenguajes):
        self.nombre = nombre
        self.edad = edad
        self.fecha_nacimiento = fecha_nacimiento
        self.lenguajes = lenguajes
    
    @classmethod
    def leer_json (cls, nombre_archivo_json):
        with open(nombre_archivo_json, "r") as file:
            datos_jso = json.load(file)
            return cls(
                datos_jso["Nombre"],
                datos_jso["Edad"],
                datos_jso["Fecha de nacimiento"],
                datos_jso["Listado de lenguajes"],
            )
    
    @classmethod
    def leer_xml (cls, nombre_archivo_xml):
        tree_xml = ET.parse(nombre_archivo_xml)
        raiz = tree_xml.getroot()
        nombre = raiz.find("nombre").text
        edad = raiz.find("edad").text
        fecha_nacimiento = raiz.find("fecha_nacimiento").text
        lenguajes_str = raiz.find("Listado_de_lenguajes").text
        lenguajes = lenguajes_str.split(", ")
        #lenguajes = [lenguaje.text for lenguaje in raiz.find("Listado_de_lenguajes")]
        return cls(nombre, edad, fecha_nacimiento, lenguajes)
    
    def __str__(self):
        return f"Nombre: {self.nombre}\nEdad: {self.edad}\nFecha de nacimiento: {self.fecha_nacimiento}\nLenguajes: {', '.join(self.lenguajes)}"

desde_json = DatosPersonales.leer_json("Chrisdev00.json")
desde_xml = DatosPersonales.leer_xml("Chrisdev00.xml")

print("\nDatos desde JSON:")
print(desde_json)
print("\nDatos desde XML:")
print(desde_xml)


