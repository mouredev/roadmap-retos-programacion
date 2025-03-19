'''
Desarrolla un programa capaz de crear un archivo que se llame como
  tu usuario de GitHub y tenga la extensión .txt.
  Añade varias líneas en ese fichero:
  - Tu nombre.
  - Edad.
  - Lenguaje de programación favorito.
  Imprime el contenido.
  Borra el fichero.
'''

import os

def crear_archivo(usuario):
    # Crear el archivo con el nombre de usuario.txt
    nombre_archivo = usuario + ".txt"
    with open(nombre_archivo, "w") as archivo:
        archivo.write("Nombre: {}\n".format(input("Introduce tu nombre: ")))
        archivo.write("Edad: {}\n".format(input("Introduce tu edad: ")))
        archivo.write("Lenguaje de programación favorito: {}\n".format(input("Introduce tu lenguaje de programación favorito: ")))
    return nombre_archivo

def leer_archivo(nombre_archivo):
    # Leer y mostrar el contenido del archivo
    with open(nombre_archivo, "r") as archivo:
        contenido = archivo.read()
        print("Contenido del archivo:")
        print(contenido)

def borrar_archivo(nombre_archivo):
    # Borrar el archivo
    os.remove(nombre_archivo)
    print("Archivo {} borrado.".format(nombre_archivo))

def main():
    usuario = input("Introduce tu nombre de usuario de GitHub: ")
    nombre_archivo = crear_archivo(usuario)
    leer_archivo(nombre_archivo)
    borrar_archivo(nombre_archivo)

if __name__ == "__main__":
    main()

'''
DIFICULTAD EXTRA (opcional):
  Desarrolla un programa de gestión de ventas que almacena sus datos en un 
  archivo .txt.
  - Cada producto se guarda en una línea del archivo de la siguiente manera:
    [nombre_producto], [cantidad_vendida], [precio].
  - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
    actualizar, eliminar productos y salir.
  - También debe poseer opciones para calcular la venta total y por producto.
  - La opción salir borra el .txt.
'''

import os

def guardar_venta(nombre_archivo, producto, cantidad, precio):
    # Guardar la venta en el archivo
    with open(nombre_archivo, "a") as archivo:
        archivo.write("{},{},{}\n".format(producto, cantidad, precio))

def consultar_ventas(nombre_archivo):
    # Consultar todas las ventas en el archivo
    with open(nombre_archivo, "r") as archivo:
        contenido = archivo.read()
        print("Ventas:")
        print(contenido)

def calcular_venta_total(nombre_archivo):
    # Calcular la venta total
    venta_total = 0
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            _, cantidad, precio = linea.strip().split(",")
            venta_total += int(cantidad) * float(precio)
    return venta_total

def calcular_venta_producto(nombre_archivo, producto):
    # Calcular la venta total de un producto
    venta_producto = 0
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            nombre, cantidad, precio = linea.strip().split(",")
            if nombre == producto:
                venta_producto += int(cantidad) * float(precio)
    return venta_producto

def actualizar_venta(nombre_archivo, producto, cantidad, precio):
    # Actualizar una venta existente o añadir una nueva
    ventas = []
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            nombre, _, _ = linea.strip().split(",")
            if nombre == producto:
                ventas.append("{},{},{}".format(producto, cantidad, precio))
            else:
                ventas.append(linea.strip())

    with open(nombre_archivo, "w") as archivo:
        archivo.write("\n".join(ventas))

def eliminar_venta(nombre_archivo, producto):
    # Eliminar una venta
    ventas = []
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            nombre, _, _ = linea.strip().split(",")
            if nombre != producto:
                ventas.append(linea.strip())

    with open(nombre_archivo, "w") as archivo:
        archivo.write("\n".join(ventas))

def main():
    nombre_archivo = "ventas.txt"

    while True:
        print("\n--- Menú ---")
        print("1. Añadir venta")
        print("2. Consultar ventas")
        print("3. Calcular venta total")
        print("4. Calcular venta por producto")
        print("5. Actualizar venta")
        print("6. Eliminar venta")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            producto = input("Nombre del producto: ")
            cantidad = input("Cantidad vendida: ")
            precio = input("Precio: ")
            guardar_venta(nombre_archivo, producto, cantidad, precio)
            print("Venta añadida con éxito.")
        elif opcion == "2":
            consultar_ventas(nombre_archivo)
        elif opcion == "3":
            venta_total = calcular_venta_total(nombre_archivo)
            print("Venta total: ${:.2f}".format(venta_total))
        elif opcion == "4":
            producto = input("Nombre del producto: ")
            venta_producto = calcular_venta_producto(nombre_archivo, producto)
            print("Venta de {}: ${:.2f}".format(producto, venta_producto))
        elif opcion == "5":
            producto = input("Nombre del producto a actualizar: ")
            cantidad = input("Nueva cantidad vendida: ")
            precio = input("Nuevo precio: ")
            actualizar_venta(nombre_archivo, producto, cantidad, precio)
            print("Venta actualizada con éxito.")
        elif opcion == "6":
            producto = input("Nombre del producto a eliminar: ")
            eliminar_venta(nombre_archivo, producto)
            print("Venta eliminada con éxito.")
        elif opcion == "7":
            # Borrar el archivo y salir
            os.remove(nombre_archivo)
            print("Archivo {} borrado. ¡Hasta luego!".format(nombre_archivo))
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
