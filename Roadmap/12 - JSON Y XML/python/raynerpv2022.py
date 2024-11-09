import xml.etree.ElementTree as ET 
import os


# * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
#  * 
#  * EJERCICIO:
#  * Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los
#  * siguientes datos (haciendo uso de la sintaxis correcta en cada caso):
#  * - Nombre
#  * - Edad
#  * - Fecha de nacimiento
#  * - Listado de lenguajes de programación
#  * Muestra el contenido de los archivos.
#  * Borrarlo despues

# XML

print(" ****  XML ****")

personal_data = {
    "Nombre":"resba", 
    "Edad":"45",
    "Fcha ":"1.1.79"
    ,"Language":["Python"," go"]
}

root  = ET.Element("Personal Data")

for k,v in personal_data.items():

    item = ET.SubElement(root, k)
    if isinstance(v,list) :
        for i in v:
            l = ET.SubElement(item,"Language")
            l.text = i
    else:
        item.text = str(v)


tree = ET.ElementTree(root)
tree.write("file.xml")

with open("file.xml") as f:
    print(f.read())

# os.remove("file.xml")
 

print(" ****  JSON ****")
import json
personal_data = {"Nombre":"resba", "Edad":45,"Fcha ":"1.1.79","Language":"Python,go"}
with open("file.json","w") as f:
    json.dump(personal_data,f,ensure_ascii=False, indent=4)

with open("file.json", "r") as f:
    data = json.load(f)

print(data)
# os.remove("file.json")

# EXTRA 


# * DIFICULTAD EXTRA (opcional):
#  * Utilizando la lógica de creación de los archivos anteriores, crea un
#  * programa capaz de leer y transformar en una misma clase custom de tu 
#  * lenguaje los datos almacenados en el XML y el JSON.
#  * Borra los archivos.
# #  */

class DAta :
    def __init__(self, name, age, cumple, languaje,f) -> None:
        self.name = name
        self.age = age 
        self.cumple = cumple
        self.language = languaje
        self.modified = False
        self.file = f

    def read_json_data(self):
        with open(self.file,"r") as f:
            data = json.load(f)
         

        self.name = data["name"]
        self.age = str(int(data["age"])+1)
        self.cumple = data["cumple"]
        self.language = data["language"]
        self.modified= True
    
  

    def write_json(self):
        with open(self.file,"w") as f:
            json.dump(self.get_data_json(),f, ensure_ascii=False, indent=4)

    def get_data_json(self):
        return   {
            "name":self.name, 
            "age":self.age,
            "cumple": self.cumple,
            "language":self.language
            }
    
    def Print_data(self):
        if self.modified :
            print(f"{self.name} ha cumplido annos")
        print(self.get_data_json())

    def remove_file(self):
        os.remove(self.file)
    
     
        
    

print("Datos del PAciente")
print()
n= input("Nombre :")
e = input("Edad :")
fn = input("Fecha nacimiento :")
l = input("Languages (separados por espacio):")
l = l.split()
file = "satochi.json"
personal = DAta(n,e,fn,l, file)

personal.write_json()
personal.read_json_data()

personal.Print_data()
personal.remove_file()





    