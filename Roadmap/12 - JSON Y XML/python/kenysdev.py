# ╔═════════════════════════════════════╗
# ║ Autor:  Kenys Alvarado              ║
# ║ GitHub: https://github.com/Kenysdev ║
# ║ 2024 -  Python                      ║
# ╚═════════════════════════════════════╝

# -----------------------------------
# * JSON Y XML
# -----------------------------------
# - son formatos de intercambio de datos que estructuran información.
# - JSON (JavaScript Object Notation) y XML (eXtensible Markup Language)

import os
import ast
import json
import xml.dom.minidom

#____________________________________
# * JSON
dict_user = {
    "name": "Ken",
    "age": 121,
    "dob": "1903-03-19",
    "prog_langs": ["cs", "py", "vb", "rs", "js"]
}

# _______________
# Serialización: el proceso de convertir un objeto a una 
# cadena de caracteres en formato JSON.
json_user = json.dumps(dict_user)
# {"name": "Ken", "age": 121, "dob": "1903-03-19", ....}

# Con indentación.
json_user = json.dumps(dict_user, indent=4)

# Crear fichero
with open("user.json", 'w') as file:
    json.dump(dict_user, file, indent=4)

# _______________
# Deserialización: convertir una cadena de caracteres JSON a un objeto.
with open("user.json", 'r') as file:
    data = json.load(file)
print("Objeto cargado\n", data, "\n")

format_json = json.dumps(data, indent=4)
print("Objeto a formato json\n",format_json, "\n")

#____________________________________
# * XML

# Serialización
doc = xml.dom.minidom.Document()
root = doc.createElement("user")
doc.appendChild(root)

for key, value in dict_user.items():
    elem = doc.createElement(key)
    text = doc.createTextNode(str(value))
    elem.appendChild(text)
    root.appendChild(elem)

# Guardar
with open("user.xml", "w") as f:
    f.write(doc.toprettyxml())

# _______________
# cargar
with open("user.xml", "r") as f:
    xml_content = f.read()
    print("Cargar documento\n", xml_content, "\n")

# cargar un elemento especifico.
doc = xml.dom.minidom.parse("user.xml")
age_value = doc.getElementsByTagName("age")[0]
age = age_value.firstChild.data
print("Edad: ", age)

#____________________________________
# EJERCICIO
"""
 * Utilizando la lógica de creación de los archivos anteriores, crea un
 * programa capaz de leer y transformar en una misma clase custom de tu 
 * lenguaje los datos almacenados en el XML y el JSON.
 * Borra los archivos.
"""

class Xml_or_json:
    def __init__(self, path):
        file_name, file_extension = os.path.splitext(path)
        self.path = path
        self.extension = file_extension.lower()
        self.dic_user = {}

    def as_dict(self) -> list:
        try:
            if self.extension == ".json":
                with open(self.path, 'r') as file:
                    self.dic_user = json.load(file)
                    print("Archivo .json cargado")
                    return self.dic_user

            elif self.extension == ".xml":
                def _get_value(key: str) -> str:
                    doc = xml.dom.minidom.parse(self.path)
                    value = doc.getElementsByTagName(key)[0]
                    value_str = value.firstChild.data
                    return value_str

                self.dic_user["name"] = _get_value("name")
                self.dic_user["age"] = int(_get_value("age"))
                self.dic_user["dob"] = _get_value("dob")
                self.dic_user["prog_langs"] = ast.literal_eval(_get_value("prog_langs"))

                print("Archivo .xml cargado")
                return self.dic_user
                
            else:
                print("Archivo no compatible.")

        except Exception as ex:
            print("Error -> ", ex)

print("\nEJERCICIO\n")
#__________
file = Xml_or_json("user.json")
dic_user: dict = file.as_dict()
print(dic_user)
#__________
file = Xml_or_json("user.xml")
dic_user: dict = file.as_dict()
print(dic_user)

# eliminar
os.remove("user.xml")
os.remove("user.json")
