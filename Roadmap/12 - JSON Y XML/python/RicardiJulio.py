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

import json
import os 
import xml.etree.ElementTree as ET

def indent(elem, level=0):
    # Función para aplicar indentación recursiva
    i = "\n" + level * "  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        for e in elem:
            indent(e, level + 1)
        if not e.tail or not e.tail.strip():
            e.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

data = {'nombre':'Julio',
        'edad': 23,
        'fecha_de_nacimiento':'04/02/2002',
        'listado_de_lenguajes':'python'}

# Creacion del archivo .json
nombre_a = 'my_data.json'
with open(nombre_a,'w') as j:
    json.dump(data,j) # Agregado de los datos al archivo
with open(nombre_a,'r') as j:
    datos = j.read()
    # print(datos) # Lectura e impresion de los archivos

# Crear el elemento raiz del archivo .xml
root = ET.Element('Datos_personales')

# Agregar los datos
datos = ET.SubElement(root,'datos')
ET.SubElement(datos,'nombre').text = 'Julio'
ET.SubElement(datos,'edad').text = '23'
ET.SubElement(datos,'fecha_de_nacimiento').text = '04/02/2002'
ET.SubElement(datos,'listado_de_lenguajes').text = 'Python'

indent(root)

# Crear un arbol XML
arbol = ET.ElementTree(root)
nombre_ax = 'my_data.xml'
# Guardar en un archivo
arbol.write(nombre_ax, encoding = "utf-8", xml_declaration = True)

with open(nombre_ax,'r') as d:
    info = d.read()
    print(info)

# DIFICULTAD EXTRA:

class Persona: # Creando clase custom
    def __init__(self,nombre,edad,fdn,ldl):
        self.nombre = nombre
        self.edad = edad
        self.fdn = fdn
        self.ldl = ldl
    
    def saludar(self):
        print (f'Hola mi nombre es {self.nombre} y tengo {self.edad}')

tree = ET.parse(nombre_ax) # Extrayendo informacio del archivo
root = tree.getroot()

for persona in root.findall('datos'):
    nombre = persona.find('nombre').text
    edad = persona.find('edad').text
    fdn = persona.find('fecha_de_nacimiento').text
    ldl = persona.find('listado_de_lenguajes').text
    
persona1 = Persona(nombre,edad,fdn,ldl) # Creando primer objeto

with open(nombre_a,'r') as on:
    info_json = json.load(on) # Extrayendo informaciond del archivo
    nombre2 = info_json['nombre']
    edad2 = info_json['edad']
    fdn2 = info_json['fecha_de_nacimiento']
    ldl2 = info_json['listado_de_lenguajes']
    
persona2 = Persona(nombre2,edad2,fdn2,ldl2) # Creando segundo objeto

persona1.saludar()
persona2.saludar() 

os.remove(nombre_a) # Eliminando los archivos
os.remove(nombre_ax)
