"""
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

import json
import csv
import os
import xml.etree.ElementTree as xml

print(f"\n## Explicación {'#' * 30}\n")

print("""
JSON nos da la posiblidad de tomar un objeto y serializarlo de manera de darle persistencia guardando 
sus propiedades en un fichero de texto:
El objeto:
    mesas = {"luis_xv": {"madera": "roble", "forma": "rectangular", "lugares": 12, "tamaño": [1.80, 1.20, 75]},
             "rustica": {"madera": "algarrobo", "forma": "redonda", "lugares": 8, "tamaño": [1.20, 0, 75]},
             "de cafe": {"madera": "cedro", "forma": "rectangular", "lugares": 0, "tamaño": [1.00, 0.50, 40]}}
Lo guardo:
    with open("mesas.json", "w") as fichero:
        json.dump(mesas, fichero, indent=4, sort_keys=True)
Para recuperarlo:
    with open("mesas.json", "r") as fichero:
        mesas_json = json.load(fichero)
Y así tenemos nuestro objeto cargado nuevamente.


XML
El objeto:
mesas = [
        {"modelo": "luis_xv", "madera": "roble", "forma": "rectangular", "lugares": 12, "tamanio": [1.80, 1.20, 75.0]},
        {"modelo": "rustica", "madera": "algarrobo", "forma": "redonda", "lugares": 8, "tamanio": [1.20, 0.0, 75.0]},
        {"modelo": "de cafe", "madera": "cedro", "forma": "rectangular", "lugares": 0, "tamanio": [1.00, 0.50, 40.0]}
        ]
Lo guardo:
root = xml.Element("mesas")
for item in mesas:
    for key, value in item.items():
        child = xml.SubElement(root, key)
        if isinstance(value, list):
            tamanio = ["largo", "ancho", "alto"]
            for list_item, nombre in zip(value, tamanio):
                xml.SubElement(child, nombre).text = str(list_item)
        else:
            child.text = str(value)

    tree = xml.ElementTree(root)
    xml.indent(tree, '    ')
    tree.write("reto_12_data.xml")
Para recuperarlo:
lista_mesas = []
dict_ = {}
tamanio = []
with open("reto_12_data.xml", "r") as xml_data:
    root = list(xml.iterparse(xml_data))
    for item in root:
        tag = item[1].tag.strip()
        value = item[1].text.strip()
        if tag in ("largo", "ancho", "alto"):
            tamanio.append(float(value))
        elif tag == "lugares":
            dict_["lugares"] = int(value)
        elif tag == "tamanio":
            dict_["tamanio"] = tamanio.copy()
            lista_mesas.append(dict_.copy())
            dict_.clear()
            tamanio.clear()
        elif tag == "mesas":
            continue
        else:
            dict_[tag] = value


CSV es un formato de fichero cuya particularidad es guardar las tuplas de manera tabular en donde la "," separa las
columnas y el salto de línea separa la filas:
El objeto:
    mesas = {"luis_xv": {"madera": "roble", "forma": "rectangular", "lugares": 12, "tamaño": [1.80, 1.20, 75]},
             "rustica": {"madera": "algarrobo", "forma": "redonda", "lugares": 8, "tamaño": [1.20, 0, 75]},
             "de cafe": {"madera": "cedro", "forma": "rectangular", "lugares": 0, "tamaño": [1.00, 0.50, 40]}}
Lo guardo:
    with open("mesas.csv", "w", newline="") as fichero:
        guardar = csv.writer(fichero, delimiter=",")
        guardar.writerow(["modelo", "madera", "forma", "lugares", "tamaño"])     # headers
        for modelo, datos in mesas.items():
            guardar.writerow([modelo, datos["madera"], datos["forma"], datos["lugares"], datos["tamaño"]])
Para recuperarlo:
    mesas_csv = {}
    with open("mesas.csv", "r") as fichero_csv:
        filas = csv.reader(fichero_csv,  delimiter=",")
        for columnas in filas:
            if filas.line_num == 1:
                headers = columnas
                continue
            mesas_csv[columnas[0]] = {headers[1]: columnas[1], headers[2]: columnas[2], headers[3]: int(columnas[3])}
            tamanios = []
            # importante: en el fichero csv la lista "tamaño" es una cadena!!! = "[1.20, 0.50, 6]" => hay que convertirla a lista de floats.
            for tamanio in columnas[4][1: -1].split(","):
                tamanios.append(float(tamanio.strip()))
            mesas_csv[columnas[0]][headers[4]] = tamanios
            
