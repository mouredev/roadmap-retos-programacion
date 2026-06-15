# Desarrolla un programa capaz de crear un archivo que se llame como tu usuario de Github y tenga la extension .txt

import os # Libreria para poder eliminar el fichero

with open("Ramirofordev.txt", "a") as f:
    for i in range(3):
        dato = input("Ingrese primero su nombre, despues su edad y por ultimo su lenguaje favorito: ")
        f.write(f"{dato}\n")

with open("Ramirofordev.txt", "r") as f:
    print(f.read())

ruta_archivo = "Ramirofordev.txt"

if os.path.exists(ruta_archivo):
    os.remove(ruta_archivo)

# Dificulatad extra gestor de ventas.

def menu():
    while True:
        opciones = int(input("""Elige una de las siguientes opciones:
        1. Añadir un producto.
        2. Consultar productos.
        3. Eliminar un producto.
        4. Actualizar un producto.
        5. Ventas por producto.
        6. Ventas totales.
        7. Mostrar el inventario.
        8. Salir:  \n"""))

        if opciones in [1, 2, 3, 4, 5, 6, 7]:
            functions(opciones)
        elif opciones == 8:
            print("Saliendo..")
            if os.path.exists("Ventas.txt"):
                os.remove("Ventas.txt")
            break
        else:
            print("Opcion no valida")

def añadir_producto():
    with open("Ventas.txt", "a") as f:
        nombre_producto = input("Inserte el nombre del producto: ")
        cantidad_vendida = input("Inserte la cantidad vendida: ")
        precio = input("Inserte el precio: ")
        f.write(f"{nombre_producto}, {cantidad_vendida}, {precio}\n")


def consultar_producto():
    producto = input("Inserte el nombre del producto que desea buscar: ")
    with open("Ventas.txt", "r") as f:
        for line in f.readlines():
            if line.split(", ")[0] == producto:
                print(line)
                break
            else:
                print("El producto no existe.")
            
def eliminar_producto():
    producto = input("Inserte el nombre del producto que desea eliminar: ")
    with open("Ventas.txt", "w+") as f:
        lines = f.readlines()
        for line in lines:
            if line.split(", ")[0] != producto:
                f.write(line)
    
def actualizar_producto():
    producto = input("Inserte el nombre del producto que desea actualizar: ") 
    with open("Ventas.txt", "w+") as f:
        lines = f.readlines()
        for line in lines:
            if line.split(", ")[0] == producto:
                nuevo_nombre = input("Inserte el nuevo nombre del producto: ")
                nueva_cantidad = input("Inserte la nueva cantidad vendida del producto: ")
                nuevo_precio = input("Inserte el nuevo precio del producto: ")
                f.write(f"{nuevo_nombre}, {nueva_cantidad}, {nuevo_precio}")

def ventas_producto():
    producto = input("Inserte el nombre del producto que desea saber su venta total: ")
    with open("Ventas.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            if line.split(", ")[0] == producto:
                cantidad = int(line.split(", ")[1])
                precio = float(line.split(", ")[2])
                print(f"La venta total del producto {producto} es de: {round(cantidad * precio)}")

def ventas_totales():
    with open("Ventas.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            cantidad = int(line.split(", ")[1])
            precio = float(line.split(", ")[2])
            total += cantidad * precio

        print(f"La venta total es de {total}")  

def mostrar_inventario():
    with open("Ventas.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            print(line)

def functions(o):
    dic = {
        1: añadir_producto,
        2: consultar_producto,
        3: eliminar_producto,
        4: actualizar_producto,
        5: ventas_producto,
        6: ventas_totales,
        7: mostrar_inventario
    }

    return dic[o]()

menu()