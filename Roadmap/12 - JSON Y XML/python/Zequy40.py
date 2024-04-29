  '''
  EJERCICIO:
  Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los
  siguientes datos (haciendo uso de la sintaxis correcta en cada caso):
  - Nombre
  - Edad
  - Fecha de nacimiento
  - Listado de lenguajes de programación
  Muestra el contenido de los archivos.
  Borra los archivos.
'''
import json
import xml.etree.ElementTree as ET
import os

# Datos a guardar
datos = {
    "nombre": "Juan",
    "edad": 35,
    "fecha_nacimiento": "1989-05-24",
    "lenguajes_programacion": ["Python", "JavaScript", "PhP"]
}

# Guardar datos en formato JSON
with open('datos.json', 'w') as json_file: #Aquí su utiliza la 'w' para poder escribir el archivo.
    json.dump(datos, json_file, indent=4)

# Guardar datos en formato XML
root = ET.Element("datos")
for key, value in datos.items():
    if isinstance(value, list):
        subelement = ET.SubElement(root, key)
        for item in value:
            ET.SubElement(subelement, "lenguaje").text = item
    else:
        ET.SubElement(root, key).text = str(value)

tree = ET.ElementTree(root)
tree.write('datos.xml')

# Mostrar contenido de los archivos
with open('datos.json', 'r') as json_file: #En este caso la 'r' es la que permite de leer el archivo a diferencia de la 'w'

    print("Contenido de datos.json:")
    print(json_file.read())

print("\n")

with open('datos.xml', 'r') as xml_file:
    print("Contenido de datos.xml:")
    print(xml_file.read())

# Borra los archivos
os.remove('datos.json') # Es la biblioteca de os que permite de borrar el contenido que sale en la consola
os.remove('datos.xml')


'''
  DIFICULTAD EXTRA (opcional):
  Utilizando la lógica de creación de los archivos anteriores, crea un
  programa capaz de leer y transformar en una misma clase custom de tu 
  lenguaje los datos almacenados en el XML y el JSON.
  Borra los archivos.
'''
import json
import xml.etree.ElementTree as ET
import os

class Datos:
    def __init__(self, nombre='', edad=0, fecha_nacimiento='', lenguajes_programacion=[]):
        self.nombre = nombre
        self.edad = edad
        self.fecha_nacimiento = fecha_nacimiento
        self.lenguajes_programacion = lenguajes_programacion

    @classmethod
    def desde_json(cls, json_file):
        with open(json_file, 'r') as file:
            datos_json = json.load(file)
            return cls(**datos_json)

    @classmethod
    def desde_xml(cls, xml_file):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        datos_xml = {}
        for child in root:
            if child.tag == 'lenguajes_programacion':
                lenguajes = [lang.text for lang in child]
                datos_xml[child.tag] = lenguajes
            else:
                datos_xml[child.tag] = child.text
        return cls(**datos_xml)

# Rutas de los archivos tanto en json como xml
ruta_json = 'datos.json'
ruta_xml = 'datos.xml'

# Crear instancia de Datos desde archivos
datos_desde_json = Datos.desde_json(ruta_json)
datos_desde_xml = Datos.desde_xml(ruta_xml)

# Mostrar los datos
print("Datos desde JSON:")
print(datos_desde_json.__dict__)
print()

print("Datos desde XML:")
print(datos_desde_xml.__dict__)

# Borra los archivos gracias a la biblioteca de os
os.remove(ruta_json)
os.remove(ruta_xml)
