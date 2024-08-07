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
 * - Cada producto se guarda en una línea del archivo de la siguiente manera:
 *   [nombre_producto], [cantidad_vendida], [precio].
 * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
 *   actualizar, eliminar productos y salir.
 * - También debe poseer opciones para calcular la venta total y por producto.
 * - La opción salir borra el .txt.
 */
"""
import os

fichero = open("alanshakir.txt", "w")
fichero.write("Mi nombre es: Alan Ramirez\nEdad: 35 años\nLenguaje de programacion: Python")
fichero.close()

with open("alanshakir.txt", "r") as fichero:
    print(fichero.read())

os.remove("alanshakir.txt")

#Extra
gestion_ventas = "ventas.txt"
def menu():
    print("\n Programa Gestion de Ventas: ")
    print("1. añadir producto")
    print("2. consultar producto")
    print("3. actualizar producto")
    print("4. eliminar producto")
    print("5. mostrar productos")
    print("6. calcular venta total")
    print("7. calcular total producto")
    print("8. Salir del programa")
    while True:
        action = int(input("Elija un numero entre 1 - 8: "))
        if action == 1:
            name_product = input("ingrese el nombre del producto: ")
            quantity = input("ingrese la cantidad vendida: ")
            price = input("ingrese el precio del producto: ")
            with open(gestion_ventas, "a") as fichero:
                fichero.write(f"{name_product},{quantity},{price}\n")
        elif action == 2:
            name_product = input("ingrese el nombre del producto: ")
            with open(gestion_ventas, "r") as fichero:
                for linea in fichero.readlines():
                    if linea.split(",")[0] == name_product:
                        print(linea)
                        break   
                else:
                    print("producto no exite")          
        elif action == 3:
            name_product = input("ingrese el nombre del producto: ")
            quantity = input("ingrese la cantidad vendida: ")
            price = input("ingrese el precio del producto: ")
            with open(gestion_ventas, "r") as fichero:
                lineas = fichero.readlines()
            with open(gestion_ventas, "w") as fichero:
                for linea in lineas:
                    if linea.split(",")[0] == name_product:
                        fichero.write(f"{name_product},{quantity},{price}\n")                        
                else:
                    fichero.write(linea) 
        elif action == 4:
            name_product = input("ingrese el nombre del producto: ")
            with open(gestion_ventas, "r") as fichero:
                lineas = fichero.readlines()
            with open(gestion_ventas, "w") as fichero:
                for linea in lineas:
                        if linea.split(",")[0] != name_product:
                            fichero.write(linea)
        elif action == 5:
            with open(gestion_ventas, "r") as fichero:
                print(fichero.read())
        elif action == 6:
            total_ventas = 0
            with open(gestion_ventas, "r") as fichero:
                for linea in fichero.readlines():
                    products = linea.split(",")
                    quantity = int(products[1])
                    price = float(products[2])
                    total_ventas += quantity + price
            print(total_ventas)
        elif action == 7:
            name_product = input("ingrese el nombre del producto: ")
            total_productos = 0
            with open(gestion_ventas, "r") as fichero:
                for linea in fichero.readlines():
                    products = linea.split(",")
                    if products[0] == name_product:
                        quantity = int(products[1])
                        price = float(products[2])
                        total_productos += quantity + price
                        break
            print(total_ventas)
        elif action == 8:
            os.remove(gestion_ventas)
            break
        else:
            print("elija una opcion valida")


menu()
