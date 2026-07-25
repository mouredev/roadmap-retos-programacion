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
 */"""

import os

"""
Ejercicio
"""
file_name="alferez.txt"

with open(file_name, "w")as file:
    file.write ("angel\n")
    file.write ("35\n")
    file.write ("python")

with open(file_name, "r") as file:
    print(file.read())

os.remove(file_name)

"Extra"

file_name="tienda.txt"
with open(file_name, "a")as file:
    pass

while True:

    print("******************")
    print("1. Añadir producto")
    print("2. Mostrar producto")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Mostrar todos los productos")
    print("6. Ventas por producto")
    print("7. Ventas totales")
    print("8. Salir")
    print("******************")

    opcion = input("\nIntroduce la opcion deseada: " )

    match opcion:
        case "1":
            print("1. Añadir producto.")
            name=input("introduce el nombre del producto ")
            cantidad=input("introduce la cantidad ")
            price=input("introduce el precio del producto ")
                        
            with open(file_name, "a")as file:
                file.write (f"{name}, {cantidad}, {price}, \n")
        
        case "2":
            print("2. Mostrar producto")
            name=input("introduce el nombre del producto: ")
            flag=0
            with open(file_name, "r") as file:
                filas = file.readlines()
                if len(filas) >= 1:
                    for line in filas:
                        if line.split(", ")[0] == name:
                            print(line)
                            flag=1
                            break
                    if flag==0:
                        print("no hay productos con ese nombre")                        
                else:
                        print("no hay productos")   

        case "3":
            print("3. Actualizar producto")
            name=input("introduce el nombre del producto: ")
            cantidad=input("introduce la cantidad ")
            price=input("introduce el precio del producto ")

            flag=0
            with open(file_name, "r") as file:
                filas = file.readlines()
            with open(file_name, "w") as file:
                if len(filas) >= 1:
                    for line in filas:
                        if line.split(", ")[0] == name:
                            file.write (f"{name}, {cantidad}, {price}, \n")
                            flag=1
                        else:
                            file.write (line)                            
                    if flag==0:
                        print("no hay productos con ese nombre")                        
                else:
                        print("no hay productos")

        case "4":
            print("4. Eliminar producto")
            name=input("introduce el nombre del producto: ")

            flag=0
            with open(file_name, "r") as file:
                filas = file.readlines()
            with open(file_name, "w") as file:
                if len(filas) >= 1:
                    for line in filas:
                        if line.split(", ")[0] != name:
                            file.write (line)
                        else:
                             flag=1
                             print(f"producto {name} eliminado")                           
                    if flag==0:
                        print("no hay productos con ese nombre")                        
                else:
                        print("no hay productos")
            
        
        case "5":
            print("5. Mostrar todos los productos")
            with open(file_name, "r") as file:
                print(file.read())

        case "6":
            print("6. Ventas por producto")
            name=input("introduce el nombre del producto: ")
            suma=0
            with open(file_name, "r") as file:
                filas = file.readlines()
                if len(filas) >= 1:
                    for line in filas:
                        if line.split(", ")[0] == name:
                            print(line.split(", ")[1])
                            print(line.split(", ")[2])
                            suma = float(line.split(", ")[1]) * float(line.split(", ")[2])
                            print(suma)
                            flag=1
                            break
                    if flag==0:
                        print("no hay productos con ese nombre")    
                else:
                        print("no hay productos")

        case "7":
            print("7. Ventas totales")
            suma=0
            with open(file_name, "r") as file:
                filas = file.readlines()
                if len(filas) >= 1:
                    for line in filas:
                        suma += float(line.split(", ")[1]) * float(line.split(", ")[2])
                    print(suma)                                                       
                else:
                        print("no hay productos")
              
        case "8":
            print("8. Salir")
            print("Saliendo...")
            #os.remove(file_name) #descomentar para borrar el archivo al salir
            break

        case _:
            print ("Introduce una opcion valida. Desde el 1 al 8")





