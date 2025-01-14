import xml.etree.ElementTree as xml
import json
import os

datos = {
    "nombre" : "Andres",
    "edad" : 21,
    "nacimiento" : "16-02-2002",
    "lista_programas" : ["python", "javascript", "appscript"]
}

name_archivo = "datos.xml"
name_archivo2 = "datos.json"

def save_xml():

    root = xml.Element("datos")

    for key, value in datos.items():
       
         child = xml.SubElement(root, key)

         if isinstance(value, list):
          for item in value:
             xml.SubElement(child,"programa").text = item
         else:
          child.text = str(value)

    tree = xml.ElementTree(root)
    tree.write(name_archivo)

   
save_xml()    

with open(name_archivo, "r") as xml_print:
   print(xml_print.read())

#os.remove(name_archivo)

#JSON 

def save_json():
   with open(name_archivo2, "w") as json_data:
    json.dump(datos, json_data)

save_json()

with open(name_archivo2, "r") as json_data:   
   print(json_data.read())

#os.remove(name_archivo2)


class datos:
   
   def __init__(self, nombre, edad, nacimiento, lista_programas) -> None:
      self.nombre = nombre
      self.edad = edad
      self.nacimiento = nacimiento
      self.lista_programas = lista_programas 


with open(name_archivo, "r") as xml_print:

  root = xml.fromstring(xml_print.read())  
  nombre = root.find("nombre").text
  edad = root.find("edad").text
  nacimiento = root.find("nacimiento").text
  lista_programas = []
  for item in root.find("lista_programas"):
     lista_programas.append(item.text)




  datos_class_xml = datos(nombre, edad, nacimiento, lista_programas) 
  print(datos_class_xml.__dict__)



  with open (name_archivo2, "r") as json_data:
     json_dict = json.load(json_data)
     json_class = datos(json_dict["nombre"],json_dict["edad"],json_dict["nacimiento"],json_dict["lista_programas"])
     print(json_class.__dict__)

   
  os.remove(name_archivo)
  os.remove(name_archivo2)

