### Ejercicio ###
import os

user_github = "Sac-Corts"
name = "Isaac Cortés"
age = 22
language = "Python"

file_name = f"{user_github}.txt"
file = open(file_name, "w")

file.write(f"Nombre: {name}\n")
file.write(f"Edad: {age}\n")
file.write(f"Lenguaje de programación: {language}\n")

file.close()

with open(file_name, "r") as file:
    content = file.read()
    print("Contenido del archivo:")
    print(content)

os.remove(file_name)
print(f"El archivo '{file_name}' ha sido borrado.")


### Ejercicio Extra ###

file_name = "OXXO.txt"

open(file_name, "a")

def main():
    while True:
        print("Menú:")
        print("1. Añadir producto:")
        print("2. Consultar producto:")
        print("3. Actualizar producto:")
        print("4. Eliminar producto:")
        print("5. Calcular venta total:")
        print("6. Calcular venta por producto:")
        print("7. Salir:")
        option = input("Ingrese una opción: ")

        if option == "1":
            add_product()
        elif option == "2":
            consult_product()
        elif option == "3":
            update_product()
        elif option == "4":
            delete_product()
        elif option == "5":
            calculate_total_sale()
        elif option == "6":
            calculate_sales_product()
        elif option == "7":
            os.remove(file_name)
            break
        else:
            print("Por favor, ingresa una opción correcta.")

def add_product():
    name = input("Nombre del producto: ")
    quantity = input("Cantidad vendida: ")
    price = input("Precio: ")
    with open(file_name, "a") as file:
        file.write(f"{name}, {quantity}, {price}\n") 

def consult_product():
    name = input("Nombre: ")
    with open(file_name, "r") as file:
        for line in file.readlines():
            if line.split(", ")[0] == name:
                print(line)

def update_product():
    name = input("Nombre del producto: ")
    quantity = input("Cantidad vendida: ")
    price = input("Precio: ")
    with open(file_name, "r") as file:
        lines = file.readlines()
    with open(file_name, "w") as file:
        for line in lines:
            if line.split(", ")[0] == name:
                file.write(f"{name}, {quantity}, {price}\n") 
            else:
                file.write(line)

def delete_product():
    name = input("Nombre del producto: ")
    with open(file_name, "r") as file:
        lines = file.readlines()
    with open(file_name, "w") as file:
        for line in lines:
            if line.split(", ")[0] != name:
                file.write(line)

def calculate_total_sale():
    total = 0
    with open(file_name, "r") as file:
        for line in file.readlines():
            components = line.split(", ")
            quantity = int(components[1])
            price = float(components[2])
            total += quantity * price
            print(total)

def calculate_sales_product():
    name = input("Nombre del producto: ")
    total = 0
    with open(file_name, "r") as file:
        for line in file.readlines():
            components = line.split(", ")
            if components[0] == name:
                quantity = int(components[1])
                price = float(components[2])
                total += quantity * price
    print(total)
            

main()



