""" Reto 11: Manejo de ficheros """

import os

file_name = "Tomu98.txt"

with open(file_name, "w") as file:
    file.write("Abel Tomás\n")
    file.write("25\n")
    file.write("Python\n")

with open(file_name, "r") as file:
    print(file.read())

os.remove(file_name)



""" Reto extra """

file_name = "Tomu_shop.txt"
open(file_name, "a")

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
                    if line.split(", ")[0] == name.lower():
                        print(line)
                        break
                    else:
                        print("No se encontró el producto.\n")
                        break
        case "3":
            name = input("Nombre: ")
            quantity = input("Cantidad: ")
            price = input("Precio: ")
            with open(file_name, "r") as file:
                lines = file.readlines()
            with open(file_name, "w") as file:
                for line in lines:
                    if line.split(", ")[0] == name.lower():
                        file.write(f"{name}, {quantity}, {price}\n")
                    else:
                        file.write(line)
        case "4":
            name = input("Nombre: ")
            with open(file_name, "r") as file:
                lines = file.readlines()
            with open(file_name, "w") as file:
                for line in lines:
                    if line.split(", ")[0] != name.lower():
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
            print(f"Total: {total}\n")
        case "7":
            name = input("Nombre: ")
            total = 0
            with open(file_name, "r") as file:
                for line in file.readlines():
                    components = line.split(", ")
                    if components[0] == name.lower():
                        quantity = int(components[1])
                        price = float(components[2])
                        total += quantity * price
                        break
            print(f"Total: {total}\n")
        case "8":
            os.remove(file_name)
            break
        case _:
            print("Selecciona una de las opciones disponibles.")
