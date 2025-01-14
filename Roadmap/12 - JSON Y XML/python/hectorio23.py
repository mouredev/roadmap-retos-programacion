# Autor: Héctor Adán
# GitHub: https://github.com/hectorio23

import json
import os
import xml.etree.ElementTree as ET

# Función para crear un archivo XML con los datos proporcionados
def create_xml(name, age, dob, languages):
    root = ET.Element("Person")
    ET.SubElement(root, "Name").text = name
    ET.SubElement(root, "Age").text = str(age)
    ET.SubElement(root, "DateOfBirth").text = dob
    lang_list = ET.SubElement(root, "ProgrammingLanguages")
    for lang in languages:
        ET.SubElement(lang_list, "Language").text = lang

    tree = ET.ElementTree(root)
    tree.write("./Person.xml")

# Función para crear un archivo JSON con los datos proporcionados
def create_json(name, age, dob, languages):
    data = {
        "Name": name,
        "Age": age,
        "DateOfBirth": dob,
        "ProgrammingLanguages": languages
    }
    with open("./Person.json", 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Función para mostrar el contenido de un archivo
def display_file_contents(filename):
    try:
        with open(filename, 'r') as file:
            print(f"Contents of {filename}:")
            print(file.read())
    except FileNotFoundError:
        print(f"File not found: {filename}")

# Función para borrar los archivos generados
def delete_files():
    try:
        os.remove("./Person.xml")
        os.remove("./Person.json")
    except FileNotFoundError:
        pass

def main():
    name = "Héctor Adán"
    age = 19
    dob = "2004-06-28"
    languages = ["C++", "Python", "JavaScript"]

    # Crear archivos XML y JSON con los datos proporcionados
    create_xml(name, age, dob, languages)
    create_json(name, age, dob, languages)

    # Mostrar el contenido de los archivos creados
    display_file_contents("./Person.xml")
    display_file_contents("./Person.json")

    # Borrar los archivos generados
    delete_files()

if __name__ == "__main__":
    main()
