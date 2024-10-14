from datetime import datetime as dt
import json
import os
import xml.etree.ElementTree as ET



datas = {
    "name": "Daniel",
    "age": 34,
    "birthdate": dt(1989, 4, 4).strftime("%d/%m/%Y"),
    "languages": ["python", "html", "sql"],
}

file = "datas.json"

# Escribir datos en el archivo
with open(file, "w") as f:
    json.dump(datas, f)

# Leer datos del archivo
with open(file, "r") as f:
    load = json.load(f)
    print(load)

# Cerrar el archivo antes de intentar eliminarlo
os.remove(file)



# Crear el elemento raíz del archivo XML
root = ET.Element("Informacion")

# Paso 2: Agregar datos al archivo XML
information = ET.SubElement(root, "Datos")
information.set("id", "1")
name = ET.SubElement(information, "nombre")
name.text = datas["name"]
age = ET.SubElement(information, "edad")
age.text = str(datas["age"])
birthday = ET.SubElement(information, "birthday")
birthday.text = str(datas["birthdate"])
languages = ET.SubElement(information, "lenguaje")
languages.text = str(datas["languages"])

# Guardar el árbol en un archivo XML
tree = ET.ElementTree(root)
tree.write("datas.xml")

# Paso 3: Leer los datos del archivo XML
tree = ET.parse("datas.xml")
root = tree.getroot()

for data in root:
    print("ID:", data.get("id"))
    print("Nombre:", data.find("nombre").text)
    print("Edad:", data.find("edad").text)
    print("Cumpleaño:", data.find("birthday").text)
    print("Lenguajes:", data.find("lenguaje").text)
    print()
    
# Paso 4: Borrar el archivo XML
os.remove("datas.xml")



###############################################################################
## DIFICULTAD EXTRA
###############################################################################
import json
import xml.etree.ElementTree as ET
import os

class Custom:
    def __init__(self, file) -> None:
        self.file = file

    def write_json(self, datas):
        with open(self.file, "w") as f:
            json.dump(datas, f, indent=4)

    def read_json(self):
        with open(self.file, "r") as f:
            load = json.load(f)
            print(load)

    def write_xml(self, datas):
        root = ET.Element("Informacion")
        information = ET.SubElement(root, "Datos")

        information.set("id", "1")
        name = ET.SubElement(information, "nombre")
        name.text = datas["name"]
        age = ET.SubElement(information, "edad")
        age.text = str(datas["edad"])
        birth_date = ET.SubElement(information, "fecha_nacimiento")
        birth_date.text = datas["fecha_nacimiento"]
        languages = ET.SubElement(information, "lenguajes")
        for lang in datas["lenguajes"]:
            ET.SubElement(languages, "lenguaje").text = lang

        tree = ET.ElementTree(root)
        tree.write(self.file)

    def read_xml(self):
        tree = ET.parse(self.file)
        root = tree.getroot()
        data = {
            "name": root.find("Datos/nombre").text,
            "edad": int(root.find("Datos/edad").text),
            "fecha_nacimiento": root.find("Datos/fecha_nacimiento").text,
            "lenguajes": [lang.text for lang in root.find("Datos/lenguajes")]
        }
        print(data)

    def delete_file(self):
        os.remove(self.file)
        print("\nArchivos borrados exitosamente.")

# Ejemplo de uso
datos = {
    "name": "Juan",
    "edad": 30,
    "fecha_nacimiento": "1994-05-20",
    "lenguajes": ["Python", "JavaScript", "Java"]
}

custom_instance = Custom("datos.xml")
custom_instance.write_xml(datos)
custom_instance.read_xml()
custom_instance.delete_file()

custom_instance = Custom("datos.json")
custom_instance.write_json(datos)
custom_instance.read_json()
custom_instance.delete_file()
