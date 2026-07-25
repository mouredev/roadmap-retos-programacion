# Importamos el módulo os, que permite interactuar con el sistema operativo (por ejemplo: borrar archivos)
import os

"""
Ficheros
"""
file_name = "Complex_303"  # Definimos el nombre del archivo que se va a crear, leer y luego borrar

# Comentario de ejemplo de cómo se podría abrir un archivo sin 'with'
# open(file_name, "w") # No se cierra automáticamente y es menos seguro

# Aquí abrimos (o creamos) el archivo en modo escritura ("w") usando with, que cierra el archivo automáticamente al salir del bloque
with open(file_name, "w") as file:
    file.write("Complex_303\n")  # Escribe la cadena "Complex_303" y un salto de línea
    file.write("24\n")           # Escribe la cadena "24" y un salto de línea
    file.write("Python")         # Escribe la cadena "Python" sin salto de línea

# Ahora volvemos a abrir el mismo archivo, pero en modo lectura ("r") para leer su contenido
with open(file_name, "r") as file:
    print(file.read())  # Leemos todo el contenido del archivo y lo mostramos por pantalla

# Finalmente, usamos os.remove() para borrar el archivo del sistema
os.remove(file_name)


""" * DIFICULTAD EXTRA (opcional):
 * Desarrolla un programa de gestión de ventas que almacena sus datos en un 
 * archivo .txt.
 * - Cada producto se guarda en una línea del archivo de la siguiente manera:
 *   [nombre_producto], [cantidad_vendida], [precio].
 * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
 *   actualizar, eliminar productos y salir.
 * - También debe poseer opciones para calcular la venta total y por producto.
 * - La opción salir borra el .txt."""


# Definimos el nombre del archivo donde se almacenarán los productos
file_name = "Complex_303_productos"

# Creamos (si no existe) el archivo en modo añadir ('a'), y lo cerramos inmediatamente
open(file_name, 'a')

# Iniciamos un bucle infinito para mostrar un menú hasta que el usuario decida salir
while True:
    # Mostramos el menú de opciones en consola
    print("1. Añadir producto")
    print("2. Consultar producto")
    print("3. Actualizar producto")
    print("4. Borrar producto")
    print("5. Mostrar productos")
    print("6. Calcular venta total")
    print("7. Calcular venta por producto")
    print("8. Salir")

    # Pedimos al usuario que ingrese una opción del menú
    option = int(input("Seleccione una opcion: "))

    # OPCIÓN 1: Añadir un producto
    if option == 1:
        # Pedimos al usuario los datos del producto
        name = input("Nombre: ")
        quantity = input("Cantidad: ")
        precio = input("Indique el precio: ")

        # Abrimos el archivo en modo añadir ('a') para escribir al final del archivo
        with open(file_name, "a") as file:
            # Guardamos el producto en una línea con el formato: nombre, cantidad, precio
            file.write(f"{name}, {quantity}, {precio}\n")

    # OPCIÓN 2: Consultar un producto por su nombre
    elif option == 2:
        name = input("Nombre: ")
        found = False  # Variable para saber si se encontró o no el producto
        with open(file_name, "r") as file:
            for line in file.readlines():  # Leemos todas las líneas una por una
                if line.split(", ")[0] == name:  # Comparamos el nombre del producto (que está en la primera posición)
                    print(line)  # Mostramos la línea completa
                    found = True
        if not found:
            print("Producto no encontrado")  # Solo muestra si no se encontró nada

    # OPCIÓN 3: Actualizar un producto existente
    elif option == 3:
        name = input("Nombre: ")
        quantity = input("Cantidad: ")
        precio = input("Indique el precio: ")

        # Leemos todas las líneas del archivo
        with open(file_name, "r") as file:
            lines = file.readlines()

        # Reescribimos el archivo completo
        with open(file_name, "w") as file:
            for line in lines:
                if line.split(", ")[0] == name:
                    # Si el nombre coincide, escribimos los nuevos datos
                    file.write(f"{name}, {quantity}, {precio}\n")
                else:
                    # Si no coincide, dejamos la línea tal como estaba
                    file.write(line)

    # OPCIÓN 4: Borrar un producto por su nombre
    elif option == 4:
        name = input("Nombre: ")
        found = False  # Variable para indicar si se eliminó algo o no

        # Leemos todas las líneas
        with open(file_name, "r") as file:
            lines = file.readlines()

        # Reescribimos el archivo sin las líneas del producto a borrar
        with open(file_name, "w") as file:
            for line in lines:
                if line.split(", ")[0] != name:
                    file.write(line)  # Escribimos las líneas que no coinciden
                else:
                    found = True  # Marcamos que se encontró y eliminó
        if not found:
            print("Producto no encontrado")  # Mostramos este mensaje solo si no se encontró

    # OPCIÓN 5: Mostrar todos los productos
    elif option == 5:
        with open(file_name, "r") as file:
            print(file.read())  # Leemos y mostramos todo el contenido del archivo

    # OPCIÓN 6: Calcular el total de todas las ventas
    elif option == 6:
        total = 0  # Inicializamos el total en cero
        with open(file_name, "r") as file:
            for line in file.readlines():
                components = line.split(", ")  # Dividimos cada línea en nombre, cantidad, precio
                quantity = int(components[1])  # Convertimos la cantidad a entero
                price = float(components[2])  # Convertimos el precio a decimal
                total += quantity * price  # Sumamos el total de cada producto (cantidad × precio)
        print(f"Total: {total}")  # Mostramos el total

    # OPCIÓN 7: Calcular la venta total de un producto específico
    elif option == 7:
        name = input("Nombre: ")
        total = 0
        with open(file_name, "r") as file:
            for line in file.readlines():
                components = line.split(", ")
                if components[0] == name:
                    quantity = int(components[1])
                    price = float(components[2])
                    total = quantity * price  # Calculamos el total de ese producto
                    break  # Ya que el producto se encontró, salimos del bucle
        print(f"Total: {total}")  # Mostramos el total del producto

    # OPCIÓN 8: Salir del programa
    elif option == 8:
        os.remove(file_name)  # Eliminamos el archivo antes de salir
        break  # Rompemos el bucle para terminar el programa

    #Si el usuario ingresa una opción que no existe
    else:
        print("Elegi una opcion valida")  # Mostramos mensaje de error


