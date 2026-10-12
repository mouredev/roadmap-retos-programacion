import os

"""Ejercicio"""

file_name = "labs-Carla.txt"


with open(file_name,"w") as file:
    file.write("Carla\n")
    file.write("25\n")
    file.write("Python\n")

with open(file_name, "r") as file:
    print(file.read())

os.remove(file_name)

"""Extra"""


def gestion_ventas():

    ventas_file = "ventas.txt"
    ventas = []

    while True:

        print("1. Añadir producto")
        print("2. Consultar producto")
        print("3. Actualizar productos")
        print("4. Eliminar productos")
        print("5. Mostrar productos")
        print("6. Calcular venta total")
        print("7. Calcular venta por producto")
        print("8. Salir")

        option = input("¿Qué desea realizar?\n")

        match option:
            case "1":
                nombre_producto = input("Nombre producto:\n")
                cantidad_vendida = int(input("Cantidad: "))
                precio = int(input("Precio: "))

                nueva_venta = {
                    "nombre_producto": nombre_producto,
                    "cantidad_vendida": cantidad_vendida,
                    "precio": precio
                }

                with open(ventas_file, "a") as file:
                    file.write(
                        f"{nombre_producto},{cantidad_vendida},{precio}\n"
                    )

                ventas.append(nueva_venta)

            case "2":
                name = input("Nombre del producto: ")

                with open(ventas_file, "r") as file:
                    for line in file.readlines():
                        if line.split(",")[0] == name:
                            print(line)
                            break
            case "3":
                nombre_producto = input("Nombre producto:\n")
                cantidad_vendida = int(input("Cantidad: "))
                precio = int(input("Precio: "))

                with open(ventas_file, "r") as file:
                    lines = file.readlines()
                with open(ventas_file, "w") as file:
                    for line in lines:
                        if line.split(",")[0] == nombre_producto:
                            file.write(f"{nombre_producto},{cantidad_vendida},{precio}\n")
                        else:
                            file.write(line)
                
            case "4":
                name = input("Nombre del producto: ")
                with open(ventas_file, "r") as file:
                    lines = file.readlines()
                with open(ventas_file, "w") as file:
                    for line in lines:
                        if line.split(",")[0] != name:
                            file.write(line)
            case "5":
                with open(ventas_file, "r") as file:
                    print(file.read())

            case "6":
                total = 0
                with open(ventas_file, "r") as file:
                    for line in file.readlines():
                        components = line.split(",")
                        quantity = int(components[1])
                        price = float(components[2])
                        total += quantity * price
                print(total)
            case "7":
                name = input("Nombre: ")
                total = 0
                with open(ventas_file, "r") as file:
                    for line in file.readlines():
                        components = line.split(",")
                        if components[0] == name:
                            quantity = int(components[1])
                            price = float(components[2])
                            total += quantity * price
                print(total)
                break
            case "8":
                os.remove(ventas_file)
                break


gestion_ventas()

