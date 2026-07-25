import os

file_name = 'idiegorojas.txt'

with open(file_name, 'w') as file:
    file.write('Diego 1\nRojas 2\n')
    file.write('28\n')
    file.write('Python\n')

with open(file_name, 'r') as file:
    print(file.read())

os.remove(file_name)


# Extra

file_name = 'sales.txt'

open(file_name, 'a')

while True:
    print('Bienvenido.')
    print("1. Añadir producto")
    print("2. Consultar producto")
    print("3. Actualizar producto")
    print("4. Borrar producto")
    print("5. Calcular venta total")
    print("6. Calcular venta por producto")
    print("7. Salir")

    option = input("Por favor selecciona una opción: ")

    if option == "1":
        name = input("Ingresa el nombre del producto: ")
        quantity = input("Ingresa la cantidad vendida: ")
        price = input("Ingresa el precio del producto vendido: ")
        with open(file_name, "a") as file:
            file.write(f"{name}, {quantity}, {price}\n")
    elif option == "2":
        name = input("Ingresa el nombre del producto a consultar: ")
        with open(file_name, "r") as file:
            for line in file.readlines():
                if line.split(", ")[0] == name:
                    print(line)
                    break
    elif option == "3":
        name = input("Nombre: ")
        quantity = input("Cantidad: ")
        price = input("Precio: ")
        with open(file_name, "r") as file:
            lines = file.readlines()
        with open(file_name, "w") as file:
            for line in lines:
                if line.split(", ")[0] == name:
                    file.write(f"{name}, {quantity}, {price}\n")
                else:
                    file.write(line)
    elif option == "4":
        name = input("Nombre: ")
        with open(file_name, "r") as file:
            lines = file.readlines()
        with open(file_name, "w") as file:
            for line in lines:
                if line.split(", ")[0] != name:
                    file.write(line)
    elif option == "5":
        total = 0
        with open(file_name, "r") as file:
            for line in file.readlines():
                components = line.split(", ")
                quantity = int(components[1])
                price = float(components[2])
                total += quantity * price
        print(total)
    elif option == "6":
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
        print(total)
    elif option == "7":
        os.remove(file_name)
        break
    else:
        print("Por favor selecciona una de las opciones disponibles.")