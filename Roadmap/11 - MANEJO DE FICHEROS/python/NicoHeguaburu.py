#Ficheros

import os

file_name = "NicoHeguaburu.txt"


with open(file_name, "w") as file:
    file.write("Nicolás Heguaburu\n")
    file.write("22\n")
    file.write("Python\n")

with open(file_name, "r") as file:
    print(file.read())


os.remove(file_name)



#Dificultad extra

file_name = "NicoHeguaburuShop.txt"


while True:
    print("1------Añadir producto")
    print("2------Consultar producto")
    print("3------Actualizar producto")
    print("4------Eliminar producto")
    print("5------Calcular la venta total")
    print("6------Calcular la venta por producto")
    print("7------Ver todos los productos")
    print("8------Salir")

    opcion = input("Selecione una opcion...")

    if opcion == "1": 
        nombre = input("Nombre:")
        cantidad = input("Cantidad:")
        precio = input("Precio:")

        with open(file_name, "a") as file:
            file.write(f"{nombre}, {cantidad}, {precio}\n")

    elif opcion == "2":
        nombre = input("Nombre:")
        with open(file_name, "r") as file:
            for linea in file.readlines():
                if linea.split(", ")[0] == nombre:
                    print(linea)
                    break

        
    elif opcion == "3":
        nombre = input("Nombre:")
        cantidad = input("Cantidad:")
        precio = input("Precio:")
        with open(file_name, "r") as file:
            lineas = file.readlines()

        with open(file_name, "w") as file:
            for linea in lineas:
                if linea.split(", ")[0] == nombre:
                    file.write(f"{nombre}, {cantidad}, {precio} \n")
                else:
                    file.write(linea)

    elif opcion == "4":
        nombre = input("Nombre:")
        with open(file_name, "r") as file:
            lineas = file.readlines()

        with open(file_name, "w") as file:
            for linea in lineas:
                if linea.split(", ")[0] != nombre:
                    file.write(linea)

        
    elif opcion == "5":
        with open(file_name, "r") as file:
            lineas = file.readlines()
            total_venta = 0
            for linea in lineas:
                total_venta += int(linea.split(", ")[1]) * int(linea.split(", ")[2])
            print(total_venta)


    elif opcion == "6":
        nombre = input("Nombre:")
        with open(file_name, "r") as file:
            lineas = file.readlines()
            for linea in lineas:
                if linea.split(", ")[0] == nombre:
                    print(int(linea.split(", ")[1]) * int(linea.split(", ")[2]))

    elif opcion == "7":
        with open(file_name, "r") as file:
            print(file.read())
    else:
        print("seleccione una opcion valida")
