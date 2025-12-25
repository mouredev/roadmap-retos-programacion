#Json y XML
"""
JSON (JavaScript Object Notation) y XML (eXtensible Markup Language) son formatos de datos ampliamente utilizados para el intercambio de información entre sistemas. 
Ambos formatos permiten estructurar datos de manera que sean legibles tanto para humanos como para máquinas, pero tienen diferencias significativas en su sintaxis y uso.

JSON: es un formato de texto ligero y fácil de leer que se utiliza para representar datos estructurados. 
Se basa en una sintaxis de pares clave-valor y es ampliamente utilizado en aplicaciones web para el intercambio de datos entre el cliente y el servidor. 
JSON es compatible con muchos lenguajes de programación y se puede analizar fácilmente en objetos nativos.

XML: es un formato de texto más complejo que utiliza etiquetas para definir la estructura de los datos. Es más verboso que JSON y se utiliza en una variedad de aplicaciones, 
incluyendo servicios web, configuración de software y almacenamiento de datos. 
XML permite definir esquemas para validar la estructura de los datos, lo que puede ser útil en aplicaciones que requieren una validación estricta.
Python proporciona bibliotecas integradas para trabajar con ambos formatos:

- json: para trabajar con JSON, permite convertir entre cadenas JSON y objetos de Python (como diccionarios y listas).
- xml.etree.ElementTree: para trabajar con XML, permite analizar y crear documentos XML de
manera sencilla.
A continuación, se presentan ejemplos básicos de cómo utilizar estas bibliotecas en Python:
"""
from logging import root
import os
import json
import xml
import xml.etree.ElementTree as XML
# Ejemplo de JSON
# Crear un diccionario de Python
data = {
    "nombre": "Juan",
    "edad": 30,
    "lenguajes_de_programacion": ["Python"],
    "fecha_de_nacimiento": "1993-01-01"
}

# Convertir el diccionario a una cadena JSON
json_file_path = "Paprikaistkrieg.json" # Nombre del archivo JSON
with open(json_file_path, "w") as jf: # Guardar la cadena JSON en un archivo
    json.dump(data, jf) # Escribir el diccionario en el archivo como JSON
# Leer y analizar un archivo JSON
with open(json_file_path, "r") as jf: # Abrir el archivo JSON en modo lectura
    data_loaded = json.load(jf) # Cargar el contenido del archivo JSON en un diccionario de Python
    print(data_loaded) # Imprimir el diccionario cargado desde el archivo JSON

xml_file = "Paprikaistkrieg.xml"
# Ejemplo de XML
# Crear un elemento raíz 
def save_XML(): # funcion para guardar en XML
    root = XML.Element("data") # Crear el elemento raíz
    for key, value in data.items(): # Iterar sobre los pares clave-valor del diccionario
        child = XML.SubElement(root, key) # Crear un subelemento para cada clave
        if isinstance(value, list): # Verificar si el valor es una lista
            for item in value: # Iterar sobre los elementos de la lista
                item_element = XML.SubElement(child, "item") # Crear un subelemento para cada ítem
                item_element.text = str(item) # Asignar el valor del ítem como texto
        else: # Si el valor no es una lista
            child.text = str(value) # Asignar el valor como texto
    tree = XML.ElementTree(root) # Crear un árbol XML a partir del elemento raíz
    tree.write("Paprikaistkrieg.xml") # Guardar el árbol XML en un archivo

save_XML() # Llamar a la función para guardar en XML

# Leer y analizar un archivo XML
with open (xml_file) as xml_data: # Abrir el archivo XML en modo lectura
    print(xml_data.read()) # Imprimir el contenido del archivo XML

os.remove(xml_file) # Eliminar el archivo XML creado
os.remove(json_file_path) # Eliminar el archivo JSON creado


#XtraJ

def save_JSON(): # funcion para guardar en JSON
    with open("Paprikaistkrieg.json", "w") as jf: # Abrir el archivo JSON en modo escritura
        json.dump(data, jf) # Escribir el diccionario en el archivo como JSON


save_JSON() # Llamar a la función para guardar en JSON

save_XML() # Llamar a la función para guardar en XML

class Data:
    def __init__(self, name, age, birth_date, programming_languages):
        self.name = name
        self.age = age
        self.birth_date = birth_date
        self.programming_languages = programming_languages

# Leer y analizar el archivo JSON y crear una instancia de Data
if os.path.exists(json_file_path):
    with open(json_file_path, "r", encoding="utf-8") as json_data:
        data_json = json.load(json_data)
        data_class_JSON = Data(
            data_json["nombre"],
            data_json["edad"],
            data_json["fecha_de_nacimiento"],
            data_json["lenguajes_de_programacion"],
        )
        print(data_class_JSON.__dict__) # Imprime el diccionario de atributos del objeto

# Leer y analizar el archivo XML y crear una instancia de Data
if os.path.exists(xml_file):
    with open(xml_file, "r", encoding="utf-8") as xml_data:
        xml_data_content = xml_data.read()
        root = XML.fromstring(xml_data_content)
        name = root.find("nombre").text
        age = root.find("edad").text
        birth_date = root.find("fecha_de_nacimiento").text
        programming_languages = []
        for item in root.findall("lenguajes_de_programacion/item"):
            programming_languages.append(item.text)

        data_class_XML = Data(name, age, birth_date, programming_languages)
        print(data_class_XML.__dict__) # Imprime el diccionario de atributos del objeto

os.remove(xml_file) # Eliminar el archivo XML creado
os.remove(json_file_path) # Eliminar el archivo JSON creado



