""" /*
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
 */ """

import os

#EJERCICIO

file_name = "davidrguez98.txt"

with open(file_name, "w") as file:
    file.write("David Rodriguez")
    file.write("\n26")
    file.write("\nPython")

with open(file_name, "r") as file:
    print(file.read())

os.remove(file_name)

#DIFICULTAD EXTRA

sale_list = "sale_list.txt"

open(sale_list, "a")

while True:
    print("1. Añadir producto.")
    print("2. Consultar producto.")
    print("3. Actualizar producto.")
    print("4. Ver lista de productos")
    print("5. Eliminar producto.")
    print("6. Calcular la venta total.")
    print("7. Calcular venta por producto.")
    print("8. Salir del programa")

    option = input("\nSelecciona una opción: ")

    match option:
        case("1"):
            name_product = input("Nombre del producto: ")
            quantity_product = input("Cantidad: ")
            price_product = input("Precio del producto: ")

            with open(sale_list, "a") as file:
                file.write(f"{name_product}, {quantity_product}, {price_product}\n")

        case("2"):
            name_product = input("¿Qué producto quieres consultar?: ")
            with open(sale_list, "r") as file:
                for line in file.readlines():
                    if line.split(", ")[0] == name_product:
                        print(line)
                        break
                else:
                    print("\nEl producto no se ha encontrado.\n")      
            
        case("3"):
            name_product = input("¿Qué producto quieres actualizar?: ")
            quantity_product = input("Nueva cantidad: ")
            price_product = input("Nuevo precio: ")

            with open(sale_list, "r") as file:
                lines = file.readlines()
            with open(sale_list, "w") as file:
                for line in lines:
                    if line.split(", ")[0] == name_product:
                        file.write(f"{name_product}, {quantity_product}, {price_product}\n")
                    else:
                        file.write(line)

    
        case("4"):
            with open(sale_list, "r") as file:
                print(file.read())

        case("5"):
            name_product = input("¿Qué producto quieres eliminar?: ")

            with open(sale_list, "r") as file:
                lines = file.readlines()
            with open(sale_list, "w") as file:
                for line in lines:
                    if line.split(", ")[0] != name_product:
                        file.write(line)

        case("6"):
            total = 0
            with open(sale_list, "r") as file:
                for line in file.readlines():
                    products_value = line.split(", ")
                    quantity_product = int(products_value[1])
                    price_product = float(products_value[2])
                    total += quantity_product * price_product
            print(total)
        
        case("7"): 
            name_product = input("¿De que producto quieres saber la venta total?: ")

            with open(sale_list, "r") as file:
                for line in file.readlines():
                    if line.split(", ")[0] == name_product:
                        quantity_product = int(line.split(", ")[1])
                        price_product = float(line.split(", ")[2])
                        print(quantity_product * price_product)
                    else:
                        print("El producto no se encuentra en la lista.")
        
        case("8"):
            os.remove(sale_list)
            break
        
        case("9"):
            print("La opción marcada no es correcta. Escoge un número del 1 al 7.")

