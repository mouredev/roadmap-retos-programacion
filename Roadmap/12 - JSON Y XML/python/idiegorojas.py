import json
import xml.etree.cElementTree as ET
import os

# Crear un diccionario
data = {
    'nombre': 'Diego',
    'edad': 28,
    'fecha_nacimiento': '1996-11-08',
    'lenguajes_programacion': ['Python', 'Javascript', 'Swift']
}

# JSON
# Definimos el nombre del archivo que se va a crear
json_file = 'idiegorojas.json'

# Convertir el diccionario a JSON
json_data = json.dumps(data, indent=4)

# Guardar JSON en un archivo
with open(json_file, 'w') as file:
    json.dump(data, file, indent=4)

# Leer JSON
with open(json_file, 'r') as file:
    datos_guardados = json.load(file)
    print('Datos cargados:', datos_guardados)

# XML
# Definir el nombre del archivo que se va a crear
xml_file = 'idiegorojas.xml'

# Se define la funcion que crea la estructura del xml
def create_xml():

    # Se crea el elmento raiz del XML
    root = ET.Element('data')

    # Iterar sobre el dict 'data' para cada par clave valor
    for clave, valor in data.items():
        # Crear un subelemento con el nombre de la clave
        elemento_hija = ET.SubElement(root, clave.replace(' ', '_'))
        # Si el elemnto es una lista crear un elemento 'item' para cada elemento
        if isinstance (valor, list):
            for item in valor:
                ET.SubElement(elemento_hija, 'item').text = item
        # Si no es una lista se asigna el elemento como un texto
        else:
            elemento_hija.text = str(valor)

    # Guardamos el archivo
    # Creamos un arbol xml con la estructura creada.
    tree = ET.ElementTree(root)
    # Guardamos el arbol en el archivo especificado
    tree.write(xml_file)

# Llamamos a nuestra funcion
create_xml()

# Leemos el xml
with open(xml_file, 'r') as file:
    print(file.read())





# Extra

class Data:

    def __init__(self, nombre, edad, fecha_nacimiento, lenguajes_programacion) -> None:
        self.nombre = nombre
        self.edad = edad
        self.fecha_nacimiento = fecha_nacimiento
        self.lenguajes_programacion = lenguajes_programacion

# Crear nuevamente los archivos JSON y XML para leerlos en la clase Data
with open(json_file, 'w') as file:
    json.dump(data, file, indent=4)

create_xml()

with open(xml_file, "r") as file:
    root = ET.fromstring(file.read())
    nombre = root.find("nombre").text
    edad = root.find("edad").text
    fecha_nacimiento = root.find("fecha_nacimiento").text
    lenguajes_programacion = []
    for item in root.find("lenguajes_programacion"):
        lenguajes_programacion.append(item.text)

    xml_class = Data(nombre, edad, fecha_nacimiento, lenguajes_programacion)
    print(xml_class.__dict__)

with open(json_file, "r") as json_data:
    json_dict = json.load(json_data)
    json_class = Data(
        json_dict["nombre"],
        json_dict["edad"],
        json_dict["fecha_nacimiento"],
        json_dict["lenguajes_programacion"]
    )
    print(json_class.__dict__)

os.remove(xml_file)
os.remove(json_file)