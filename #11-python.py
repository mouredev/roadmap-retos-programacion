'''
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
'''

import os

fichero = "RicardoSDev.txt"

with open (fichero, "a") as file:
    file.write("Ricardo\n")
    file.write("60\n")
    file.write("Python")           

with open (fichero, "r") as file:
    print(file.read())

os.remove(fichero)    

'''
DIFICULTAD EXTRA (opcional):
* Desarrolla un programa de gestión de ventas que almacena sus datos en un 
* archivo .txt.
* - Cada producto se guarda en una línea del archivo de la siguiente manera:
*   [nombre_producto], [cantidad_vendida], [precio].
* - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
*   actualizar, eliminar productos y salir.
* - También debe poseer opciones para calcular la venta total y por producto.
* - La opción salir borra el .txt.
*
'''

archivo = "archivo.txt"

while True:
    print("1.- Añadir producto")
    print("2.- Consultar producto por nombre")
    print("3.- Actualizar producto")
    print("4.- Eliminar producto")
    print("5.- Listar productos")
    print("6.- Calcular venta total")
    print("7.- Calcular venta por producto")
    print("8.- Salir")

    opcion = input("Elige una opción: ")

    match(opcion):
        case "1":
            with open (archivo, "a") as catalogo:
                Nombre = input("Nombre: ")
                Cantidad = input("Cantidad: ")
                Precio = input("Precio: ")
                catalogo.write(f"{Nombre}, {Cantidad}, {Precio}\n")
        case "2":
            with open (archivo, "r") as catalogo:
                Nombre = input("Nombre a consultar: ")
                for line in catalogo.readlines():
                    if Nombre == line.split(", ")[0]:
                        print(line)
                        continue
        case "3":
            Nombre = input("Nombre: ")
            Cantidad = input("Cantidad: ")
            Precio = input("Precio: ")
            with open (archivo, "r") as catalogo:
                lines = catalogo.readlines()
            with open (archivo, "w") as catalogo:    
                for line in lines:
                    if Nombre == line.split(", ")[0]:
                        catalogo.write(f"{Nombre}, {Cantidad}, {Precio}\n")
                    else:
                        catalogo.write(line)
        case "4":
            Nombre = input("Nombre: ")
            with open (archivo, "r") as catalogo:
                lines = catalogo.readlines()
            with open (archivo, "w") as catalogo:    
                for line in lines:
                    if line.split(", ")[0] != Nombre:
                        catalogo.write(line)
        case "5":
            with open (archivo, "r") as catalogo:
                print(catalogo.read())

        case "6":
            total = 0
            with open (archivo, "r") as catalogo:
                lines = catalogo.readlines()
                for line in lines:
                    total += int(line.split(", ")[1]) * int(line.split()[2])
                print(f"Las ventas totales son de {total} €.") 
              
        case "7":
            total = 0
            Nombre = input("Producto para total por nombre: ")
            with open (archivo, "r") as catalogo:
                lines = catalogo.readlines()
                for line in lines:
                    if Nombre == line.split(", ")[0]:
                        total += int(line.split(", ")[1]) * int(line.split()[2])            
            print(f"Las ventas totales son de {total} € para {Nombre}.")

        case "8":
            break
        case _:
            print("Elige una opción válida")
            pass
