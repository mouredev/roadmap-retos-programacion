
import json
from dataclasses import dataclass
import xml.etree.ElementTree as ET
import os

user= {
    "name" : "Tomas",
    "age" : 20,
    "date" : "19-07-2006",
    "lenguages" : ["c#", "Python"]
}


with open("user.json", "w") as archivo:
    json.dump(user, archivo, indent=4)

with open("user.json", "r") as archivo:
    contenido2 = json.load(archivo)

person = ET.Element("Persona")
name = ET.SubElement(person, "Nombre")
name.text = "Tomy"

age = ET.SubElement(person, "Edad")
age.text = "20"

date = ET.SubElement(person,"Fecha")
date.text = "19-07-2006"

lenguages = ET.SubElement(person, "lenguajes")
ET.SubElement(lenguages, "lenguaje").text = "Python"
ET.SubElement(lenguages, "lenguaje").text = "c#"

arbol = ET.ElementTree(person)
arbol.write("user.xml")

arbol = ET.parse("user.xml")
raiz = arbol.getroot()

# for element in raiz:
#     print(element.tag, element.text)


@dataclass
class Custom:
    name:str
    age : int
    date: str
    lenguage : list
    def print_info (self):
        print(f"Nombre: {self.name}| Edad: {self.age}| Fecha: {self.date}| Lenguajes: {self.lenguage}")
    

persona_json = Custom (
    name=contenido2["name"],
    age=contenido2["age"],
    date=contenido2["date"],
    lenguage=contenido2["lenguages"])

persona_json.print_info()

lista_lenguajes = [lang.text for lang in raiz.find("lenguajes")]

persona_xml = Custom(
    name=raiz.find("Nombre").text,
    age=int(raiz.find("Edad").text), 
    date=raiz.find("Fecha").text,
    lenguage=lista_lenguajes
)
persona_xml.print_info()

os.remove("user.json")
os.remove("user.xml")
            

