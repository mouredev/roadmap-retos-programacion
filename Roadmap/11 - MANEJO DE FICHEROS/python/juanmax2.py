"""
Manejo de ficheros
"""
import os
"""


file_name = "juanmax2.txt"
with open(file_name, "w") as file:
    file.write("Juan Manuel\n")
    file.write("32\n")
    file.write("Python")

with open(file_name, "r") as file:
    print(file.read())

os.remove(file_name)
"""
"""
* DIFICULTAD EXTRA (opcional):
 * Desarrolla un programa de gestión de ventas que almacena sus datos en un 
 * archivo .txt.
 * - Cada producto se guarda en una línea del archivo de la siguiente manera:
 *   [nombre_producto], [cantidad_vendida], [precio].
 * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
 *   actualizar, eliminar productos y salir.
 * - También debe poseer opciones para calcular la venta total y por producto.
 * - La opción salir borra el .txt.
"""
continuar = True
nombre_fichero = "ventas.txt"

while continuar == True:
    print("1. Añadir producto")
    print("2. Consultar producto")
    print("3. Actualizar producto")
    print("4. Borrar producto")
    print("5. Mostrar todos los productos")
    print("6. Calcular venta total")
    print("7. Calcular venta por producto")
    print("8. Salir")

    option = input("Selecciona una opción: ")
    
    if option == "1":
        nombre = input("Nombre: ")
        cantidad = input("Cantidad: ")
        precio = input("Precio: ")
        with open(nombre_fichero, "a") as file:
            file.write(f"{nombre}, {cantidad}, {precio}\n")
    elif option == "2":
        nombre = input("Nombre: ")
        with open(nombre_fichero, "r") as file:
            for line in file.readlines():
                if line.split(", ")[0] == nombre:
                    print(line)
    elif option == "3":
        nombre = input("Nombre: ")
        cantidad = input("Cantidad: ")
        precio = input("Precio: ")
        with open(nombre_fichero, "r") as file:
            lines = file.readlines()
        with open(nombre_fichero, "w") as file:
            for line in lines:
                if line.split(", ")[0] == nombre:
                    file.write(f"{nombre}, {cantidad}, {precio}\n")
                else:
                    file.write(line)                
    elif option == "4":
        nombre = input("Nombre: ")
        with open(nombre_fichero, "r") as file:
            lines = file.readlines()
        with open(nombre_fichero, "w") as file:
            for line in lines:
                if line.split(", ")[0] != nombre:
                    file.write(line)   
    elif option == "5":
        with open(nombre_fichero, "r") as file:
            print(file.read())
    elif option == "6":
        total = 0
        with open(nombre_fichero, "r") as file:
            for line in file.readlines():
                componentes = line.split(", ")
                cantidad = int(componentes[1])
                precio = float(componentes[2])
                total += cantidad * precio
        print(f"Total: {total}")
    elif option == "7":
        suma = 0
        nombre = input("Nombre: ")
        with open(nombre_fichero, "r") as file:
            for line in file.readlines():
                componentes = line.split(", ")
                if componentes[0] == nombre:
                    cantidad = int(componentes[1])
                    precio = int(componentes[2])
                    suma = cantidad * precio
        print(f"Precio: {suma}")
    elif option == "8":
        os.remove(nombre_fichero)
        continuar = False
    else:
        print("Selecciona una de las opciones disponibles.")