"""
EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los
 * siguientes datos (haciendo uso de la sintaxis correcta en cada caso):
 * - Nombre
 * - Edad
 * - Fecha de nacimiento
 * - Listado de lenguajes de programación
 * Muestra el contenido de los archivos.
 * Borra los archivos.

 Declaración XML
*  xml_declaration=True  Linea 56

 * Zebenpixel 2025 *******************************************************
"""

import json
import xml.etree.ElementTree as ET
import os

def crear_datos():
    """
    Crea un diccionario con los datos personales que se desean guardar.
    """
    return {
        "Nombre": "ZEBEN",
        "Edad": 99,
        "FechaNacimiento": "1900-01-01",
        "LenguajesDeProgramacion": ["Python", "Java", "GO", "C#"]
    }

def guardar_json(datos, nombre_archivo="datos.json"):
    """
    Guarda los datos en formato JSON.
    """
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)
    print(f"Archivo JSON '{nombre_archivo}' creado correctamente.")

def guardar_xml(datos, nombre_archivo="datos.xml"):
    """
    Guarda los datos en formato XML.
    """
    root = ET.Element("Datos")

    for clave, valor in datos.items():
        if isinstance(valor, list):
            lista_elemento = ET.SubElement(root, clave)
            for item in valor:
                ET.SubElement(lista_elemento, "Lenguaje").text = item
        else:
            ET.SubElement(root, clave).text = str(valor)

    arbol = ET.ElementTree(root)
    arbol.write(nombre_archivo, encoding="utf-8", xml_declaration=True) 
    print(f"Archivo XML '{nombre_archivo}' creado correctamente.")

def mostrar_contenido(archivo):
    """
    Muestra el contenido de un archivo de texto si existe.
    """
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            print(f"\nContenido de '{archivo}':")
            print(f.read())
    except FileNotFoundError:
        print(f"No se pudo abrir el archivo '{archivo}' porque no existe.")

def borrar_archivo(archivo):
    """
    Elimina un archivo si existe.
    """
    if os.path.exists(archivo):
        os.remove(archivo)
        print(f"Archivo '{archivo}' eliminado exitosamente.")
    else:
        print(f"El archivo '{archivo}' no existe o ya fue eliminado.")

def main():
    # Crear datos
    datos = crear_datos()

    # Guardar en archivos
    print("+++ Guardando los Archcivos")
    guardar_json(datos)
    guardar_xml(datos)

    # Mostrar contenido de los archivos
    print("+++ Mostrando los Archivos")
    mostrar_contenido("datos.json")
    mostrar_contenido("datos.xml")

    # Eliminar archivos
    #print("+++ Eliminando los Archivos")
    #borrar_archivo("datos.json")
    #borrar_archivo("datos.xml")

if __name__ == "__main__":
    main()
