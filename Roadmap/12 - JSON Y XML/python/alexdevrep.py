'''
/*
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
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la lógica de creación de los archivos anteriores, crea un
 * programa capaz de leer y transformar en una misma clase custom de tu 
 * lenguaje los datos almacenados en el XML y el JSON.
 * Borra los archivos.
 */
'''
#Importamos las librerías necesarias
import json
import xml.etree.ElementTree as ET
import os

#Creamos una función con un diccinario con los datos

def crear_datos():
    datos = {
        "Nombre": "Alejandro",
        "Edad": 24,
        "Fecha de nacimiento": "22-07-1999",
        "Lenguajes de programacion": ["Python","Java","JavaScript"]
    }
    return datos
#Creamos el fichero XML
def guardar_xml(datos):
    #Creamos un nuevo elemento en la estructura de árbol XML
    root=ET.Element("Datos")
    #Iteramos tanto las claves como los valores del diccionario
    for key, value in datos.items():
        #Si el valor es una lista (para el apartado de lenguajes de programacion que es una lista)
        if isinstance (value,list):
            #Creamos un elemento secundario dentro del principal que es root
            sub_element = ET.SubElement(root, key) #Key es el nombre del elemento secundario
            #Iteramos cada objeto en la lista value
            for item in value:
                #Creamos un elemento llamado lenguaje que es elemento secundario de Key
                ET.SubElement(sub_element, "lenguaje").text = item #Establecemos el texto de este elemento como el valor de item
        else:
            # Si el valor no es una lista, creamos un elemento secundario
            # del elemento principal 'root' y establecemos su texto como una cadena de texto
            ET.SubElement(root, key).text = str(value)

    #Creamos un nuevo elemento que representa el arbol completo   
    tree = ET.ElementTree(root)
    #Escribimos el contenido del arbol en un archivo externo llamado datos.xml
    tree.write("datos.xml")

#Creamos el archivo JSON
def guardar_json(datos):
    #usamos with para asegurarnos que los recursos son liberados adecuadamente al salir del bloque de codigo
    with open("datos.json","w") as json_file:
        #tomamos los datos que deseamos escribir en formato JSON y los escribimos en un archivo .JSON
        json.dump(datos, json_file, indent=4)

def main():
    datos = crear_datos()
    guardar_xml(datos)
    guardar_json(datos)
    print("Datos guardados correctamente")
    #Borramos los archivos
    os.remove("datos.xml")
    print("Archivo borrado exitosamente")
    os.remove("datos.json")
    print("Archivo json borrado exitosamente")
    
if __name__ == "__main__":
    main()



