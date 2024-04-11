# Reto 12 JSON Y XML

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
 """

import xml.etree.ElementTree as ET
import os
import json

# Datos con los que trabajaremos

data = {
    "name": "Fede Airala",
    "age": 43,
    "birth_day": "25/06/1980",
    "programming_languages": ["Python", "MySql","Java"]
}

data2 = {
    "name": "Juan Perez",
    "age": 25,
    "birth_day": "03/08/1970",
    "programming_languages": ["Javascript", "MySql"]
}

xml_file = "new_data.xml"
json_file = "new_data.json"




# Creación de archivo xml

def create_xml():                                         # Función para crear archivos xml

    datos = ET.Element("datos")                           # Se crea un elemento tipo xml de nombre datos

    for key,value in data.items():                        # Se recorre los datos del diccionario creado data
        eDatos = ET.SubElement(datos,key)                 # Le asignamos a una variable un sub elemento  del elemento datos antes creado y le pasamos la llave del dicc
        if isinstance(value,list):                        # Preguntamos si el tipo de valor es una lista
            for i in value:                               # Si es una lista, la recorremos
                ET.SubElement(eDatos,"item").text = i     # y escribimos por cada subelemento el valor
        else:                                             # Si no es una lista
            eDatos.text = str(value)                      # se escribe directamente el valor
    
    tree = ET.ElementTree(datos)                          # Se crea un árbol de los elementos antes creados
    tree.write(xml_file)                                  

create_xml()

with open(xml_file, "r") as file:                         # Abre el archivo xml de tipo lectura
    print(file.read())                                    # Imprime por pantalla el archivo xml

os.remove("new_data.xml")                                 # Elimina el fichero creado

print ("-"*60)

# Creación de archivo json

def create_json():                                        # Función para crear archivos json

    with open (json_file, "w") as file:                   # Abre el archivo tipo escritura
        json.dump(data2,file,indent=4)                    # Se pasan los datos a crear tipo de archivo json

create_json()

with open(json_file, "r") as file:                       # Abre el archivo json de tipo lectura
    print(file.read())                                   # Imprime por pantalla el archivo json

os.remove("new_data.json")                               # Elimina el fichero creado

print ("-"*60)

"""
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la lógica de creación de los archivos anteriores, crea un
 * programa capaz de leer y transformar en una misma clase custom de tu 
 * lenguaje los datos almacenados en el XML y el JSON.
"""
try:
    create_xml()


    class Data:
        def __init__(self,name,age,birthday,languages) -> None:
            self.name = name
            self.age = age
            self.birthday =birthday
            self.languages = languages
        
        def print (self):
            print (f"Nombre y Apellido: {self.name}")
            print (f"Edad: {self.age}")
            print (f"Fecha de Nacimiento: {self.birthday}")
            print (f"Lenguages: {self.languages}")


    with open (xml_file, "r") as file:
    
        raiz = ET.fromstring(file.read())
        name = raiz.find("name").text   
        age = raiz.find("age").text   
        birth_day = raiz.find("birth_day").text 
        languages = []
        for i in raiz.find("programming_languages"):
            languages.append(i.text)
        xml_class = Data(name,age,birth_day,languages)
        print ("xml a Clase Custom")
        xml_class.print()
    create_json()

    print ("-"*60)

    with open(json_file, "r") as file:
        json_data = json.load(file)
        json_class = Data(
            json_data["name"],
            json_data["age"],
            json_data["birth_day"],
            json_data["programming_languages"])
        print ("Json a Clase Custom")
        json_class.print()

except Exception as e:
    print("Error ",e)

finally:
    os.remove("new_data.xml") 
    os.remove("new_data.json")     



    




