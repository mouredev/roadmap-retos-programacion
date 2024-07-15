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

""" Ejercicio """

# file_name = "LucasRebuffo.txt"


# with open(file_name, "w") as file:
#     file.write(f"Lucas Rebuffo \n")
#     file.write(f"27 \n")
#     file.write(f"Python \n")

# with open(file_name, "r") as file:
#     print(file.read())

# os.remove(file_name)


""" * DIFICULTAD EXTRA (opcional):
 * Desarrolla un programa de gestión de ventas que almacena sus datos en un 
 * archivo .txt.
 * - Cada producto se guarda en una línea del archivo de la siguiente manera:
 *   [nombre_producto], [cantidad_vendida], [precio].
 * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
 *   actualizar, eliminar productos y salir.
 * - También debe poseer opciones para calcular la venta total y por producto.
 * - La opción salir borra el .txt.
 */  """

file_name = "Ventas.txt"


while True:
    print("1. Agregar producto")
    print("2. Comsultar producto")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Mostrar inventario")
    print("6. Calcular venta total")
    print("7. Calcular venta por producto")
    print("8. Salir")
    print("")

    operacion = input("Elige una opcion\n")

    match operacion:
        case "1":
            name = input("Nombre: ")
            quantity = input("Cantidad: ")
            price = input("Precio: ")

            with open(file_name, "a") as file:
                file.write(f"{name},{quantity},{price}\n")

        case "2":
            name = input("Nombre: ")
            with open(file_name, "r") as file:
                for line in file.readlines():
                    if line.split(sep=",")[0] == name:
                        print(f"--> {line}")

        case "3":
            name = input("Nombre: ")
            quantity = input("Cantidad: ")
            price = input("Precio: ")
            with open(file_name, "r") as file:
                lines = file.readlines()

            with open(file_name, "w") as file:
                for line in lines:
                    if line.split(sep=",")[0] == name:
                        file.write(f"{name},{quantity},{price}\n")
                    else:
                        file.write(line)

        case "4":

            name = input("Nombre: ")

            with open(file_name, "r") as file:
                lines = file.readlines()

            with open(file_name, "w") as file:
                for line in lines:
                    if line.split(sep=",")[0] != name:
                        file.write(line)

        case "5":
            print("---------------------------------------")
            with open(file_name, "r") as file:
                print(file.read())
            print("---------------------------------------\n")
        case "6":

            with open(file_name, "r") as file:
                lines = file.readlines()

            total: float = 0
            for line in lines:
                if line != "\n":
                    line = line.split(sep=",")
                    total += float(line[1]) * float(line[2])

            print(f"--> El total de ventas es {total}\n")

        case "7":

            with open(file_name, "r") as file:
                lines = file.readlines()

            sub_totales: dict = {}
            for line in lines:
                if line != "\n":
                    line = line.split(sep=",")
                    sub_totales[line[0]] = float(line[1]) * float(line[2])
            print("Los subtotales son: ")
            for (prod,subtotal) in sub_totales.items():
                print(f"{prod}: {subtotal}")
            print("\n")

        case "8":
            os.remove(file_name)
            break
        case _:
            print("No corresponde a ninguna operacion.")
