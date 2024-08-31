# 11 - MANEJO DE FICHEROS
import os

# Ejercicio

nombre_archivo = "SooHav.txt"

# Abrimos el fichero
with open(nombre_archivo, 'w') as fichero:
    # Datos
    lista = ["Sofia", "46", "Python"]
    # Escribir datos
    for linea in lista:
        fichero.write(linea + "\n")

# Leemos  y borramos el fichero
with open(nombre_archivo, 'r') as fichero_lectura:
    print(fichero_lectura.read())

try:
    os.remove(nombre_archivo)
    print("Archivo eliminado.")
except FileNotFoundError:
    print("El archivo no existe.")

# Dificultad Extra
# Inventario


def generar_archivo():
    productos = []
    # Escribir archivo y agregar productos
    with open("archivo.txt", 'a') as archivo:
        while True:
            producto = {}
            producto['Nombre'] = input("Nombre del producto: ")

            # Verificar si el producto ya existe
            if any(prod['Nombre'] == producto['Nombre'] for prod in productos):
                print("El producto ya existe. Intente con otro nombre.")
                continue

            while True:
                try:
                    producto['Cantidad'] = int(input("Cantidad: "))
                    print(
                        f"El número ingresado de productos es {producto['Cantidad']}")
                    break
                except ValueError as e:
                    print(f"Error: {e}")

            while True:
                try:
                    producto['Precio'] = float(input("Precio unitario: "))
                    print(f"El precio ingresado es {producto['Precio']}")
                    break
                except ValueError as e:
                    print(f"Error: {e}")

            productos.append(producto)

            agregar_otro = input("¿Desea agregar otro producto? (s/n): ")
            if agregar_otro.lower() != 's':
                break

        for producto in productos:
            archivo.write(
                f"{producto['Nombre']}, {producto['Cantidad']}, {producto['Precio']}\n")
        print(productos)
    return productos


def leer_archivo(archivo):
    lista = []
    with open(archivo, 'r') as archivo:
        for linea in archivo.readlines():
            producto = linea.strip().split(', ')
            lista.append(producto)
    return lista


def consultar(archivo):
    # Consultar el archivo
    while True:
        try:
            palabra_clave = input(
                "Ingrese la palabra clave para la búsqueda: ")
            productos = leer_archivo(archivo)  # Leer el archivo nuevamente
            encontrados = False
            for producto in productos:
                # Comparar con el nombre del producto
                if producto[0].lower() == palabra_clave.lower():
                    print(producto)
                    encontrados = True
            if not encontrados:
                raise Exception(
                    "No se encontraron productos con la palabra clave proporcionada.")
        except Exception as e:
            print(f"Error al buscar productos: {e}")

        buscar_otro = input("¿Desea buscar otro producto? (s/n): ")
        if buscar_otro.lower() != 's':
            break


def actualizar(archivo):
    while True:
        productos = leer_archivo(archivo)
        # Actualizar el archivo
        try:
            palabra_clave = input(
                "Ingrese la palabra clave para la búsqueda: ")
            productos_encontrados = []
            encontrados = False
            for producto in productos:
                if producto[0].lower() == palabra_clave.lower():
                    nuevo_nombre = input("Ingrese el nuevo nombre: ")
                    nueva_cantidad = input("Ingrese la nueva cantidad: ")
                    nuevo_precio = input("Ingrese el nuevo precio: ")
                    producto[0] = nuevo_nombre
                    producto[1] = nueva_cantidad
                    producto[2] = nuevo_precio
                    encontrados = True
                    # Escribir el contenido corregido de vuelta al archivo
                    with open(archivo, 'w') as file:
                        for producto in productos:
                            file.write(
                                f"{producto[0]}, {producto[1]}, {producto[2]}\n")
            if not encontrados:
                raise Exception(
                    "No se encontraron productos con la palabra clave proporcionada.")
        except Exception as e:
            print(f"Error al buscar productos: {e}")

        continuar = input("¿Desea seguir actualizando productos? (s/n): ")
        if continuar.lower() != 's':
            break


def eliminar_producto(archivo, palabra_clave):
    # Leer el contenido actual del archivo
    with open(archivo, 'r') as file:
        productos = file.readlines()

    # Buscar la línea a eliminar
    with open(archivo, 'w') as file:
        for producto in productos:
            if palabra_clave not in producto:
                file.write(producto)


# Uso del inventario
while True:
    print("\nMenú:")
    print("1. Generar archivo")
    print("2. Consultar productos")
    print("3. Actualizar productos")
    print("4. Eliminar producto")
    print("5. Mostrar productos inventariados")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        generar_archivo()
    elif opcion == "2":
        consultar("archivo.txt")
    elif opcion == "3":
        actualizar("archivo.txt")
    elif opcion == "4":
        palabra_clave = input(
            "Ingrese la palabra clave del producto a eliminar: ")
        eliminar_producto("archivo.txt", palabra_clave)
    elif opcion == "5":
        with open('archivo.txt', 'r') as archivo:
            print(archivo.read())
    elif opcion == "6":
        os.remove("archivo.txt")
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
