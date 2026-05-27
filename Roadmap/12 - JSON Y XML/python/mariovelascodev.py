import os,json,xml.etree.ElementTree as ET

def create_json():
    with open("json_file.json", "w+") as file:
        data = {
            "name": "Mario",
            "age": 36,
            "date_birth": "07/02/1990",
            "programming_languages": ["Python", "Java"]
        }

        #Crea el fichero json
        json.dump(data, file, indent = 2)

create_json()

#Lee el fichero
with open("json_file.json", "r") as file:
    for line in file.readlines():
        print(line)

#Borrar archivo
os.remove("json_file.json")

def create_xml(name, age, date_birth, *programming_languages):
    #Crea elemento raiz
    xml_file = ET.Element("desarrollador")

    #Crea subelementos
    eName = ET.SubElement(xml_file, "nombre")
    eAge = ET.SubElement(xml_file, "edad")
    eBirth = ET.SubElement(xml_file, "fecha_nacimiento")
    eLanguages = ET.SubElement(xml_file, "lenguajes_programacion")

    #Añadir datos
    eName.text = str(name)
    eAge.text = str(age)
    eBirth.text = str(date_birth)

    #Al ser una lista, creamos el subelemento al añadirle datos
    for language in programming_languages:
        languages = ET.SubElement(eLanguages, "lenguajes")
        languages.text = str(language)

    #Definir elemento raiz
    eRoot = ET.ElementTree(xml_file)

    #Escribir fichero xml
    eRoot.write("desarrollador.xml",encoding='utf-8',xml_declaration=True)

create_xml("Mario", 36, "07/02/1990", "Python", "Java")

#Leer contenido
with open("desarrollador.xml", "r") as file:
    print(file.read())

#Borrar archivo
os.remove("desarrollador.xml")


#Extra

create_xml("Mario", 36, "07/02/1990", "Python", "Java")
create_json()

class UserData:
    
    def __init__(self, name, age, birth_date, programming_languages) -> None:
            self.name = name
            self.age = age
            self.birth_date = birth_date
            self.programming_languages = programming_languages

with open("json_file.json", "r") as json_data:
    #Convertimos el fichero json en un diccionario
    json_dict = json.load(json_data)
    json_class = UserData(
        json_dict["name"],
        json_dict["age"],
        json_dict["date_birth"],
        json_dict["programming_languages"]
    )
    print(json_class.__dict__)

with open("desarrollador.xml", "r") as xml_data:
    #Convertimos el fichero xml en un string y buscamos las etiquetas creadas para asignar cada una a una variable
    root = ET.fromstring(xml_data.read())
    name = root.find("nombre").text
    age = root.find("edad").text
    birth_date = root.find("fecha_nacimiento").text
    programming_languages = []
    for item in root.find("lenguajes_programacion"):
        programming_languages.append(item.text)

    xml_class = UserData(name, age, birth_date, programming_languages)
    print(xml_class.__dict__)

os.remove("json_file.json")
os.remove("desarrollador.xml")
