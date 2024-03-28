"""
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo que se llame como
 * tu usuario de GitHub y tenga la extensión .txt.
 * Añade varias líneas en ese fichero:
 * - Tu nombre.
 * - Edad.
 * - Lenguaje de programación favorito.
 * Imprime el contenido.
 * Borra el fichero.
"""
from time import sleep
from os import remove

def txt_file():
    with open("avcenal.txt","w+") as my_file:
        my_file.writelines("Nombre: Alex\nEdad: 39\nLenguaje Favorito: Python")

    my_file.close()

    with open("avcenal.txt","r+") as my_file:
        for line in my_file.readlines():
            print(line)
            

    my_file.close()
    remove("avcenal.txt")

txt_file()

"""
* DIFICULTAD EXTRA (opcional):
 * Desarrolla un programa de gestión de ventas que almacena sus datos en un 
 * archivo .txt.
 * - Cada producto se guarda en una línea del arhivo de la siguiente manera:
 *   [nombre_producto], [cantidad_vendida], [precio].
 * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
 *   actualizar, eliminar productos y salir.
 * - También debe poseer opciones para calcular la venta total y por producto.
 * - La opción salir borra el .txt.
"""

def add_products(path):
    product_name = input("Dime el nombre del producto: ")
    product_units_sold = input ("Dime cuantas unidades has veniddo: ") #podría controlar que sea una cifra con una regex
    product_price = input ("Dime el precio del producto: ")
    with open(path,"a") as file:
        file.write(f"{product_name}, {product_units_sold}, {product_price}\n")

    file.close
    print(f"El producto {product_name} ha sido añadido al archivo de ventas\n")
    sleep(1)

def check_products(path):
    try:
        with open(path,"r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("No hay registros de ventas por el momento...\n")
        sleep(1)
    else:
        print("Estos son los productos que tenemos en el sistema:\n")
        for line in lines:
            print(line)

def update_products(path):
    try:
        with open(path,"r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("No hay registros de ventas por el momento...\n")
        sleep(1)
    else:
        file.close()
        product = input("Dime el nombre producto a actualizar por favor: ")
        for index in range(0,len(lines)):
            products = lines[index].split(",")
            if product in products:
                line_number = index
                while True:
                    option = input("¿Quieres actualizar las unidades vendidas(U) o el precio(P)?: ").upper()
                    if option == "U":
                        units = input("Perfecto, dime las unidades que has vendido en total: ")
                        temp_line = lines[line_number].split(",")
                        temp_line[1] = units
                        lines[line_number] = f"{temp_line[0]}, {temp_line[1]}, {temp_line[2]}"
                        print(f"El producto {product} ha sido actualizado\n")
                        sleep(1)
                        break
                    elif option == "P":
                        price = input("Entendido, dime el nuevo precio: ")
                        temp_line = lines[line_number].split(",")
                        temp_line[2] = price
                        lines[line_number] = f"{temp_line[0]}, {temp_line[1]}, {temp_line[2]}\n"
                        print(f"El producto {product} ha sido actualizado\n")
                        sleep(1)
                        break
                    else:
                        print("La opción no es válida, prueba de nuevo...\n")
                        sleep(1)
                with open(path,"w") as file:
                    file.writelines(lines)
                file.close()
                break
            elif index == len(lines)-1:
                print("El producto indicado no se encuentra en el archivo de ventas\n")
                sleep(1)
                break

def erase_products(path):
    try:
        with open(path,"r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("No hay registros de ventas por el momento...\n")
        sleep(1)
    else:
        file.close()
        product = input("¿Qué producto deseas eliminar?: ")
        for index in range(0,len(lines)):
            if product in lines[index].split(","):
                line_number = index
                lines.remove(lines[line_number])
                with open(path,"w") as file:
                    file.writelines(lines)

                print("Producto eliminado del archivo de ventas\n")
                sleep(1)
                break
        if index == len(lines)-1:
            print("El producto no se encuentra en el archivo de ventas\n")
            sleep(1)

def total_sales(path):
    try:
        with open(path,"r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("No hay registros de ventas por el momento...\n")
        sleep(1)
    else:
        file.close()
        print("\n")
        print("El total de ventas por producto es:")
        for index in range(0,len(lines)):
            line = lines[index].split(",")
            total = int(line[1]) * int(line[2])
            print(f"{line[0]} - total ventas (EUR): {total}")
    print("\n")
    sleep(1)

def sales_management():
    file_path = "sales.txt"
    print("Bienvenido/a al programa de gestión de ventas")
    while True:
        option = input("¿Qué deseas hacer?\n A - Añadir Productos\n C - Consultar Productos\n U - Actualizar Productos\n V - Venta total por producto\n E - Eliminar Productos\n S - Salir\n Escribe tu opción ---> ").upper()
        if option == "A":
            add_products(file_path)
        elif option == "C":
            check_products(file_path)
        elif option == "U":
            update_products(file_path)
        elif option == "V":
            total_sales(file_path)
        elif option == "E":
            erase_products(file_path)
        elif option == "S":
            print("Gracias por usar nuestro sistema. Hasta pronto\n")
            try:
                remove(file_path)
            except:
                pass
            break
        else:
            print("La opcion es incorrecta, prueba de nuevo por favor\n")
            sleep(1)
        
sales_management()
