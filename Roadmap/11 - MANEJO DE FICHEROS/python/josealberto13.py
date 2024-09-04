"""/*
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
 * Borra el fichero."""

import os

file_name = "josealberto13.txt"
with open(file_name, "w") as file:
    file.write("Jose Alberto\n")
    file.write("26\n")
    file.write("Python")
    
with open(file_name, "r") as file:
    print(file.read())

os.remove(file_name)


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
*/"""
file_name = "josealberto13_shop.txt"

while True:
    print("1. Añadir producto")
    print("2. Consultar productos")
    print("3. Actualizar producto")
    print("4. Buscar producto")
    print("5. Calcular venta total")
    print("6. Calcular venta por producto")
    print("7. Eliminar producto")
    print("8. Eliminar Todo y Salir")
    
    option = input("Selecciona una opción: ")
    
    match option:
        case "1":
            name = input("Nombre del Producto: ")
            quantity = input("Cantidad: ")
            price = input("Precio: ")
            with open(file_name, "a") as file:
                file.write(f"{name}, {quantity}, {price}\n")
        case "2":
            with open(file_name, "r") as file:
                print(file.read())       
        case "3":
            search = input("Nombre del Producto: ")
            with open(file_name, "r") as file:
                lines = file.readlines()
# Sobre escribimos todos los elementos guardados en "lines" y reemplazmos en el caso que encontremos el producto buscado
            with open(file_name, "w") as file: 
                aux = False
                for line in lines:
                    if line.split(", ")[0] == search:
                        name = input("Nombre del Producto: ")
                        quantity = input("Cantidad: ")
                        price = input("Precio: ")
                        file.write(f"{name}, {quantity}, {price}\n")
                        aux = True
                    else:
                        file.write(line)
                if aux == False:
                    print("¡ERROR, El producto no existe!\n")
        case "4":
            search = input("Nombre del Producto: ")
            with open(file_name, "r") as file:
                for line in file.readlines():
                    if line.split(", ")[0] == search:
                        print(line)
                        break
                    else:
                        print("¡ERROR, El producto no existe!\n")
                        break
        case "5":
            total = 0
            with open(file_name, "r") as file:
                for line in file.readlines():
# total = quantity[1] * price[2] se transforman a int, ya que son guardados como str, para evitar errores seria mejor transformar a float
                    total += int(line.split(", ")[1]) * int(line.split(", ")[2])
            print(total)
        case "6":
            total = 0
            search = input("Nombre del Producto: ")
            with open(file_name, "r") as file:
                for line in file.readlines():
                    if line.split(", ")[0] == search:
                        total += int(line.split(", ")[1]) * int(line.split(", ")[2])
            print(total)
        case "7":
            search = input("Nombre del Producto: ")
            with open(file_name, "r") as file:
                lines = file.readlines()
            with open(file_name, "w") as file:
                for line in lines:
                    if line.split(", ")[0] != search:
                        file.write(line)
        case "8":
            os.remove(file_name) # Elimina el archivo que hemos creado
            print("Saliste del programa")
            break
        case _:
            print("Selecciona unda de las opciones disponibles!")