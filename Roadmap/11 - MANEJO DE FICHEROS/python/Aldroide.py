""" 
    Ejercicio
    Desarrollar un programa capaz de crear un archivo con tunombre de github
    y extensión txt
    Añade en varias lineas:
        * Nombre
        * Edad
        * Lenguaje de programación
    Imprime el contenido
    Borra el fichero
"""

import os

file_name = "aldroide.txt"

with open(file_name, 'w') as file:
    file.write("Aldo Avila\n")
    file.write("36\n")
    file.write("Python")

with open(file_name, 'r') as file:
    print(file.read())

os.remove(file_name)

"""
    Dificultad Extra
    Desarrollar un programa de gestión de ventas que almacena sus datos
    en un archivo txt.
        * Cada producto se fuarda en una linea del archivo de la siguiente manera:
        * Nombre, Cantidad, precio
        * Siguiendo ese formato, y mediante terminal debe permitir añadir, consultar
        * actualizar, aliminar productos y salir
    Tambien debe poseer opciones para calcular la venta total y por producto
    la opcion salir borra el .txt.
"""

file_name = "Tiendita.txt"

open(file_name, "a")

while True:
    print("1. Añadir producto")
    print("2. Consultar producto")
    print("3. Actualizar producto")
    print("4. Borrar producto")
    print("5. Mostrar producto")
    print("6. Calcular venta total")
    print("7. Calcular venta por producto")
    print("8. salir")

    option = input("Selecciona una opción: ")

    match option:
        case "1":
            name = input("Nombre: ")
            quantity = input("Cantidad: ")
            price = input("Precio: ")
            with open(file_name, "a") as file:
                file.write(f"{name}, {quantity}, {price}\n")
        case "2":
            name = input("Nombre: ")
            with open(file_name, "r") as file:
                for line in file.readlines():
                    if line.split(", ")[0] == name:
                        print(line)
                        break
        case "3":
            name = input("Nombre: ")
            quantity = input("Cantidad: ")
            price = input("Precio: ")
            with open(file_name, "r") as file:
                lines = file.readlines()
            with open(file_name, "w") as file:
                for line in lines:
                    if line.split(", ")[0] == name:
                        file.write(f"{name}, {quantity}, {price}\n")
                    else:
                        file.write(line)
        case "4":
            name = input("Nombre: ")
            with open(file_name, "r") as file:
                lines = file.readlines()
            with open(file_name, "w") as file:
                for line in lines:
                    if line.split(", ")[0] != name:
                        file.write(line)
        case "5":
            with open(file_name, "r") as file:
                print(file.read())
        case "6":
            total = 0
            with open(file_name, "r") as file:
                for line in file.readlines():
                    components = line.split(", ")
                    quantity = int(components[1])
                    price = float(components[2])
                    total += quantity * price
            print(total)
        case "7":
            name = input("Nombre: ")
            total = 0
            with open(file_name, "r") as file:
                for line in file.readlines():
                    components = line.split(", ")
                    if components[0] == name:
                        quantity = int(components[1])
                        price = float(components[2])
                        total += quantity * price
                        break
            print(total)
        case "8":
            os.remove(file_name)
            break
        case _:
            print("Selecciona una de las opciones disponibles.")
