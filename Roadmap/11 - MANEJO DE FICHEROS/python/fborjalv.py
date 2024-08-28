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
# import os 

# file_name = "fborjalv.txt"

# with open (file_name, "w") as file:
#     file.write("Borja LV\n")
#     file.write("32\n")
#     file.write("['Python','JavaScript']")
# with open (file_name, "r") as file: 
#     print(file.read())

# os.remove("fborjalv.txt")


"""
Desarrolla un programa de gestión de ventas que almacena sus datos en un 
 * archivo .txt.
 * - Cada producto se guarda en una línea del archivo de la siguiente manera:
 *   [nombre_producto], [cantidad_vendida], [precio].
 * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
 *   actualizar, eliminar productos y salir.
 * - También debe poseer opciones para calcular la venta total y por producto.
 * - La opción salir borra el .txt.
"""
file_name = "fborjalv_shop.txt"

open(file_name, "a")

while True: 
    print("1. Añadir producto ")
    print("2. Consultar productos ")
    print("3. Actualizar productos ")
    print("4. Eliminar productos ")
    print("5. Calcular la venta total ")
    print("6. Calcular ventas por producto ")
    print("7. Salir ")
    option = input("Introduce una opción ")

    if option == "1":
        product_name = input("Nombre del producto: ")
        amount = input("Cantidad: ")
        product_price = input("Precio: ")
        with open(file_name, "a") as file:
            file.write(f"{product_name}, {amount}, {product_price}\n")
    elif option == "2": 
        print("Mostrando todos los productos")
        with open(file_name, "r") as file:
            print(file.read())
    elif option == "3":
        product_update = input("Introduce el nombre del producto que deseas actualizar: ")
        with open(file_name, "r") as file:
            lines = file.readlines()
        with open(file_name, "w") as file: 
            for line in lines:
                if line.split(",")[0] == product_update:
                    amount_update = input("Introduce la cantidad de producto: ")
                    product_price = input("Introduce el precio del producto: ")
                    file.write(f"{product_update}, {amount_update}, {product_price}\n")
                else:
                    file.write(line)                
    elif option == "4": 
        detele_product = input("¿Qué producto deseas eliminar?") # misma lógica comprobar que tenemos en lines y que queremos mantener
        with open(file_name, "r") as file: 
            lines = file.readlines()
        with open(file_name, "w") as file:
            for item in lines: 
                if detele_product != item.split(",")[0]:
                    file.write(item)
    elif option == "5": 
        total = 0
        print(total)
        with open(file_name, "r") as file:
            lines = file.readlines()
        for item in lines:
            total += int(item.split(",")[1]) * float(item.split(",")[2])
        print(total)
    elif option == "6": 
        product_incomes = input("Introduce el nombre de un producto: ")
        with open(file_name, "r") as file: 
            lines = file.readlines()
        for item in lines: 
            if item.split(",")[0] == product_incomes:
                print(int(item.split(",")[1]) * float(item.split(",")[2]))
    elif option == "7":
        print("Saliendo del programa")
        break
    else:
        print("Ha seleccionado una opción no válida")