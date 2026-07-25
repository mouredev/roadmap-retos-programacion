"#[número] - [lenguaje_utilizado]"
# 
# IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
# 
# EJERCICIO:
# Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los
# siguientes datos (haciendo uso de la sintaxis correcta en cada caso):
# - Nombre
# - Edad
# - Fecha de nacimiento
# - Listado de lenguajes de programación
# Muestra el contenido de los archivos.
# Borra los archivos.
# 
# DIFICULTAD EXTRA (opcional):
# Utilizando la lógica de creación de los archivos anteriores, crea un
# programa capaz de leer y transformar en una misma clase custom de tu 
# lenguaje los datos almacenados en el XML y el JSON.
# Borra los archivos.
# 

import os
from random import randint
from random import choice
from datetime import date
from datetime import datetime

def serparacion(cadena):
    print('{}'.format(cadena * 20))

import json as jsonlib
import xml.etree.ElementTree as xmllib

lenguajes_programacion = [
    "Python",
    "JavaScript",
    "Java",
    "C#",
    "C++",
    "C",
    "TypeScript",
    "Ruby",
    "PHP",
    "Swift",
    "Kotlin",
    "Go",
    "Rust",
    "SQL",
    "Perl",
    "Scala",
    "Lua",
    "R",
    "Dart",
    "Haskell"
]

personajes_clasicos = [
    # Looney Tunes / Merrie Melodies
    "Bugs Bunny",
    "Pato Lucas",
    "Porky",
    "Silvestre",
    "Piolín",
    "Correcaminos",
    "Wile E. Coyote",
    "Sam Bigotes",
    "Elmer Gruñón",
    
    # Hanna-Barbera
    "Pedro Picapiedra",
    "Pablo Mármol",
    "Scooby-Doo",
    "Shaggy Rogers",
    "Oso Yogui",
    "Bubu",
    "Don Gato",
    "Benito Bodoque",
    "Tiro Loco McGraw",
    "Supersónico", # (George Jetson)
    
    # MGM / Fleischer / Varios
    "Tom",
    "Jerry",
    "Popeye",
    "Olivia Olivo",
    "Brutus",
    "La Pantera Rosa",
    "Pájaro Loco", # (Woody Woodpecker)
    "Félix el Gato",
    
    # Disney (Clásicos)
    "Mickey Mouse",
    "Pato Donald",
    "Goofy"
]


class Persona:

    def __init__(self, name: str, program_lenguages: list, birth_date=None, age=None):
        self.name = name
        self.program_lenguages = program_lenguages
        self.birth_date = birth_date
        self.age = age
        if self.birth_date == None or self.age == None: self.create_date()

    def __str__(self) -> str:
        return f'Nombre: {self.name}, Birth: {self.date_spain()}, Age: {self.age}, Program lenguages: {self.program_lenguages}'

    def date_spain(self) -> str:
        return f'{self.birth_date.day:02}/{self.birth_date.month:02}/{self.birth_date.year:04}'

    def create_date(self) -> tuple[date, int]:
        self.syear = randint(1900, 2025)
        self.smonth = randint(1, 12)
        if self.smonth == 2 and self.syear % 4 == 0:
            self.sday = randint(1, 29)
        elif self.smonth == 2:
            self.sday = randint(1, 28)
        elif self.smonth in [1, 3, 5, 7, 8, 10, 12]:
            self.sday = randint(1, 31)
        elif self.smonth in [4, 6, 9, 11]:
            self.sday = randint(1, 30)
        self.birth_date = date(self.syear, self.smonth, self.sday)
        self.age = (2025 - self.syear)

def create_json_xml():
    students = []
    for indxstu in range(randint(7,20)):
        lenguage = []
        for indxlg in range(randint(1,5)):
            while True:
                lg = choice(lenguajes_programacion)
                if lg not in lenguage:
                    lenguage.append(lg)
                    break
        namecho = choice(personajes_clasicos)
        personajes_clasicos.remove(namecho)
        students.append(Persona(namecho, lenguage))

    with open("barrancus.json", mode="w", encoding="utf-8") as write_file:
        write_file.write('[\n')
        counter = 0
        for student in students:
            counter += 1
            x = {
                "Nombre": student.name,
                "Edad": student.age,
                "Nacimiento": student.date_spain(),
                "Lenguajes": student.program_lenguages
            }
            jsonlib.dump(x, write_file, indent=4)
            if counter != len(students): write_file.write(',\n')
        write_file.write('\n]')

    with open("barrancus.json", "r") as json_file:
        # loading json file data to variable data
        data = jsonlib.load(json_file)
        
    # Building the root element of the xml file
    root = xmllib.Element("Estudiantes")
    root.tag = "Estudiantes"
    root.text = '\n\t'
    countline = 0
    for line in data:
        countline += 1
        stud = xmllib.SubElement(root, "Estudiante")
        stud.text = '\n\t\t'
        if len(students) == countline:
            stud.tail = '\n'
        else:
            stud.tail = '\n\t'
        name = xmllib.SubElement(stud, "Nombre")
        name.text = f'{line["Nombre"]}'
        name.tail = '\n\t\t'
        age = xmllib.SubElement(stud, "Edad")
        age.text = str(line["Edad"])
        age.tail = '\n\t\t'
        birthday = xmllib.SubElement(stud, "Nacimiento")
        birthday.text = str(line["Nacimiento"])
        birthday.tail = '\n\t\t'
        lenguages = xmllib.SubElement(stud, "Lenguajes")
        lenguages.text = str(line["Lenguajes"])
        lenguages.tail = '\n\t'

    tree = xmllib.ElementTree(root)
    tree.write("barrancus.xml", encoding= "UTF-8", method= 'xml')

def obtaintopersona():
    personas_json = []
    with open("barrancus.json", "r") as json_file:
        # loading json file data to variable data
        data_json = jsonlib.load(json_file)

    for line in data_json:
        birth = datetime.strptime(line["Nacimiento"], "%d/%m/%Y")
        personas_json.append(Persona(str(line["Nombre"]), line["Lenguajes"], birth, line["Edad"]))

    for persona in personas_json:
        print(persona)

    serparacion('-----')
    personas_xml = []
    data_xml = xmllib.parse("barrancus.xml")
    root = data_xml.getroot()
    for child in root:
        estudent_xml=[subchild.text for subchild in child]
        personas_xml.append(Persona(
            estudent_xml[0],
            estudent_xml[3],
            datetime.strptime(estudent_xml[2], "%d/%m/%Y"),
            int(estudent_xml[1])
            )
        )
    for personita in personas_xml:
        print(personita)
        
def main():
    create_json_xml()
    obtaintopersona()
    os.remove("barrancus.json")
    os.remove("barrancus.xml")

main()
