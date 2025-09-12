#Reto 11

''' * Desarrolla un programa capaz de crear un archivo que se llame como
* tu usuario de GitHub y tenga la extensión .txt.
* Añade varias líneas en ese fichero:
* - Tu nombre.
* - Edad.
* - Lenguaje de programación favorito.
* Imprime el contenido.
* Borra el fichero.
*
* DIFICULTAD EXTRA (opcional):
* Desarrolla un programa de gestión de ventas que almacena sus datos en un 
* archivo .txt.
* - Cada producto se guarda en una línea del archivo de la siguiente manera:
*   [nombre_producto], [cantidad_vendida], [precio].
* - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
*   actualizar, eliminar productos y salir.
* - También debe poseer opciones para calcular la venta total y por producto.
* - La opción salir borra el .txt.
*/'''

import os

txt_file = open("C-Gabs.txt","w+")
txt_file.write("Gabriel\n35\nPython")
txt_file.close()
txt_file = open("C-Gabs.txt","r+")
for line in txt_file.readlines():
    print(line)
txt_file.close()
os.remove("C-Gabs.txt")


#Reto extra
try:
    txt_file = open("productos.txt","x")
    txt_file.close()
except FileExistsError:
    print("El archivo ya existe")

while True:

    print("")
    print("1. Añadir producto")
    print("2. Consultar producto")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Calcular venta total")
    print("6. Calcular venta por producto")
    print("7. Salir")

    opcion = input("Elija una opción: ")
    match opcion:
        case "1":
            with open("productos.txt","a") as txt_file:
                producto = input("Ingrese el nombre del producto: ")
                cantidad_vendida = input("Ingrese la cantidad vendida: ")
                precio = input("Ingrese el precio: ")
                txt_file.write(f"{producto}, {cantidad_vendida}, {precio}\n")
        case "2":
            with open("productos.txt","r") as txt_file:
                producto = input("Ingrese el nombre del producto: ")
                for line in txt_file.readlines():
                    if producto in line:
                        print(line)
                        break
                    else:
                        print("El producto no figura en el archivo")
                else:
                    print("El archivo está vacio")

        case "3":
            with open("productos.txt","r") as txt_file:
                producto = input("Ingrese el nombre del producto: ")
                cantidad_vendida = input("Ingrese la nueva cantidad vendida: ")
                precio = input("Ingrese el nuevo precio: ")
                product_list = txt_file.readlines()
            with open("productos.txt","w") as txt_file:
                for line in product_list:
                    if producto in line:
                        txt_file.write(f"{producto}, {cantidad_vendida}, {precio}\n")
                    else:
                        txt_file.write(line)
        case "4":
            with open("productos.txt","r") as txt_file:
                producto = input("Ingrese el nombre del producto: ")
                product_list = txt_file.readlines()
            with open("productos.txt","w") as txt_file:
                for line in product_list:
                    if producto not in line:
                        print(f"El producto {producto} se ha eliminado")
                        txt_file.write(line)
        case "5":
            with open("productos.txt","r") as txt_file:
                venta_total = 0
                for line in txt_file.readlines():
                    if len(line) > 1:
                        line = line.replace("\n","").split(", ")
                        venta_total = venta_total + int(line[1])*int(line[2])
                print(f"Venta total: {venta_total}")
        case "6":
            with open("productos.txt","r") as txt_file:
                for line in txt_file.readlines():
                    if len(line) > 1:
                        line = line.replace("\n","").split(",")
                        venta_producto = int(line[1])*int(line[2])
                        print(f"Venta del producto {line[0]}: {venta_producto}")
        case "7":
            os.remove("productos.txt")
            print("Finalizando el programa")
            break
        case _:
            print("Esta opción no es válida")
