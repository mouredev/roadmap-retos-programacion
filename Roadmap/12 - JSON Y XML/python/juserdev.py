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
 */ """

import json
import os
import xml.etree.ElementTree as xml # este es un modulo que permite manejar xml de manera mas simple

xml_file = "juserdev.xml"
json_path = "./data.json"

data = {
  "name": "Juan",
  "age": 34,
  "birth_date": "09-03-1991",
  "lenguages": ["Python", "TypeScript"]
}

# XML

def save_xml():
  root = xml.Element("data")

  for key, value in data.items():
    child = xml.SubElement(root, key)
    if isinstance(value, list):
      for item in value:
        xml.SubElement(child, "item").text = item

    else:
      child.text = str(value)

  tree = xml.ElementTree(root)
  tree.write(xml_file)

save_xml()
  
with open(xml_file) as xml_data:
  print(xml_data.read())

# os.remove(xml_file)

# JSON

def create_data():
  with open(json_path, "w") as file:
    json.dump(data, file, indent=2)
    print("Documento creado correctamente\n")
  

create_data()

with open(json_path, "r") as file:
  print(file.read())

# os.remove(json_path)

### EXTRA ###

class Data:
  def __init__(self, name: str, age: int,birth_date: str, lenguages: list):
    self.name = name
    self.age = age
    self.birth_date = birth_date
    self.lenguages = lenguages

with open(xml_file, "r") as xml_data:
  root = xml.fromstring(xml_data.read())
  name = root.find("name").text
  age = root.find("age").text
  birth_date = root.find("birth_date").text
  lenguages = []
  for item in root.find("lenguages"):
    lenguages.append(item.text)

data_from_xml = Data(name,age, birth_date, lenguages)
print(data_from_xml.__dict__) # de esta manera lo imprime en formato diccionario


with open(json_path, "r") as json_data:
  data = json.load(json_data) # importante tener en cuenta que de esta manera si imprime un dict
  data_from_json = Data(
    data["name"], 
    data["age"], 
    data["birth_date"],
    data["lenguages"]
    )
  
  print(data_from_json.__dict__)

os.remove(json_path)
os.remove(xml_file)

'''
  Para este ejercicio creamos el archivo.xml y el archivo.json
  luego creamos una clase con la estructura del json o el xml
  
      class Data:
      def __init__(self, name: str, age: int,birth_date: str, lenguages: list):
        self.name = name
        self.age = age
        self.birth_date = birth_date
        self.lenguages = lenguages
    
  luego abrimos el archivo en modo lectura y lo leemos
  ya en este punto podemos crear las variables con los datos que se ajustan a la estructura
  y luego creamos el objeto con la clase Data()

  al momento de imprimir el objeto print(data_from_xml.__dict__)
  usamos data_from_xml.__dict__ para imprimir en formato diccionario

  para trabajar con json es mas facil y rapido que con un archivo xml ya que su lectura es mucho mas simple 
  y requiere menos pasos para acceder a su imformacion
  con el simple hecho de abrir el documento en modo lectura y dale estructura con el metodo json.load()
  podemos conseguir leer los datos
  posteriormente podemos crear directamente la clase sin pasos añadidos en la clase
'''