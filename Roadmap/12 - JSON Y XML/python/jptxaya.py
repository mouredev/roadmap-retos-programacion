#JSON AND XML

#Creacion de fichero XML

datos = {"nombre": "jptxaya",
         "edad": "45",
         "fecha_nacimiento": "19/03/1979",
         "lenguajes": ["python","java","react"]}

#XML

#Creacion de fichero XML
import xml.etree.ElementTree as gfg
import os
import json


try:
    root = gfg.Element("Datos")
    for key,value in datos.items():
        elem = gfg.SubElement(root,key)
        if isinstance(value,list):
            i = 0
            for value_list in value:
                lang = gfg.SubElement(elem,"lenguaje_" + str(i))
                lang.text = value_list
                i += 1
        else:
           elem.text = value
    tree = gfg.ElementTree(root)
    tree.write("newxml.xml", encoding="UTF-8", xml_declaration=True)


# Read from XML file
    with open("newxml.xml", "r") as xml_read:
        root = gfg.fromstring(xml_read.read())
        nombre = root.find("nombre").text
        edad = root.find("edad").text
        birth = root.find("fecha_nacimiento").text
        lenguajes = []
        for language in root.find("lenguajes"):
            lenguajes.append(language.text)

        print(f"Nombre: {nombre} Edad:{edad} Fecha Nac:{birth}")
        print("Lenguajes:")
        for leng in lenguajes:
            print(leng)

#Borrado fichero xml
#    os.remove("newxml.xml")

except Exception as exc:
    print(f"Exception {exc}")

#JSON

try:
#Creacion de Fichero json
    json_object = json.dumps(datos,indent=4)
    with open("newjson.json","w") as new_json:
        new_json.write(json_object)

#Read File json
    with open("newjson.json","r") as new_json:
        json_string = new_json.read()
        json_object = json.loads(json_string)

        
        nombre = json_object["nombre"]
        edad = json_object["edad"]
        birth = json_object["fecha_nacimiento"]
        lenguajes = []
        for language in json_object["lenguajes"]:
            lenguajes.append(language)

        print(f"Nombre: {nombre} Edad:{edad} Fecha Nac:{birth}")
        print("Lenguajes:")
        for leng in lenguajes:
            print(leng)

#Borrado fichero json
#    os.remove("newjson.json") 
        
except Exception as exc:
    print(f"Exception {exc}")


#Dificultad Extra

print ("#######Dificultad extra")

class Persona:

    def __init__(self,file) -> None:
        datos = self.read_file(file)
        self.name = datos["name"]
        self.age = datos["age"]
        self.birth = datos["birth"]
        self.languages = datos["languages"]


    def read_file(self, file):
        datos = {}
        if file.endswith(".xml"):
           with open(file, "r") as xml_read:
            root = gfg.fromstring(xml_read.read())
            nombre = root.find("nombre").text
            edad = root.find("edad").text
            birth = root.find("fecha_nacimiento").text
            lenguajes = []
            for language in root.find("lenguajes"):
                lenguajes.append(language.text)
            datos  = {"name": nombre, "age": edad, "birth": birth, "languages": lenguajes}

        else:
             with open(file,"r") as new_json:
                json_string = new_json.read()
                json_object = json.loads(json_string)
                datos  = {"name": json_object["nombre"], "age": json_object["edad"], "birth": json_object["fecha_nacimiento"], "languages": json_object["lenguajes"]}
        return datos
    
    def __str__(self) -> str:
        part1 = "Nombre:" + self.name + " Edad:" + self.age + " Fecha Nacimiento:" + self.birth + "\n" + "Lenguages"
        part2 = ""
        for leng in self.languages:
            part2 = part2 + "," + leng 
        return part1 + part2

try:
    print("File xml")
    person1 = Persona("newxml.xml")
    print(str(person1))
    print("File json")
    person2 = Persona("newjson.json")
    print(str(person2))
except Exception as ex:
    print("File not support or  format not correct")

os.remove("newxml.xml")
os.remove("newjson.json")


