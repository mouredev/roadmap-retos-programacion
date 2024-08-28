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
 */
 """

import os
import xml.etree.ElementTree as xml

programador = {
    "nombre": "Lucas Rebuffo",
    "edad": 27,
    "fecha_nac": "10-02-1997",
    "lenguajes_de_programacion": ["python", "javascript", "java"],
}


xml_file = "LucasRebuffo.xml"


def guardar_xml():

    raiz = xml.Element("data")

    for key, value in programador.items():
        hijo = xml.SubElement(raiz, key)
        if isinstance(value, list):
            for item in value:
                xml.SubElement(hijo, "item").text = str(item)
        else:
            hijo.text = str(value)

    tree = xml.ElementTree(raiz)
    tree.write(xml_file)


guardar_xml()

with open(xml_file, "r") as xml_data:
    print(xml_data.read())

# os.remove(xml_file)

print("\n")

import json

json_file = "LucasRebuffo.json"


with open(json_file, "w") as json_data:
    json.dump(programador, json_data)

with open(json_file, "r") as json_data:
    print(json_data.read())

# os.remove(json_file)


print("\n")
"""  * DIFICULTAD EXTRA (opcional):
 * Utilizando la lógica de creación de los archivos anteriores, crea un
 * programa capaz de leer y transformar en una misma clase custom de tu 
 * lenguaje los datos almacenados en el XML y el JSON.
 * Borra los archivos.
 */ """


class Programador:

    def __init__(
        self, nombre: str, edad: int, fecha_nac: str, lenguajes_de_programacion: list
    ) -> None:
        self.nombre = nombre
        self.edad = edad
        self.fecha_nac = fecha_nac
        self.lenguajes_de_programacion = lenguajes_de_programacion

    def __str__(self) -> str:
        return f"Nombre: {self.nombre} | Edad: {self.edad} | Fecha de nacimiento: {self.fecha_nac} | Lenguajes: {self.lenguajes_de_programacion}"


with open(xml_file, "r") as xml_data:

    root = xml.fromstring(xml_data.read())
    nombre = root.find("nombre").text
    edad = root.find("edad").text
    fecha_nac = root.find("fecha_nac").text
    lenguajes_de_programacion = []
    for item in root.find("lenguajes_de_programacion"):
        lenguajes_de_programacion.append(item.text)

data = Programador(nombre, edad, fecha_nac, lenguajes_de_programacion)

print(data)
print("\n")


with open(json_file, "r") as json_data:

    json_dict = json.load(json_data)

    json_class = Programador(
        json_dict["nombre"],
        int(json_dict["edad"]),
        json_dict["fecha_nac"],
        json_dict["lenguajes_de_programacion"],
    )


print(json_class)
