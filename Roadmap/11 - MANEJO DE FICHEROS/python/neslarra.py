"""
 EJERCICIO:
 Desarrolla un programa capaz de crear un archivo que se llame como
 tu usuario de GitHub y tenga la extensión .txt.
 Añade varias líneas en ese fichero:
 - Tu nombre.
 - Edad.
 - Lenguaje de programación favorito.
 Imprime el contenido.
 Borra el fichero.

 DIFICULTAD EXTRA (opcional):
 Desarrolla un programa de gestión de ventas que almacena sus datos en un
 archivo .txt.
 - Cada producto se guarda en una línea del arhivo de la siguiente manera:
   [nombre_producto], [cantidad_vendida], [precio].
 - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
   actualizar, eliminar productos y salir.
 - También debe poseer opciones para calcular la venta total y por producto.
 - La opción salir borra el .txt.
"""
import os

print(f"\n\n##  Explicación  {'#' * 40}", end="\n\n")
print(f"""
Para poder operar con el contenido de un fichero (o generarlo) utilizamos la función 'open' a la 
cual le pasaremos dos argumentos: el nombre del fichero y el modo en que se va a abrir =>
'r' para lectura, 'w' para [sobre]escritura y 'a' para agregar. Cualquiera de ellos se puede concatenar
a dos modificadores: '+' para indicar que se harán ambas operaciones simultáneamente (read y write)
y 'b' para indicar que se operará con un stream binario.
Las operaciones podrán ser 'write', 'writelines', 'read', 'readline' y 'readlines' <= 'write' y 'read'
operan con cadenas mientras que 'writelines' y 'readlines' operan con listas (IMPORTANTE: en estas dos 
últimas 'lines' NO significa que agregará o leerá un 'linefeed' => solo indica que operará con listas => 
el linefeed, si es necesario, se deberá agregar manualmente). Por último 'readline' también opera con
cadenas pero las lee fila a fila.
Para liberar el fichero haremos un 'flush' (fuerza la descarga de datos) y un 'close' para cerrarlo.

data = '''Ultima operación: creado
Lorem ipsum dolor sit amet.
'''
fichero = open("reto_11.txt", "w")
fichero.write(data)
fichero.flush()
fichero.close()

_ = input("Revisa el fichero y luego apreta cualquier tecla")

fichero = open("reto_11.txt", "r+")
num_linea = 0
data = ""
while True:
    linea = fichero.readline()
    if not linea:
        break
    if num_linea:
        data += linea
    else:
        data += linea.split(":")[0] + " modificado.""" + '\\n"' + """
    num_linea += 1
data += "Consectetur adipiscing elit"
fichero.seek(0)              # vuelvo al ppio del fichero
fichero.truncate()           # trunco la data anterior para postear la nueva
fichero.write(data)
fichero.flush()
fichero.close()
  
""")

data = '''Ultima operación: creado
Lorem ipsum dolor sit amet.
'''
fichero = open("reto_11.txt", "w")
fichero.write(data)
fichero.flush()
fichero.close()

_ = input("Revisa el fichero y luego apreta cualquier tecla")

fichero = open("reto_11.txt", "r+")
num_linea = 0
data = ""
while True:
    linea = fichero.readline()
    if not linea:
        break
    if num_linea:
        data += linea
    else:
        data += linea.split(":")[0] + " modificado.\n"
    num_linea += 1
data += "Consectetur adipiscing elit"
fichero.seek(0)
fichero.truncate()
fichero.write(data)
fichero.flush()
fichero.close()

print(f"""
Podemos simplificar el uso de un fichero a través del uso de "context manager", el cual se encarga de la
operatoria de abrir el fichero, asignarlo a una variable, descargar los datos y cerrarlo => solo operaremos
con los métodos para manupular los datos:

data = '''Hola Mundo
Pythoneando con ficheros'''
with open('reto_11.txt', 'w') as fichero:
    fichero.write(data)

with open('reto_11.txt', 'r') as fichero:
    while True:
        linea = fichero.readline()
        if linea:
            print(linea)
        else:
            print(""" + '\\n"' + """)
            break
""")

_ = input("Revisa el fichero y luego apreta cualquier tecla")

data = '''Hola Mundo
Pythoneando con ficheros'''
with open('reto_11.txt', 'w') as fichero:
    fichero.write(data)

with open('reto_11.txt', 'r') as fichero:
    while True:
        linea = fichero.readline()
        if linea:
            print(f"{linea}", end="")
        else:
            print("\n")
            break

_ = input("Revisa el fichero y luego apreta cualquier tecla")

os.remove('reto_11.txt')

print(f"\n\n##  Dificultad Extra  {'#' * 40}", end="\n\n")

"""
 Desarrolla un programa de gestión de ventas que almacena sus datos en un
 archivo .txt.
 - Cada producto se guarda en una línea del arhivo de la siguiente manera:
   [nombre_producto], [cantidad_vendida], [precio].
 - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
   actualizar, eliminar productos y salir.
 - También debe poseer opciones para calcular la venta total y por producto.
 - La opción salir borra el .txt.
"""

import os

FILE = "retos_11_ventas.txt"

set_de_productos = set()


