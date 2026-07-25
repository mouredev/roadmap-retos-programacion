'''
IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
 
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los
   siguientes datos (haciendo uso de la sintaxis correcta en cada caso):
   - Nombre
   - Edad
   - Fecha de nacimiento
   - Listado de lenguajes de programación
 * Muestra el contenido de los archivos.
 * Borra los archivos.
  
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la lógica de creación de los archivos anteriores, crea un
   programa capaz de leer y transformar en una misma clase custom de tu 
 * lenguaje los datos almacenados en el XML y el JSON.
 * Borra los archivos.
'''

import xml.etree.ElementTree as ET
import xml.dom.minidom
import json
import os

# 📌 Datos de ejemplo
data = {
    "name": "Jesús García",
    "age": 41,
    "birth_date": "1984-03-25",
    "programming_languages": ["Python", "JavaScript", "Java"]
}

# 🗂️ Archivos
xml_file = "jesusgdev.xml"
json_file = "jesusgdev.json"

# 🛠️ Crear XML
def create_xml():
    root = ET.Element("data")
    for key, value in data.items():
        child = ET.SubElement(root, key)
        if isinstance(value, list):
            for item in value:
                ET.SubElement(child, "item").text = item
        else:
            child.text = str(value)

    raw_xml = ET.tostring(root, encoding="utf-8")
    pretty_xml = xml.dom.minidom.parseString(raw_xml).toprettyxml(indent="  ")

    with open(xml_file, "w", encoding="utf-8") as f:
        f.write(pretty_xml)
        print(f"✅ Archivo XML creado: {xml_file}")

# 🛠️ Crear JSON
def create_json():
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"✅ Archivo JSON creado: {json_file}")

# 🧹 Borrar archivos
def delete_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
        print(f"🗑️ Archivo eliminado: {file_name}")
    else:
        print(f"⚠️ Archivo no encontrado: {file_name}")

# 🔽 Crear archivos
create_xml()
create_json()

# 📄 Mostrar contenido XML
print("\n📄 Contenido del archivo XML:\n")
with open(xml_file, "r", encoding="utf-8") as f:
    print(f.read())

# 📄 Mostrar contenido JSON
print("\n📄 Contenido del archivo JSON:\n")
with open(json_file, "r", encoding="utf-8") as f:
    print(f.read())

# 🧹 Eliminar archivos
print("\n🧹 Eliminando archivos...")
delete_file(xml_file)
delete_file(json_file)

# 🧪 Extra: Crear objetos desde XML y JSON (simulación)
print("\n🧪 Extra: Conversión a objetos en Python")

# 🧱 Clase contenedora
class Data:
    def __init__(self, name, age, birth_date, programming_languages):
        self.name = name
        self.age = age
        self.birth_date = birth_date
        self.programming_languages = programming_languages

# ✨ Recrear archivos temporalmente para la prueba
create_xml()
create_json()

# 📤 Leer XML y mostrar como texto XML
with open(xml_file, "r", encoding="utf-8") as f:
    xml_content = f.read()
    print("\n📤 Datos convertidos desde XML (formato XML):\n")
    print(xml_content)

# 📦 Convertir XML a objeto
root = ET.fromstring(xml_content)
name = root.find("name").text
age = root.find("age").text
birth_date = root.find("birth_date").text
languages = [item.text for item in root.find("programming_languages")]
xml_obj = Data(name, age, birth_date, languages)

# 📦 Leer JSON y convertir a objeto
with open(json_file, "r", encoding="utf-8") as f:
    json_dict = json.load(f)
    json_obj = Data(
        json_dict["name"],
        json_dict["age"],
        json_dict["birth_date"],
        json_dict["programming_languages"]
    )

# 📋 Imprimir contenido como diccionario
print("\n📤 Datos convertidos desde JSON (formato diccionario):")
print(json.dumps(json_obj.__dict__, indent=4, ensure_ascii=False))

# 🧹 Eliminar archivos
print("\n🧹 Eliminando archivos...")
delete_file(xml_file)
delete_file(json_file)










