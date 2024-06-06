"""
    * #11 MANEJO DE FICHEROS
"""

import os


def crear_archivo():
    nombre = "cesar-ch"
    edad = 4
    lenguaje_favorito = "JavaScript"
    contenido = f"Nombre: {nombre}\nEdad: {edad}\nLenguaje de programación favorito: {lenguaje_favorito}"
    with open(f"{nombre}.txt", "w") as file:
        file.write(contenido)
    print(f"1. Archivo {nombre}.txt creado exitosamente")
    print("2. Contenido añadido al archivo")
    leer_archivo(nombre)


def leer_archivo(nombre):
    with open(f"{nombre}.txt", "r") as file:
        data = file.read()
        print("3. Contenido leído del archivo")
        print(data)
    borrar_archivo(nombre)


def borrar_archivo(nombre):
    os.remove(f"{nombre}.txt")
    print("4. Archivo eliminado exitosamente")
    menu()


"""
    * DIFICULTAD EXTRA
"""


def menu():
    print("\n=== Gestión de Ventas ===")
    print("1. Añadir producto")
    print("2. Consultar producto")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Calcular venta total")
    print("6. Calcular venta por producto")
    print("7. Salir")
    print("===========================")
    seleccionar_opcion()


def seleccionar_opcion():
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        añadir_producto()
    elif opcion == "2":
        consultar_producto()
    elif opcion == "3":
        actualizar_producto()
    elif opcion == "4":
        eliminar_producto()
    elif opcion == "5":
        calcular_venta_total()
    elif opcion == "6":
        calcular_venta_por_producto()
    elif opcion == "7":
        eliminar_archivo()
        exit()
    else:
        seleccionar_opcion()


def añadir_producto():
    nombre = input("Introduce el nombre del producto: ")
    cantidad = input("Introduce la cantidad del producto: ")
    precio = input("Introduce el precio del producto: ")
    producto = f"{nombre},{cantidad},{precio}\n"
    with open("productos.txt", "a") as file:
        file.write(producto)
    print("Producto añadido correctamente")
    file.close()
    menu()


def consultar_producto():
    nombre = input("Introduce el nombre del producto a consultar: ")
    with open("productos.txt", "r") as file:
        data = file.readlines()
        for producto in data:
            if producto.split(",")[0] == nombre:
                print(f"Producto encontrado: {producto.strip()}")
                file.close()
                menu()

        else:
            print("Producto no encontrado")
            menu()


def actualizar_producto():
    nombre = input("Introduce el nombre del producto a actualizar: ")
    cantidad = input("Introduce la nueva cantidad del producto: ")
    precio = input("Introduce el nuevo precio del producto: ")
    nuevo_producto = f"{nombre},{cantidad},{precio}\n"
    with open("productos.txt", "r") as file:
        data = file.readlines()
    with open("productos.txt", "w") as file:
        for producto in data:
            if producto.split(",")[0] == nombre:
                productosfiltrados = list(
                    filter(lambda x: x.split(",")[0] != nombre, data)
                )
                file.writelines(productosfiltrados)
                file.write(nuevo_producto)
                print("Producto actualizado correctamente")
                file.close()
                menu()
        else:
            print("Producto no encontrado")
            menu()


def eliminar_producto():
    nombre = input("Introduce el nombre del producto a eliminar: ")
    with open("productos.txt", "r") as file:
        data = file.readlines()
    with open("productos.txt", "w") as file:
        for producto in data:
            if producto.split(",")[0] != nombre:
                file.write(producto)
            else:
                print("Producto eliminado correctamente")
    file.close()
    menu()


def calcular_venta_total():
    total = 0
    with open("productos.txt", "r") as file:
        data = file.readlines()
        for producto in data:
            nombre, cantidad, precio = producto.split(",")
            total += int(cantidad) * float(precio)
    print(f"Venta total: {total}")
    file.close()
    menu()


def calcular_venta_por_producto():
    nombre = input("Introduce el nombre del producto a consultar: ")
    with open("productos.txt", "r") as file:
        data = file.readlines()
        for producto in data:
            if producto.split(",")[0] == nombre:
                nombre, cantidad, precio = producto.split(",")
                total = int(cantidad) * float(precio)
                print(f"Venta total: {total}")
                file.close()
                menu()
        else:
            print("Producto no encontrado")
            menu()


def eliminar_archivo():
    os.remove("productos.txt")
    print("Archivo eliminado correctamente")


if __name__ == "__main__":
    crear_archivo()