"""
Otra forma mas optima
"""

import os  # Importamos el módulo os para operaciones con el sistema (como eliminar archivos)

# 📌 Nombre del archivo donde se almacenarán los productos
file_name = "Complex_303_productos"

# 📌 Si el archivo no existe, lo creamos vacío para evitar errores al intentar abrirlo después
if not os.path.exists(file_name):
    open(file_name, 'w').close()

# 📦 Función para cargar todos los productos desde el archivo a una lista en memoria
def cargar_productos():
    productos = []  # Lista vacía para almacenar los productos
    with open(file_name, "r") as file:
        for line in file:
            # Cada línea se divide en nombre, cantidad y precio, separados por ", "
            name, quantity, price = line.strip().split(", ")
            # Se almacena como un diccionario
            productos.append({"name": name, "quantity": int(quantity), "price": float(price)})
    return productos

# 💾 Función para guardar todos los productos desde la lista al archivo
def guardar_productos(productos):
    with open(file_name, "w") as file:
        for p in productos:
            # Cada producto se guarda como una línea en formato: nombre, cantidad, precio
            file.write(f"{p['name']}, {p['quantity']}, {p['price']}\n")

# 📋 Función para mostrar el menú de opciones
def mostrar_menu():
    print("""
1. Añadir producto
2. Consultar producto
3. Actualizar producto
4. Borrar producto
5. Mostrar productos
6. Calcular venta total
7. Calcular venta por producto
8. Salir
""")

# ➕ Añadir producto nuevo a la lista
def añadir_producto(productos):
    name = input("Nombre: ")
    quantity = int(input("Cantidad: "))
    price = float(input("Precio: "))
    # Añadimos el producto como un diccionario a la lista
    productos.append({"name": name, "quantity": quantity, "price": price})
    print("✅ Producto añadido.")

# 🔍 Consultar un producto por nombre
def consultar_producto(productos):
    name = input("Nombre: ")
    for p in productos:
        if p["name"] == name:
            print(f"{p['name']}, {p['quantity']}, {p['price']}")
            return  # Salimos si se encuentra
    print("❌ Producto no encontrado.")

# 🛠️ Actualizar datos de un producto existente
def actualizar_producto(productos):
    name = input("Nombre: ")
    for p in productos:
        if p["name"] == name:
            # Solicitamos nuevos valores y los actualizamos
            p["quantity"] = int(input("Nueva cantidad: "))
            p["price"] = float(input("Nuevo precio: "))
            print("✅ Producto actualizado.")
            return
    print("❌ Producto no encontrado.")

# ❌ Borrar un producto de la lista
def borrar_producto(productos):
    name = input("Nombre: ")
    for p in productos:
        if p["name"] == name:
            productos.remove(p)  # Eliminamos el producto de la lista
            print("✅ Producto eliminado.")
            return
    print("❌ Producto no encontrado.")

# 📄 Mostrar todos los productos registrados
def mostrar_productos(productos):
    if not productos:
        print("⚠️ No hay productos registrados.")
    else:
        for p in productos:
            print(f"{p['name']}, {p['quantity']}, {p['price']}")

# 💰 Calcular el total de todas las ventas
def calcular_total_ventas(productos):
    total = sum(p["quantity"] * p["price"] for p in productos)
    print(f"💸 Total de ventas: {total}")

# 💵 Calcular total de venta de un producto específico
def calcular_venta_producto(productos):
    name = input("Nombre: ")
    for p in productos:
        if p["name"] == name:
            total = p["quantity"] * p["price"]
            print(f"💰 Total de {name}: {total}")
            return
    print("❌ Producto no encontrado.")

# 🚀 Bucle principal del programa
productos = cargar_productos()  # Cargamos productos desde el archivo al iniciar

# Mientras no se elija salir
while True:
    mostrar_menu()  # Mostramos menú de opciones

    try:
        option = int(input("Seleccione una opción: "))  # Leemos la opción elegida
    except ValueError:
        print("❌ Debes ingresar un número.")
        continue  # Si no es número, vuelve a mostrar el menú

    # Según la opción elegida, ejecutamos la función correspondiente
    if option == 1:
        añadir_producto(productos)
        guardar_productos(productos)
    elif option == 2:
        consultar_producto(productos)
    elif option == 3:
        actualizar_producto(productos)
    elif option == 4:
        borrar_producto(productos)
    elif option == 5:
        mostrar_productos(productos)
    elif option == 6:
        calcular_total_ventas(productos)
    elif option == 7:
        calcular_venta_producto(productos)
    elif option == 8:
        # Antes de salir, guardamos los productos actualizados
        guardar_productos(productos)
        # Eliminamos el archivo si así se desea
        os.remove(file_name)
        print("✅ Archivo eliminado y programa cerrado.")
        break  # Terminamos el bucle y cerramos programa
    else:
        print("⚠️ Opción no válida.")
