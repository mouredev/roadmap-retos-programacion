"""
 * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
 * 
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo que se llame como
 * tu usuario de GitHub y tenga la extensión .txt.
 * Añade varias líneas en ese fichero:
 * - Tu nombre.
 * - Edad.
 * - Lenguaje de programación favorito.
 * Imprime el contenido.
 * Borra el fichero.
"""

import os

usuario_github = 'Juanppdev'
nombre_archivo = f"{usuario_github}.txt"

nombre = "  Juan Pablo"
edad = "25 Años"
lenguaje_favorito = "Python y Kotlin"

try:
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(f"Nombre: {nombre}\n")
        archivo.write(f"Edad: {edad}\n")
        archivo.write(f"Lenguaje de Programación Favorito: {lenguaje_favorito}\n")
    print(f"Archivo {nombre_archivo} creado exitosamente.")
except Exception as e:
    print(f"Error al crear el archivo: {e}")

try:
    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.read()
        print(contenido)
except Exception as e:
    print(f"Error al leer el archivo: {e}")

"""
try:
    os.remove(nombre_archivo)
    print(f"Archivo {nombre_archivo} borrado exitosamente.")
except Exception as e:
    print(f"Error al borrar el archivo: {e}")
"""

"""
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla un programa de gestión de ventas que almacena sus datos en un 
 * archivo .txt.
 * - Cada producto se guarda en una línea del archivo de la siguiente manera:
 *   [nombre_producto], [cantidad_vendida], [precio].
 * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
 *   actualizar, eliminar productos y salir.
 * - También debe poseer opciones para calcular la venta total y por producto.
 * - La opción salir borra el .txt.
"""

import os

nombre_archivo = 'ventas.txt'

def agregar_producto():
    nombre_producto = input("Nombre del producto: ")
    cantidad_vendida = input("Cantidad vendida: ")
    precio = input("Precio: ")
    try:
        with open(nombre_archivo, 'a') as archivo:
            archivo.write(f"{nombre_producto}, {cantidad_vendida}, {precio}\n")
        print(f"Producto {nombre_producto} agregado exitosamente.")
    except Exception as e:
        print(f"Error al agregar el producto: {e}")

def consultar_productos():
    try:
        if os.path.exists(nombre_archivo):
            with open(nombre_archivo, 'r') as archivo:
                print(archivo.read())
        else:
            print("No hay productos registrados.")
    except Exception as e:
        print(f"Error al consultar los productos: {e}")

def actualizar_producto():
    try:
        productos = []
        if os.path.exists(nombre_archivo):
            with open(nombre_archivo, 'r') as archivo:
                productos = archivo.readlines()
            nombre_producto = input("Nombre del producto a actualizar: ")
            for i, producto in enumerate(productos):
                if producto.startswith(nombre_producto):
                    cantidad_vendida = input("Nueva cantidad vendida: ")
                    precio = input("Nuevo precio: ")
                    productos[i] = f"{nombre_producto}, {cantidad_vendida}, {precio}\n"
                    break
            with open(nombre_archivo, 'w') as archivo:
                archivo.writelines(productos)
            print(f"Producto {nombre_producto} actualizado exitosamente.")
        else:
            print("No hay productos registrados.")
    except Exception as e:
        print(f"Error al actualizar el producto: {e}")

def eliminar_producto():
    try:
        productos = []
        if os.path.exists(nombre_archivo):
            with open(nombre_archivo, 'r') as archivo:
                productos = archivo.readlines()
            nombre_producto = input("Nombre del producto a eliminar: ")
            productos = [producto for producto in productos if not producto.startswith(nombre_producto)]
            with open(nombre_archivo, 'w') as archivo:
                archivo.writelines(productos)
            print(f"Producto {nombre_producto} eliminado exitosamente.")
        else:
            print("No hay productos registrados.")
    except Exception as e:
        print(f"Error al eliminar el producto: {e}")

def calcular_venta_total():
    try:
        total = 0
        if os.path.exists(nombre_archivo):
            with open(nombre_archivo, 'r') as archivo:
                for linea in archivo:
                    _, cantidad_vendida, precio = linea.strip().split(', ')
                    total += int(cantidad_vendida) * float(precio)
            print(f"Venta total: {total}")
        else:
            print("No hay productos registrados.")
    except Exception as e:
        print(f"Error al calcular la venta total: {e}")

def calcular_venta_por_producto():
    try:
        ventas = {}
        if os.path.exists(nombre_archivo):
            with open(nombre_archivo, 'r') as archivo:
                for linea in archivo:
                    nombre_producto, cantidad_vendida, precio = linea.strip().split(', ')
                    ventas[nombre_producto] = int(cantidad_vendida) * float(precio)
            for producto, venta in ventas.items():
                print(f"{producto}: {venta}")
        else:
            print("No hay productos registrados.")
    except Exception as e:
        print(f"Error al calcular la venta por producto: {e}")

def salir():
    try:
        if os.path.exists(nombre_archivo):
            os.remove(nombre_archivo)
        print("Archivo de ventas eliminado. Saliendo del programa.")
    except Exception as e:
        print(f"Error al eliminar el archivo: {e}")

def menu():
    while True:
        print("\nGestión de Ventas")
        print("1. Añadir producto")
        print("2. Consultar productos")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Calcular venta total")
        print("6. Calcular venta por producto")
        print("7. Salir")
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            agregar_producto()
        elif opcion == '2':
            consultar_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            calcular_venta_total()
        elif opcion == '6':
            calcular_venta_por_producto()
        elif opcion == '7':
            salir()
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

menu()
