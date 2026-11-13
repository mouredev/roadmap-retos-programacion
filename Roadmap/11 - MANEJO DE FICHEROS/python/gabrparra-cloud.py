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
"""
import os

file_name="gabrparra-cloud.txt"

with open(file_name,"w") as file:
    file.write("Gabriel Parra\n")
    file.write("39\n")
    file.write("Python\n")

with open(file_name,"r") as file:
    print(file.read())

os.remove(file_name)

file_name="Ejercicio.txt"
open(file_name,"a")

while True:
    print("1- Añadir producto")
    print("2- Consultar productos")
    print("3- Actualizar productos")
    print("4- Eliminar productos")
    print("5- Calcualar venta total")
    print("6- Calcualar venta por producto")
    print("7- Salir")



    option = input("Selecciona una opción:")

    match option:

        case "1":
            name = input("Nombre del producto: ")
            quantity = input("Cantidad de producto: ")
            price = input("precio: ")

            with open(file_name,"a") as file:
                file.write(f"{name}, {quantity}, {price}\n")

            with open(file_name,"r") as file:
                print(file.read())
       
        case "2":
            name = input("Nombre: ")
            with open(file_name,"r") as file:
                for line in file.readlines():
                  if  line.split(", ")[0] == name:
                      print(line)
        
        case "3":
            name = input("Nombre del producto: ")
            quantity = input("Cantidad de producto: ")
            price = input("precio: ")

            with open(file_name,"r") as file:
                lines=file.readlines()
            with open(file_name,"+w") as file:
                for line in lines:
                    if  line.split(", ")[0] == name:
                        file.write(f"{name}, {quantity}, {price}\n")
                    else:
                        file.write(line)
        case "4":
            name = input("Nombre del producto: ")
            
            with open(file_name,"r") as file:
                lines=file.readlines()
            with open(file_name,"+w") as file:
                for line in lines:
                    if  line.split(", ")[0] != name:
                        file.write(line)
        
        case "5":
            total=0
            with open(file_name,"r") as file:
                for line in file.readlines():
                    quantity = int(line.split(", ")[1])
                    price = float(line.split(", ")[2])
                    total+=quantity*price
            print(f"La venta total es de {total}")
        case "6":
            total=0
            name = input("de que producto quiere calcular el valor de la venta")
            with open(file_name,"r") as file:
                for line in file.readlines():
                    components= line.split(", ")
                    if components[0]==name:
                        quantity = int(components[1])
                        price = float(components[2])
                        total+=quantity*price
            print(f"la venta total del {name} es de {total}")           

        case "7":
            print("Saliendo del programa")
            os.remove(file_name)
            break

        case _:
            print("Seleccione una opción valida del 1 al 7")
