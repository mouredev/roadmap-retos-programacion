# RETO 11 MANEJO DE FICHEROS
import os
"Crea un programa capaz de crear un archivo txt, imprime el contenido y borra el fichero"

file_name = "zetared92.txt"

with open(file_name, "w") as file:
    file.write("Zeta Vega\n")
    file.write("31\n")
    file.write("Python")

with open(file_name, "r") as file:
    print(file.read())

os.remove(file_name)


# Extra

print("🧩 DIFICULTAD EXTRA - GESTIÓN DE VENTAS 🧩")
file_name = "zeta_sales.txt"

open(file_name, "a")

while True:
    print("1. Add product")
    print("2. Check product")
    print("3. Update product")
    print("4. Delete product")
    print("5. Show products")
    print("6. Calculate total sales")
    print("7. Calculate sales by product")
    print("8. Exit")

    option = input("Select an option")

    if option == "1":
        name = input("Name: ")
        quantity = input("Quantity: ")
        price = input("Price: ")
        with open(file_name, "a") as file:
            file.write(f"{name}, {quantity}, {price}\n")
    elif option == "2":
        name = input("Name: ")
        with open(file_name, "r") as file:
            for line in file.readlines():
                if line.split(", ")[0] == name:
                    print(line)
                    break
    elif option == "3":
        name = input("Name: ")
        quantity = input("Quantity: ")
        price = input("Price: ")
        with open(file_name, "r") as file:
            lines = file.readlines()
        with open(file_name, "w") as file:
            for line in lines:
                if line.split(", ")[0] == name:
                    file.write(f"{name}, {quantity}, {price}\n")
                else:
                    file.write(line)
    elif option == "4":
        name = input("Name: ")
        with open(file_name, "r") as file:
            lines = file.readlines()
        with open(file_name, "w") as file:
            for line in lines:
                if line.split(", ")[0] != name:
                    file.write(line)
    elif option == "5":
        with open(file_name, "r") as file:
            print(file.read())
    elif option == "6":
        total = 0
        with open(file_name, "r") as file:
            for line in file.readlines():
                components = line.split(", ")
                quantity = int(components[1])
                price = float(components[2])
                total == quantity * price
        print(total)
    elif option == "7":
        name = input("Name: ")
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
    elif option == "8":
        os.remove(file_name)
        break
    else:
        print("Select one of the available options.1")