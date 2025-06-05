import os
import xml.etree.ElementTree as xml
import json
# /*
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
#  */


data = {
    'name' : 'rayn1er',
    'age' : 26,
    'birth_date' : '05-04-1999',
    'programming_languages' : ['python','javascript']
}
#creando xml 

def save_xml():

    root = xml.Element('data')
    
    for key,value in data.items():
        
        child = xml.SubElement(root,key)
        if isinstance(value,list):
            for item in value:
                xml.SubElement(child,'item').text = item
        else:
            child.text = str(value)

    tree = xml.ElementTree(root)
    tree.write("rayn1er.xml")

save_xml()

with open('rayn1er.xml','r') as xml_data:
    print(xml_data.read())

# os.remove('rayn1er.xml')

#Json

def save_json():
    with open('rayn1er.json','w') as json_data:
        json.dump(data, json_data)

save_json()

with open('rayn1er.json','r') as json_data:
    print(json_data.read())

# os.remove('rayn1er.json')

#extra 

class Data:

    def __init__(self,name,age,birthday,languages):
        self.name = name
        self.age = age
        self.birthday = birthday
        self.languages = languages


with open('rayn1er.xml','r') as xml_data:
    
    root = xml.fromstring(xml_data.read())
    name = root.find('name').text
    age = root.find('age').text
    birthday = root.find('birth_date').text
    programming_languages = []
    for item in root.find("programming_languages"):
        programming_languages.append(item.text)
        
    xml_class = Data(name,age,birthday,programming_languages)
    print(xml_class.__dict__)


with open('rayn1er.json','r') as json_data:

    json_dict = json.load(json_data)
    json_class = Data(json_dict['name'],json_dict['age'],json_dict['birth_date'],json_dict['programming_languages'])
    print(json_class.__dict__)

os.remove('rayn1er.xml')
os.remove("rayn1er.json")