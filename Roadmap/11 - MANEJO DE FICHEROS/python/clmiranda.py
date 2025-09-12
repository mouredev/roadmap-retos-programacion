# MANEJO DE FICHEROS

import os

username = "clmiranda.txt"

with open(username, "w") as f:
    f.write("Cliver\n")
    f.write("27 años\n")
    f.write("Python")

with open(username, "r") as f:
    print(f.read())

os.remove(username)


# Ejercicio - Dificultad Extra

store_file = "store.txt"

while True:
    try:
        option = int(input("""\n1.- Agregar Producto
2.- Consultar Producto
3.- Mostrar Todos los Productos
4.- Actualizar Producto
5.- Eliminar Producto
6.- Calcular Venta Total
7.- Calcular Venta por Producto
8.- Salir\n
Elija una opción: """))
        if option not in [1, 2, 3, 4, 5, 6, 7]:
            raise IndexError
    except ValueError:
        print("Debe ingresar un entero válido")
    except IndexError:
        print("Debe elegir una de las opciones")
    
    match option:
        case 1:
            name = input("Ingrese el Producto: ")
            quantity = int(input("Ingrese la Cantidad: "))
            price = float(input("Ingrese el Precio: "))
            with open(store_file, "a") as file:
                line = f"{name}, {quantity}, {price}\n"
                file.write(line)
        case 2:
            name = input("Ingrese el Nombre del Producto a Consultar: ")
            with open(store_file, "r") as file:
                for line in file.readlines():
                    product = line.split(", ")
                    if product[0] == name:
                        print(f"Producto: {product[0]}, Cantidad: {product[1]}, Precio: {product[2]}")
                        break
        case 3:
            with open(store_file, "r") as file:
                for line in file.readlines():
                    product = line.split(", ")
                    print(f"Producto: {product[0]}, Cantidad: {product[1]}, Precio: {product[2]}")
        case 4:
            name = input("Ingrese el Producto a Actualizar: ")
            quantity = int(input("Ingrese la Cantidad a Actualizar: "))
            price = float(input("Ingrese el Precio a Actualizar: "))
            with open(store_file, "w") as file:
                for line in file.readlines():
                    if line.split(", ")[0] == name:
                        line = f"{name}, {quantity}, {price}\n"
                        file.write(line)
        case 5:
            name = input("Ingrese el Producto a Eliminar: ")
            with open(store_file, "w") as file:
                for line in file.readlines():
                    if line.split(", ")[0] != name:
                        file.write(line)
        case 6:
            total_sale = 0
            with open(store_file, "r") as file:
                for line in file.readlines():
                    quantity, price = int(line.split(", ")[1]), float(line.split(", ")[2])
                    total_sale += quantity * price
            print(total_sale)
        case 7:
            name = input("Ingrese el Nombre del Producto: ")
            total_sale = 0
            with open(store_file, "r") as file:
                for line in file.readlines():
                    if line.split(", ")[0] == name:
                        quantity, price = int(line.split(", ")[1]), float(line.split(", ")[2])
                        total_sale += quantity * price
                        break
            print(f"Las ventas del producto {name} son: {total_sale}")
        case 8:
            os.remove(store_file)
            print("Finalizando la ejecución del programa")
            break