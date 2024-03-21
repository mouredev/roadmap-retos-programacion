"""
/*
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
 *
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla un programa de gestión de ventas que almacena sus datos en un 
 * archivo .txt.
 * - Cada producto se guarda en una línea del arhivo de la siguiente manera:
 *   [nombre_producto], [cantidad_vendida], [precio].
 * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
 *   actualizar, eliminar productos y salir.
 * - También debe poseer opciones para calcular la venta total y por producto.
 * - La opción salir borra el .txt.
 */
"""

import os

nombre_usuario_github = "santyjl"
nombre_archivo = nombre_usuario_github + ".txt"

with open(nombre_archivo, "w") as archivo: #with para manejar ficheros , w : escribe en el fichero
    archivo.write("Nombre: Santiago José López Ayala\n")
    archivo.write("Edad: 14 años\n")
    archivo.write("Lenguaje de programación favorito: Python\n")

with open(nombre_archivo, "r") as archivo: # r : lee el archivo
    contenido = archivo.read()

print("Contenido del archivo:")
print(contenido)

os.remove(nombre_archivo)
print("El archivo ha sido borrado.")

###EXTRA###
archivo_de_ventas = "venta.txt"
print("Hola mundo, tienes las siguientes opciones para ejecutar en 'venta':")

while True:
    opcion = int(input("""
    1- Añadir producto
    2- Consultar productos
    3- Actualizar producto
    4- Eliminar producto
    5- Calcular venta total
    6- Calcular venta por producto
    7- Salir del programa
    -- Elija según el índice: """))

    if opcion == 1:
        nombre = input("Introduce el nombre del producto: ")
        precio = float(input("Introduce el precio del producto: "))

        with open(archivo_de_ventas, "a") as archivo: #a : añade un texto a al txt
            archivo.write(f"{nombre} / {precio}\n")

        print("Producto añadido")

    elif opcion == 2:
        with open(archivo_de_ventas, "r") as archivo: #lee el archivo
            contenido = archivo.read()

        print(contenido)

    elif opcion == 3:
        nombre = input("Introduce el nombre del producto a actualizar: ")
        nuevo_nombre = input("Introduce el nuevo nombre del producto: ")
        nuevo_precio = float(input("Introduce el nuevo precio del producto: "))

        with open(archivo_de_ventas, "r") as archivo:
            lineas = archivo.readlines() #crea un iterable de las lineas

        with open(archivo_de_ventas, "w") as archivo:
            for linea in lineas:
                if nombre in linea:
                    archivo.write(f"{nuevo_nombre} / {nuevo_precio}\n")
                else:
                    archivo.write(linea)

        print("Producto actualizado")

    elif opcion == 4:
        nombre = input("Introduce el nombre del producto a eliminar: ")

        with open(archivo_de_ventas, "r") as archivo:
            lineas = archivo.readlines()

        with open(archivo_de_ventas, "w") as archivo:
            for linea in lineas:
                if nombre not in linea: #si el nombre no esta en el iterable lo vuelce a escribir
                    archivo.write(linea)

        print("Producto eliminado")

    elif opcion == 5:
        total_ventas = 0

        with open(archivo_de_ventas, "r") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                partes = linea.split(" / ") #el divisor del nombre y el precio es / entonces el segundo elemento es el precio
                total_ventas += float(partes[1])

        print(f"La venta total es: {round(total_ventas , 2)}")

    elif opcion == 6:
        nombre = input("Introduce el nombre del producto para calcular su venta: ")
        venta_producto = 0

        with open(archivo_de_ventas, "r") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                partes = linea.split(" / ")
                if partes[0] == nombre:
                    venta_producto += float(partes[1])

        print(f"La venta del producto {nombre} es: {venta_producto}")

    elif opcion == 7:
        print("Saliendo del programa...")
        os.remove(archivo_de_ventas)
        break

    else:
        print("Opción inválida. Por favor, elija una opción válida del menú.")
