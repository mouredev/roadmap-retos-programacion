import os, json
import xml.etree.cElementTree as ET
from xml.dom import minidom
from datetime import datetime as date
os.system('cls')
"""
 * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
 *
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los
 * siguientes datos (haciendo uso de la sintaxis correcta en cada caso):
 * - Nombre
 * - Edad
 * - Fecha de nacimiento
 * - Listado de lenguajes de programación
 * Muestra el contenido de los archivos.
 * Borra los archivos.
 *
"""

	
#ruta = r"C:\Users\jesus\Documents\Python3project\roadmap_python\#12\\"


nacimiento = 1975
edad = date.now().year - nacimiento

empresa = ET.Element("EMPRESA")

programador = ET.SubElement(empresa, "PROGRAMADOR")
ET.SubElement(programador, "NOMBRE").text = "Jesus"
ET.SubElement(programador, "LENGUAJES").text = "[Python, Java, PhP]"
ET.SubElement(programador, "NACIMIENTO").text = str(nacimiento)
ET.SubElement(programador, "EDAD").text = str(edad)
programador = ET.SubElement(empresa, "PROGRAMADOR")
ET.SubElement(programador, "NOMBRE").text = "Sandra"
ET.SubElement(programador, "LENGUAJES").text = "[Javascript, HTML, CSS]"
ET.SubElement(programador, "NACIMIENTO").text = "1991"
ET.SubElement(programador, "EDAD").text = str(date.now().year - 1991)

file = ET.ElementTree(empresa)
file.write("empresa.xml") #file.write(ruta + "empresa.xml") si queremos incluir la ruta

json_file = '''{
 "nombre": "Jesus",
 "fecha de nacimiento": "1975",
 "lenguages": ["python", "java", "php"] 
}
'''
#string

yo = json.loads(json_file)#Transforma un string con formato json en un objeto diccionario python
print(yo)
print(type(yo))#dict

python_dict = {
 "nombre": "Jesus",
 "fecha de nacimiento": "1975",
 "lenguajes": ["python", "java", "php"]
}#dict

yo = json.dumps(python_dict)#Transforma un objeto diccionario python en un string
print(yo)
print(type(yo))#str


"""
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la lógica de creación de los archivos anteriores, crea un
 * programa capaz de leer y transformar en una misma clase custom de tu 
 * lenguaje los datos almacenados en el XML y el JSON.
 * Borra los archivos.
"""

class Programador:
    def __init__(self):
      self.primary_list = []


    def create_file_json(self,filename:str):
        self.filename = filename
        self.file = self.filename+'.json'
        with open(self.file, 'w') as create_json:
           json.dump(self.file,create_json, indent=4, sort_keys=False)

    def create_file_xml(self,filename:str, rootname:str):
        self.filename = filename
        self.rootname = rootname
        self.file = self.filename+'.xml'
        root = ET.Element(rootname)
        tree = ET.ElementTree(root)
        tree.write(self.file)

    def create_dict(self, name:str, birth_year:int, languages:list)->dict:
        self.name = name
        self.birth_year = birth_year
        self.languages = languages
        dict = {"Name":self.name,
                "Birth_year":self.birth_year,
                "Age": date.now().year - self.birth_year, 
                "Languages": self.languages}
        return dict

    def add_dict_json(self,file:str,dict:dict):
        self.file = file
        self.dict = dict
        self.primary_list.append(self.dict)
        with open(self.file , 'w') as write_json:
            json.dump(self.primary_list, write_json , indent=4, sort_keys=False)
        

    def print_json_contain(self, file:str):
        with open(file) as contains:
            payload = json.load(contains)
        for element in  payload:
            print(element)

    def print_xml_contain(self,root:object):
        rough_string = ET.tostring(root, 'utf-8')
        reparsed = minidom.parseString(rough_string)
        print (reparsed.toprettyxml(indent="  ", newl="\n"))

    def add_dict_xml(self,subroot:str,file:str, python_dict:dict):
        self.python_dict = python_dict
        self.file = file
        self.subroot = subroot
        tree = ET.parse(file)
        root = tree.getroot()
        subroot = ET.SubElement(root,self.subroot)
        for key, value in self.python_dict.items():
            programador = ET.SubElement(subroot, key)
            if isinstance(value, list):
                for element in value:
                    ET.SubElement(programador, "language").text = element
            else:
                programador.text = str(value)
      
        tree.write(file)


programador = Programador()
programador.create_file_json('programadores')
programador.add_dict_json("programadores.json",programador.create_dict("Jesus", 1975, ["python", "java", "php"]))
programador.add_dict_json("programadores.json",programador.create_dict("Sandra", 1991, ["HTML", "CSS", "Javascript"]))
programador.add_dict_json("programadores.json",programador.create_dict("Pepe", 1980, ["C#", "C", "Assembly"]))
programador.add_dict_json("programadores.json",programador.create_dict("Brais", 1988, ["Swift", "Kotlin", "Python"]))
programador.print_json_contain("programadores.json")
print()


programador.create_file_xml("empresa", "EMPRESA")
programador.add_dict_xml("Programador","empresa.xml",programador.create_dict("Jesus", 1975, ["Java","Python","PhP"]))
programador.add_dict_xml("Programador","empresa.xml",programador.create_dict("Sandra", 1991, ["HTML", "CSS", "Javascript"]))
programador.add_dict_xml("Programador","empresa.xml",programador.create_dict("Pepe", 1980, ["C#", "C", "Assembly"]))
programador.add_dict_xml("Programador","empresa.xml",programador.create_dict("Brais", 1988, ["Swift", "Kotlin", "Python"]))
programador.print_xml_contain(ET.parse("empresa.xml").getroot())



