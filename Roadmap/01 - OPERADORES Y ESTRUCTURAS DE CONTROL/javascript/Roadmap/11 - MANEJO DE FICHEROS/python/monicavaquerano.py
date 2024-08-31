# 11 MANEJO DE FICHEROS
# Monica Vaquerano
# https://monicavaquerano.dev

# IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
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
"""
import os


def crear_archivo(nombre, edad, lenguaje):
    try:
        with open("monicavaquerano.txt", "a+") as f:
            texto = f"{nombre}, {edad}, {lenguaje}\n"
            f.write(texto)
    except FileNotFoundError as e:
        print(f"Error al abrir el archivo: {e}")
    except Exception as e:
        print(f"Error al guardar la venta: {e}")


def leer_archivo():
    try:
        with open("monicavaquerano.txt") as f:
            for line in f:
                nombre, edad, lenguaje = line.strip().split(", ")
                print(f"{nombre:<15}|{edad:^10}| {lenguaje:>10}")
    except FileNotFoundError as e:
        print(f"Error al abrir el archivo: {e}")
    except Exception as e:
        print(f"Error al guardar la venta: {e}")


def eliminar_archivo():
    try:
        if os.path.exists("monicavaquerano.txt"):
            os.remove("monicavaquerano.txt")
            print("Eliminado con éxito")
        else:
            print("Este archivo no existe")
    except Exception as e:
        print(f"Error al eliminar el archivo: {e}")


while True:
    print("--- Mi archivo ---")
    choice = input(
        "¿Qué deseas hacer?:\n1. Crear o añadir al archivo\n2. Leer el archivo\n3. Eliminar el archivo\n4. Salir a DIFICULTAD EXTRA (opcional)\n> "
    ).strip()
    if choice == "1":
        os.system("clear")
        print("--- Crear o añadir ---")
        nombre = input("¿Cuál es tu nombre? > ").strip().lower()
        edad = input("¿Cuál es tu edad? > ").strip().lower()
        lenguaje = (
            input("¿Cuál es tu lenguaje de pregramación favorito? > ").strip().lower()
        )
        crear_archivo(nombre, edad, lenguaje)
        print()
    elif choice == "2":
        os.system("clear")
        print("--- Mi archivo ---")
        leer_archivo()
        print()
    elif choice == "3":
        os.system("clear")
        print("--- Eliminar ---")
        eliminar_archivo()
        print()
    elif choice == "4":
        print("Ciao!")
        break

os.system("clear")

"""
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


def guardar_venta(nombre_producto, cantidad_vendida, precio):
    try:
        with open("ventas.txt", "a") as f:
            venta = f"{nombre_producto}, {cantidad_vendida}, {precio}\n"
            f.write(venta)
    except FileNotFoundError as e:
        print(f"Error al abrir el archivo: {e}")
    except Exception as e:
        print(f"Error al guardar la venta: {e}")


def leer_ventas():
    try:
        with open("ventas.txt") as f:
            for line in f:
                nombre_producto, cantidad_vendida, precio = line.strip().split(", ")
                print(f"{nombre_producto:<15}|{cantidad_vendida:^10}| ${precio:>10}")
    except FileNotFoundError as e:
        print(f"Error al abrir el archivo: {e}")
    except Exception as e:
        print(f"Error al leer las ventas: {e}")


def eliminar_ventas():
    try:
        if os.path.exists("ventas.txt"):
            os.remove("ventas.txt")
            print("Archivo 'ventas.txt' eliminado con éxito")
        else:
            print("Archivo 'ventas.txt' no existe")
    except Exception as e:
        print(f"Error al eliminar el archivo: {e}")


def calcular_ventas(producto=None):
    ventas = []
    total = 0
    cantidad = 0
    try:
        with open("ventas.txt", "r") as f:
            for line in f:
                nombre_producto, cantidad_vendida, precio = line.strip().split(", ")
                ventas.append([nombre_producto, int(cantidad_vendida), float(precio)])
    except FileNotFoundError as e:
        print(f"Error al abrir el archivo: {e}")
        return
    except Exception as e:
        print(f"Error al procesar las ventas: {e}")
        return

    if producto:
        for item in ventas:
            if producto == item[0]:
                total += item[1] * item[2]
                cantidad += item[1]
        print(f"Total de ventas de {producto}: $ {total:,.2f} ({cantidad} unidades)")
    else:
        for item in ventas:
            total += item[1] * item[2]
        print(f"Ventas totales: $ {total:,.2f}")


def actualizar_ventas(producto):
    ventas_actualizadas = []
    try:
        with open("ventas.txt", "r") as f:
            for line in f:
                nombre_producto, cantidad_vendida, precio = line.strip().split(", ")
                if producto == nombre_producto:
                    nombre_producto = input("Nuevo nombre? > ")
                    cantidad_vendida = int(input("Nueva cantidad? > "))
                    precio = float(input("Nuevo precio? > "))
                ventas_actualizadas.append([nombre_producto, cantidad_vendida, precio])

        with open("ventas.txt", "w") as f:
            for item in ventas_actualizadas:
                f.write(f"{item[0]}, {item[1]}, {item[2]}\n")
    except FileNotFoundError as e:
        print(f"Error al abrir el archivo: {e}")
    except Exception as e:
        print(f"Error al actualizar las ventas: {e}")


while True:
    print("--- Mis Ventas ---")
    choice = input(
        "¿Qué deseas hacer?:\n1. Crear o añadir ventas\n2. Ver ventas\n3. Calcular ventas\n4. Actualizar ventas\n5. Salir\n> "
    ).strip()
    if choice == "1":
        os.system("clear")
        print("--- Crear o añadir ---")
        nombre_producto = input("¿Cuál es el nombre del producto? > ").strip().lower()
        cantidad_vendida = int(input("¿Cuál es la cantidad vendida? > "))
        precio = float(input("¿Cuál es el precio? > "))
        guardar_venta(nombre_producto, cantidad_vendida, precio)
        print()
    elif choice == "2":
        os.system("clear")
        print("--- Mis ventas ---")
        leer_ventas()
        print()
    elif choice == "3":
        os.system("clear")
        print("--- Calcular ---")
        producto = (
            input(
                "Calcular por:\n* Producto (ingresa nombre de producto y luego presiona enter)\n* Total (solo presiona enter)\n> "
            )
            .strip()
            .lower()
        )
        calcular_ventas(producto)
        print()
    elif choice == "4":
        os.system("clear")
        print("--- Actualizar ---")
        producto = input("Qué producto actualizar?:\n> ").strip().lower()
        actualizar_ventas(producto)
        print()
    elif choice == "5":
        eliminar_ventas()
        print("Ciao!")
        break
