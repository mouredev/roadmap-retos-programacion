import os

"""
Ejercicio
"""

file_name = "briansilvero.txt"

with open(file_name, "w") as file:
    file.write("Brian Silvero\n" )
    file.write("27\n")
    file.write("Python\n")

with open(file_name, "r") as file:
    print(file.read())

os.remove(file_name)

"""
Extra
"""
file_name = "briansilvero_shop.txt"
open(file_name,"w")

while True:
    print("1.Añadir producto")
    print("2.Consultar producto")
    print("3.Actualizar producto")
    print("4.Borrar producto")
    print("5.Mostrar producto")
    print("6.Calcular venta total")
    print("7.Calcular venta por producto")
    print("8.Salir")
    
    """def insertar_producto(nombre):
        cantidad = input("Cantidad: ").lower()
        precio = input("Precio: ").lower()
        """
    
    option = input("Seleccione una opcion: ").lower()
    
    if option == "1":
        nombre = input("Nombre: ").lower()
        cantidad = input("Cantidad: ").lower()
        precio = input("Precio: ").lower()
        with open(file_name, "a") as file:
            file.write(f"{nombre},{cantidad},{precio}\n")
    elif option == "2":
        name = input("Nombre: ")
        with open(file_name, "r") as file:
            for line in file.readlines():
                if line.strip().split(",")[0] == name:
                    print (line)
                    break
            else:
                print("No existe este producto")
                break
    elif option == "3":
        nombre = input("Nombre: ").lower()
        cantidad = input("Cantidad: ").lower()
        precio = input("Precio: ").lower()
        with open(file_name, "r") as file:
            lines = file.readlines()
        with open(file_name, "w") as file:
            for line in lines:
                if line.split(",")[0] == nombre:
                    file.write(f"{nombre}, {cantidad},{precio}\n")
                else:
                    file.write(line)
    elif option == "4":
        nombre = input("Nombre: ").lower()
        with open(file_name, "r") as file:
            lines = file.readlines()
        with open(file_name, "w") as file:
            for line in lines:
                if line.strip().split(",")[0] != nombre:
                    file.write(line)
    elif option == "5":
        with open(file_name, "r") as file:
            print(file.read())
    elif option == "6":
        total = 0
        with open(file_name, "r") as file:
            for line in file.readlines():
                components = line.strip().split(",")
                cantidad = int(components[1])
                precio = float(components[2])
                total += cantidad * precio
            print(f"El total de la venta es: {total}")
    elif option == "7":
        nombre = input("Nombre: ").lower()
        total = 0
        with open(file_name, "r") as file:
            for line in file.readlines():
                components = line.split(",")
                if components[0] == nombre:
                    cantidad = int(components[1])
                    precio = float(components[2])
                    total += cantidad * precio
                    print(f"El total de la venta es: {total}")
                    break
    elif option == "8":
        print("Saliendo del programa")
        os.remove(file_name)
        break
    else:
        print("Seleccione una opciones disponibles.")
