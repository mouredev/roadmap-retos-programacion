# 12 JSON Y XML
# Monica Vaquerano
# https://monicavaquerano.dev

# IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
"""
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
# --------------------------------
# XML (Extensible Markup Language)
# --------------------------------
# XML es un lenguaje de marcado que se utiliza para almacenar y transportar datos de forma legible tanto por humanos como por máquinas.
# Utiliza etiquetas para definir la estructura y el significado de los datos.
# En Python se puede trabajar con XML utilizando la biblioteca xml.etree.ElementTree.

# --------------------
# Crear un archivo XML:
# --------------------

import os, xml.etree.ElementTree as ET

# Crear el elemento raíz
root = ET.Element("data")

# Añadir subelementos
child1 = ET.SubElement(root, "item")
child1.text = "Contenido del item 1"

child2 = ET.SubElement(root, "item")
child2.text = "Contenido del item 2"

# Crear el árbol XML
tree = ET.ElementTree(root)

# Guardar el árbol en un archivo
tree.write("archivo.xml")

# --------------------
# Leer un archivo XML:
# --------------------

# Parsear el archivo XML
tree = ET.parse("archivo.xml")

# Obtener el elemento raíz
root = tree.getroot()

# Iterar sobre los elementos
for child in root:
    print(child.tag, child.text)

# ----------------------
# Editar un archivo XML:
# ----------------------

# Parsear el archivo XML
tree = ET.parse("archivo.xml")

# Obtener el elemento raíz
root = tree.getroot()

# Editar un elemento existente
root[0].text = "Nuevo contenido del item 1"

# Guardar los cambios
tree.write("archivo.xml")

# ----------------------
# Editar un archivo XML:
# ----------------------

# Eliminar el archivo
os.remove("archivo.xml")

# ---------------------------------
# JSON (JavaScript Object Notation)
# ---------------------------------
# JSON es un formato de intercambio de datos ligero y fácil de leer que se utiliza ampliamente para transmitir datos estructurados entre un servidor y un cliente.
# En Python se puede trabajar con JSON utilizando el módulo json.

# ----------------------
# Crear un archivo JSON:
# ----------------------
import json

# Datos en forma de diccionario
data = {"nombre": "Juan", "edad": 30, "ciudad": "Berlin"}

# Guardar los datos en un archivo JSON
with open("archivo.json", "w") as f:
    json.dump(data, f)

# ----------------------
# Leer un archivo JSON:
# ----------------------

# Leer datos desde un archivo JSON
with open("archivo.json", "r") as f:
    data = json.load(f)

# Imprimir los datos
print(data)

# ----------------------
# Editar un archivo JSON:
# ----------------------

# Leer datos desde un archivo JSON
with open("archivo.json", "r") as f:
    data = json.load(f)

# Modificar los datos
data["ciudad"] = "Stuttgart"

# Guardar los cambios
with open("archivo.json", "w") as f:
    json.dump(data, f)

# -------------------------
# Formatear los resultados:
# -------------------------
# El método json.dumps() tiene parametros que facilitan la lectura de los resultados.

# Aquí usa 4 espacios de indentación para facilitar la lectura:
print("json.dumps(json.dumps(data, indent=4)) =>")
print(json.dumps(data, indent=4))

# Aquí . y espacio para separar los objetos, y un espacio, un = y un espacio para separar las keys de sus valores.
# Además de ordenar en orden alfabético las llaves:
print("json.dumps(data, indent=4, separators=('. ', ' = ')) =>")
print(json.dumps(data, indent=4, separators=(". ", " = "), sort_keys=True))

# -------------------------
# Eliminar un archivo JSON:
# -------------------------

# Eliminar el archivo
os.remove("archivo.json")

# Es importante manejar adecuadamente los errores y excepciones al trabajar con archivos para garantizar un comportamiento robusto de tu aplicación.
# -------------------------


def create_XML(name, age, dob, languages_list):
    # Create root element
    root = ET.Element("info")

    # Add subelements
    name_se = ET.SubElement(root, "name")
    name_se.text = name

    age_se = ET.SubElement(root, "age")
    age_se.text = age

    dob_se = ET.SubElement(root, "date_of_birth")
    dob_se.text = dob

    languages_list_se = ET.SubElement(root, "programming_languages_list")
    languages_list_se.text = languages_list

    # Create the XML tree
    tree = ET.ElementTree(root)

    # Save the tree in a file
    tree.write("info.xml")


def create_JSON(name, age, dob, languages_list):
    info = {
        "name": name,
        "age": age,
        "date of birth": dob,
        "programming languages list": languages_list,
    }

    # Saves the data in a JSON file
    with open("info.json", "w") as f:
        json.dump(info, f)


def read_XML(file):
    # Parse the XML file
    tree = ET.parse(file)

    # Get root element
    root = tree.getroot()

    # Iterate over the elements
    for child in root:
        print(child.tag, "=", child.text)


def read_JSON(file):
    # Reads the data from a JSON file
    with open(file, "r") as f:
        data = json.load(f)

    # Print the data
    print(json.dumps(data, indent=4))


def eliminate_files(files):
    for file in files:
        try:
            # Eliminates any file
            os.remove(file)
        except FileNotFoundError:
            print(f"Archivo '{file}' no existe")


"""
* DIFICULTAD EXTRA (opcional):
* Utilizando la lógica de creación de los archivos anteriores, crea un
* programa capaz de leer y transformar en una misma clase custom de tu 
* lenguaje los datos almacenados en el XML y el JSON.
* Borra los archivos.
"""


class FileCreator:
    def __init__(self, fname, ext):
        self.fname = fname
        self.ext = "." + ext
        self.file = f"{self.fname}{self.ext}"

    def input_info(self, name, age, dob, languages_list):
        self.name, self.age, self.dob, self.languages_list = (
            name,
            age,
            dob,
            languages_list,
        )
        if self.ext == ".json":
            info = {
                "name": name,
                "age": age,
                "date of birth": dob,
                "programming languages list": languages_list,
            }
            # Saves the data in a JSON file
            with open(self.file, "w") as f:
                json.dump(info, f)
        elif self.ext == ".xml":
            # Create root element
            root = ET.Element("info")
            # Add subelements
            name_se = ET.SubElement(root, "name")
            name_se.text = self.name
            age_se = ET.SubElement(root, "age")
            age_se.text = str(self.age)
            dob_se = ET.SubElement(root, "date_of_birth")
            dob_se.text = self.dob
            languages_list_se = ET.SubElement(root, "programming_languages_list")
            languages_list_se.text = self.languages_list
            # Create the XML tree
            tree = ET.ElementTree(root)
            # Save the tree in a file
            tree.write(self.file)
        else:
            print("Archivo no compatible")

    def edit_info(self, key, new_value):
        if self.ext == ".json":
            try:
                # Leer datos desde un archivo JSON
                with open(self.file, "r") as f:
                    data = json.load(f)
                # Modificar los datos
                data[key] = new_value
                # Guardar los cambios
                with open(self.file, "w") as f:
                    json.dump(data, f)
            except FileNotFoundError as e:
                print(e)
            except Exception as e:
                print(e)
        elif self.ext == ".xml":
            try:
                # Parse XML file
                tree = ET.parse(self.file)
                # Get root element
                root = tree.getroot()
                # Get key
                for child in root:
                    if child.tag == key:
                        # Edit an existin element
                        child.text = new_value
                        break
                # Guardar los cambios
                tree.write(self.file)
            except FileNotFoundError as e:
                print(e)
            except Exception as e:
                print(e)
        else:
            print("Archivo no compatible")

    def print_file(self):
        if self.ext == ".json":
            try:
                # Reads the data from a JSON file
                with open(self.file, "r") as f:
                    data = json.load(f)
                # Print the data
                print(json.dumps(data, indent=4))
            except FileNotFoundError as e:
                print(e)
        elif self.ext == ".xml":
            try:
                # Parse the XML file
                tree = ET.parse(self.file)
                # Get root element
                root = tree.getroot()
                # Iterate over the elements
                for child in root:
                    print(child.tag, "=", child.text)
            except FileNotFoundError as e:
                print(e)
        else:
            print("Este archivo no es compatible")

    def __str__(self) -> str:
        return self.file


while True:
    print("\n--- Ejercicios ---")
    choice = input("1. Ejercicio\n2. DIFICULTAD EXTRA (opcional)\n3. Salir\n> ")
    if choice == "1":
        os.system("clear")
        print("--- Creación de un archivo XML y JSON ---")
        # Prompt info
        name = input("Ingresa tu nombre: > ").lower().strip()
        age = input("Ingresa tu edad: > ")
        dob = input("Ingresa tu fecha de nacimiento: > ")
        languages_list = input("Ingresa tus lenguajes de programación preferidos: > ")
        # Create files
        create_XML(name, age, dob, languages_list)
        create_JSON(name, age, dob, list(languages_list.split(", ")))
        # Read files
        try:
            print("\nXML File:")
            read_XML("info.xml")
            print("\nJSON File:")
            read_JSON("info.json")
            # Eliminate files
            eliminate_files(["info.xml", "info.json"])
        except FileNotFoundError as e:
            print(f"El archivo no existe: {e}")
        except Exception as e:
            print(f"Ha ocurrido un error: {e}")

    elif choice == "2":
        os.system("clear")
        soyJSON = FileCreator("soyJSON", "json")
        soyJSON.input_info("Alice", 88, "10/10/88", "python, javascript, php")
        print(soyJSON)
        print("\nJSON File:")
        soyJSON.print_file()
        soyJSON.edit_info("name", "Bob")
        print("\nJSON File:")
        soyJSON.print_file()

        soyXML = FileCreator("soyXML", "xml")
        soyXML.input_info("Charlie", 88, "10/10/88", "python, javascript, php")
        print(soyXML)
        print("\nXML File:")
        soyXML.print_file()
        soyXML.edit_info("name", "Dan")
        print("\nXML File:")
        soyXML.print_file()

        eliminate_files(["soyJSON.json", "soyXML.xml"])
    elif choice == "3":
        print("\nAdiós")
        break
