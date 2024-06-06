'''
* IMPORTANTE: Solo debes subir el fichero de codigo como parte del ejercicio.
 * 
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo que se llame como
 * tu usuario de GitHub y tenga la extension .txt.
 * Añade varias lineas en ese fichero:
 * - Tu nombre.
 * - Edad.
 * - Lenguaje de programacion favorito.
 * Imprime el contenido.
 * Borra el fichero.
'''

import os

def crear_archivo():
    file = open("rantamhack.txt", "w")
    f = ["Me llamo Rantam\n", "Mi edad es de 25 años\n", "Mi lenguaje de programacion favorito es python\n"]
    file.writelines(f)
    file.close()
    print("\nEl archivo rantamhack.txt ha sido creado\n")
    
crear_archivo()
    
def leer_archivo():
    file = open("rantamhack.txt", "r")
    print(file.read())
    file.close()
    
leer_archivo()


def borrar_archivo():
    if os.path.exists("rantamhack.txt"):
        os.remove("rantamhack.txt")
        print("El archivo rantamhack.txt ha sido eliminado\n")
    else:
        print("El archivo no existe")
        
borrar_archivo()    

'''
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla un programa de gestion de ventas que almacena sus datos en un 
 * archivo .txt.
 * - Cada producto se guarda en una linea del arhivo de la siguiente manera:
 *   [nombre_producto], [cantidad_vendida], [precio].
 * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
 *   actualizar, eliminar productos y salir.
 * - Tambien debe poseer opciones para calcular la venta total y por producto.
 * - La opcion salir borra el .txt.
'''

store = "sales.txt"

open(store, "a")

def add_product():
    name = input("Nombre: ")
    quantity = input("Cantidad vendida: ")
    price = input("Precio: ")
    with open(store, "a") as file:
        file.write(f"{name}, {quantity}, {price}\n")
        
def consult_product():
    name = input("Nombre: ")
    with open(store, "r") as file:
        for line in file.readlines():
            if line.split(", ")[0] == name:
                print(line)
                break
            
def update_product():
    name = input("Nombre: ")
    quantity = input("Cantidad: ")            
    price = input("Precio: ")
    with open(store, "r") as file:
        lines = file.readlines()
    with open(store, "w") as file:
        for line in lines:
            if line.split(", ")[0] == name:
                file.write(f"{name}, {quantity}, {price}\n")
            else:
                file.write(line)
                
def delete_product():
    name = input("Nombre: ")
    with open(store, "r") as file:
        lines = file.readlines()
    with open(store, "w") as file:
        for line in lines:
            if line.split(", ")[0] != name:
                file.write(line)
                                    
def read_file():
    with open(store, "r") as file:
        print(file.read())
        
def product_sales():
    total = 0
    name = input("Nombre: ")
    with open(store, "r") as file:
        for line in file.readlines():
            if line.split(", ")[0] == name:
                quantity = float(line.split(", ")[1])
                price = float(line.split(", ")[2])
                total = quantity * price
                break
    print(f"\nEl total de las ventas de {name} es: {total}\n")
              
def total_sales():
    total = 0
    with open(store, "r") as file:
        for line in file.readlines():
            quantity = float(line.split(", ")[1])
            price = float(line.split(", ")[2])
            total += quantity * price
    print(f"\nEl total de las ventas es: {total}\n")
    
    

while True: 
    
    print("\nBienvenido al menu de opciones\n")

    print("1) Añadir producto")
    print("2) Consultar producto")
    print("3) Actualizar producto")
    print("4) Eliminar producto")
    print("5) Consultar archivo de productos")
    print("6) Calculadora de ventas por producto")    
    print("7) Calculadora de ventas totales")
    print("8) Salir")
    
    option = input("\nElige la opcion que quieres hacer: ")     
    
    if option == "1":
        add_product()
    elif option == "2":
        consult_product()
    elif option == "3":
        update_product()
    elif option == "4":
        delete_product()
    elif option == "5":
        read_file()
    elif option == "6":
        product_sales()
    elif option == "7":
        total_sales()
    elif option == "8":
        print("\n[+] Saliendo del programa....\n")
        os.remove("sales.txt")
        break
    else:
        print("\nLa opcion elegida no es correcta")
    
        
    
