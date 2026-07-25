'''
EJERCICIO:
Desarrolla un programa capaz de crear un archivo que se llame como tu
usuario de GitHub y tenga la extension .txt.

Añade varias líneas en ese fichero:
- Tu nombre.
- Edad.
- Lenguaje de programación favorito.
Imprime el contenido.
Borra el fichero.
'''
import os

def program_file():
    
    file_name = "DaniQB99.txt"

    lines = ["- Dani\n", "- 25\n", "- Python\n"]
    
    with open(file_name, "w") as file: # Escribe en el archivo
        file.writelines(lines)

    with open(file_name, "r") as file: # Lee el archivo
        print(file.read())

    os.remove(file_name) # Borra el archivo

program_file()

'''
DIFICULTAD EXTRA (opcional):
Desarrolla un programa de gestión de ventas que almacena sus datos en un 
archivo .txt.
- Cada producto se guarda en una línea del arhivo de la siguiente manera:
[nombre_producto], [cantidad_vendida], [precio].
- Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
actualizar, eliminar productos y salir.
- También debe poseer opciones para calcular la venta total y por producto.
- La opción salir borra el .txt.
'''

def program_shop():

    file_name = "DaniQB99_shop.txt"

    while True:
        print("1. Añadir producto")
        print("2. Consultar producto")
        print("3. Actualizar producto")
        print("4. Borrar producto") 
        print("5. Mostrar productos")
        print("6. Calcular venta total")
        print("7. Calcular venta por producto")
        print("8. Salir")
        
        option = input("Selecciona una opción: ")

        if option == "1":
            name = input("Nombre del producto: ")
            quantity = input("Cantidad: ")
            price = input("Precio: ")

            with open(file_name, "a") as file:
                file.write(f"{name}, {quantity}, {price}\n")
                print("Producto añadido con éxito.")

        elif option == "2":
            name = input("Nombre del producto: ")

            with open(file_name, "r") as file:
                for line in file.readlines():
                    if line.split(", ")[0] == name:
                        print(line)
                        break
        
        elif option == "3":
            name = input("Nombre del producto: ")
            quantity = input("Nueva cantidad: ")
            price = input("Nuevo precio: ")
            
            with open(file_name, "r") as file:
                lines = file.readlines()
            
            with open(file_name, "w") as file:
                for line in lines:
                    if line.split(", ")[0] == name:
                        file.write(f"{name}, {quantity}, {price}\n")
                        print("Producto actualizado con éxito.")
                    else:
                        file.write(line)
                        print("Producto no encontrado.")

        elif option == "4":
            name = input("Nombre del producto: ")
            
            with open(file_name, "r") as file:
                lines = file.readlines()
                for line in lines:
                    if line.split(", ")[0] != name:
                        file.write(line)
                        print("Producto eliminado con éxito.")
                        break
                    else:
                        file.write(line)
                        print("Producto no encontrado.")
                        break
        
        elif option == "5":
            with open(file_name, "r") as file:
                print("Productos almacenados: \n")
                print(file.read())
        
        elif option == "6":
            total = 0
            with open(file_name, "r") as file:
                for line in file.readlines():
                    components = line.split(", ")
                    quantity = int(components[1])
                    price = float(components[2])
                    total += quantity * price # += es el acumulador de suma
            print('El total de la venta es:', total)
        
        elif option == "7":
            name = input("Nombre del producto: ")
            total = 0
            with open(file_name, "r") as file:
                for line in file.readlines():
                    components = line.split(", ")
                    if components[0] == name:
                        quantity = int(components[1])
                        price = float(components[2])
                        total += quantity * price # += es el acumulador de suma
                        break
            print('El total de la venta por este producto es:', total)
        
        elif option == "8":
            os.remove(file_name)
            break
        
        else:
            print("Selecciona una de las opciones disponibles.")
            program_file()

program_shop()
                
            