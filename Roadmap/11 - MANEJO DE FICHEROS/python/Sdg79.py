"""* IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
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
"""
 
import os

archivo = open("c:/Users/SergioDGiovagnoli/Documents/Python/Curso_Mouredev/Sdg79.txt", "w+")
archivo.write("Sergio\n46\nPython")
archivo.seek(0)
print(archivo.read())
#for i in archivo.readlines():
#    print(i)
archivo.close()

if os.path.exists("c:/Users/SergioDGiovagnoli/Documents/Python/Curso_Mouredev/Sdg79.txt"):
    os.remove("c:/Users/SergioDGiovagnoli/Documents/Python/Curso_Mouredev/Sdg79.txt")
else:
    print("El archivo no existe")


# DIFICULTAD EXTRA:
"""* Desarrolla un programa de gestión de ventas que almacena sus datos en un 
 * archivo .txt.
 * - Cada producto se guarda en una línea del archivo de la siguiente manera:
 *   [nombre_producto], [cantidad_vendida], [precio].
 * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
 *   actualizar, eliminar productos y salir.
 * - También debe poseer opciones para calcular la venta total y por producto.
 * - La opción salir borra el .txt.
 """
import os

path = "c:/Users/SergioDGiovagnoli/Documents/Python/Curso_Mouredev/ventas.txt"

while True:
    opcion = input("""Seleccione la opcion deseada:
                    1. Añadir producto
                    2. Consultar producto
                    3. Actualizar producto
                    4. Eliminar producto
                    5. Calcular venta total
                    6. Calcular venta por producto
                    7. Salir
                    """)
    match opcion:
        case "1":
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = input("Ingrese la cantidad vendida: ")
            precio = input("Ingrese el precio del producto: ")
            existe = os.path.exists(path)
            ventas_txt = open(path, "a")
            ventas_txt.write(f"{nombre}, {cantidad}, {precio}\n")
            ventas_txt.close()

        case "2":
            ventas_txt = open(path, "r")
            print(ventas_txt.read())
            nombre = input("Ingrese el nombre del producto a consultar: ")
            ventas_txt.seek(0)
            for linea in ventas_txt.readlines():
                if linea.split(", ")[0] == nombre:
                    print(linea)
                    break
            ventas_txt.close()
            
        case "3":
            ventas_txt = open(path, "r")
            print(ventas_txt.read())
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = input("Ingrese la cantidad vendida: ")
            precio = input("Ingrese el precio del producto: ")       
            ventas_txt.seek(0)
            lineas = ventas_txt.readlines()
            ventas_txt = open(path, "w")
            for linea in lineas:
                if linea.split(", ")[0] == nombre:
                    ventas_txt.write(f"{nombre}, {cantidad}, {precio}\n")
                else:
                    ventas_txt.write(linea)
                    break
            ventas_txt.close()

        case "4":
            ventas_txt = open(path, "r")
            print(ventas_txt.read())
            nombre = input("Ingrese el nombre del producto a eliminar: ")
            ventas_txt.seek(0)
            lineas = ventas_txt.readlines()
            ventas_txt = open(path, "w")
            for linea in lineas:
                if linea.split(", ")[0] == nombre:
                    continue
                else:
                    ventas_txt.write(linea)
                    break
            ventas_txt.close()

        case "5":
            total = 0
            ventas_txt = open(path, "r")
            ventas_txt.seek(0)
            for linea in ventas_txt.readlines():
                total += (int(linea.split(", ")[1]) * float(linea.split(", ")[2]))
            print(f"La venta total asciende a: {total}")
            ventas_txt.close()

        case "6":
            ventas_txt = open(path, "r")
            print(ventas_txt.read())
            nombre = input("Ingrese el nombre del producto a consultar ventas: ")
            ventas_txt.seek(0)
            for linea in ventas_txt.readlines():
                if linea.split(", ")[0] == nombre:
                    print((int(linea.split(", ")[1])) * float(linea.split(", ")[2]))
                    break
            ventas_txt.close()

        case "7":
            if os.path.exists(path):
                os.remove(path)
            else:
                print("El archivo no existe")
            break
        case _:
            print("Opción no válida. Elige una opción de la lista.")
