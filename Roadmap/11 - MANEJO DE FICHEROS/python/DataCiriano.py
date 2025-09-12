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
* - Cada producto se guarda en una línea del arhivo de la siguiente manera:
*   [nombre_producto], [cantidad_vendida], [precio].
* - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
*   actualizar, eliminar productos y salir.
* - También debe poseer opciones para calcular la venta total y por producto.
* - La opción salir borra el .txt.
"""
import os

file_name = 'DataCiriano.txt'

with open(file_name, "w") as file:
    file.write("Mi usuario de GitHub es: Data Ciriano\n")
    file.write("Tengo 33 años\n")
    file.write("Mi lenguaje de programación favorito es Python\n")
    
with open(file_name, "r") as file:
    print(file.read())
    
os.remove(file_name)


#-----EXTRA----

file_name = "shop.txt"

while True:
    
    action = input("""Introduzca una de las siguientes opciones:\n
                   1- Añadir Producto\n
                   2- Consultar Producto\n3
                   3- Actualizar Producto\n
                   4- Borrar Producto\n
                   5- Mostrar Producto\n
                   6- Calcular venta total\n
                   7- Calcular venta por producto\n
                   8- Salir\n\n""")
    
    match action:
        
        case "1":
            name = input("Introduzca el nombre del producto: ")
            quantity = input("Cantidad: ")
            price = input("Price: ")
            
            with open(file_name, "a") as file:
                file.write(f"{name}, {quantity}, {price}\n")
                
        case "2":
            name = input("Introduzca el nombre del archivo que desea consultar: ")
            
            with open(file_name, "r") as file:
                for line in file.readlines():
                    if line.split(", ")[0] == name:
                        print(line)
                else:
                    print(f"No existe un producto con el nombre: {name}")
                        
        case "3":
            name = input("Introduzca el nombre del producto que desea actualizar: ")
            quantity = input("Introduzca la cantidad de este producto: ")
            price = input("Introduzca el precio del producto: ")
            
            with open(file_name, "r") as file:
                lines = file.readlines()
                
            with open(file_name, "w") as file:
                for line in lines:
                    if line.split(", ")[0] == name:
                        file.write(f"{name}, {quantity}, {price}\n")
                    else:
                        file.write(line)
                        
        case "4":
            name = input("Introduzca el nombre del producto que desea borrar: ")
            
            with open(file_name, "r") as file:
                lines = file.readlines()
            
            with open(file_name, "w") as file:
                for line in lines:
                    if line.split(", ")[0] != name:
                        file.write(line)
                        
        case "5":
            name = input("Introduzca el nombre del producto que desea ver: ")
            
            with open(file_name, "r") as file:
                lines = file.readlines()
                
                for line in lines:
                    if line.split(", ")[0] == name:
                        print(line)
                        break
                else:
                    print(f"No existe el producto {name}")
                    
        case "6":
            total = 0
            
            with open(file_name, "r") as file:
                for line in file.readlines():
                    components = line.split(", ")
                    quantity = int(components[1])
                    price = float(components[2])
                    total += quantity * price
            
            print(f"El total de ventas es: {total}")
            
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
            
            print(f"Las ventas totales de {name} son: {total}")
            
                
        case "8":
            os.remove(file_name)
            print("Archivo borrado")
            break
                  
        case _:
            print("Seleccione una de las opciones disponibles")
            