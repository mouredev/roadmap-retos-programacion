import json
import os
import xml.etree.ElementTree as ET

# json extension

dct = {
    "firstname": "Duban",
    "lastname": "Quiroga",
    "country": "Colombia",
    "skills": [
        "Python", "Java"
    ]
}

def file_creates_and_read(path:str, dct:dict) -> str:
    
    with open("./jsonfile.json", "w") as file:
        json.dump(dct, file, indent=4)
        

    #with open("./jsonfile.json") as file:
    #    content = json.load(file)
    #os.remove(path)
    #return json.dumps(content, indent=4)
    

print(file_creates_and_read("jsonfile.json", dct))

# XML extension

def create_file():
    # Crear el elemento raiz
    root = ET.Element("person")

    # Añadir subelementos
    firstname = ET.SubElement(root, "firstname")
    firstname.text = "Duban"

    lastname = ET.SubElement(root, "lastname")
    lastname.text = "Quiroga"

    country = ET.SubElement(root, "country")
    country.text = "Colombia"

    # Se crea un subelemento para los skills con una lista de lenguajes
    skills = ET.SubElement(root, "skills")
    skill1 = ET.SubElement(skills, "skill")
    skill1.text = "Python"
    skill2 = ET.SubElement(skills, "skill")
    skill2.text = "Java"

    # Se guarda el archivo
    tree = ET.ElementTree(root)
    with open("person.xml", "wb") as f:
        tree.write(f)

def show_content():
    #Mostrar el contenido del archivo
    print("-" * 5, "Contenido del archivo XML", "-" * 5)
    tree = ET.parse("person.xml")
    root = tree.getroot()
    for element in root:
        if element.tag == "skills":
            print("Skills: ", [skill.text for skill in element])
        else:
            print(f"{element.tag.capitalize()}: {element.text}")

def remove_file():
    # Eliminar archivo
    if os.path.exists("person.xml"):
        os.remove("person.xml")
    else:
        print("El archivo no existe")


""" Extra """

create_file()


class Custom:

    def __init__(self, fname, lname, country, skills):
        self.fname = fname
        self.lname = lname
        self.country = country
        self.skills = skills

file_name = "jsonfile.json"
xml_file = "person.xml"

with open(file_name) as file:
    content = file.read()
    data_json = json.loads(content)
    person_json = Custom(data_json["firstname"], data_json["lastname"], data_json["country"], data_json["skills"])


print(person_json.__dict__)

with open(xml_file, "r") as file:
    data = file.read()
    root = ET.fromstring(data)
    fname = root.find("firstname").text
    lname = root.find("lastname").text
    country = root.find("country").text
    skills = []
    for skill in root.find("skills"):
        skills.append(skill.text)

    person_xml = Custom(fname, lname, country, skills)
    print(person_xml.__dict__) # Datos en formato diccionario

os.remove(file_name)
os.remove(xml_file)