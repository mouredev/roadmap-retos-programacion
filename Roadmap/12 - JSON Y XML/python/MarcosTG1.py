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
import xml.etree.ElementTree as xml
import os
import json

# <data>
#     <country name="Liechtenstein">
#         <rank>1</rank>
#         <year>2008</year>
#         <gdppc>141100</gdppc>
#         <neighbor name="Austria" direction="E"/>
#         <neighbor name="Switzerland" direction="W"/>
#     </country>
#     <country name="Singapore">
#         <rank>4</rank>
#         <year>2011</year>
#         <gdppc>59900</gdppc>
#         <neighbor name="Malaysia" direction="N"/>
#     </country>
#     <country name="Panama">
#         <rank>68</rank>
#         <year>2011</year>
#         <gdppc>13600</gdppc>
#         <neighbor name="Costa Rica" direction="W"/>
#         <neighbor name="Colombia" direction="E"/>
#     </country>
# </data>

data = {
    "name": "Marcos",
    "edad": 21,
    "fecha_nacimiento": "22-10-2004",
    "listado_lenguajes": ["Python", "Go", "R"]

}



def save_xml(file_name):

    root = xml.Element("data")

    for key, value in data.items():
        # print(f"Esta es la key : {key}")
        # print(f"Este es el value : {value}")
        child = xml.SubElement(root, key)

        if isinstance(value, list):
            for item in value:
                nodo_hoja = xml.SubElement(child, "item")
                nodo_hoja.text = str(item)
                print(nodo_hoja.text)
        else:
            child.text = str(value)
            print(child.text)
        
    for child in root:
        print(child.tag, "->", child.text)
    for item in child:
        print(item.text)

    tree = xml.ElementTree(root)
    tree.write(file_name)

    
# print(data.items())
# [("name", "Marcos"), ("edad", 21) ...

# tag_bytes = b"persona" 
# print(type(tag_bytes))

xml_file = "MarcosTG1.xml"
save_xml(xml_file)

# with open(xml_file, "r", encoding="utf-8") as file:
#     print(file.read())

# os.remove(file_name)

# --------- JSON ---------

# print(json.dumps([1, 2, 3, 4, {"hola": 2, "adiós": 3}], separators=(",", ":"), ensure_ascii=True))

json_file = "MarcosTG1.json"

with open(json_file, "w", encoding="utf-8") as file:
    json.dump(data, file)

# with open(json_file, "r", encoding="utf-8") as file:
#     print(file.read())

print(int("1F40D", 16))


"""
* DIFICULTAD EXTRA (opcional):
* Utilizando la lógica de creación de los archivos anteriores, crea un
* programa capaz de leer y transformar en una misma clase custom de tu 
* lenguaje los datos almacenados en el XML y el JSON.
* Borra los archivos.
"""

class Data:

    def __init__(self, name: str, age: int, birth_date: str, programming_languages: list[str]) -> None:
        self.name = name
        self.age = age
        self.birth_date = birth_date
        self.programming_languages = programming_languages

with open(xml_file, "r") as xml_data:
    root = xml.fromstring(xml_data.read())
    name = root.find("name").text
    age = root.findtext("edad")
    birth_date = root.findtext("fecha_nacimiento")
    programming_languages = []
    for lenguaje in root.find("listado_lenguajes"):
        programming_languages.append(lenguaje.text)

    xml_class = Data(name, age, birth_date, programming_languages)
    print(xml_class.__dict__)

tree = xml.ElementTree(root)
    
programa = str(input("Qué programa deseas añadir?: "))

listado_nodo = root.find("listado_lenguajes")
nuevo_item = xml.SubElement(listado_nodo, "item")
nuevo_item.text = programa

tree.write(xml_file, encoding="utf-8")
xml_class.programming_languages.append(programa)

with open(json_file, "r") as json_data:
    json_dict = json.load(json_data)
    print(json_dict)
    print(type(json_dict))

    json_class = Data(
        json_dict["name"],
        json_dict["edad"],
        json_dict["fecha_nacimiento"],
        json_dict["listado_lenguajes"]
    )
    print(json_class.__dict__)


