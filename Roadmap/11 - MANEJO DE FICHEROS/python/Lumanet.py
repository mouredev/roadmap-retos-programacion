import os

file_name = "Lumanet.txt"
os.system("clear") # Limpiar terminal
with open(file_name, "w") as file: # Crear archivo si no existe
    file.write("Marcos\n")
    file.write("42\n")
    file.write("Python")

with open(file_name, "r") as file:
    print(file.read())

os.remove(file_name)

"""
DIFICULTAD EXTRA (opcional):
Desarrolla un programa de gestión de ventas que almacena sus datos en un 
archivo .txt.
- Cada producto se guarda en una línea del archivo de la siguiente manera:
  [nombre_producto], [cantidad_vendida], [precio].
- Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
  actualizar, eliminar productos y salir.
- También debe poseer opciones para calcular la venta total y por producto.
- La opción salir borra el .txt.
"""
os.system("clear") # Limpiar terminal
file_name = "tienda.txt"

open(file_name, "a") # Crear archivo si no existe
os.system("clear") # Limpiar terminal

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
        nombre = input("Nombre: ")
        cantidad = input("Cantidad: ")
        precio = input("Precio: ")
        with open(file_name, "a") as file:
            file.write(f"{nombre}, {cantidad}, {precio}\n")
    elif option == "2":
        nombre = input("Nombre: ")
        with open(file_name, "r") as file:
            for line in file.readlines():
                if line.split(", ")[0] == nombre:
                    print(line)
                    break
    elif option == "3":
        nombre = input("Nombre: ")
        cantidad = input("Cantidad: ")
        precio = input("Precio: ")
        with open(file_name, "r") as file:
            lines = file.readlines()
        with open(file_name, "w") as file:
            for line in lines:
                if line.split(", ")[0] == nombre:
                    file.write(f"{nombre}, {cantidad}, {precio}\n")
                else:
                    file.write(line)
    elif option == "4":
        nombre = input("Nombre: ")
        with open(file_name, "r") as file:
            lines = file.readlines()
        with open(file_name, "w") as file:
            for line in lines:
                if line.split(", ")[0] != nombre:
                    file.write(line)
    elif option == "5":
        with open(file_name, "r") as file:
            print(file.read())
    elif option == "6":
        total = 0
        with open(file_name, "r") as file:
            for line in file.readlines():
                elemento = line.split(", ")
                cantidad = int(elemento[1])
                precio = float(elemento[2])
                total += cantidad * precio
        print(total)
    elif option == "7":
        nombre = input("Nombre: ")
        total = 0
        with open(file_name, "r") as file:
            for line in file.readlines():
                elemento = line.split(", ")
                if elemento[0] == nombre:
                    cantidad = int(elemento[1])
                    precio = float(elemento[2])
                    total += cantidad * precio
                    break
        print(total)
    elif option == "8":
        os.remove(file_name)
        break
    else:
        print("Selecciona una de las opciones disponibles.")
