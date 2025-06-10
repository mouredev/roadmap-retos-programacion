import os
import xml.etree.ElementTree as xml # 📦 Módulo para trabajar con XML
import json
"""
JSON Y XML
"""

#JSON: Formato ligero de texto para almacenar datos usando llaves {} y corchetes [].
#XML: Formato de texto para almacenar datos usando etiquetas <etiqueta> </etiqueta>.

#ALT + SHIFT + F

# Diccionario de datos con diferentes tipos de valores
data = {
    "name": "Complex_303",
    "age": 24,
    "birth_date": "01-01-2001",
    "programming_languages": ["Python", "SQL", "C#"]
}


#XML
# Nombre del archivo XML que se va a crear
xml_file = "Complex_303.xml"

# 📌 Definir función para guardar los datos en formato XML
def create_xml():

    # Crear elemento raíz del XML llamado <data>
    root = xml.Element("data")

    # Recorrer el diccionario data clave-valor
    for key, value in data.items():
        # Crear un subelemento para cada clave (ej. <name>, <age>, etc.)
        child = xml.SubElement(root, key)

        # Si el valor es una lista (ej. lista de lenguajes de programación)
        if isinstance(value, list):
            # Por cada elemento en la lista, crear un subelemento <item> y asignarle su valor
            for item in value:
                xml.SubElement(child, "item").text = item
        else:
            # Si no es lista, se asigna directamente el valor como texto
            child.text = str(value)

    # Crear árbol XML a partir del elemento raíz
    tree = xml.ElementTree(root)

    # Escribir el árbol en un archivo XML
    tree.write(xml_file)

# 📌 Llamar a la función para generar el archivo
create_xml()

#Abril el archivo y leerlo
with open(xml_file, "r") as xml_data: 
    print(xml_data.read())

#os.remove(xml_file) #borrarlo


#JSON
json_file = "Complex_303.json"


def create_json():

# 📌 Abrimos (o creamos) el archivo en modo escritura ("w")
# con el nombre json_file, y lo llamamos json_data dentro del bloque
    with open(json_file, "w") as json_data:
        # Convertimos un diccionario (o cualquier estructura válida) a JSON 
        # y lo escribimos en el archivo abierto
        json.dump(data, json_data)

create_json()

# Ahora abrimos el mismo archivo pero en modo lectura ("r")
with open(json_file, "r") as json_data: 
    # Leemos todo el contenido del archivo JSON y lo mostramos por pantalla
    print(json_data.read())

# Finalmente eliminamos el archivo JSON que creamos
#os.remove(json_file)


""" DIFICULTAD EXTRA (opcional):
 * Utilizando la lógica de creación de los archivos anteriores, crea un
 * programa capaz de leer y transformar en una misma clase custom de tu 
 * lenguaje los datos almacenados en el XML y el JSON.
 * Borra los archivos."""


# Definimos una clase llamada Data para almacenar información estructurada
class Data:
    # Método constructor que se ejecuta al crear una instancia de Data
    def __init__(self, name, age, birth_date, programming_languages):
        # Guardamos los valores recibidos en atributos de la clase
        self.name = name
        self.age = age
        self.birth_date = birth_date
        self.programming_language = programming_languages


# Abrimos el archivo XML en modo lectura
with open("Complex_303.xml", "r") as xml_data:
    # Leemos y convertimos el contenido XML en una estructura de árbol
    root = xml.fromstring(xml_data.read())
    
    # Buscamos y extraemos el texto de cada etiqueta usando find()
    name = root.find("name").text
    age = root.find("age").text
    birth_date = root.find("birth_date").text
    
    # Creamos una lista vacía para almacenar los lenguajes de programación
    programming_languages = []
    # Iteramos sobre los elementos <item> dentro de <programming_languages>
    for item in root.find("programming_languages"):
        programming_languages.append(item.text)
    
    # Creamos una instancia de la clase Data usando los valores extraídos del XML
    xml_class = Data(name, age, birth_date, programming_languages)
    # Imprimimos los atributos de esa instancia en forma de diccionario
    print(xml_class.__dict__)


# Abrimos el archivo JSON en modo lectura
with open("Complex_303.json", "r") as json_data:
    # Cargamos el contenido JSON y lo convertimos en diccionario de Python
    json_dict = json.load(json_data)
    
    #Creamos una instancia de la clase Data usando los valores extraídos del JSON
    json_class = Data(
        json_dict["name"], 
        json_dict["age"], 
        json_dict["birth_date"], 
        json_dict["programming_languages"]
    )
    
    #Imprimimos los atributos de esa instancia en forma de diccionario
    print(json_class.__dict__)


# Eliminamos los archivos XML y JSON que habíamos usado
os.remove("Complex_303.xml")
os.remove("Complex_303.json")





# fromstring()	Convierte texto XML en árbol DOM
# find()	Busca una etiqueta XML específica
# for item in ...	Itera sobre subetiquetas <item> dentro de una lista XML
# json.load()	Carga un JSON desde archivo a diccionario
# __dict__	Devuelve los atributos de una instancia como diccionario
# os.remove()	Borra archivos físicos del sistema
