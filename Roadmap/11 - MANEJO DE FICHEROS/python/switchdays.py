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

def files():

    # Abrir el archivo en modo escritura y lectura
    with open("switchdays.txt", "w+") as my_file:

        # Escribir líneas en el archivo
        my_file.writelines(["Nombre: Víctor Meseguer\n", "Edad: 25\n", "Lenguaje favorito: Python\n"])

        print(f'El archivo {my_file.name} ha sido creado.')

        # Volver al principio del archivo para leerlo
        my_file.seek(0)

        # Leer y mostrar las líneas del archivo
        for line in my_file.readlines():
            print(line.strip())

    # Eliminar el archivo después de cerrarlo
    os.remove("switchdays.txt")
    print(f'El archivo switchdays.txt ha sido eliminado.')

files()


"""
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla un programa de gestión de ventas que almacena sus datos en un 
 * archivo .txt.
 * - Cada producto se guarda en una línea del arhivo de la siguiente manera:
 *   [nombre_producto], [cantidad_vendida], [precio].
 * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
 *   actualizar, eliminar productos y salir.
 * - También debe poseer opciones para calcular la venta total y por producto.
 * - La opción salir borra el .txt.
"""

import os

# Función para añadir un producto al archivo
def agregar_producto(archivo):
    nombre = input("Introduce el nombre del producto: ")
    cantidad = input("Introduce la cantidad vendida: ")
    precio = input("Introduce el precio: ")
    linea = f"{nombre}, {cantidad}, {precio}\n"
    archivo.write(linea)
    print("Producto añadido correctamente.")

# Función para consultar todos los productos
def consultar_productos(archivo):
    archivo.seek(0)
    print("Productos:")
    for linea in archivo.readlines():
        print(linea.strip())

# Función para actualizar un producto
def actualizar_producto(archivo):
    nombre_actualizar = input("Introduce el nombre del producto a actualizar: ")
    lineas = archivo.readlines()
    archivo.seek(0)
    archivo.truncate()
    for linea in lineas:
        if nombre_actualizar not in linea:
            archivo.write(linea)
        else:
            agregar_producto(archivo)
    print("Producto actualizado correctamente.")

# Función para eliminar un producto
def eliminar_producto(archivo):
    nombre_eliminar = input("Introduce el nombre del producto a eliminar: ")
    lineas = archivo.readlines()
    archivo.seek(0)
    archivo.truncate()
    for linea in lineas:
        if nombre_eliminar not in linea:
            archivo.write(linea)
    print("Producto eliminado correctamente.")

# Función para calcular la venta total
def calcular_venta_total(archivo):
    archivo.seek(0)
    venta_total = sum([float(linea.split(", ")[1]) * float(linea.split(", ")[2]) for linea in archivo.readlines()])
    print(f"Venta total: {venta_total}")

# Función para calcular la venta por producto
def calcular_venta_producto(archivo):
    nombre_producto = input("Introduce el nombre del producto: ")
    archivo.seek(0)
    for linea in archivo.readlines():
        if nombre_producto in linea:
            cantidad = float(linea.split(", ")[1])
            precio = float(linea.split(", ")[2])
            venta_producto = cantidad * precio
            print(f"Venta del producto {nombre_producto}: {venta_producto}")
            return
    print("Producto no encontrado.")

# Función principal
def main():
    archivo = open("ventas.txt", "a+")
    while True:
        print("\n--- Menú ---")
        print("1. Añadir producto")
        print("2. Consultar productos")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Calcular venta total")
        print("6. Calcular venta por producto")
        print("7. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            agregar_producto(archivo)
        elif opcion == "2":
            consultar_productos(archivo)
        elif opcion == "3":
            actualizar_producto(archivo)
        elif opcion == "4":
            eliminar_producto(archivo)
        elif opcion == "5":
            calcular_venta_total(archivo)
        elif opcion == "6":
            calcular_venta_producto(archivo)
        elif opcion == "7":
            archivo.close()
            os.remove("ventas.txt")
            print("Archivo eliminado. ¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
