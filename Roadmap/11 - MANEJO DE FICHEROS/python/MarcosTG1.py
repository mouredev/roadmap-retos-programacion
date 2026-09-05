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
"""

import os

try:
    # Creación delicada, en caso de que el fichero ya exista devuelve un FileExistsError
    file_1 = open("MarcosTG1.txt", "x", encoding="utf-8") 
except FileExistsError:
    print(f"El archivo ya existe con ese nombre.")


with open("MarcosTG1.txt", "r+") as f:

    f.seek(0, 2) # Devolver el cursor a la última posición del fichero para escribir y acumular
                 # Desplazándose 0 bytes de esa posición

    f.writelines("\nMarcos\n")
    print(f.tell())
    f.writelines("21\n")
    print(f.tell())
    f.writelines("Python")
    last_wrote = f.tell()
    print(last_wrote)

    print("")
    f.seek(0, 0) # Devolver el cursos a la primera posición del fichero para leer
    print(f.tell())

    print(f.read())
    print("")

# with open("MarcosTG2.txt", "r+") as f:
#     pass

os.remove("MarcosTG1.txt")

# f.read() ----- No se pueden hacer operaciones en fichero ya cerrado

"""
* DIFICULTAD EXTRA (opcional):
* Desarrolla un programa de gestión de ventas que almacena sus datos en un 
* archivo .txt.
* - Cada producto se guarda en una línea del archivo de la siguiente manera:
*   [nombre_producto], [cantidad_vendida], [precio].
* - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
*   actualizar, eliminar productos y salir.
* - También debe poseer opciones para calcular la venta total y por producto.
* - La opción salir borra el .txt.
"""

# print("       hola cola como te va0      ".strip())

def pedir_cantidad():
    while True:
        try:
            cantidad_vendida = int(input("¿Cuántas ventas ha tenido?\n"))
            if cantidad_vendida >= 0:
                return cantidad_vendida
            print("Debes introducir una cantidad mayor o igual a 0.")
        except ValueError:
            print("Debes introducir un número entero válido.")


def pedir_precio():
    while True:
        try:
            precio = float(input("¿Cuánto cuesta?\n"))
            if precio >= 0:
                return precio
            print("Debes introducir un precio mayor o igual a 0.")
        except ValueError:
            print("Debes introducir un número válido (ej: 15 o 15.50).")


def add():
    while True:
        nombre_producto = input("¿Qué producto quieres añadir?\n").strip()
        if nombre_producto:
            break
        print("Debes introducir un nombre válido.")

    cantidad_vendida = pedir_cantidad()
    precio = pedir_precio()

    return nombre_producto, cantidad_vendida, precio


# Garantizamos que el fichero existe antes de abrirlo en modo "r+"
if not os.path.exists("gestion_file_sales.txt"):
    open("gestion_file_sales.txt", "w", encoding="utf-8").close()

with open("gestion_file_sales.txt", mode="r+", encoding="utf-8") as file:

    running = True

    while running:

        print("Pulsa 1 para añadir")
        print("Pulsa 2 para consultar")
        print("Pulsa 3 para actualizar")
        print("Pulsa 4 para eliminar")
        print("Pulsa 5 para salir")
        print("Pulsa 6 para calcular los ingresos totales")
        print("Pulsa 7 para calcular los ingresos de un producto")
        print("\n")

        try:
            opcion = int(input(""))
        except ValueError:
            print("Opción no válida. Introduce un número del 1 al 5.\n")
            continue

        match opcion:

            case 1:
                file.seek(0, 2) # Desplazar cursor al final del fichero para no sobreescribir
                nombre_producto, cantidad_vendida, precio = add()
                file.write(f"{nombre_producto}, {cantidad_vendida}, {precio}\n")
                print("Producto añadido exitosamente.")
            case 2:
                file.seek(0, 0)
                contenido = file.read()
                if contenido.strip():
                    print(contenido)
                else:
                    print("El registro de ventas está vacío.")
            case 3:
                nombre_producto_actualizar = input("¿Qué producto quieres actualizar?\n").strip()
                file.seek(0, 0)
                lines = file.readlines()

                if any(line.strip().split(", ")[0] == nombre_producto_actualizar for line in lines):
                    print(f"Introduce los nuevos datos para '{nombre_producto_actualizar}':")
                    cantidad_vendida = pedir_cantidad()
                    precio = pedir_precio()

                    file.seek(0, 0)
                    file.truncate(0)

                    for line in lines:
                        if nombre_producto_actualizar == line.strip().split(", ")[0]:
                            file.write(f"{nombre_producto_actualizar}, {cantidad_vendida}, {precio}\n")
                        else:
                            file.write(line)
                    print("Producto actualizado exitosamente.")
                else:
                    print(f"El producto '{nombre_producto_actualizar}' no existe.")

            case 4:
                nombre_producto_eliminar = input("¿Qué producto quieres eliminar?\n").strip()
                file.seek(0, 0)
                lines = file.readlines()

                if any(line.strip().split(", ")[0] == nombre_producto_eliminar for line in lines):
                    
                    file.seek(0, 0)
                    file.truncate() 

                    for line in lines:
                        if line.strip().split(", ")[0] == nombre_producto_eliminar:
                            pass
                        else:
                            file.write(line)
                else:
                    print(f"El producto '{nombre_producto_eliminar}' no existe.")

            case 5:
                running = False
            
            case 6:
                file.seek(0, 0)
                lines = file.readlines()

                facturacion = 0

                for line in lines:
                    cantidad = int(line.strip().split(", ")[1])
                    precio = float((line.strip().split(", ")[2]))
                    facturacion += cantidad * precio
                
                print(f"La facturación total es de {facturacion} euros.")

            case 7:
                file.seek(0, 0)
                lines = file.readlines()
                file.seek(0, 0)

                nombre_producto_calcular_facturacion = str(input("¿De qué producto quieres calcular la facturación?\n"))
                facturacion_producto = 0

                if any(line.strip().split(", ")[0] == nombre_producto_calcular_facturacion for line in lines):
                    for line in lines:
                        if line.strip().split(", ")[0] == nombre_producto_calcular_facturacion:
                            cantidad = int(line.strip().split(", ")[1])
                            precio = float(line.strip().split(", ")[2])
                            facturacion_producto = cantidad * precio
                        else:
                            pass
                    print(f"El producto ha facturado un total de {facturacion_producto} euros.")

                else:
                    print("No existe ningún producto con ese nombre.")
            case _:
                print("Opción no válida. Selecciona un número del 1 al 5.")

# Al salir del bloque 'with', el archivo se ha cerrado y se puede borrar sin conflictos
if os.path.exists("gestion_file_sales.txt"):
    os.remove("gestion_file_sales.txt")

print("Programa de ventas borrado satisfactoriamente.")

