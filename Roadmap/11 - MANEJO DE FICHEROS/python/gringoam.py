import os

"""
Ejercicio
"""

""" file_name = "mouredev.txt"

with open(file_name, "w") as file:
    file.write("Brais Moure\n")
    file.write("36\n")
    file.write("Python")

with open(file_name, "r") as file:
    print(file.read())

os.remove(file_name) """

"""
Extra
"""

file_name = "gringoam_shop.txt"

open(file_name, "a")

def agregar_producto(nombre, cantidad_vendida, precio):
    with open(file_name, "a") as file:
        file.write(f"{nombre},{cantidad_vendida},{precio}\n")

def consulta_prod(nombre):
    encontrado=""
    with open(file_name, "r") as file:
        for line in file.readlines():
           
            if line.split(",")[0]== nombre:
                encontrado=line
                print(line)
                break
        if encontrado=="":
            print("no se encontró producto")
        else:
            print(encontrado)

def actualizar_producto(nombre, cantidad_vendida, precio):
    with open(file_name, "r") as file:
        lines=file.readlines()
    with open(file_name,"w") as file:
        for line in lines:
           if line.split(",")[0]== nombre:
                file.write(f"{nombre},{cantidad_vendida},{precio}\n")
           else:
                file.write(line)

def borrar_producto(nombre):
    with open(file_name, "r") as file:
        lines=file.readlines()
    with open(file_name,"w") as file:
        for line in lines:
           if line.split(",")[0]== nombre:
                print(f"Producto: {nombre} borrado\n")
           else:
                file.write(line)

def mostrar_productos():
    
    with open(file_name, "r") as file:
            print(file.read())

def ventas_totales():
    total=0
    with open(file_name, "r") as file:
        for line in file.readline():
            venta=line.split(",")
            cantidad=int(venta[1])
            precio=float (venta[2])
            total+=cantidad * precio
    print(f"Total de ventas en pesos: {total}")                

def venta_por_producto():
    pass

while True:
    print("1. Añadir producto")
    print("2. Consultar producto")
    print("3. Actualizar producto")
    print("4. Borrar producto")
    print("5. Mostrar productos")
    print("6. Calcular venta total")
    print("7. Calcular venta por producto")
    print("8. Salir\n")

    op = input("Selecciona una opción: ")
    
    match op:
        case "1":
            nombre=input("Nombre: ")
            cantidad_vendida=input("Catidad vendida: ")
            precio=input("Precio: \n")
            agregar_producto(nombre, cantidad_vendida, precio)

        case "2":
             nombre=input("Nombre: ")
             consulta_prod(nombre)

        case "3":
            nombre=input("Nombre: ")
            cantidad_vendida=input("Catidad vendida: ")
            precio=input("Precio: \n")
            actualizar_producto(nombre, cantidad_vendida, precio)
        case "4":
            nombre=input("Nombre: ")
            borrar_producto(nombre)
        case "5":
            mostrar_productos()

        case "6":
            ventas_totales()
        case "7":
            venta_por_producto()
        case "8":
            os.remove(file_name)
            break



