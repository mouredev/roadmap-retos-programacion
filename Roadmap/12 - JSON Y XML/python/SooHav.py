# 12 - JSON y XML
import xml.etree.ElementTree as ET
import json
import os
# Ejercicio
# Json


def generar_archivo_json(diccionario: dict):
    with open('SooHav.json', 'w') as file:
        json.dump(diccionario, file, indent=4)

# XML


def generar_archivo_xml(etiqueta, diccionario):
    elemento = ET.Element(etiqueta)
    for clave, valor in diccionario.items():
        if clave == 'lenguajes':
            lenguajes = ET.SubElement(elemento, clave)
            for lenguaje in valor:
                l = ET.SubElement(lenguajes, 'lenguaje')
                l.text = lenguaje
        else:
            hijo = ET.SubElement(elemento, clave)
            # Aquí se agrega el valor como texto del elemento
            hijo.text = str(valor)
    ET.ElementTree(elemento).write('SooHav.xml', encoding='utf8')

# Ejercicio Extra


class Datos:
    def __init__(self, nombre, edad, fecha_nacimiento, lenguajes) -> None:
        self.nombre = nombre
        self.edad = edad
        self.fecha_nacimiento = fecha_nacimiento
        self.lenguajes = lenguajes

    def __str__(self):
        return f"Nombre: {self.nombre}\nEdad: {self.edad}\nFecha de Nacimiento: {self.fecha_nacimiento}\nLenguajes: {', '.join(self.lenguajes)}"

    @staticmethod
    def cargar_desde_archivo(archivo):
        if archivo.endswith('.json'):
            with open(archivo, 'r') as file:
                informacion = json.load(file)
                return Datos(informacion['nombre'], informacion['edad'], informacion['fecha_nacimiento'], informacion['lenguajes'])
        # leyendo desde un archivo y extrayendo la info
        elif archivo.endswith('.xml'):
            tree = ET.parse(archivo)
            root = tree.getroot()
            nombre = root.find('nombre').text
            edad = int(root.find('edad').text)
            fecha_nacimiento = root.find('fecha_nacimiento').text
            lenguajes = [elem.text for elem in root.find(
                'lenguajes').findall('lenguaje')]
            return Datos(nombre, edad, fecha_nacimiento, lenguajes)
        else:
            raise ValueError("Formato de archivo no válido.")


# Uso de las funciones creadas
info = {
    "nombre": "Sofia",
    "edad": 46,
    "fecha_nacimiento": "26-02-1978",
    "lenguajes": ["Python", "R"]
}

if __name__ == "__main__":
    while True:
        print("\nMenú:")
        print("1. Generar archivo JSON")
        print("2. Consultar archivo JSON")
        print("3. Generar archivo XML")
        print("4. Consultar archivo XML")
        print("5. Leer y transformar en clase custom")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            generar_archivo_json(info)
            print("Archivo JSON generado exitosamente.\n")

        elif opcion == "2":
            try:
                with open('SooHav.json', 'r') as file:
                    archivo = json.load(file)
                    print(archivo)
            except FileNotFoundError:
                print("El archivo JSON no existe.")

        elif opcion == "3":
            archivo_xml = generar_archivo_xml('informacion', info)
            print("Archivo XML generado exitosamente.\n")

        elif opcion == "4":
            try:
                with open('SooHav.xml', 'r') as file:
                    archivo = file.read()
                    print(archivo)
            except FileNotFoundError:
                print("El archivo XML no existe.")

        elif opcion == "5":
            archivo = input(
                "Ingrese el nombre del archivo (incluyendo la extensión .json o .xml): ")
            try:
                datos = Datos.cargar_desde_archivo(archivo)
                print("Datos cargados exitosamente:")
                print(datos.__dict__)
            except FileNotFoundError:
                print(f"El archivo '{archivo}' no existe.")
            except ValueError as e:
                print(e)

        elif opcion == "6":
            if os.path.exists("SooHav.json"):
                os.remove("SooHav.json")
            if os.path.exists("SooHav.xml"):
                os.remove("SooHav.xml")
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
