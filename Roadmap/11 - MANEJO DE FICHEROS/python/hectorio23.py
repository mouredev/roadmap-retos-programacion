# Autor: Héctor Adán
# GitHub: https://github.com/hectorio23

import os

# Constantes
nameFile = "./hectorio23.txt"
language = "Python/C++"
name = "Héctor Adán"
age = 19

# Función para escribir en el archivo
def write_file():
    with open(nameFile, 'w') as file:
        file.write(f"Nombre: {name}\n")
        file.write(f"Lenguajes favoritos: {language}\n")
        file.write(f"Edad: {age}\n")

# Función para imprimir el contenido del archivo
def print_file_values():
    with open(nameFile, 'r') as file:
        for line in file:
            print(line, end='')

# Función para agregar un producto al archivo de ventas
def agregar_producto(nombre, cantidad, precio):
    with open("ventas.txt", 'a') as archivo:
        archivo.write(f"{nombre}, {cantidad}, {precio}\n")

# Función para consultar todos los productos en el archivo de ventas
def consultar_productos():
    with open("ventas.txt", 'r') as archivo:
        for line in archivo:
            print(line, end='')

# Función para actualizar un producto en el archivo de ventas
def actualizar_producto(nombre, cantidad, precio):
    with open("ventas.txt", 'r') as archivo, open("temporal.txt", 'w') as temporal:
        for line in archivo:
            nombre_producto, cant_actual, precio_actual = line.strip().split(', ')
            if nombre_producto == nombre:
                temporal.write(f"{nombre}, {cantidad}, {precio}\n")
            else:
                temporal.write(f"{nombre_producto}, {cant_actual}, {precio_actual}\n")

# Función para eliminar un producto del archivo de ventas
def eliminar_producto(nombre):
    with open("ventas.txt", 'r') as archivo, open("temporal.txt", 'w') as temporal:
        for line in archivo:
            nombre_producto, cant_actual, precio_actual = line.strip().split(', ')
            if nombre_producto != nombre:
                temporal.write(f"{nombre_producto}, {cant_actual}, {precio_actual}\n")

# Función para calcular la venta total del archivo de ventas
def calcular_venta_total():
    total = 0
    with open("ventas.txt", 'r') as archivo:
        for line in archivo:
            nombre_producto, cantidad, precio = line.strip().split(', ')
            total += int(cantidad) * float(precio)
    return total

# Función para calcular la venta de un producto específico del archivo de ventas
def calcular_venta_por_producto(nombre):
    with open("ventas.txt", 'r') as archivo:
        for line in archivo:
            nombre_producto, cantidad, precio = line.strip().split(', ')
            if nombre_producto == nombre:
                return int(cantidad) * float(precio)
    return 0

# Función para manejar la opción de salir del programa
def salir():
    os.remove("ventas.txt")
    print("Archivo borrado. Saliendo del programa...")
    exit(0)

# Función principal
def main():
    # Crear archivo con datos requeridos
    print("\nEJERCICIO\n")
    print("Creando archivo hectorio23.txt e insertando datos\n")
    write_file()

    # Imprimir los valores del archivo
    print("Imprimiendo los valores contenidos en el archivo hectorio23.txt\n")
    print_file_values()

    # Ejercicio Extra - Gestión de Ventas
    print("\nEJERCICIO EXTRA\n")

    while True:
        print("===== Gestión de Ventas =====")
        print("1. Añadir producto")
        print("2. Consultar productos")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Calcular venta total")
        print("6. Calcular venta por producto")
        print("7. Salir")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad vendida: "))
            precio = float(input("Precio: "))
            agregar_producto(nombre, cantidad, precio)
        elif opcion == 2:
            print("Productos registrados:")
            consultar_productos()
        elif opcion == 3:
            nombre = input("Nombre del producto a actualizar: ")
            cantidad = int(input("Nueva cantidad vendida: "))
            precio = float(input("Nuevo precio: "))
            actualizar_producto(nombre, cantidad, precio)
        elif opcion == 4:
            nombre = input("Nombre del producto a eliminar: ")
            eliminar_producto(nombre)
        elif opcion == 5:
            print(f"Venta total: ${calcular_venta_total()}")
        elif opcion == 6:
            nombre = input("Nombre del producto para calcular venta: ")
            print(f"Venta de {nombre}: ${calcular_venta_por_producto(nombre)}")
        elif opcion == 7:
            salir()
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()
