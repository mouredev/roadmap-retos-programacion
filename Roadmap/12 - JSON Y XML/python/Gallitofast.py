#JSON & XML
""" EJERCICIO:
  Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los
  siguientes datos (haciendo uso de la sintaxis correcta en cada caso):
  - Nombre
  - Edad
  - Fecha de nacimiento
  - Listado de lenguajes de programación
  Muestra el contenido de los archivos.
  Borra los archivos."""
import json
import os
import xml.etree.ElementTree as ET

dicc_json = {"Nombre":"Jose","Edad":"24","Fecha_de_nacimiento": "02/04/2002","Lista_de_lenguajes": ["Python","Typescript"]}
dicc_xml = {"Nombre":"Miguel","Edad":"24","Fecha_de_nacimiento": "02/04/2002","Lista_de_lenguajes": ["Typescript","Python"]}

xml_file = "new_data.xml"
json_file = "new_data.json"

#XML 
def create_xml():
    datos = ET.Element("datos")
    for key,value in dicc_xml.items():
        eDatos = ET.SubElement(datos,key)  
        if isinstance(value,list):
            for i in value: 
                ET.SubElement(eDatos,"item").text = i
        else: 
            eDatos.text = str(value)   
    tree = ET.ElementTree(datos)     
    ET.indent(tree, space="    ")
    tree.write(xml_file)    

create_xml()
with open(xml_file, "r") as file: 
    print(file.read())
os.remove("new_data.xml")  


#JSON

print ("-"*60)
def create_json():
    with open(json_file,"w") as file:
        json.dump(dicc_json,file,indent=4)


create_json()
with open(json_file,"r") as file:
    print(file.read())

os.remove("new_data.json")
print ("-"*60)

"""
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la lógica de creación de los archivos anteriores, crea un
 * programa capaz de leer y transformar en una misma clase custom de tu 
 * lenguaje los datos almacenados en el XML y el JSON.
"""

try:
    #XML
    create_xml()

    class Data():
        def __init__(self,name,age,birthday,languages) -> None:
            self.name = name
            self.age = age
            self.birthday =birthday
            self.languages= languages
        
        def print (self):
            print(f"Nombre y apellido: {self.name}")
            print(f"Edad: {self.age}")
            print(f"Fecha de nacimiento: {self.birthday}")
            print(f"Lenguajes de programacion: {self.languages}")
        
    with open(xml_file,"r") as file:
        raiz = ET.fromstring(file.read())
        name = raiz.find("Nombre").text
        age = raiz.find("Edad").text
        birthday = raiz.find("Fecha_de_nacimiento").text
        languages = []
        for i in raiz.find("Lista_de_lenguajes"):
            languages.append(i.text)
        
        xml_class= Data(name,age,birthday,languages)
        print("xml a Clase custom")
        xml_class.print()
    #Clase json
    
    create_json()
    print("-"*60)
    with open(json_file,"r") as file:
        json_data = json.load(file)
        json_class = Data(
            json_data["Nombre"],
            json_data["Edad"],
            json_data["Fecha_de_nacimiento"],
            json_data["Lista_de_lenguajes"])
        print("Json a Clase custom")
        json_class.print()



except Exception as e:
    print("Error",e)
finally:
    os.remove("new_data.xml")
    os.remove("new_data.json")