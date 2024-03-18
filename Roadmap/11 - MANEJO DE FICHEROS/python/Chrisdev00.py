"""
* IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
* 
* EJERCICIO:
* Desarrolla un programa capaz de crear un archivo que se llame como
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
* - Cada producto se guarda en una línea del arhivo de la siguiente manera:
*   [nombre_producto], [cantidad_vendida], [precio].
* - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
*   actualizar, eliminar productos y salir.
* - También debe poseer opciones para calcular la venta total y por producto.
* - La opción salir borra el .txt.
"""
import os

def crear_archivo(user_github):

    nombre_archivo = f"{user_github}.txt"

    lineas = [
        "Nombre: Christian",
        "Edad: 30",
        "Lenguaje de programacion favorito: Python"        
    ]

    with open(nombre_archivo, "w") as file:
        for linea in lineas:
            file.write(linea + "\n")

    print(f"Contenido del archivo {nombre_archivo}:\n")

    with open(nombre_archivo, "r") as file:
        for linea in file:
            print(linea.strip())

    os.remove(nombre_archivo)
    print(f"\nEl archivo {nombre_archivo} ha sido borrado.")

if __name__=="__main__":
    usuario = "Chrisdev00"
    crear_archivo(usuario)



########  --------------------------  EXTRA  ------------------------------  ###############
    
import os

def agregar_producto(archivo):

    nombre = input("Nombre del producto: ")
    cantidad = int(input("Cantidad vendida: "))
    precio = float(input("Precio por unidad: "))

    with open(archivo, "a") as file:
        file.write(f"{nombre}, {cantidad}, {precio}\n")

    print("Producto añadido correctamente.\n")

def consultar_ventas(archivo):

    print("ventas registradas:")
    with open(archivo, "r") as file:
        for linea in file:
            print(linea.strip())

def actualizar_producto (archivo):

    producto_actualizar = input("Ingrese el nombre del producto a actualizar: ")
    nueva_cantidad = int(input("Ingrese la nueva cantidad vendida: "))
    nuevo_precio = float(input("Ingrese el nuevo precio: "))

    with open(archivo, "r") as file:
        lineas = file.readlines()

    with open(archivo, "w") as file:
        for linea in lineas:
            producto, cantidad, precio = linea.strip().split(', ')
            if producto == producto_actualizar:
                cantidad = str(nueva_cantidad)
                precio = str(nuevo_precio)
            file.write(f"{producto}, {cantidad}, {precio}\n")

    print("Producto actualizado correctamente.\n")

def eliminar_producto(archivo):

    producto_eliminar = input("Ingrese el nombre del producto a eliminar: ")

    with open(archivo, "r") as file:
        lineas = file.readlines()

    with open(archivo, "w") as file:
        for linea in lineas:
            producto, _, _ = linea.strip().split(', ')
            if producto != producto_eliminar:
                file.write(linea)

    print("Producto eliminado correctamente.\n")

def venta_total (archivo):

    total = 0
    with open(archivo, "r") as file:
        for linea in file:
            _, cantidad, precio = linea.strip().split(', ')
            total += int(cantidad) * float(precio)

    print(f"La venta total es: ${total:.2f}\n")

def venta_producto (archivo):

    producto_consultar = input("Ingrese el nombre del producto: ")

    with open(archivo, 'r') as file:
        for linea in file:
            producto, cantidad, precio = linea.strip().split(', ')
            if producto == producto_consultar:
                total = int(cantidad) * float(precio)
                print(f"Venta de {producto}: {total:.2f}\n")
                return
            
        print("Producto no encontrado.\n")

def main():

    archivo = "ventas.txt"

    while  True:
        print("======= Gestión de Ventas =======")
        print("1. Añadir producto")
        print("2. Consultar ventas")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Venta total")
        print("6. Venta por producto")
        print("7. Salir")

        option = input("Seleccione una opcion: ")

        if option == "1":
            agregar_producto(archivo)
        elif option == "2":
            consultar_ventas(archivo)
        elif option == "3":
            actualizar_producto(archivo)
        elif option == "4":
            eliminar_producto(archivo)
        elif option == "5":
            venta_total(archivo)
        elif option == "6":
            venta_producto(archivo)
        elif option == "7":
            os.remove(archivo)
            print("Gracias por utilizar el sistema")
            break
        else:
            print("Opcion invalida. Porfavor seleccione una opcion valida.\n")

if __name__== "__main__":
    main()

