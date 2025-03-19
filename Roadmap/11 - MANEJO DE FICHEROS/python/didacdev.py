# ejecicio 1
import os

file = open("didacdev.txt", "w")

file.write("Diego Sánchez Escribano\n")
file.write("28 años\n")
file.write("Python")

file.close()

file = open("didacdev.txt", "r")

contenido = file.read()
print(contenido)

file.close()

os.remove(file.name)


# ejercicio 2
def start():

    while True:

        print("\nQué desea hacer:")
        print("1 - Añadir")
        print("2 - Consultar")
        print("3 - Actualizar")
        print("4 - Eliminar")
        print("5 - Salir")

        option: int = input("> ")

        match option:
            case "1":
                add()
            case "2":
                read()
            case "3":
                update()
            case "4":
                remove()
            case "5":
                print("Hasta pronto")
                break
            case _:
                print("Opción incorrecta")


def add():
    file = open("venta.txt", "a")

    product_name = input("\nNombre del producto: ")
    product_quantity = input("Unidades del producto: ")
    product_price = input("Precio del producto: ")

    file.write(f"{product_name} {product_quantity} {product_price}\n")

    file.close()


def read():
    print("\nProducto | Unidades | Precio")
    file = open("venta.txt", "r")

    for product_info in file:
        print(product_info)

    file.close()


def update():
    contenido = list()

    product_name = input("\nNombre del producto: ")
    product_quantity = input("Unidades del producto: ")
    product_price = input("Precio del producto: ")

    with open("venta.txt", "r+") as file:
        contenido = file.readlines()
        for product in contenido:
            name = product.split(" ")

            if name[0] == product_name:
                product_info = product_name + " " + product_quantity + " " + product_price + "\n"
                contenido[contenido.index(product)] = product_info

    with open("venta.txt", "w") as file:
        file.writelines(contenido)


def remove():
    contenido = list()

    product_name = input("\nNombre del producto: ")

    with open("venta.txt", "r+") as file:
        contenido = file.readlines()
        for product in contenido:
            name = product.split(" ")

            if name[0] == product_name:
                contenido.remove(product)

    with open("venta.txt", "w") as file:
        file.writelines(contenido)


start()
