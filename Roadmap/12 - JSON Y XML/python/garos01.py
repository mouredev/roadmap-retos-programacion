import json
import xml.etree.ElementTree as ET
import os


def crear_archivo_xml(datos):
    root = ET.Element("persona")
    for key, value in datos.items():
        if key == "lenguajes":
            lenguajes = ET.SubElement(root, "lenguajes")
            for lenguaje in value:
                ET.SubElement(lenguajes, "lenguaje").text = lenguaje
        else:
            ET.SubElement(root, key).text = str(value)

    tree = ET.ElementTree(root)
    tree.write("datos.xml")


def crear_archivo_json(datos):
    with open("datos.json", "w") as json_file:
        json.dump(datos, json_file, indent=4)


def mostrar_contenido_archivos():
    with open("datos.xml", "r") as xml_file:
        print("Contenido del archivo XML:")
        print(xml_file.read())

    with open("datos.json", "r") as json_file:
        print("\nContenido del archivo JSON:")
        print(json_file.read())


def borrar_archivos():
    os.remove("datos.xml")
    os.remove("datos.json")
    print("Archivos borrados exitosamente.")


# Datos
datos = {
    "nombre": "Oscar",
    "edad": 29,
    "fecha_nacimiento": "11-09-1994",
    "lenguajes": ["Python", "JavaScript"],
}

# Crear archivos XML y JSON
crear_archivo_xml(datos)
crear_archivo_json(datos)

# Mostrar contenido de los archivos
mostrar_contenido_archivos()

# Borrar archivos
borrar_archivos()