""")

print(f"\n## Dificultad extra {'#' * 30}\n")


class Programadores:
    programadores = {}
    tipo_fichero = "xml"    # probar con csv, xml o con json

    def __init__(self, nombre: str, edad: int, fecha_nacimiento: str, lenguajes: list):
        self.nombre = nombre
        self.edad = edad
        self.fecha_nacimiento = fecha_nacimiento
        self.lenguajes = lenguajes
        if not Programadores.programadores:
            Programadores.cargar_programadores()
        self.guardar_programador()

    def __str__(self):
        return f"{self.nombre}   /  {self.edad}  /  {self.fecha_nacimiento}  /  {self.lenguajes}"

    def guardar_programador(self):
        if not Programadores.existe_programador(self.nombre):
            Programadores.programadores[self.nombre] = {"edad": self.edad, "fecha_nacimiento": self.fecha_nacimiento, "lenguajes": self.lenguajes}
        else:
            self.edad = Programadores.programadores[self.nombre]["edad"]
            self.fecha_nacimiento = Programadores.programadores[self.nombre]["fecha_nacimiento"]
            self.lenguajes = Programadores.programadores[self.nombre]["lenguajes"]

    def eliminar_programador(self) -> str:
        del (Programadores.programadores[self.nombre])
        return ""

    def modificar_programador_edad(self, edad: int):
        self.edad = edad
        Programadores.programadores[self.nombre]["edad"] = edad

    def modificar_programador_fecha_nacimiento(self, fecha_nacimiento: str):
        self.fecha_nacimiento = fecha_nacimiento
        Programadores.programadores[self.nombre]["fecha_nacimiento"] = fecha_nacimiento

    def modificar_programador_lenguajes(self, lenguajes: list):
        self.lenguajes = lenguajes
        Programadores.programadores[self.nombre]["lenguajes"] = lenguajes

    @classmethod
    def lista_programadores(cls) -> str:
        cls.cargar_programadores()
        lista_completa = ""
        if cls.programadores:
            for nombre, datos in cls.programadores.items():
                lista_completa += f"\nNombre: {nombre} / Edad: {datos['edad']}, / Fecha Nacimiento: {datos['fecha_nacimiento']}"
                lenguajes = ""
                if datos['lenguajes']:
                    for lenguaje in datos['lenguajes']:
                        lenguajes += lenguaje + ", "
                lista_completa += f"\n\tLenguajes: {lenguajes[0:-2]}"
        return lista_completa

    @classmethod
    def existe_programador(cls, nombre: str):
        return nombre in cls.programadores.keys()

    @classmethod
    def cargar_programadores(cls):
        if not cls.programadores:
            try:
                if cls.tipo_fichero == "json":
                    with open("reto_12_data.json", "r") as fichero:
                        cls.programadores = json.load(fichero)
                elif cls.tipo_fichero == "csv":
                    with open("reto_12_data.csv", "r") as fichero:
                        filas = csv.reader(fichero, delimiter=",")
                        for columnas in filas:
                            if filas.line_num == 1:
                                headers = columnas
                                continue
                            cls.programadores = {columnas[0]: {headers[1]: columnas[1], headers[2]: columnas[2]}}
                            lenguajes = ""
                            for lenguaje in columnas[3][1:-1].replace("'", "").split(","):
                                lenguajes += lenguaje + ", "
                            cls.programadores[columnas[0]]["lenguajes"] = lenguajes
                elif cls.tipo_fichero == "xml":
                    dict_ = {}
                    lenguajes = []
                    with open("reto_12_data.xml", "r") as xml_data:
                        root = list(xml.iterparse(xml_data))
                        for item in root:
                            tag = item[1].tag.strip()
                            value = item[1].text.strip()
                            if tag in ("largo", "ancho", "alto"):
                                lenguajes.append(float(value))
                            elif tag == "lugares":
                                dict_["lugares"] = int(value)
                            elif tag == "tamanio":
                                dict_["lenguajes"] = lenguajes.copy()
                                cls.programadores = dict_.copy()
                                dict_.clear()
                                lenguajes.clear()
                            elif tag == "mesas":
                                continue
                            else:
                                dict_[tag] = value
                else:
                    print(f"Formato {cls.tipo_fichero} no reconocido.")
                    quit()
            except FileNotFoundError:
                pass

    @classmethod
    def programadores_to_file(cls):
        if cls.tipo_fichero == "json":
            with open("reto_12_data.json", "w") as fichero:
                json.dump(cls.programadores, fichero, indent=4, sort_keys=True)
        elif cls.tipo_fichero == "csv":
            with open("reto_12_data.csv", "w", newline="") as fichero:
                guardar = csv.writer(fichero, delimiter=",")
                guardar.writerow(["nombre", "edad", "fecha_nacimiento", "lenguajes"])  # headers
                for nombre, datos in Programadores.programadores.items():
                    guardar.writerow([nombre, datos["edad"], datos["fecha_nacimiento"], datos["lenguajes"]])
        elif cls.tipo_fichero == "xml":
            root = xml.Element("programdores")
            for key, value in cls.programadores.items():
                child = xml.SubElement(root, key)
                if isinstance(value, list):
                    for list_item in value:
                        xml.SubElement(child, "lenguaje").text = str(list_item)
                else:
                    child.text = str(value)

                tree = xml.ElementTree(root)
                xml.indent(tree, '    ')
                tree.write("reto_12_data.xml")
        else:
            print(f"Formato {cls.tipo_fichero} no reconocido.")


def indicar_tipo_fichero() -> str:
    tipo_fichero = ""
    while tipo_fichero not in ("json", "xml", "csv"):
        tipo_fichero = input("Ingresar el tipo de fichero a probar (json, xml, csv): ").lower()
    return tipo_fichero


Programadores.tipo_fichero =  indicar_tipo_fichero()

print("\nCargo programadores")
progi1 = Programadores("neslarra", 59, "23-marzo-1965", ["python", "ruby", "bash", "plsql", "sql", "awk", "java", "javascript"])
print(f"progi1 = {progi1}")
progi2 = Programadores("tele tuby", 12, "20-marzo-2012", ["cobol", "BASIC"])
print(f"progi2 = {progi2}")
progi3 = Programadores("tito livio", 89, "12-agosto-1934", ["kotlin", "go"])
print(f"progi3 = {progi3}")
progi4 = Programadores("lola mora", 40, "4-febrero-1984", ["pascal", "cobol", "smalltalk", "assembler"])
print(f"progi4 = {progi4}")
print(f"\nCantidad de programadores: {Programadores.programadores.__len__()}")
print(f"\nLista de programadores: {Programadores.lista_programadores()}")

print("\nGuardo las altas en JSON, XML o CSV (según la variable de clase -cambiarla para probar uno u otro-)")
Programadores.programadores_to_file()

_ = input("Revisar los ficheros y dar Enter (se van a modificar)!!!")

print("\nElimino programador")
progi3 = progi3.eliminar_programador()
print(f"progi3 = {progi3}")
print(f"\nCantidad de programadores: {Programadores.programadores.__len__()}")
print(f"\nLista de programadores: {Programadores.lista_programadores()}")

print("\nModifico programador")
progi1.modificar_programador_fecha_nacimiento("20-febrero-2001")
print(f"progi1 = {progi1}")
progi1.modificar_programador_edad(23)
print(f"progi1 = {progi1}")
nueva_lista_lenguajes = progi1.lenguajes
_ = nueva_lista_lenguajes.pop()
_ = nueva_lista_lenguajes.pop(0)
nueva_lista_lenguajes.append("a-go-go")
progi1.modificar_programador_lenguajes(nueva_lista_lenguajes)
print(f"progi1 = {progi1}")
print(f"\nCantidad de programadores: {Programadores.programadores.__len__()}")
print(f"\nLista de programadores: {Programadores.lista_programadores()}")

print("\nGuardo los cambios en JSON, XML o CSV (según la variable de clase -cambiarla para probar uno u otro-)")
Programadores.programadores_to_file()

_ = input("Revisar los fichero y dar Enter (se van a borrar)!!!")

try:
    os.remove("reto_12_data.json")
except FileNotFoundError as e:
    pass
except PermissionError as e:
    print(str(e))
try:
    os.remove("reto_12_data.csv")
except FileNotFoundError as e:
    pass
except PermissionError as e:
    print(str(e))

try:
    os.remove("reto_12_data.xml")
except FileNotFoundError as e:
    pass
except PermissionError as e:
    print(str(e))
