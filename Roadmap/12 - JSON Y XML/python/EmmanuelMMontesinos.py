"""
/*
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los
 * siguientes datos (haciendo uso de la sintaxis correcta en cada caso):
 * - Nombre
 * - Edad
 * - Fecha de nacimiento
 * - Listado de lenguajes de programación
 * Muestra el contenido de los archivos.
 * Borra los archivos.
 */
"""

# Ejercicio Base

# Super Clase Custom
class Custom:
    def delete(self,archivo_custom):
        os.remove(archivo_custom)


'''JSON'''

# Necesito el modulo os para borrar los archivos
import os
import json

class CustomJson(Custom):
    archivo_json = "emmanuelmmontesinos.json"
    def add_json(self,nombre,edad,fecha,lenguajes):
        datos = {
            "nombre":nombre,
            "edad":edad,
            "fecha":fecha,
            "lenguajes":lenguajes    
        }
        
        with open(CustomJson.archivo_json,"w") as archivo:
            json.dump(datos,archivo, indent= 4)
    
    def show(self):
        with open(CustomJson.archivo_json,"r") as archivo:
            print(json.load(archivo))
    
    def delete(self):
        return super().delete(CustomJson.archivo_json)
    

# Pruebas Json
prueba = CustomJson()
prueba.add_json("Emmanuel",33,"17/05/999",["Python","Bash"])
prueba.show()
prueba.delete()

'''XML'''

import xml.etree.ElementTree as ET

class CustomXml(Custom):
    archivo_xml = "emmanuelmmontesinos.xml"
    ficha = ET.Element("Ficha")
    ficha.text = "Ficha"
    def add_xml(self,nombre,edad,fecha,lenguajes):
        nombre_root = ET.SubElement(CustomXml.ficha,"nombre")
        nombre_root.text = nombre
        
        edad_root = ET.SubElement(CustomXml.ficha,"edad")
        edad_root.text = edad
        
        fecha_root = ET.SubElement(CustomXml.ficha,"fecha")
        fecha_root.text = fecha
        
        lenguajes_root = ET.SubElement(CustomXml.ficha,"lenguajes")
        lenguajes_root.text = ",".join(lenguajes)
        tree = ET.ElementTree(CustomXml.ficha)
        tree.write(file_or_filename=CustomXml.archivo_xml,encoding="utf-8",xml_declaration=True)
    def show_xml(self):
        ficha = ET.parse(CustomXml.archivo_xml)
        root = ficha.getroot()
        ET.dump(root)
    def delete(self):
        super().delete(CustomXml.archivo_xml)
        
prueba_xml = CustomXml()
prueba_xml.add_xml("emmanuel","33","17/05/999",["Python","Bash"])
prueba_xml.show_xml()
prueba_xml.delete()

# Ejercicio Extra

"""
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la lógica de creación de los archivos anteriores, crea un
 * programa capaz de leer y transformar en una misma clase custom de tu 
 * lenguaje los datos almacenados en el XML y el JSON.
 * Borra los archivos.
"""
class CustomClass:
    def __init__(self,archivo:str) -> None:
        self.archivo = archivo
        if archivo.endswith(".xml"):
            ficha = ET.parse(archivo)
            root = ficha.getroot()
            self.tipo = "XML"
            self.nombre = root.find('nombre').text
            self.edad = root.find('edad').text
            self.fecha = root.find('fecha').text
            lenguajes_elem = root.find('lenguajes')
            self.lenguajes = lenguajes_elem.text.split(",")
        elif archivo.endswith(".json"):
            with open(archivo,"r") as importado:
                datos = json.load(importado)
            self.tipo = "JSON"
            self.nombre = datos["nombre"]
            self.edad = datos["edad"]
            self.fecha = datos["fecha"]
            self.lenguajes = datos["lenguajes"]
            pass
    def mostrar(self):
        print(f"Tipo: {self.tipo}")
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Fecha: {self.fecha}")
        print(f"Lenguajes: {self.lenguajes}")
    
    def delete(self):
        os.remove(self.archivo)
        print("Archivo eliminado")
        
# prueba_clase = CustomClass("prueba.xml")
# prueba_clase.mostrar()
prueba_clase = CustomClass("prueba.json")
prueba_clase.mostrar()
prueba_clase.delete()