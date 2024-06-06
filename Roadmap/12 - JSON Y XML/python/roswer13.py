"""
IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.

EJERCICIO:
Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los
siguientes datos (haciendo uso de la sintaxis correcta en cada caso):
- Nombre
- Edad
- Fecha de nacimiento
- Listado de lenguajes de programación
Muestra el contenido de los archivos.
Borra los archivos.

DIFICULTAD EXTRA (opcional):
Utilizando la lógica de creación de los archivos anteriores, crea un
programa capaz de leer y transformar en una misma clase custom de tu 
lenguaje los datos almacenados en el XML y el JSON.
Borra los archivos.
"""
from abc import ABC, abstractmethod

file_name = "roswer13.txt"

class Transformation(ABC):
    @abstractmethod
    def generate(self) -> str:
        pass

class XML(Transformation):
    def __init__(self, data: dict):
        self.data = data

    def generate(self) -> str:
        xml = "<data>\n"
        for key, value in self.data.items():
            xml += f"\t<{key}>{value}</{key}>\n"
        xml += "</data>"
        return xml
    
class JSON(Transformation):
    def __init__(self, data: dict):
        self.data = data

    def generate(self) -> str:
        import json
        return json.dumps(self.data)
    
class FileOperation:
    def __init__(self, file_name: str):
        self.file_name = file_name

    def write(self, data: Transformation):
        with open(self.file_name, "w") as file:
            file.write(data.generate())

    def read(self):
        with open(self.file_name, "r") as file:
            print(file.read())

    def delete(self):
        import os
        os.remove(self.file_name)

if __name__ == "__main__":
    try:
        name = input("Nombre: ")
        age = int(input("Edad: "))
        birth_date = input("Fecha de nacimiento: ")
        languages = input("Listado de lenguajes de programación: ").split(",")
        data = {
            "name": name,
            "age": age,
            "birth_date": birth_date,
            "languages": languages
        }
        print("-" * 50)
        # Write and read XML file.
        xml = XML(data=data)
        file = FileOperation(file_name=f"{file_name}.xml")
        file.write(data=xml)
        file.read()
        file.delete()
        print("-" * 50)
        # Write and read JSON file.
        json = JSON(data=data)
        file = FileOperation(file_name=f"{file_name}.json")
        file.write(data=json)
        file.read()
        file.delete()
        print("-" * 50)
    except ValueError:
        print("Error al ingresar la información.")