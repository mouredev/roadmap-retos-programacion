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
import xml.etree.ElementTree as ET
import json


# Archivo XML:
root = ET.Element('root')

child1 = ET.SubElement(root, 'child1')
child1.text = 'Nombre: Hernan'

child2 = ET.SubElement(root, 'child2')
child2.text = 'Edad: 23 años'

child3 = ET.SubElement(root, 'child3')
child3.text = 'Fecha de nacimiento: 03-08-00'

child4 = ET.SubElement(root, 'child4')
child4.text = 'Listado de lenguajes de programacion: Python, JavaScript'

tree = ET.ElementTree(root)
tree.write('archivo.xml')

with open('archivo.xml', 'r') as file:
    contenido = file.read()
    print(contenido)

# Archivo JSON:
datos = {
    'nombre': 'Hernan',
    'edad': 23,
    'fecha_nacimiento': '03-08-00',
    'lenguajes_programacion': ['python', 'javascript']
}

nombre_archivo = "datos.json"

with open(nombre_archivo, "w") as archivo:
    json.dump(datos, archivo)

with open(nombre_archivo, 'r') as file:
    contenido = file.read()
    print(contenido)