def cargar_ventas():
    global set_de_productos
    data = ""
    print("Cargar los tres campos. Control-C para salir")
    while True:
        try:
            producto = input("\tProducto: ")
            if producto.lower() in set_de_productos:
                print("\nEl producto YA existe => cargar otro.\n")
                continue
            set_de_productos.add(producto.lower())
            data += producto + ","
            data += input("\tVentas: ") + ","
            data += input("\tPrecio unitario: ") + ",\n"
        except (KeyboardInterrupt, InterruptedError):
            data = data[0:data.__len__() - 1]                                        # saco el útlimo "\n"
            if data and not data[0:data.__len__() - 1].split(",").__len__() % 3:     # controla que los tres campos estén cargados
                guardar_fichero(data, "a")
                return
            print("\nDeben cargarse los tres campos\n")


def eliminar_producto() -> None:
    global set_de_productos
    producto = seleccionar_producto()
    nueva_data = ""
    if producto:
        data = leer_fichero().split("\n")
        for fila in data:
            if fila:
                col = fila.split(",")
                if col[0].lower() != producto.lower():
                    nueva_data += fila + "\n"
                else:
                    set_de_productos.remove(col[0])
        nueva_data = nueva_data[0:nueva_data.__len__() - 1]
        guardar_fichero(nueva_data, "w")


def guardar_fichero(data: str, operacion: str) -> None:
    global FILE
    with open(FILE, operacion) as fichero:
        fichero.write(data + "\n")


def leer_fichero() -> str:
    global set_de_productos
    data = ""
    try:
        with open(FILE, 'r') as fichero:
            while True:
                linea = fichero.readline()
                if not linea:
                    break
                set_de_productos.add(linea.split(",")[0].lower())
                data += linea
    except FileNotFoundError:
        print("\nNo se han cargado datos\n")
    finally:
        if not data.split("\n")[-1]:
            data = data[0:-1]
        return data


def main():
    while True:
        opcion = menu(menues("ppal"))
        match opcion:
            case 0:
                salir()
            case 1:
                cargar_ventas()
            case 2:
                eliminar_producto()
            case 3:
                mostrar_ventas()
            case 4:
                modificar_producto()


def menu(menu: tuple) -> int:
    """
    Arma un menú de selección donde el primer elemento de la tupla es el título, y el último la salida (siempre "0")
    Retorna el número de item seleccionado.
    """
    while True:
        for index, item in enumerate(menu):
            if index == 0:                                                            # Título del menú
                print(f"\n{item}")
            else:
                if index < menu.__len__() - 1:                                        # lista de ítems"
                    print(f"\t{index}- {item}")
                else:                                                                 # Salida
                    print(f"\t0- {item}")
        opcion = input(f"Ingrese una opcion [0-{menu.__len__() - 2}]: ")              # -2 <=> Título y Salida
        if opcion and opcion.isnumeric() and 0 <= int(opcion) <= menu.__len__() - 2:
            return int(opcion)


def menues(menu: str) -> tuple:
    """
    data = {"nombre_menu": ("Títutlo Menu", "item1", "item2"..., "itemN", "salida"),}  donde la "salida SIEMPRE es 0
    """
    def enumerar_productos() -> tuple:
        data = ["Seleccionar Producto."]
        lista_de_productos = list(set_de_productos)
        lista_de_productos.sort()
        for index, producto in enumerate(lista_de_productos):
            data.append(producto.title())
        data.append("Volver")
        return tuple(data)

    data = {
        "ppal": ("Gestión de ventas.", "Alta", "Baja", "Consulta", "Modificación", "Salir"),
        "confirmacion": ("Confirmar.", "Si", "No"),
        "productos": enumerar_productos(),
    }
    return data[menu]


def modificar_producto() -> None:
    producto = seleccionar_producto()
    nueva_data = ""
    if producto:
        data = leer_fichero().split("\n")
        for index, fila in enumerate(data):
            if fila:
                col = fila.split(",")
                if col[0].lower().strip() == producto.lower():
                    nueva_data += col[0].strip() + ","
                    nueva_data += input("\tVentas: ") + ","
                    nueva_data += input("\tPrecio unitario: ") + ",\n"
                else:
                    nueva_data += fila + "\n"
        nueva_data = nueva_data[0:nueva_data.__len__() - 1]                                     # elimino el último "\n"
        if nueva_data and not nueva_data[0:nueva_data.__len__() - 1].split(",").__len__() % 3:  # no cuento la última "," para control de tres cols
            guardar_fichero(nueva_data, "w")


def mostrar_ventas():
    data = leer_fichero().split("\n")
    productos = []
    cantidades = []
    precios = []
    for fila in data:
        if fila:
            col = fila.split(",")
            productos.append(col[0])
            cantidades.append(col[1])
            precios.append(col[2])

    for producto, cantidad, precio in zip(productos, cantidades, precios):
        print(f"Nombre: {producto}  /  Cantidad: {cantidad}  /  Precio: {precio}  /  Ventas: ${int(cantidad) * int(precio)}")
    return


def salir() -> None:
    try:
        os.remove(FILE)
    except FileNotFoundError:
        pass
    quit()


def seleccionar_producto() -> str:
    opcion = menu(menues("productos"))
    lista_de_productos = list(set_de_productos)
    lista_de_productos.sort()
    return "" if opcion == 0 else lista_de_productos[opcion - 1]


if __name__ == "__main__":
    main()
