"""
------------------
MANEJO DE FICHEROS
------------------
IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.

EJERCICIO:
Desarrolla un programa capaz de crear un archivo que se llame como
tu usuario de GitHub y tenga la extensión .txt.
Añade varias líneas en ese fichero:
- Tu nombre.
- Edad.
- Lenguaje de programación favorito.
Imprime el contenido.
Borra el fichero.

DIFICULTAD EXTRA (opcional):
Desarrolla un programa de gestión de ventas que almacena sus datos en un 
archivo .txt.
- Cada producto se guarda en una línea del arhivo de la siguiente manera:
  [nombre_producto], [cantidad_vendida], [precio].
- Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
  actualizar, eliminar productos y salir.
- También debe poseer opciones para calcular la venta total y por producto.
- La opción salir borra el .txt.
"""
import os

# Ejercicio

file_name = "SergioGI99.txt"

with open(file_name, "w") as file:
    file.write("Sergio Garcia\n") 
    file.write("24 años\n")
    file.write("Python")

with open(file_name, "r") as file:
    print(file.read())

os.remove(file_name)

# Extra

file_name = "sales.txt"

open(file_name, "a")

def name_check(name):
    in_list = False
    with open(file_name, "r") as file:
        for line in file.readlines():
            if line.split(", ")[0] == name:
                in_list = True
    if in_list == False:
        print("No se ha encontrado el producto")
    

def check_list():
    name = input("Nombre del producto a buscar: ")
    name_check(name)
    with open(file_name, "r") as file:
        for line in file.readlines():
            if line.split(", ")[0] == name:
                print(line)
    continue_check()

def add():
    name = input("Nombre del producto: ")
    amount = input("Cantidad vendida: ")
    price = input("Precio: ")
    with open(file_name, "a") as file:
        file.write(f"{name}, {amount}, {price}\n")
    print(f"{name} ha sido añadido.")
    continue_check()

def update():
    name = input("Nombre del producto a actualizar: ")
    name_check(name)
    update_value = input("Que quieres actualizar?\n- Nombre\n- Cantidad\n- Precio")
    with open(file_name, "r") as file:
            lines = file.readlines()
    with open(file_name, "w") as file:
        for line in lines:
            if line.split(", ")[0] == name:
                if update_value.lower() == "nombre":
                    new_name = input("Escribe el nuevo nombre: ")
                    amount = line.split(", ")[1]
                    price = line.split(", ")[2]
                    file.write(f"{new_name}, {amount}, {price}\n")
                elif update_value.lower() == "cantidad":
                    new_amount = input("Escribe la cantidad vendida: ")
                    name = line.split(", ")[0]
                    price = line.split(", ")[2]
                    file.write(f"{name}, {new_amount}, {price}\n")
                elif update_value.lower() == "precio":
                    new_price = input("Escribe el precio actualizado: ")
                    name = line.split(", ")[1]
                    amount = line.split(", ")[2]
                    file.write(f"{name}, {amount}, {new_price}\n")
                else:
                    print("Opción incorrecta.")
                    update()
            else:
                file.write(line)
    continue_check()

def delete():
    name = input("Nombre del producto a eliminar: ")
    name_check(name)
    with open(file_name, "r") as file:
            lines = file.readlines()
    with open(file_name, "w") as file:
        for line in lines:
            if line.split(", ")[0] != name:
                file.write(line)
    continue_check()

def show_list():
    with open(file_name, "r") as file:
        print(file.read())
    continue_check()

def total_sales():
    total = 0
    with open(file_name, "r") as file:
        lines = file.readlines()
        for line in lines:
            total = total + (int(line.split(", ")[1]) * int(line.split(", ")[2]))
    print(f"Valor ventas total: {total}")
    continue_check()

def product_sales():
    name = input("Nombre del producto: ")
    name_check(name)
    total = 0
    with open(file_name, "r") as file:
        lines = file.readlines()
        for line in lines:
            if line.split(", ")[0] == name:
                total = total + (int(line.split(", ")[1]) * int(line.split(", ")[2]))
                print(f"Valor ventas total: {total}")
    continue_check()

def exit():
    return None

def continue_check():
    input("(pulsa enter)")
    sales()

input_list = {
    "1":check_list,
    "2":add,
    "3":update,
    "4":delete,
    "5":show_list,
    "6":total_sales,
    "7":product_sales,
    "8":exit
}

def sales():
    print("¿Que operación quieres realizar?\n1 - Consultar\n2 - Añadir\n3 - Actualizar\n4 - Eliminar\n5 - Listado\n6 - Venta total\n7 - Venta por producto\n8 - Salir")
    user_input = input(": " )
    if user_input.lower() in input_list:
        input_list[user_input]()
    else:
        print(f"{user_input} no es correcto.")
        continue_check()

sales()

os.remove(file_name)